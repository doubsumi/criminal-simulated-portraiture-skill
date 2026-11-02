---
name: forensic-facial-composite
description: Supports evidence-traceable forensic facial composite research and structured facial description. Use when organizing FISWG, IAI, IFSA, NIST/OSAC, anatomy, or eyewitness-memory sources, documenting image limitations, or preparing later composite workflows.
compatibility: Requires the local knowledge/, schemas/, scripts/, and docs/ directories. Verify external sources at their official publisher pages before citation.
metadata:
  version: "0.1.2-prompt-workflow"
---

# Forensic Facial Composite

This skill is being built in phases. Phase 0 establishes the project and source controls. Phase 1 acquires and registers professional material. Phase 2 provides the source-linked 19-component ontology and observation boundaries. Phase 3 provides validated data structures. Phase 4 provides an evidence-bound image-description workflow.

## Source handling

- Treat `knowledge/source_manifest.yaml` as the public source registry.
- Preserve publisher URL, version, date, access status, and license status. The registry links to publishers; it does not bundle third-party originals.
- Do not infer a current standard from an older edition. Mark drafts, historical editions, access failures, and unclear licenses explicitly.
- Do not use a source as an operational rule until its scope and limitations have been reviewed.

## Current knowledge layer

Read `knowledge/ontology/facial-components.yaml` for the FISWG component taxonomy, `knowledge/ontology/descriptors.yaml` for controlled dimensions and states, and `knowledge/observability/rules.md` for image quality, laterality, spatial relation, asymmetry, and stability rules.

## Data structures

Read `schemas/facial_profile.schema.json` for the unified profile, `schemas/feature_observation.schema.json` for V1.1 observations, and `scripts/validate_schemas.py` for the project validation gate.

## Image workflow

Read `docs/image-observation-protocol.md` before image analysis. Use `scripts/image_description.py` to review a structured image-derived Profile only after the host has actually observed the authorized image. Without vision or authorization, report limitations instead of facial traits.

For a manual image-generation test, record eyebrow/brow-ridge appearance, upper and lower lips separately, face composition, and supported spatial relations in the image Profile. Use `scripts/prompt_compiler.py` with truthful `--vision-attested --image-authorized` flags to compile JSON or `--format text`. The compiler only includes accepted, evidence-backed observations and relations. Age appearance, gender presentation, and temporary expression are rendering cues, never verified identity, exact age, or personality. The user runs external image tools and judges likeness.

After user review of a generated result, record the actual failure modes and add `prompt_focus` entries referencing accepted observation and relation IDs. Give the original image priority when revising observations; generated images are evidence of prompt failure, not evidence of the subject's appearance. Keep viewpoint in internal quality records and omit it from generation prompts. Chinese terminology from CN03 is limited to qualitative observation; see `docs/image-observation-protocol.md`.

## Planned next phases

Phase 5 will add a non-leading memory interview workflow. The current prompt compiler is an early, image-only Phase 6 preview; model adapters and the full Phase 6 workflow remain future work.
