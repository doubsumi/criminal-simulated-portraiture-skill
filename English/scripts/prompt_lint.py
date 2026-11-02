#!/usr/bin/env python3
"""Diagnose a compiled prompt before it reaches an image model.

The linter reads a FacialProfile (compiled on the fly) or an existing
PromptOutput and reports prompt-level risks that are known to hurt
identity fidelity in text-to-image models:

* instruction leakage - sentences addressed to a human, not visual tokens;
* vagueness - relative qualifiers a diffusion text encoder cannot calibrate;
* negation in the positive prompt;
* length - long attribute lists dilute per-attribute adherence;
* missing identity anchors - coarse, high-salience features that carry most
  of the recognisability (face outline, proportions, spacing, skin tone,
  age band, gender presentation, hairline);
* missing rendering anchors - framing, lens, lighting, background.

The score is a heuristic "prompt-readiness index" (0-100), not a similarity
metric. It is designed to be compared across compiler versions on the same
profile, not across different profiles.

    python prompt_lint.py examples/facial_profile.synthetic-cn.json
    python prompt_lint.py prompt.json --format markdown
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from prompt_compiler import compile_profile  # noqa: E402

IMPERATIVES = {
    "create", "make", "preserve", "keep", "leave", "do", "don't", "ensure",
    "avoid", "render", "show", "use", "draw", "depict", "maintain", "retain",
    "respect", "include", "omit", "specify", "produce",
}
VAGUE = [
    "slightly", "relatively", "moderately", "gently", "mild", "mildly",
    "soft", "softly", "somewhat", "rather", "fairly", "quite", "almost",
    "approximately", "a little", "tendency", "appears", "appearance of",
]
STYLE_ANCHORS = ["lens", "camera", "lighting", "light", "background", "framing",
                 "headshot", "portrait", "studio", "35mm", "85mm", "depth of field"]
ANCHOR_RULES = {
    "face_outline": {"F02.C02"},
    "face_proportions": {"F03.C01"},
    "eye_spacing": {"F07.C01", "F07.C02"},
    "nose_width": {"F09.C01", "F09.C06"},
    "mouth_width": {"F11.C02"},
    "skin_tone": {"F01.C03"},
    "hairline": {"F04.C06"},
    "age_band": set(),      # supplied by appearance_context: age_appearance
    "gender_presentation": set(),
}


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.;])\s+|\n+", text)
    return [part.strip() for part in parts if part.strip()]


def calibrate(text: str) -> dict:
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    sentences = split_sentences(text)
    instruction_sentences = []
    for sentence in sentences:
        first = re.match(r"[A-Za-z']+", sentence)
        head = first.group(0).lower() if first else ""
        if head in IMPERATIVES or re.search(r"\b(do not|don't|must not|should not)\b", sentence, re.I):
            instruction_sentences.append(sentence)
    instruction_words = sum(len(re.findall(r"[A-Za-z][A-Za-z'-]*", s)) for s in instruction_sentences)
    vague_hits = []
    lowered = text.lower()
    for term in VAGUE:
        count = len(re.findall(r"\b" + re.escape(term) + r"\b", lowered))
        if count:
            vague_hits.append({"term": term, "count": count})
    return {
        "words": len(words),
        "tokens_est": int(round(len(words) * 1.33)),
        "sentences": len(sentences),
        "instruction_sentences": len(instruction_sentences),
        "instruction_word_share": round(instruction_words / len(words), 3) if words else 0.0,
        "vague_qualifiers": vague_hits,
        "vague_total": sum(item["count"] for item in vague_hits),
        "negations_in_positive": len(re.findall(r"\b(do not|don't|no |without|avoid)\b", text, re.I)),
        "style_anchor_hits": [term for term in STYLE_ANCHORS if term in lowered],
    }


def analyse(profile: dict, prompt: dict) -> dict:
    positive = prompt["positive_prompt"]
    negative = prompt.get("negative_prompt", "")
    stats = calibrate(positive)

    by_id = {item["observation_id"]: item for item in profile["features"]}
    included = [by_id[oid] for oid in prompt.get("included_observations", []) if oid in by_id]
    covered = sorted({item["component_id"] for item in included})
    missing = [f"F{n:02d}" for n in range(1, 20) if f"F{n:02d}" not in covered]

    feature_ids = {item["feature_id"] for item in included}
    anchors_present, anchors_missing = [], []
    for name, ids in ANCHOR_RULES.items():
        if name == "age_band":
            present = any(cue["category"] == "age_appearance" for cue in profile.get("appearance_context", []))
        elif name == "gender_presentation":
            present = any(cue["category"] == "gender_presentation" for cue in profile.get("appearance_context", []))
        else:
            present = bool(ids & feature_ids)
        (anchors_present if present else anchors_missing).append(name)

    negative_items = [item for item in re.split(r";", negative) if item.strip()]

    score = 100
    findings = []
    if stats["tokens_est"] > 120:
        penalty = min(15, (stats["tokens_est"] - 120) // 10)
        score -= penalty
        findings.append({
            "severity": "high" if stats["tokens_est"] > 200 else "medium",
            "issue": f"prompt is long ({stats['tokens_est']} tokens est.); per-attribute adherence falls off on long prompts",
            "evidence": f"{stats['words']} words, {stats['sentences']} sentences",
            "fix": "compress to a 60-110 token identity core; move styling to a separate clause",
        })
    if stats["instruction_word_share"] > 0.12:
        score -= 20
        findings.append({
            "severity": "high",
            "issue": f"{stats['instruction_word_share']:.0%} of words are instructions addressed to a human",
            "evidence": f"{stats['instruction_sentences']} of {stats['sentences']} sentences are imperative",
            "fix": "delete meta-instructions; encode only visible attributes as concrete noun phrases",
        })
    if stats["vague_total"] >= 5:
        score -= min(20, stats["vague_total"] * 2)
        findings.append({
            "severity": "high",
            "issue": f"{stats['vague_total']} relative qualifiers",
            "evidence": ", ".join(f"{h['term']}×{h['count']}" for h in stats["vague_qualifiers"]),
            "fix": "replace relative qualifiers with ordinal anchors or explicit comparisons",
        })
    if stats["negations_in_positive"]:
        score -= min(9, stats["negations_in_positive"] * 3)
        findings.append({
            "severity": "medium",
            "issue": f"{stats['negations_in_positive']} negations inside the positive prompt",
            "evidence": "text encoders do not reliably bind negation to the intended attribute",
            "fix": "move prohibitions to the negative prompt or drop them",
        })
    if anchors_missing:
        score -= min(24, len(anchors_missing) * 4)
        findings.append({
            "severity": "high",
            "issue": f"{len(anchors_missing)} of 9 identity anchors absent: {', '.join(anchors_missing)}",
            "evidence": "coarse, high-salience features carry most of a face's recognisability",
            "fix": "record and compile the missing anchors first; they are worth more than fine detail",
        })
    if not stats["style_anchor_hits"]:
        score -= 6
        findings.append({
            "severity": "medium",
            "issue": "no framing/lens/lighting anchor",
            "evidence": "models vary angle, focal length and lighting by default",
            "fix": "add one fixed rendering clause so candidates are comparable",
        })
    if len(negative_items) > 6:
        score -= 4
        findings.append({
            "severity": "low",
            "issue": f"{len(negative_items)} negative items; long negatives can distort sampling",
            "evidence": negative[:160] + ("..." if len(negative) > 160 else ""),
            "fix": "keep 3-4 negatives that target observed failure modes only",
        })

    return {
        "prompt_id": prompt.get("prompt_id"),
        "profile_id": prompt.get("profile_id"),
        "compiler_version": prompt.get("compiler_version"),
        "score": max(0, score),
        "stats": stats,
        "components_covered": covered,
        "components_missing": missing,
        "anchors_present": anchors_present,
        "anchors_missing": anchors_missing,
        "negative_items": len(negative_items),
        "findings": sorted(findings, key=lambda item: {"high": 0, "medium": 1, "low": 2}[item["severity"]]),
        "note": "heuristic prompt-readiness index; not an identity-similarity metric",
    }


def render_markdown(result: dict) -> str:
    stats = result["stats"]
    lines = [
        f"# Prompt diagnostics: {result['prompt_id']}",
        "",
        f"- profile: {result['profile_id']} · compiler {result['compiler_version']}",
        f"- readiness score: **{result['score']}/100** (heuristic)",
        f"- tokens (est.): {stats['tokens_est']} · words: {stats['words']} · sentences: {stats['sentences']}",
        f"- instruction share: {stats['instruction_word_share']:.0%} · vague qualifiers: {stats['vague_total']} · negations in positive: {stats['negations_in_positive']}",
        f"- components: {len(result['components_covered'])}/19 covered; missing {', '.join(result['components_missing'])}",
        f"- anchors missing: {', '.join(result['anchors_missing']) or 'none'}",
        "",
        "## Findings",
        "",
    ]
    for item in result["findings"]:
        lines += [f"### [{item['severity']}] {item['issue']}", f"- evidence: {item['evidence']}", f"- fix: {item['fix']}", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="FacialProfile JSON or PromptOutput JSON")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if "positive_prompt" in data:
        prompt = data
        if "features" not in data:
            raise SystemExit("PromptOutput alone lacks feature context; pass the FacialProfile instead")
        profile = data
    else:
        profile = data
        try:
            prompt = compile_profile(profile, vision_attested=True, image_authorized=True)
        except ValueError as exc:
            print(f"cannot lint: {exc}", file=sys.stderr)
            return 1
    result = analyse(profile, prompt)
    print(render_markdown(result) if args.format == "markdown" else json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
