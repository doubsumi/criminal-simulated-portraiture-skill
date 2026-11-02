#!/usr/bin/env python3
"""Compile a FacialProfile into model-specific, identity-first prompts (v2 preview).

Differences from prompt_compiler.py (v0.3.0), all motivated by the Phase 4
likeness failure:

1. No meta-instructions. Only visible attributes are emitted as noun phrases.
2. Coarse identity anchors come first (outline, proportions, spacing, nose and
   mouth width, skin tone, hairline, age band, gender presentation), because
   those carry most of the recognisability. Fine detail is capped.
3. A fixed rendering clause keeps candidates comparable.
4. Per-model renderings: natural language (FLUX / Qwen-Image), tag style
   (SDXL), parameter style (Midjourney), and Chinese-language rendering for
   Chinese-native models.
5. A separate reference-image branch documents what must be done when the
   source photograph exists (the only way to preserve identity).
6. Missing anchors are reported, never invented.

This script does not call a model and does not claim that any prompt alone can
reproduce an identity.

    python prompt_compiler_v2.py profile.json --format json
    python prompt_compiler_v2.py profile.json --model sdxl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from image_description import assess  # noqa: E402

VERSION = "2.0.0-preview"

ANCHOR_ORDER = [
    ("F02.C02", "face outline"),
    ("F02.C01", "cranial vault"),
    ("F03.C01", "feature proportions"),
    ("F07.C01", "intercanthal distance"),
    ("F07.C02", "interpupillary distance"),
    ("F09.C01", "nasal outline"),
    ("F09.C06", "alar width"),
    ("F11.C02", "mouth width"),
    ("F01.C03", "skin tone"),
    ("F04.C06", "hairline"),
    ("F12.C01", "chin and jawline"),
]
DETAIL_ORDER = [
    "F07.C03", "F07.C04", "F07.C09", "F07.C10", "F06.C01", "F06.C02",
    "F09.C02", "F09.C04", "F11.C03", "F11.C04", "F11.C06", "F05.C01",
    "F05.C02", "F04.C01", "F08.C01", "F10.C01", "F12.C02",
]
RENDER = "photorealistic portrait"
MAX_CORE_TOKENS = 90


def _tokens(text: str) -> int:
    return int(round(len(text.split()) * 1.33))


def _shorten(display: str) -> str:
    text = display.strip().rstrip(".")
    text = text.replace(" with a ", ", ").replace(" with ", ", ")
    text = text.replace("that is ", "").replace("which is ", "")
    text = text.replace("the ", "", 1) if text.lower().startswith("the ") else text
    return text


def _appearance(profile: dict) -> list[str]:
    cues = []
    for cue in profile.get("appearance_context", []):
        if cue["confirmation_status"] == "rejected_by_user":
            continue
        cues.append(cue["display_en"].strip().rstrip("."))
    return cues


def _relationship_text(profile: dict, accepted: list[dict]) -> tuple[list[str], list[str], list[str], list[str]]:
    feature_ids = {item["feature_id"] for item in accepted}
    relations, relation_ids, asymmetries, asymmetry_ids = [], [], [], []
    for relation in profile.get("spatial_relations", []):
        value = relation.get("value", {})
        text = value.get("display_en", "") if isinstance(value, dict) else ""
        if text and relation["subject_feature_id"] in feature_ids and relation["reference_feature_id"] in feature_ids:
            relations.append(text.strip().rstrip("."))
            relation_ids.append(relation["relation_id"])
    for asym in profile.get("asymmetries", []):
        text = asym.get("difference", {}).get("display_en", "").strip().rstrip(".")
        if text:
            asymmetries.append(text)
            asymmetry_ids.append(asym["asymmetry_id"])
    return relations, relation_ids, asymmetries, asymmetry_ids


def build_plan(profile: dict) -> dict:
    review = assess(profile, vision_attested=True, image_authorized=True)
    if not review["can_describe"]:
        raise ValueError("profile failed review: " + "; ".join(review["issues"]))

    accepted = [item for item in review["accepted"]
                if isinstance(item["observation"]["display_en"], str) and item["observation"]["display_en"].strip()]
    by_feature: dict[str, list[dict]] = {}
    for item in accepted:
        by_feature.setdefault(item["feature_id"], []).append(item)

    core_items = [item for fid, _ in ANCHOR_ORDER for item in by_feature.get(fid, [])]
    core_ids = {item["observation_id"] for item in core_items}
    detail_items = [item for fid in DETAIL_ORDER for item in by_feature.get(fid, []) if item["observation_id"] not in core_ids]

    core: list[str] = []
    core_zh: list[str] = []
    used: list[str] = []
    for item in core_items:
        phrase = _shorten(item["observation"]["display_en"])
        candidate = "; ".join(core + [phrase])
        if _tokens(candidate) > MAX_CORE_TOKENS and core:
            break
        core.append(phrase)
        core_zh.append(item["observation"]["display_zh"].strip().rstrip("。"))
        used.append(item["observation_id"])
    for item in detail_items:
        phrase = _shorten(item["observation"]["display_en"])
        candidate = "; ".join(core + [phrase])
        if _tokens(candidate) > MAX_CORE_TOKENS:
            continue
        core.append(phrase)
        core_zh.append(item["observation"]["display_zh"].strip().rstrip("。"))
        used.append(item["observation_id"])

    cues = _appearance(profile)
    relation_text, relation_ids, asymmetry_text, asymmetry_ids = _relationship_text(profile, accepted)
    if relation_text:
        core.append("; ".join(relation_text))
        core_zh.append("；".join(relation_text))
    if asymmetry_text:
        core.append("; ".join(asymmetry_text))
        core_zh.append("；".join(asymmetry_text))
    present_ids = {item["feature_id"] for item in accepted}
    missing_anchors = [label for fid, label in ANCHOR_ORDER if fid not in present_ids]
    if not any(cue for cue in cues):
        missing_anchors += ["age band", "gender presentation"]
    if not core:
        raise ValueError("no accepted observations: fill the profile before compiling a prompt")

    core_text = "; ".join(core)
    return {
        "compiler_version": VERSION,
        "profile_id": profile["profile_id"],
        "core_tokens_est": _tokens(core_text),
        "core": core_text,
        "core_zh": "；".join(core_zh),
        "appearance_cues": cues,
        "included_observations": used,
        "included_relations": relation_ids,
        "included_asymmetries": asymmetry_ids,
        "relationships": relation_text,
        "asymmetries": asymmetry_text,
        "excluded_observations": [item["id"] for item in review["excluded"]],
        "missing_anchors": missing_anchors,
        "needs_observation": missing_anchors,
        "renderings": renderings(core_text, cues, "；".join(core_zh)),
        "reference_branch": reference_branch(),
        "iteration": iteration_protocol(),
        "limitations": [
            "A text prompt cannot reconstruct a specific identity; it can only specify coarse attributes.",
            "Missing anchors must be observed, not inferred.",
            "All renderings are hypotheses to be compared against the source image.",
        ],
    }


def renderings(core: str, cues: list[str], core_zh: str) -> dict:
    cue_text = "; ".join(cues)
    base = f"{core}; {RENDER}"
    if cue_text:
        base = f"{core}; {cue_text}; {RENDER}"
    return {
        "natural": base,
        "flux": f"A photorealistic head-and-shoulders portrait of a person. Facial description: {base}.",
        "sdxl": {
            "positive": base.replace("; ", ", "),
            "negative": "cartoon, illustration, 3d render, distorted proportions, oversmoothed skin, extra features",
        },
        "midjourney": f"{base} --ar 3:4 --style raw --s 50",
        "chinese_model": f"照片级人像：{core_zh}。",
        "note": "FLUX and other guidance-distilled models ignore negative prompts; do not rely on them.",
    }


def reference_branch() -> dict:
    return {
        "applicability": "Only when the source photograph is available and authorised.",
        "methods": {
            "instantid": "single-image IdentityNet; keeps facial geometry; good default for photo-realism",
            "pulid": "contrastive ID embedding; fast, works without ControlNet",
            "ip_adapter_faceid": "SDXL IP-Adapter plus face embedding; plug-in, lower fidelity than InstantID",
            "infiniteyou": "identity-preserving recrafting with layout control",
        },
        "settings_starting_point": {
            "identity_strength": "0.6-0.8 (sweep 0.4-1.0; higher strength suppresses prompt adherence)",
            "prompt_strength_img2img": "0.25-0.45 when editing rather than regenerating",
            "seed": "fix per candidate, vary across candidates",
        },
        "rule": "Reference mode measures the ceiling of the pipeline; description-only mode measures the skill, not the model.",
    }


def iteration_protocol() -> dict:
    return {
        "step_1": "generate 6-12 candidates with fixed prompt and varying seeds",
        "step_2": "score against the source: landmark geometry, face embedding, human rating",
        "step_3": "keep the best candidate; edit one component at a time with inpainting",
        "step_4": "re-score after each edit; revert edits that lower the score",
        "step_5": "log which prompt phrases map to which visual change",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--model", choices=["natural", "flux", "sdxl", "midjourney", "chinese_model"], default="natural")
    parser.add_argument("--format", choices=["json", "text"], default="json")
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    try:
        plan = build_plan(profile)
    except ValueError as exc:
        print(f"cannot compile: {exc}", file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(plan, ensure_ascii=False, indent=2))
    else:
        chosen = plan["renderings"][args.model]
        print(chosen["positive"] if isinstance(chosen, dict) else chosen)
        print()
        print("MISSING ANCHORS:", ", ".join(plan["missing_anchors"]) or "none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
