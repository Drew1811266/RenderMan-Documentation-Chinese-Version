# Review Batch 086: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 085. This batch targets remaining RenderMan University resource/tutorial index pages, RenderMan shutter prose, bridge navigation panels, Katana camera navigation, PxrMetallicWorkflow explanatory prose, and implicit-surface prose.

Preserve exact product names, resource titles, artist names, node names, parameter names, RIB snippets, UI labels, DCC names, file-format names, URLs, and proper nouns. Translate ordinary prose terms and navigation labels where English is only descriptive wording rather than an identifier.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/606306371-Official Example Scenes.html` | 12/low | Review RenderMan Digital Studio and Point Reyes Electric as preserved resource/proper names. |
| 2 | `RU/599654509-Tutorials.html` | 10/low | Review tutorial titles and artist names as preserved proper names. |
| 3 | `RU/600113259-Texture Maps.html` | 9/low | Review texture pack names and translate descriptive preset wording where appropriate. |
| 4 | `REN27/542231276-Shutter.html` | 9/low | Clarify shutter placeholder prose around `opentime` and `closetime` while preserving RIB identifiers. |
| 5 | `RFH27/544643637-Geometric Settings.html` | 7/low | Translate Houdini geometric-settings navigation labels while preserving `Pref` and `primvars`. |
| 6 | `RFB27/544639419-Rendering in Blender.html` | 7/low | Translate Blender rendering navigation labels while preserving AOV and feature names. |
| 7 | `RFB27/544637526-Geometry in Blender.html` | 6/low | Translate Blender geometry navigation labels while preserving OpenVDB and exact feature names where needed. |
| 8 | `RFK27/546178629-Cameras in Katana.html` | 5/low | Translate Katana camera navigation labels while preserving Katana and exact node/product names. |
| 9 | `REN27/542224201-PxrMetallicWorkflow.html` | 5/low | Translate ordinary pattern/workflow prose and normalize DCC wording while preserving parameter labels. |
| 10 | `REN27/542213207-Implicit Surfaces.html` | 5/low | Translate ordinary fluid-cache wording while preserving RiBlobby, OpenVDB, Maya Fluids, and Bifrost names. |

## Results

Completed 10 / 10 pages. Eight pages received text-node edits; two RenderMan University index pages were reviewed and left unchanged because the remaining English consists of resource titles, tutorial titles, artist names, and other proper names.

| Order | Page | Result |
|---:|---|---|
| 1 | `RU/606306371-Official Example Scenes.html` | 12/low -> 12/low; remaining candidates are preserved resource/company/artist proper names such as `RenderMan Digital Studio`, `Point Reyes Electric`, and `Eugene Riecansky`. |
| 2 | `RU/599654509-Tutorials.html` | 10/low -> 10/low; remaining candidates are preserved tutorial titles and artist names. |
| 3 | `RU/600113259-Texture Maps.html` | 9/low -> 7/low; translated descriptive preset labels while preserving texture-pack names. |
| 4 | `REN27/542231276-Shutter.html` | 9/low -> 9/low; clarified prose around `opentime`, `closetime`, and Bezier curves while preserving RIB placeholders and parameter identifiers. |
| 5 | `RFH27/544643637-Geometric Settings.html` | 7/low -> 0/low. |
| 6 | `RFB27/544639419-Rendering in Blender.html` | 7/low -> 1/low; remaining candidate is preserved `Holdouts` feature wording. |
| 7 | `RFB27/544637526-Geometry in Blender.html` | 6/low -> 0/low. |
| 8 | `RFK27/546178629-Cameras in Katana.html` | 5/low -> 0/low. |
| 9 | `REN27/542224201-PxrMetallicWorkflow.html` | 5/low -> 5/low; remaining candidates are preserved parameter/product/workflow names such as `Metallic`, `Substance Designer`, and `Base Color`. |
| 10 | `REN27/542213207-Implicit Surfaces.html` | 5/low -> 2/low; remaining candidates are preserved DCC/product names `Maya Fluids` and `Bifrost`. |

## Validation

Passed after Batch 086:

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2575 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`
- `python3 tools/audit_official_layout_alignment.py`: 816 / 816 static pages pass, 816 / 816 browser-sampled pages pass, 0 unrewritten Confluence links.

Overall terminology review progress: 763 / 816 = 93.50%.
