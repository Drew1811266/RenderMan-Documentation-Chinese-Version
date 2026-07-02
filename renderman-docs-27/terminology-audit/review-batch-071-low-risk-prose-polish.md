# Review Batch 071: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 070. This batch targets content-heavy RenderMan University prose and selected Maya/Katana/Solaris workflow pages where ordinary English remains inside Chinese sentences.

Preserve exact product names, node names, parameter labels, UI labels, AOV/LPE acronyms, filenames, page titles where they are asset names, and RenderMan/host-DCC identifiers. Translate ordinary prose terms such as machine learning denoiser, turn-around, test, final render times, full convergence, ingest, rendered file, project, references, texturing, lookdev, materials, inspiration, images, software, reference board, metallic/non-metallic, pattern, instances, seed, slider value, filters, primitive, display driver, integrator, material/shader, energy, brass, chrome, and bronze when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/657621139-Treasure Denoising.html` | 14/low | Translate denoising prose around machine learning denoiser, turnaround/test/final render time, convergence, ingest, rendered EXR file, and Denoise application. |
| 2 | `RU/657162426-Hippie Dragon References.html` | 14/low | Translate reference-board prose around project, references, texturing, lookdev, materials, inspiration, images, software, and reference board while preserving PureRef. |
| 3 | `RU/632783516-Lama Car Paints.html` | 14/low | Translate Lama car-paint prose around solid/metallic/non-metallic/material wording while preserving Lama, BAC, and MonoR names. |
| 4 | `RFM27/544543597-Variation of Instances in Maya.html` | 14/low | Translate Maya instance variation prose around Pattern node, instancer attributes, instances, seed, color, slider value, and hue while preserving exact UI/parameter labels. |
| 5 | `RFK27/546178680-Display & Sample Filters in Katana.html` | 14/low | Translate display/sample filter prose while preserving Katana node names and exact Material/NetworkMaterial/MaterialAssign labels. |
| 6 | `RFH27/634748959-RenderMan Render Settings.html` | 14/low | Translate USD Render Settings prose around primitive, display driver, integrator, display/sample filters, filename, and render settings while preserving RenderMan LOP/node labels. |
| 7 | `RU/619773953-Dielectrics and Conductors.html` | 13/low | Translate dielectric/conductor/material/shader/energy/metal prose while preserving lesson titles where appropriate. |

## Results

- `RU/657621139-Treasure Denoising.html`: 14/low -> 2/low. Translated machine-learning denoiser, turnaround/test/final render time, convergence, rendered EXR file, and application prose while preserving Treasure and Render Elements naming.
- `RU/657162426-Hippie Dragon References.html`: 14/low -> 0/low. Translated project, references, texturing, lookdev, materials, inspiration, images, software, and reference-board prose while preserving PureRef as the software name.
- `RU/632783516-Lama Car Paints.html`: 14/low -> 2/low. Translated Lama car-paint prose around solid/metallic/non-metallic/material wording while preserving Lama, BAC, MonoR, Solid, and Metallic labels.
- `RFM27/544543597-Variation of Instances in Maya.html`: 14/low -> 9/low. Translated Pattern node, instance, seed, color, slider value, and hue prose while preserving exact Maya/UI/parameter labels such as Particle ID, Object Index, Vary Source, Primvar, and Variable Name.
- `RFK27/546178680-Display & Sample Filters in Katana.html`: 14/low -> 2/low. Translated display/sample filter prose while preserving Katana node names and exact Material/NetworkMaterial/MaterialAssign labels.
- `RFH27/634748959-RenderMan Render Settings.html`: 14/low -> 10/low. Translated USD Render Settings prose around primitive, display driver, integrator, display/sample filters, filename, and render settings while preserving RenderMan LOP/node labels.
- `RU/619773953-Dielectrics and Conductors.html`: 13/low -> 0/low. Translated dielectric/conductor/material/shader/energy/metal prose, including brass/chrome/bronze as Chinese metal names.

Batch 071 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 643 / 816 = 78.80%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2705 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
