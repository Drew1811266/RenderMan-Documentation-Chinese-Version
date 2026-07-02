# Review Batch 079: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 078. This batch targets color-management/tutorial pages and RenderMan node-reference pages where ordinary English remains in Chinese prose.

Preserve exact product names, node names, parameter labels, UI labels, file names, paths, acronyms, and proper names. Translate ordinary prose terms such as scene, config file, viewer, workflow, color profile, shading tasks, lobe, look, gain, weighting, Fundamentals, bump, look-dev, rolling/global shutter, shutter function, clamp, gamma function, bump mapping, infinite, world space, trace groups, pattern node, bump roughness map, manifold, amount, and unfiltered/closest when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/657227810-Stirling Color Management.html` | 9/low | Translate color-management prose around scene setup, config file, viewer, workflow, and color profiles while preserving ACES/OCIO/RMANTREE. |
| 2 | `RU/608796697-Best Practices - PxrSurface.html` | 9/low | Translate PxrSurface best-practices prose around shading tasks, lobes, look, gain, weighting, and next steps while preserving component labels. |
| 3 | `RU/599523361-R.F. - Patterns.html` | 9/low | Translate RenderMan Fundamentals Patterns prose around bump, material variation, procedural grime, custom outputs, and look-dev while preserving course titles. |
| 4 | `REN27/542231817-Camera Shutter.html` | 9/low | Translate rolling/global shutter and shutter-function prose while preserving parameter value labels and RIS/XPU names. |
| 5 | `REN27/542223459-PxrFacingRatio.html` | 9/low | Translate facing-ratio prose around clamp, gamma function, and bump mapping while preserving parameter labels and coordinate names. |
| 6 | `REN27/542223198-PxrDirt.html` | 9/low | Translate PxrDirt prose around cosine distribution, infinite distance, world space, object/camera coordinate names, and trace groups while preserving parameter labels. |
| 7 | `REN27/542222907-PxrBumpRoughness.html` | 9/low | Translate Bump Roughness prose around Pattern node, bump roughness map, manifold, amount, and unfiltered/closest while preserving node/parameter labels and proper names. |

## Results

- `RU/657227810-Stirling Color Management.html`: 9/low -> 1/low. Translated color-management prose around scene setup, config file, viewer, workflow, and color profiles while preserving ACES/OCIO/RMANTREE.
- `RU/608796697-Best Practices - PxrSurface.html`: 9/low -> 1/low. Translated PxrSurface best-practices prose around shading tasks, lobes, look, gain, weighting, and next steps while preserving component labels.
- `RU/599523361-R.F. - Patterns.html`: 9/low -> 5/low. Translated RenderMan Fundamentals Patterns prose around bump, material variation, custom outputs, and look-dev while preserving course titles.
- `REN27/542231817-Camera Shutter.html`: 9/low -> 1/low. Translated rolling/global shutter and shutter-function prose while preserving parameter value labels and RIS/XPU names.
- `REN27/542223459-PxrFacingRatio.html`: 9/low -> 4/low. Translated facing-ratio prose around clamp, Gamma function, and bump mapping while preserving parameter labels and coordinate names.
- `REN27/542223198-PxrDirt.html`: 9/low -> 6/low. Translated PxrDirt prose around infinite distance, world space, coordinate names, and trace groups while preserving parameter labels.
- `REN27/542222907-PxrBumpRoughness.html`: 9/low -> 8/low. Translated Bump Roughness prose around Pattern node, manifold, amount, and unfiltered/closest while preserving node/parameter labels and proper names.

Batch 079 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 699 / 816 = 85.66%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2631 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
