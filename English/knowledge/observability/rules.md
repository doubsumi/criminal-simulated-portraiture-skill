# Observability and Evidence Rules

These rules combine S01's scope limits with S02 image-factor guidance and are project rules for later schemas.

## Observation states

- `observed`: visible in the supplied image under the recorded view and quality conditions.
- `reported_memory`: stated by a witness/user; it is not an image observation.
- `not_observable`: the component may be present but pose, occlusion, blur, lighting, resolution, crop, or image artifact prevents a reliable observation.
- `unknown`: no usable evidence was supplied.
- `not_applicable`: the field does not apply to the case.

Never convert `not_observable` or `unknown` into a guessed descriptor.

## Spatial relationships

S01 permits relative descriptions such as eye position relative to face length, nose width relative to eye distances, or ear position relative to facial features. These are qualitative or approximate relationships. Store them as relation records with `relation_type`, `reference_feature`, `comparison_feature`, `direction_or_category`, and `evidence_ref`; do not turn ordinary photographs into calibrated measurements.

Recommended relation types: `above_below`, `medial_lateral`, `proximal_distal`, `relative_width`, `relative_length`, `relative_prominence`, `angle`, `alignment`, and `symmetry_difference`.

## Laterality

Use anatomical right/left only when the view and orientation are established. Add `laterality_basis` (`anatomical`, `image_left`, `image_right`, `unknown`) to each sided observation. Do not map image-left to anatomical-left automatically.

## Asymmetry

Asymmetry is a comparison observation between corresponding right and left structures. It is not an inference that the person has a disease or abnormality. Record the compared structures, the observed difference, view, and evidence. S01 explicitly includes asymmetry for eyebrows, eyes, ears, nose, mouth and other components.

## Stability

Use S03 to record possible change factors such as age, weight, health, expression, grooming, cosmetic alteration and time gap. A stable component is not an immutable identity marker. A transient facial mark requires contemporaneous imagery before absence is meaningful.

## Image quality gate

Before extracting a descriptor, record the relevant S02 factors: resolution/detail, sharpness, illumination, noise, artifacts, occlusion, pose, distortion and crop. A low-quality image can support a limited description; it cannot justify filling every field.
