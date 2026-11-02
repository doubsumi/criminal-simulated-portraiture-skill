#!/usr/bin/env python3
"""Compile an evidence-bound FacialProfile into a model-neutral prompt.

This program does not call an image model. It consumes only observations that
pass the image-description review and keeps their IDs in the output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from image_description import assess

COMPILER_VERSION = "0.3.0"
GROUPS = [
    ("Facial layout", {"F03", "F02"}),
    ("Brow region and eyes", {"F05", "F06", "F07"}),
    ("Nose, mouth and chin", {"F09", "F11", "F12"}),
    ("Hair and visible styling", {"F04", "F18"}),
    ("Other visible details", {"F01", "F08", "F10", "F13", "F14", "F15", "F16", "F17", "F19"}),
]
def _appearance_cues(profile: dict, accepted: list[dict]) -> tuple[list[str], list[str]]:
    evidence_ids = {ref["evidence_id"] for item in accepted for ref in item["evidence_refs"]}
    cues: list[str] = []
    excluded: list[str] = []
    for cue in profile.get("appearance_context", []):
        if cue["confirmation_status"] == "rejected_by_user" or cue["source_type"] not in {"direct_visual_observation", "user_free_recall", "user_cued_recall", "user_response_to_neutral_clarification"}:
            excluded.append(f"appearance:{cue['category']}: unconfirmed suggestion or rejected")
        elif not cue["evidence_refs"] or not set(cue["evidence_refs"]) <= evidence_ids:
            excluded.append(f"appearance:{cue['category']}: missing accepted evidence")
        else:
            cues.append(cue["display_en"].strip())
    return cues, excluded


def _relation_text(profile: dict, accepted: list[dict]) -> tuple[list[str], list[str], list[str]]:
    by_feature: dict[str, set[str]] = {}
    for item in accepted:
        by_feature.setdefault(item["feature_id"], set()).update(ref["evidence_id"] for ref in item["evidence_refs"])
    descriptions: list[str] = []
    ids: list[str] = []
    excluded: list[str] = []
    for relation in profile["spatial_relations"]:
        value = relation["value"]
        text = value.get("display_en", "") if isinstance(value, dict) else ""
        if (
            not text.strip()
            or relation["subject_feature_id"] not in by_feature
            or relation["reference_feature_id"] not in by_feature
            or relation["viewpoint"] not in profile["image_context"]["viewpoints"]
            or not relation["evidence_refs"]
            or not set(relation["evidence_refs"]) <= (by_feature.get(relation["subject_feature_id"], set()) | by_feature.get(relation["reference_feature_id"], set()))
        ):
            excluded.append(f"relation:{relation['relation_id']}: missing accepted features, evidence, or English description")
            continue
        descriptions.append(text.strip().rstrip("."))
        ids.append(relation["relation_id"])
    return descriptions, ids, excluded


def _focus(profile: dict, accepted: list[dict], relation_ids: list[str]) -> tuple[list[str], list[str], list[str], list[str], list[str]]:
    observations = {item["observation_id"]: item for item in accepted}
    valid_relations = {item["relation_id"]: item for item in profile["spatial_relations"] if item["relation_id"] in relation_ids}
    descriptions: list[str] = []
    relations: list[str] = []
    negatives: list[str] = []
    used_observations: list[str] = []
    used_relations: list[str] = []
    for focus in profile.get("prompt_focus", []):
        missing = set(focus["observation_ids"]) - observations.keys()
        missing |= set(focus["relation_ids"]) - valid_relations.keys()
        if missing or not (focus["observation_ids"] or focus["relation_ids"]):
            raise ValueError(f"Prompt focus {focus['focus_id']} has unaccepted references: {', '.join(sorted(missing))}")
        for oid in focus["observation_ids"]:
            if oid not in used_observations:
                descriptions.append(observations[oid]["observation"]["display_en"].strip().rstrip("."))
                used_observations.append(oid)
        for rid in focus["relation_ids"]:
            if rid not in used_relations:
                relations.append(valid_relations[rid]["value"]["display_en"].strip().rstrip("."))
                used_relations.append(rid)
        negatives.extend(text.strip().rstrip(".") for text in focus["avoid_en"])
    return descriptions, relations, negatives, used_observations, used_relations


def compile_profile(profile: dict, *, vision_attested: bool = False, image_authorized: bool = False) -> dict:
    review = assess(profile, vision_attested=vision_attested, image_authorized=image_authorized)
    if not review["can_describe"]:
        raise ValueError("Profile cannot be compiled: " + " | ".join(review["issues"]))

    accepted = [item for item in review["accepted"] if isinstance(item["observation"]["display_en"], str) and item["observation"]["display_en"].strip()]
    omitted = [item["observation_id"] for item in review["accepted"] if item not in accepted]
    if not accepted:
        raise ValueError("Profile contains no evidence-backed facial descriptions")

    sections = ["Photorealistic portrait of an adult woman with the recorded facial structure and visible features."]
    cues, omitted_cues = _appearance_cues(profile, accepted)
    if cues:
        sections.append("Presentation cues: " + "; ".join(cues) + ".")
    relations, relation_ids, omitted_relations = _relation_text(profile, accepted)
    focus_descriptions, focus_relations, focus_negatives, focused_ids, focused_relations = _focus(profile, accepted, relation_ids)
    if focus_descriptions:
        sections.append("Priority facial features: " + "; ".join(focus_descriptions) + ".")
    if focus_relations:
        sections.append("Priority feature relationships: " + "; ".join(focus_relations) + ".")
    included_ids: list[str] = []
    present_components: set[str] = {item["component_id"] for item in accepted}
    focused_components: set[str] = {item["component_id"] for item in accepted if item["observation_id"] in focused_ids}
    for heading, components in GROUPS:
        items = [item for item in accepted if item["component_id"] in components and item["observation_id"] not in focused_ids]
        if not items:
            continue
        included_ids.extend(item["observation_id"] for item in items)
        parts = []
        for item in items:
            description = item["observation"]["display_en"].strip().rstrip(".")
            parts.append(description)
        sections.append(heading + ": " + "; ".join(parts) + ".")

    remaining_relations = [description for description, rid in zip(relations, relation_ids) if rid not in focused_relations]
    if remaining_relations:
        sections.append("Keep these relative relationships: " + "; ".join(remaining_relations) + ".")
    included_asymmetries: list[str] = []
    asymmetry_text: list[str] = []
    for asym in profile["asymmetries"]:
        text = asym["difference"].get("display_en", "").strip().rstrip(".")
        if text:
            asymmetry_text.append(text)
            included_asymmetries.append(asym["asymmetry_id"])
    if asymmetry_text:
        sections.append("Recorded left-right differences: " + "; ".join(asymmetry_text) + ".")
    negatives = ["unobserved facial details", "beautified or standardized facial proportions"]
    negatives.extend(focus_negatives)
    if {"F02", "F03"} & present_components:
        negatives.append("do not change the recorded face outline or feature placement")
    if {"F05", "F06"} & present_components:
        negatives.append("do not flatten or exaggerate the recorded brow region")
    if "F11" in present_components and "F11" not in focused_components:
        negatives.append("do not change the recorded upper-to-lower lip fullness")
    if "F04" in present_components:
        negatives.append("do not change the recorded hair shape or color")

    revision = profile["updated_at"]
    canonical = json.dumps(profile, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(f"{canonical}|{COMPILER_VERSION}".encode()).hexdigest()[:12]
    return {
        "schema_version": "1.0.0",
        "prompt_id": f"PROMPT-{digest}",
        "profile_id": profile["profile_id"],
        "profile_revision": revision,
        "compiler_version": COMPILER_VERSION,
        "positive_prompt": "\n".join(sections),
        "negative_prompt": "; ".join(negatives) + ".",
        "included_observations": focused_ids + included_ids,
        "included_relations": relation_ids,
        "included_asymmetries": included_asymmetries,
        "excluded_observations": [item["id"] for item in review["excluded"]] + omitted + omitted_cues + omitted_relations,
        "limitations": list(profile["image_quality_report"]["limitations"]) + ["Gender presentation, apparent age and expression are rendering cues, not identity facts."] if cues else list(profile["image_quality_report"]["limitations"]),
        "created_at": None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--out", type=Path, help="Write PromptOutput JSON here instead of stdout")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="Output structured JSON or a copyable prompt")
    parser.add_argument("--vision-attested", action="store_true")
    parser.add_argument("--image-authorized", action="store_true")
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    output = compile_profile(profile, vision_attested=args.vision_attested, image_authorized=args.image_authorized)
    if args.format == "text":
        text = output["positive_prompt"] + "\n\nNegative prompt:\n" + output["negative_prompt"] + "\n"
    else:
        text = json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
