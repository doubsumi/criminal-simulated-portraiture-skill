#!/usr/bin/env python3
"""Compare compiler versions on the same profile with the prompt linter.

This is a regression gate for Phase 6 prompt work: it keeps the v0.3.0 baseline
and the v2 preview behind one command so that changes to the compiler can be
scored before any image is generated.

    python prompt_compare.py examples/facial_profile.synthetic-cn.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import prompt_compiler  # noqa: E402
import prompt_compiler_v2  # noqa: E402
import prompt_lint  # noqa: E402


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    profile = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    baseline = prompt_compiler.compile_profile(profile, vision_attested=True, image_authorized=True)
    plan = prompt_compiler_v2.build_plan(profile)
    candidate = {
        "prompt_id": "PROMPT-V2-PREVIEW",
        "profile_id": plan["profile_id"],
        "compiler_version": plan["compiler_version"],
        "positive_prompt": plan["renderings"]["natural"],
        "negative_prompt": plan["renderings"]["sdxl"]["negative"],
        "included_observations": plan["included_observations"],
    }

    rows = []
    for label, prompt in (("v0.3.0", baseline), ("v2.0.0", candidate)):
        result = prompt_lint.analyse(profile, prompt)
        rows.append((label, result))

    print(f"profile: {profile['profile_id']}")
    print(f"{'compiler':10} {'score':>6} {'tokens':>7} {'instr%':>7} {'vague':>6} {'anchors':>8} {'neg':>4}")
    for label, result in rows:
        stats = result["stats"]
        print(f"{label:10} {result['score']:>6} {stats['tokens_est']:>7} "
              f"{stats['instruction_word_share'] * 100:>6.0f}% {stats['vague_total']:>6} "
              f"{len(result['anchors_present'])}/9 {result['negative_items']:>4}")

    print("\nremaining gaps (v2):")
    for name in rows[-1][1]["anchors_missing"]:
        print(f"- missing anchor: {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
