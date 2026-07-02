# Review Batch 072: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 071. This batch targets RenderMan University resource/topic pages plus Katana and Houdini workflow/FAQ pages where ordinary English remains in Chinese prose.

Preserve exact product names, project/resource names, artist names, node names, UI labels, parameter labels, filenames, AOV acronyms, ROP/VOP names, and code identifiers. Translate ordinary prose terms such as topics, modeling, created by, features, concept, materials, shader, particles, per-particle width primitive variable, geometry type, per-point normals, disks, spheres, group, release, major version change, point release, bug, shaders, output, display filter, pattern, dynamic array, integer, shop pane, shader slot, displacement bound, and material op path when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/608632849-Introduction to Best Practices.html` | 14/low | Translate topic labels and course-title fragments while preserving proper lesson names where useful. |
| 2 | `RU/608337987-Ship Shape.html` | 14/low | Translate project metadata labels and concept/model credits while preserving project and artist names. |
| 3 | `RU/600113366-Materials & Presets.html` | 13/low | Translate material/preset/resource prose while preserving exact pack names where useful. |
| 4 | `RFK27/546177992-Particles in Katana.html` | 13/low | Translate particle prose around particles, per-particle width primitive variable, geometry type, normals, disks, and spheres while preserving pointcloud. |
| 5 | `RFH27/544647299-Frequently Asked Questions.html` | 13/low | Translate FAQ prose around group, release cadence, major/point releases, bug reporting, shaders, and output while preserving forum/product names. |
| 6 | `RFH27/544646545-Stylized Looks in Houdini Overview.html` | 13/low | Translate stylized workflow prose around display filters, AOVs, pattern, dynamic array, integer, stylized looks, and display filter while preserving exact ROP/tool/node labels. |
| 7 | `RFH27/544644703-Creating A Material.html` | 13/low | Translate Houdini material-creation prose around shop pane, Pattern VOP, shader slot, displacement bound, and material op path while preserving node/UI labels. |

## Results

- `RU/608632849-Introduction to Best Practices.html`: 14/low -> 0/low. Translated topic labels and course-title fragments while preserving PxrSurface and the texture-map guide title.
- `RU/608337987-Ship Shape.html`: 14/low -> 2/low. Translated project metadata labels and concept/model credits while preserving Ship Shape, Stylized Looks, artist names, and challenge naming.
- `RU/600113366-Materials & Presets.html`: 13/low -> 4/low. Translated material/preset/resource prose while preserving Holiday Pack 1 and Fun-Da-Mentals as pack/resource names.
- `RFK27/546177992-Particles in Katana.html`: 13/low -> 0/low. Translated particle prose around particles, per-particle width primitive variable, geometry type, normals, disks, and spheres while preserving pointcloud.
- `RFH27/544647299-Frequently Asked Questions.html`: 13/low -> 0/low. Translated FAQ prose around group, release cadence, major/point releases, bug reporting, shaders, and output while preserving forum/product names.
- `RFH27/544646545-Stylized Looks in Houdini Overview.html`: 13/low -> 4/low. Translated stylized workflow prose around display filters, AOVs, Pattern node, dynamic array, integer, stylized looks, and display filter while preserving exact ROP/tool/node labels.
- `RFH27/544644703-Creating A Material.html`: 13/low -> 3/low. Translated Houdini material-creation prose around SHOP pane, Pattern VOP, shader slot, displacement bound, and material op path while preserving node/UI labels.

Batch 072 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 650 / 816 = 79.66%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2695 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
