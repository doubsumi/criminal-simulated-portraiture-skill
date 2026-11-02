# Changelog

## Unreleased

- Moved public documentation into `docs/` and public source metadata into `knowledge/`.
- Archived development records and third-party originals outside the publishable tree.
- Added `docs/likeness-diagnosis-and-optimization.md` with the five-layer likeness failure analysis, prompt rules, reference-image ceiling measurement, and staged evaluation protocol.
- Added `scripts/prompt_lint.py` (prompt readiness diagnostics), `scripts/prompt_compiler_v2.py` (identity-first, zero-instruction, per-model rendering preview), and `scripts/prompt_compare.py` (compiler regression comparison).
- Added `examples/facial_profile.synthetic-cn.json`, a synthetic Chinese-face fixture used only for prompt diagnostics.

## 0.1.2-prompt-workflow - 2026-11-01

- Added evidence-bound `prompt_focus` support to prioritize accepted observations and relationships.
- Removed all viewpoint instructions from compiled prompts while retaining viewpoint in image quality records.
- Assessed the Chinese materials, incorporated SF/T 0125 observation dimensions into the image protocol, and corrected local paths in the Chinese source manifest.

## 0.1.1-phase-4-prompt-preview - 2026-11-01

- Added an evidence-gated prompt compiler that carries observation and spatial-relation IDs into PromptOutput, filters unsupported appearance cues, and provides copyable text output.

## 0.1.0-phase-1 - 2026-11-01

- Initialized the Agent Skills project files.
- Added the Phase 1 source manifest for S01-S24.
- Archived seven FISWG PDFs and one IFSA PDF downloaded from official publisher pages.
- Added acquisition notes, access blockers, and research summaries under `docs/`.
- Added the S01 extraction notes, 19-component ontology, 85 characteristic records, descriptor dimensions, anatomy cross-reference, and observability rules.
- Added eight Draft 2020-12 schemas, two valid examples, and `scripts/validate_schemas.py` for Phase 3.
- Added the Phase 4 image-description reviewer, 19-component report renderer, and observation protocol. Corrected the phase order: image description is Phase 4; prompt compilation is Phase 6.
