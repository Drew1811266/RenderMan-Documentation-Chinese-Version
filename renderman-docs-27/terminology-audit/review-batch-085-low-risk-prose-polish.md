# Review Batch 085: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 084. This batch targets glass parameter prose, UDIM workflow prose, camera/split-diopter prose, Blender/Cycles conversion prose, Stylized Canvas prose, LamaMix prose, license-update prose, and selected bridge navigation pages.

Preserve exact product names, node names, parameter names, enum names, menu paths, file names, URLs, acronyms, and proper nouns. Translate ordinary prose terms such as Bold Face, Italicized, Specular, Glass Parameters, Roughness, Ior, Transmission, Atlas Style, Value, Alternative, UV tile, world space, pattern node, Shading Network, Lama network, Display Filter, layers, layer, layering, color AOV, BG texture, Comp, beauty, over operator, mix, mask, Get License, File Menu, As Archive, cameras, Motion Blur, Bokeh, Camera Projections, Workflow, Adding, Displacement, and Subdivision when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542215694-Glass Parameters.html` | 7/low | Translate glass parameter prose around headings, Specular, Roughness, Ior, Thin, Transmission, and Fundamentals while preserving parameter labels. |
| 2 | `RFB27/544638640-UDIMs in Blender.html` | 6/low | Translate UDIM workflow/table prose around Atlas Style, Value, Alternative, and UV tile while preserving file patterns. |
| 3 | `REN27/542231710-Split Diopter.html` | 6/low | Translate split-diopter prose around Toy Story and world space while preserving film title/proper names. |
| 4 | `REN27/542222811-PxrBlenderPrincipledInputs.html` | 6/low | Translate Blender Principled conversion prose around pattern node, Shading Network, and Lama network while preserving node names. |
| 5 | `REN27/542221812-Stylized Canvas.html` | 6/low | Translate Stylized Canvas prose around Display Filter, layers, layer, layering, color AOV, BG texture, Comp, and beauty while preserving parameter labels. |
| 6 | `REN27/542219328-LamaMix.html` | 6/low | Translate LamaMix prose around over operator, material1/2, mix, and mask while preserving parameter labels. |
| 7 | `REN27/542212468-Updating Existing Installations.html` | 6/low | Translate license-update prose around Get License and License App while preserving log lines and platform names. |
| 8 | `RFM27/544543164-Manual RIB Export.html` | 5/low | Translate manual RIB export prose around File Menu and As Archive while preserving Maya menu labels. |
| 9 | `RFH27/544644797-Cameras in Houdini.html` | 5/low | Translate Houdini camera navigation prose and link titles while preserving RenderMan names. |
| 10 | `RFH27/544640549-Geometry in Solaris.html` | 5/low | Translate Solaris geometry navigation labels while preserving product/context names. |

## Results

Completed 10 / 10 pages. Ordinary explanatory English was translated where it affected Chinese reading flow, while protected product names, node names, UI labels, parameter names, file/menu labels, acronyms, and proper nouns were preserved.

| Order | Page | Result |
|---:|---|---|
| 1 | `REN27/542215694-Glass Parameters.html` | 7/low -> 4/low; remaining candidates are protected parameter/title terms such as `Ior`, `Thin`, and `Transmission`. |
| 2 | `RFB27/544638640-UDIMs in Blender.html` | 6/low -> 0/low. |
| 3 | `REN27/542231710-Split Diopter.html` | 6/low -> 4/low; remaining candidates are preserved proper-title words in `Toy Story`. |
| 4 | `REN27/542222811-PxrBlenderPrincipledInputs.html` | 6/low -> 6/low; remaining candidates are preserved node/renderer names such as `Cycles` and `Principled`. |
| 5 | `REN27/542221812-Stylized Canvas.html` | 6/low -> 2/low; remaining candidates are preserved labels/titles such as `Layer` and `Texture`. |
| 6 | `REN27/542219328-LamaMix.html` | 6/low -> 3/low; remaining candidates are preserved parameter or node-context terms such as `Material` and `mix`. |
| 7 | `REN27/542212468-Updating Existing Installations.html` | 6/low -> 6/low; remaining candidates are preserved UI/product-label words in `Pixar License App` and `Get License`. |
| 8 | `RFM27/544543164-Manual RIB Export.html` | 5/low -> 5/low; remaining candidates are preserved Maya UI/menu-label words in `File Menu > Export All > As Archive`. |
| 9 | `RFH27/544644797-Cameras in Houdini.html` | 5/low -> 0/low. |
| 10 | `RFH27/544640549-Geometry in Solaris.html` | 5/low -> 0/low. |

## Validation

Passed after Batch 085:

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2580 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`
- `python3 tools/audit_official_layout_alignment.py`: 816 / 816 static pages pass, 816 / 816 browser-sampled pages pass, 0 unrewritten Confluence links.

Overall terminology review progress: 753 / 816 = 92.28%.
