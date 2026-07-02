# Review Batch 049: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 048. This batch targets RenderMan node-reference prose, RenderMan University resource/learning prose, Katana orientation prose, and Maya depth-of-field prose.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, resource names, artist names, and acronyms. Translate ordinary prose terms such as kelvin, color temperatures, cool/warm colors, exposure, roughness/diffuse maps, grunge/smudge/edge-breakup maps, diffuse/roughness/anisotropy networks, texture/specular/bump maps, shader, community, external learning, training resources, computer graphics, animated films, courses, professionals, tutorials, projects, artists, surface orientation, handedness, reflection, geometric primitives, surface normals, inside-out, culling, shading, solids, single-sided, backface culling, shading network, texture maps, procedural patterns, workflow, depth of field, viewport render, focus region, object details, viewport, and focus-puller prose when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542222617-PxrBlackBody.html` | 31/low | Translate temperature/color-temperature/cool-warm/exposure prose while preserving parameter names and output names. |
| 2 | `RU/609157121-Grunge Maps Vol.1.html` | 30/low | Translate resource labels, roughness/diffuse-map, grunge/smudge/edge-breakup, diffuse-network, roughness-map, and anisotropy-network prose. |
| 3 | `RU/608829457-Best Practices - Wood Table.html` | 30/low | Translate texture-map, diffuse/albedo/specular/bump/roughness/best-practice/shader prose while preserving lesson labels and BumpRoughness. |
| 4 | `RU/506298373-External Learning.html` | 30/low | Translate community/external-learning/training-resource, computer-graphics, animated-film, course/professional, DCC, tutorial/project/artist prose while preserving source names. |
| 5 | `RFK27/546178221-Surface Orientation.html` | 30/low | Translate surface-orientation, handedness, reflection, geometric-primitive, normal, culling, shading, solid, single-sided, and backface-culling prose while preserving UI values. |
| 6 | `REN27/542224681-PxrRGBtoNG.html` | 28/low | Translate shading-network, texture-map, procedural-pattern, and workflow prose while preserving resultNG and parameter names. |
| 7 | `RFM27/544541982-Depth of Field in Maya.html` | 27/low | Translate DOF/focus/viewport/object-details/focus-puller prose while preserving Maya UI labels and related page titles. |

## Results

Edited 42 visible article text-node update operations across 7 pages. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `REN27/542222617-PxrBlackBody.html` | 3/low | Translated temperature/color-temperature/cool-warm/exposure prose while preserving parameter names and output names. |
| 2 | `RU/609157121-Grunge Maps Vol.1.html` | 11/low | Translated resource labels, roughness/diffuse-map, grunge/smudge/edge-breakup, diffuse-network, roughness-map, and anisotropy-network prose. |
| 3 | `RU/608829457-Best Practices - Wood Table.html` | 11/low | Translated texture-map, diffuse/albedo/specular/bump/roughness/best-practice/shader prose while preserving lesson labels and BumpRoughness. |
| 4 | `RU/506298373-External Learning.html` | 7/low | Translated community/external-learning/training-resource, computer-graphics, animated-film, course/professional, DCC, tutorial/project/artist prose while preserving source names. |
| 5 | `RFK27/546178221-Surface Orientation.html` | 6/low | Translated surface-orientation, handedness, reflection, geometric-primitive, normal, culling, shading, solid, single-sided, and backface-culling prose while preserving UI values. |
| 6 | `REN27/542224681-PxrRGBtoNG.html` | 0/low | Translated shading-network, texture-map, procedural-pattern, and workflow prose while preserving resultNG and parameter names. |
| 7 | `RFM27/544541982-Depth of Field in Maya.html` | 28/low | Translated DOF/focus/viewport/object-details/focus-puller prose while preserving Maya UI labels and related page titles. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 32 flagged terms, and 3007 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
