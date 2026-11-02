#!/usr/bin/env python3
"""Create a manual external-generation comparison record without image access."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from prompt_compiler import COMPILER_VERSION


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    record = {
        "record_schema_version": "0.1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "profile_id": profile["profile_id"],
        "profile_revision": profile["updated_at"],
        "compiler_versions": [COMPILER_VERSION, "2.0.0-preview"],
        "generation_tool": {"name": None, "version": None, "language": None, "settings": {}, "seed_or_run_ids": []},
        "viewpoint_condition": "record internally; omit from prompt text",
        "variants": [
            {"variant_id": "baseline", "compiler": COMPILER_VERSION, "prompt_file": None, "candidates": []},
            {"variant_id": "optimized", "compiler": "2.0.0-preview", "prompt_file": None, "candidates": []},
        ],
        "candidate_schema": {
            "candidate_id": "",
            "external_image_path": None,
            "seed_or_run_id": None,
            "upper_lip": "unreviewed",
            "brow_eye": "unreviewed",
            "overall_layout": "unreviewed",
            "user_choice": "unreviewed",
            "failure_attribution": [],
            "notes": "",
        },
        "limitations": ["This template does not inspect or score images.", "User judgment is required for likeness assessment."],
    }
    args.out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
