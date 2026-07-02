# Review Batch 033: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 032. This batch targets pages with ordinary English still embedded in Chinese explanatory prose across Solaris lookdev, RenderMan pattern/reference material, RenderMan University modeling/material pages, and Katana setup/baking workflows.

Preserve exact RenderMan node names, DCC UI labels, menu labels, parameter labels, file identifiers, and artwork/project names. Translate ordinary prose terms such as material, shading, network, texture, model, surface, lighting, bake, and workflow when they are not exact labels.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFH27/544641013-Solo Material - Patterns.html` | 45/low | Translate solo/lookdev/visualizer prose while preserving the Visualizer node concept and exact UI names. |
| 2 | `REN27/542222881-PxrBumpMixer.html` | 45/low | Translate bump-map, surface-gradient, masking, scalar/channel, and normal-mixing prose while preserving node/output labels. |
| 3 | `RU/654639145-Toy Car Modeling.html` | 44/low | Translate modeling/photogrammetry/reference/topology/shading workflow prose. |
| 4 | `RU/606240846-Lama Metals.html` | 44/low | Translate metal/material/IOR/reference/noise/map/detail prose while preserving Lama/Pxr node and parameter names. |
| 5 | `RFK27/546179060-Baking in Katana.html` | 44/low | Translate bake/pattern-network/texture/point-cloud/render prose while preserving Katana node and render-mode labels. |
| 6 | `RFK27/546177260-Scene Setup.html` | 44/low | Translate ordinary setup/render/material prose while preserving Katana node names, menus, attributes, and parameter labels. |

## Results

Edited 43 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFH27/544641013-Solo Material - Patterns.html` | 4/low | Translated lookdev, shading-node, material-network, layer-mask, texture-map, and visualizer prose while preserving `solo`, `un-solo`, and `visualize` labels. |
| 2 | `REN27/542222881-PxrBumpMixer.html` | 10/low | Translated bump-map, masking, scalar/channel, surface-gradient, and normal-mixing prose while preserving `resultNG`, node names, and parameter labels. |
| 3 | `RU/654639145-Toy Car Modeling.html` | 1/low | Translated photogrammetry, reference data, model, topology, shading, surface behavior, and real-time rendering prose. |
| 4 | `RU/606240846-Lama Metals.html` | 10/low | Translated metal/material, reference, real-world metal, single-map, detail, tech-metal, noise, bump, roughness, and parameter prose while preserving node/parameter names. |
| 5 | `RFK27/546179060-Baking in Katana.html` | 8/low | Translated bake, pattern-network, texture-image, point-cloud, hider setting, and render prose while preserving Katana node/render labels. |
| 6 | `RFK27/546177260-Scene Setup.html` | 44/low | Reviewed and polished setup/material/render prose; remaining English is dominated by Katana node, menu, tab, attribute, and parameter labels. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 54 flagged terms, and 3295 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
