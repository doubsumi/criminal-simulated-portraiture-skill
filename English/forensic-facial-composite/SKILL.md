---
name: forensic-facial-composite
description: Supports evidence-traceable forensic facial composite research and structured facial description. Use when organizing FISWG, IAI, IFSA, NIST/OSAC, anatomy, or eyewitness-memory sources, documenting image limitations, or preparing later composite workflows.
compatibility: Requires the parent project's knowledge/, schemas/, scripts/, and docs/ directories. Verify external sources at official publisher pages before citation.
metadata:
  version: "0.1.2-prompt-workflow"
---

# Forensic Facial Composite

Phase 0 establishes the project and source controls. Phase 1 acquires and registers professional material. Phase 2 provides the source-linked 19-component ontology and observation boundaries. Phase 3 provides validated data structures. Phase 4 provides an evidence-bound image-description workflow. The parent project's `knowledge/source_manifest.yaml` is the public source registry.

## Source handling

- Keep public source metadata in `../knowledge/source_manifest.yaml`; consult publishers for originals.
- Preserve publisher URL, version, date, access status, and license status.
- Do not infer a current standard from an older edition. Mark drafts, historical editions, access failures, and unclear licenses explicitly.
- Do not use a source as an operational rule until its scope and limitations have been reviewed.

## Current knowledge layer

Read `../knowledge/ontology/facial-components.yaml` for the FISWG component taxonomy, `../knowledge/ontology/descriptors.yaml` for controlled dimensions and states, and `../knowledge/observability/rules.md` for image quality, laterality, spatial relation, asymmetry, and stability rules. For likeness-oriented observations, also consult `../knowledge/description/facial-layout.yaml`, `../knowledge/description/perioral.yaml`, `../knowledge/description/brow-eye.yaml`, and `../knowledge/prompt/semantic-mapping.yaml`; these files keep layout, mouth, brow-eye, and Chinese-English semantic mappings explicit instead of filling gaps with population averages.

## Data structures

Read `../schemas/facial_profile.schema.json` for the unified profile, `../schemas/feature_observation.schema.json` for V1.1 observations, and `../scripts/validate_schemas.py` for the project validation gate.

## Image workflow

Read `../docs/image-observation-protocol.md` before image analysis. Use `../scripts/image_description.py` to review a structured image-derived Profile only after the host has actually observed the authorized image. Without vision or authorization, report limitations instead of facial traits.

For manual generation tests, record brow ridges, eyebrow shape, upper and lower lips, face composition, and evidence-backed spatial relations separately. Compile the reviewed Profile with `../scripts/prompt_compiler.py` and truthful `--vision-attested --image-authorized` flags. `--format text` produces a copyable prompt. Age, gender presentation, and expression are rendering cues only; the user runs external tools and evaluates similarity.

Record user review in `prompt_focus` with accepted observation and relation IDs; use the original image to revise appearance observations. Do not treat generated results as subject evidence. Viewpoint stays in internal quality records and is omitted from generation prompts. Chinese terminology from CN03 is limited to qualitative observation; see `../docs/image-observation-protocol.md`. Use `../docs/generation-evaluation-protocol.md` and `../scripts/create_generation_record.py` to make repeatable baseline/optimized comparison records.

## Planned next phases

Phase 5 will add a non-leading memory interview workflow. The current image-only prompt compiler previews Phase 6; model adapters and full Phase 6 remain planned.
