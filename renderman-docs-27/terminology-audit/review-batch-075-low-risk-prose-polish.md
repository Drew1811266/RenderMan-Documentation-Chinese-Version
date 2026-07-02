# Review Batch 075: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 074. This batch targets PxrSurface training/resource pages plus Maya, Katana, and Houdini workflow/UI pages where ordinary English remains in Chinese prose.

Preserve exact product names, node names, parameter labels, UI labels, shelf/menu names, page/resource titles where needed, acronyms, paths, and code identifiers. Translate ordinary prose terms such as start here, dielectric/conductive materials, metallic workflow, layering, geometry, home, archives, preferences, user interface, sections, nodes, presets, parameters, triple bar, stylized looks, beginner macro, daisy-chain, shading node, pane, tool, network, integrator, depth of field, camera properties, and sampling when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/599163179-PxrSurface.html` | 11/low | Translate PxrSurface training/resource prose around start here, dielectric/conductive materials, metallic workflow, and layering while preserving PxrSurface and page titles. |
| 2 | `RFM27/544539616-Geometry in Maya.html` | 11/low | Translate Maya geometry navigation prose and page labels while preserving product names. |
| 3 | `RFM27/544539308-RenderMan Preferences.html` | 11/low | Translate preferences navigation labels while preserving Maya Preferences, OpenColorIO, and Preset Browser names. |
| 4 | `RFM27/544538919-User Interface in Maya.html` | 11/low | Translate Maya UI prose around interface sections, string tokens, nodes, presets, parameters, and triple-bar menu while preserving shelf/menu names. |
| 5 | `RFK27/546178301-Stylized Looks in Katana Overview.html` | 11/low | Translate Katana stylized-look setup prose around beginner macro, daisy-chain, macro, and shading node while preserving node labels. |
| 6 | `RFH27/544646266-Setup.html` | 11/low | Translate Houdini setup prose around /out pane, ROP tool, RIS Network, and integrator VOP while preserving exact UI/node labels. |
| 7 | `RFH27/544644900-Depth of Field.html` | 11/low | Translate depth-of-field prose while preserving camera/parameter labels. |

## Results

- `RU/599163179-PxrSurface.html`: 11/low -> 2/low. Translated PxrSurface training/resource prose around start here, dielectric/conductive materials, metallic workflow, and layering while preserving PxrSurface and page titles.
- `RFM27/544539616-Geometry in Maya.html`: 11/low -> 0/low. Translated Maya geometry navigation prose and page labels while preserving product names.
- `RFM27/544539308-RenderMan Preferences.html`: 11/low -> 1/low. Translated preferences navigation labels while preserving Maya Preferences, OpenColorIO, and Preset Browser names.
- `RFM27/544538919-User Interface in Maya.html`: 11/low -> 0/low. Translated Maya UI prose around interface sections, string tokens, nodes, presets, parameters, and triple-bar menu while preserving shelf/menu names.
- `RFK27/546178301-Stylized Looks in Katana Overview.html`: 11/low -> 2/low. Translated Katana stylized-look setup prose around beginner macro, daisy-chain, macro, and shading node while preserving Nodegraph/Tab and node labels.
- `RFH27/544646266-Setup.html`: 11/low -> 5/low. Translated Houdini setup prose around /out pane, ROP tool, RIS Network, and integrator VOP while preserving exact UI/node labels.
- `RFH27/544644900-Depth of Field.html`: 11/low -> 6/low. Translated depth-of-field prose while preserving camera/parameter labels.

Batch 075 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 671 / 816 = 82.23%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2665 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
