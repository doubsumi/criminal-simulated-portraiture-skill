#!/usr/bin/env python3
"""Lightweight Phase 3 gate.

This script does not replace a full Draft 2020-12 validator. It verifies that
all schema files are valid JSON, that the supplied examples satisfy the
required cross-field rules, and that the source references used by examples
are registered in knowledge/source_manifest.yaml.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"


def fail(message: str) -> None:
    raise ValueError(message)


def require_keys(obj: dict, keys: list[str], label: str) -> None:
    missing = [key for key in keys if key not in obj]
    if missing:
        fail(f"{label}: missing {', '.join(missing)}")


def validate_feature(item: dict) -> None:
    required = ["schema_version", "observation_id", "component_id", "feature_id", "dimension_id", "feature_name_en", "feature_name_zh", "viewpoint", "laterality", "observation", "visibility", "confidence", "source_type", "confirmation_status", "knowledge_refs", "evidence_refs", "limitations"]
    require_keys(item, required, "FeatureObservation")
    if item["schema_version"] != "1.1.0": fail("FeatureObservation: schema_version")
    if not re.fullmatch(r"(?:D\d{2}|D_UNKNOWN)", item["dimension_id"]): fail("FeatureObservation: dimension_id")
    if not re.fullmatch(r"F(0[1-9]|1[0-9])", item["component_id"]): fail("FeatureObservation: component_id")
    lat = item["laterality"]
    require_keys(lat, ["side", "reference_frame", "mirror_status"], "laterality")
    if lat["reference_frame"] == "anatomical" and lat["mirror_status"] == "unknown": fail("anatomical laterality requires known mirror_status")
    if item["source_type"] == "agent_suggestion" and item["confirmation_status"] != "unconfirmed": fail("agent_suggestion must start unconfirmed")
    if item["visibility"] == "not_visible" and item["source_type"] == "direct_visual_observation": fail("not_visible cannot be a determinate direct visual observation")
    if not isinstance(item["knowledge_refs"], list) or not isinstance(item["evidence_refs"], list): fail("references must be arrays")
    for ref in item["knowledge_refs"]:
        if not re.fullmatch(r"(?:S|CN)\d{2,}", ref): fail(f"invalid knowledge_ref: {ref}")
    for evidence in item["evidence_refs"]:
        require_keys(evidence, ["evidence_id", "evidence_type", "asset_id", "region", "timecode"], "evidence_ref")


def validate_profile(profile: dict) -> None:
    require_keys(profile, ["schema_version", "profile_id", "created_at", "updated_at", "task_mode", "features", "spatial_relations", "asymmetries", "audit_log"], "FacialProfile")
    if profile["schema_version"] != "1.1.0": fail("FacialProfile: schema_version")
    if profile["task_mode"] not in {"image_to_description", "memory_to_composite"}: fail("FacialProfile: task_mode")
    for item in profile["features"]: validate_feature(item)
    seen_focus_ids: set[str] = set()
    for focus in profile.get("prompt_focus", []):
        require_keys(focus, ["focus_id", "observation_ids", "relation_ids", "avoid_en", "source", "note"], "prompt_focus")
        if focus["focus_id"] in seen_focus_ids: fail("prompt_focus: duplicate focus_id")
        seen_focus_ids.add(focus["focus_id"])
        if focus["source"] not in {"user_visual_feedback", "image_review"}: fail("prompt_focus: invalid source")
        if not isinstance(focus["observation_ids"], list) or not isinstance(focus["relation_ids"], list) or not isinstance(focus["avoid_en"], list): fail("prompt_focus: references and avoid_en must be arrays")
        if not focus["observation_ids"] and not focus["relation_ids"]: fail("prompt_focus: at least one reference is required")
    for event in profile["audit_log"]:
        require_keys(event, ["event_id", "event_type", "timestamp", "actor_type", "description"], "audit_event")


def main() -> int:
    schema_files = sorted(SCHEMA_DIR.glob("*.schema.json"))
    if len(schema_files) < 8:
        fail("expected at least eight schema files")
    for path in schema_files:
        json.loads(path.read_text(encoding="utf-8"))
    feature = json.loads((ROOT / "examples/feature_observation.valid.json").read_text(encoding="utf-8"))
    profile = json.loads((ROOT / "examples/facial_profile.valid.json").read_text(encoding="utf-8"))
    validate_feature(feature)
    validate_profile(profile)
    manifest = (ROOT / "knowledge/source_manifest.yaml").read_text(encoding="utf-8")
    for ref in feature["knowledge_refs"]:
        if not re.search(rf"(?m)^  - id: {re.escape(ref)}$", manifest):
            fail(f"knowledge reference not in manifest: {ref}")
    print(f"validated {len(schema_files)} JSON schemas and 2 examples")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
