# Review Batch 077: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 076. This batch targets RenderMan node-reference pages, PxrSurface/Lama training material, a Treasure AOV workflow note, and Houdini coordinate/baking workflow pages where ordinary English remains in Chinese prose.

Preserve exact product names, node names, parameter labels, UI labels, file names, paths, acronyms, data types, and mode values. Translate ordinary prose terms such as pattern graphs, primitive variables, variable, shader, coordinate system, pattern, gamma, contrast, import, nodes, template, software versions, group, script, subsurface scattering, procedural object, baking, color parameter, output filename, specular, roughness, bump, properties, and double-sided when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542225473-PxrVariable.html` | 11/low | Translate primitive-variable and pattern-graph prose while preserving parameter labels, data types, and coordinate names. |
| 2 | `REN27/542223036-PxrColorCorrect.html` | 11/low | Translate color-correction prose around pattern, Gamma, contrast, and HSV wording while preserving parameter labels. |
| 3 | `REN27/542215275-Specular Parameters.html` | 11/low | Translate specular/roughness/bump/properties/double-sided explanatory prose while preserving parameter labels and material preset names. |
| 4 | `RU/657391684-Treasure AOVs.html` | 10/low | Translate Treasure AOV workflow prose around import, nodes, template, software versions, group, and script while preserving project/tool names. |
| 5 | `RU/600113153-R.F. - Materials - Lama.html` | 10/low | Translate Lama course prose around subsurface scattering and course-path wording while preserving node/course titles. |
| 6 | `RFH27/544646740-Coordinate System.html` | 10/low | Translate coordinate-system prose around shader, coordinate system, procedural object, transform, and shader parameters while preserving null OBJ and RiCoordinateSystem. |
| 7 | `RFH27/544645511-Baking.html` | 10/low | Translate baking workflow prose around baking, RIS Network, color parameter, and output filename while preserving hider modes and node labels. |

## Results

- `REN27/542225473-PxrVariable.html`: 11/low -> 5/low. Translated primitive-variable and Pattern-graph prose while preserving parameter labels, data types, and coordinate names.
- `REN27/542223036-PxrColorCorrect.html`: 11/low -> 9/low. Translated color-correction prose around Pattern, Gamma, and contrast while preserving parameter labels and HSV labels.
- `REN27/542215275-Specular Parameters.html`: 11/low -> 7/low. Translated specular/roughness/bump/properties/double-sided explanatory prose while preserving parameter labels and material preset names.
- `RU/657391684-Treasure AOVs.html`: 10/low -> 3/low. Translated Treasure AOV workflow prose around import, nodes, template, software versions, group, and script while preserving project/tool names.
- `RU/600113153-R.F. - Materials - Lama.html`: 10/low -> 7/low. Translated Lama course prose around subsurface scattering and course-path wording while preserving node/course titles.
- `RFH27/544646740-Coordinate System.html`: 10/low -> 3/low. Translated coordinate-system prose around shader, coordinate system, procedural object, transform, and shader parameters while preserving null OBJ and RiCoordinateSystem.
- `RFH27/544645511-Baking.html`: 10/low -> 6/low. Translated baking workflow prose around baking, RIS Network, color parameter, and output filename while preserving hider modes and node labels.

Batch 077 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 685 / 816 = 83.95%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2643 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
