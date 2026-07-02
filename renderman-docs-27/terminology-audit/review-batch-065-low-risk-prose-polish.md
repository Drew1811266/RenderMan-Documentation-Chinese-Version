# Review Batch 065: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 064. This batch targets the next highest remaining residual-English pages across RenderMan University rendering/shading lessons, RenderMan license-server installation pages, diffuse parameter documentation, and PxrAdjustNormal.

Preserve exact product names, package names, paths, button labels, file names, node names, parameter labels, AOV/LPE acronyms, and official lesson/film titles. Translate ordinary prose terms such as final image, passes, light, headlights, fog layers, video, compositing, look, shading path, shading network, practical lessons, randomisation, props, instances, procedural dirt, installer, license server, downloads, specular/diffuse/roughness/exponent, pattern, bump mapping, bump map, normals, and normal pattern when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/567017582-The Hunted Finalizing.html` | 18/low | Translate rendering/compositing prose around final image, passes, lights, fog layers, video, recompositing, comp, final render, and looks while preserving media filenames and AOV/LPE acronyms. |
| 2 | `RU/599163154-Shading Path.html` | 18/low | Translate RenderMan University shading-path titles and descriptions while preserving product names, PxrSurface, MaterialX Lama, ILM, Pixar University, Elucidae, and Win or Lose. |
| 3 | `RU/624918545-Shading Practical Lessons.html` | 18/low | Translate practical shading lesson titles/descriptions around cupcake shading, randomisation, props, instances, and procedural dirt while preserving official lesson names when needed. |
| 4 | `REN27/542212504-Installing The License Server.html` | 17/low | Translate license-server installer prose while preserving product/package names, button labels, paths, platform names, and package versions. |
| 5 | `REN27/542212629-Windows License Server.html` | 17/low | Translate Windows license-server prose while preserving LicenseApp, Windows paths, service names, package placeholders, and script names. |
| 6 | `REN27/542215119-Diffuse Parameters.html` | 17/low | Translate diffuse-parameter prose around specular model, diffuse gain/color/roughness/exponent, pattern, bump mapping, global bump normal, double-sided, and transmit color while preserving parameter labels. |
| 7 | `REN27/542222488-PxrAdjustNormal.html` | 17/low | Translate PxrAdjustNormal prose around pattern, bump map, normals, bump nodes, normal pattern, bump settings, and bumps while preserving node/parameter labels. |

## Results

- `RU/567017582-The Hunted Finalizing.html`: 18/low -> 0/low. Translated final-image, passes, lights, fog layers, video, recompositing, final-render, comp, and look prose while preserving movie filenames and AOV/LPE acronyms.
- `RU/599163154-Shading Path.html`: 18/low -> 5/low. Translated shading learning-path/resource titles and descriptions while preserving PxrSurface, MaterialX Lama, ILM, Pixar University, Elucidae, and Win or Lose.
- `RU/624918545-Shading Practical Lessons.html`: 18/low -> 1/low. Translated practical shading lesson titles and props/instances/procedural-dirt prose while preserving Pixar University.
- `REN27/542212504-Installing The License Server.html`: 17/low -> 7/low. Translated installer/license-server/download/configuration prose while preserving package/product names, button labels, paths, platform names, sudo/root, and package version strings.
- `REN27/542212629-Windows License Server.html`: 17/low -> 5/low. Translated Windows license-server heading/service prose while preserving paths, LicenseApp, package placeholders, script names, and service/product labels.
- `REN27/542215119-Diffuse Parameters.html`: 17/low -> 8/low. Translated diffuse/specular/pattern/roughness/exponent/bump prose while preserving parameter labels and Double-Sided UI terms.
- `REN27/542222488-PxrAdjustNormal.html`: 17/low -> 0/low. Translated pattern, bump map, normals, bump nodes, normal pattern, bump setting, and bump prose while preserving node/parameter labels.

Batch 065 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 601 / 816 = 73.65%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 19 flagged terms, 2779 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
