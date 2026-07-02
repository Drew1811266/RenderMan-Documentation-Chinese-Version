# Review Batch 074: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 073. This batch targets Houdini OSL/instancing, Blender curves/OpenVDB volumes, RenderMan projection/primvar node references, and a RenderMan University USD workflow page.

Preserve exact product names, node names, parameter labels, UI labels, file names, environment variables, paths, acronyms, data types, and code identifiers. Translate ordinary prose terms such as shader, instancing, curve primitive, hair and fur, pattern, radius, strand variation, density grid, logarithmic falloff, shading, time to first pixel, projection plug-in, Compression/projection prose, primitive variables, pattern graphs, variable, diagnostic output, result, modelling tips and tricks, modeller, render, and model when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544644451-OSL Patterns.html` | 12/low | Translate OSL shader-description prose while preserving environment variables, file extensions, and pxrosl identifiers. |
| 2 | `RFH27/544644181-Instances.html` | 12/low | Translate instancing prose around Houdini instances and material overrides while preserving Copy to Points, Instance OBJ, and Material SOP labels. |
| 3 | `RFB27/544637943-Curves.html` | 12/low | Translate curve/hair/fur prose and PxrHairColor option prose while preserving node and primvar names. |
| 4 | `RFB27/544637687-OpenVDB Volumes in Blender.html` | 12/low | Translate OpenVDB volume prose around shader, density grid, logarithmic falloff, shading, time to first pixel, and off while preserving DSO/OpenVDB labels. |
| 5 | `REN27/542231871-PxrPanini.html` | 12/low | Translate projection plug-in and Panini compression/projection prose while preserving parameter labels. |
| 6 | `REN27/542224365-PxrPrimvar.html` | 12/low | Translate primitive-variable, pattern-graph, variable, diagnostic-output, and result prose while preserving data types and parameter labels. |
| 7 | `RU/405700728-USD Workflows.html` | 11/low | Translate USD workflow prose around modelling tips, modeller, render, and model while preserving page/resource titles. |

## Results

- `RFH27/544644451-OSL Patterns.html`: 12/low -> 10/low. Translated OSL shader-description prose while preserving environment variables, file extensions, `pxrosl:2`, and path/UI labels.
- `RFH27/544644181-Instances.html`: 12/low -> 10/low. Translated instancing prose around Houdini instances and material overrides while preserving Copy to Points, Instance OBJ, and Material SOP labels.
- `RFB27/544637943-Curves.html`: 12/low -> 8/low. Translated curve/hair/fur prose and PxrHairColor option prose while preserving node names, primvar names, and option labels.
- `RFB27/544637687-OpenVDB Volumes in Blender.html`: 12/low -> 2/low. Translated OpenVDB volume prose around shader, density grid, logarithmic falloff, shading, time to first pixel, and Off while preserving DSO/OpenVDB labels.
- `REN27/542231871-PxrPanini.html`: 12/low -> 6/low. Translated projection plug-in and Panini compression/projection prose while preserving parameter labels.
- `REN27/542224365-PxrPrimvar.html`: 12/low -> 0/low. Translated primitive-variable, Pattern-graph, variable, diagnostic-output, and result prose while preserving data types and parameter labels.
- `RU/405700728-USD Workflows.html`: 11/low -> 4/low. Translated USD workflow prose around modelling tips, modeller, render, and model while preserving page/resource titles.

Batch 074 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 664 / 816 = 81.37%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2676 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
