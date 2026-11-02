# Forensic Facial Composite Skill

An in-progress Agent Skill for evidence-traceable facial description and composite prompt preparation. It is a research tool, not an identity recognition system or a certified forensic method.

## Status

The current release contains a 19-component facial ontology, image observation rules, eight JSON schemas, example profiles, an image-description reviewer, and an image-only prompt compiler. The memory interview and full model-adapter workflows remain planned. Generated-image likeness has not been validated; users judge visual results themselves.

## Use

Read [`SKILL.md`](SKILL.md) and the [image observation protocol](docs/image-observation-protocol.md). A host with actual vision capability creates and reviews a structured Profile from an authorized image. The scripts validate and compile that Profile; they do not inspect image pixels or generate images.

```text
python scripts/validate_schemas.py
python scripts/image_description.py PATH_TO_PROFILE --vision-attested --image-authorized
python scripts/prompt_compiler.py PATH_TO_PROFILE --vision-attested --image-authorized --format text
python scripts/prompt_lint.py PATH_TO_PROFILE
python scripts/prompt_compiler_v2.py PATH_TO_PROFILE --format text --model chinese_model
```

`prompt_lint.py` scores a compiled prompt for instruction leakage, length, vague qualifiers and missing identity anchors before any image is generated. `prompt_compiler_v2.py` is a preview of the identity-first compiler; it does not replace the reviewed Phase 4 compiler yet. See [`docs/likeness-diagnosis-and-optimization.md`](docs/likeness-diagnosis-and-optimization.md).

Each feature observation must include a controlled `dimension_id` so that distinct dimensions of one facial feature (for example, upper-lip vermilion height and vermilion-border shape) are not collapsed during conflict checks. The reviewer also reports `likeness_prompt_readiness`; this is a completeness gate for the key anchors (outline, layout, mouth, and brow-eye regions), not a likeness score or a prediction of generated-image similarity. Manual generation comparisons are documented in [`docs/generation-evaluation-protocol.md`](docs/generation-evaluation-protocol.md); the project records the prompt and user judgment while the user runs external image tools.

Use the attestation flags only when the corresponding review and authorization have occurred. `examples/` contains synthetic structural examples, not retained test photos.

## Repository

- `docs/`: public protocol, documentation index, and changelog.
- `knowledge/`: project-authored ontology, rules, terminology, and public source metadata.
- `schemas/`, `examples/`, `scripts/`: data contracts, examples, and local tools.
- `forensic-facial-composite/`: Agent Skills entry for the repository layout.

The [public source manifest](knowledge/source_manifest.yaml) records publisher links, source versions, access status, and rights notes. Downloaded third-party originals and development research are held in a local ignored archive and are not part of the publishable tree.

## Rights and limitations

Project-authored code and content are released under the [GNU Lesser General Public License v3.0 (LGPL-3.0)](../LICENSE); [`COPYING`](../COPYING) contains the GPL-3.0 text that LGPL-3.0 references. Third-party standards and papers remain under their publishers' terms; a public download link does not grant redistribution rights. Do not treat project translations or summaries as publisher-approved standards.
