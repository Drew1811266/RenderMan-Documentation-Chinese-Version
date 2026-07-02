# Review Batch 070: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 069. This batch targets RenderMan node-reference pages plus Houdini Solaris/Kaboom pages where ordinary English remains mixed into Chinese prose.

Preserve exact product names, node names, parameter labels, UI labels, enum values, file names, paths, acronyms, and renderer identifiers. Translate ordinary prose terms such as specular, procedural, roughness, signal, bump, network, remap, clamp, channel, manifold, shading graph, object, seed, light filter, multiplier, contribution, combine mode, geometry attribute, opinion, object node, spare parameter, and install-button prose when they are explanatory wording rather than exact identifiers. Keep USD/Hydra terms as technical names where needed; correct HDA expansion to Houdini Digital Asset.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542220045-LamaSheen.html` | 14/low | Translate sheen prose around specular lobes, procedural texture, roughness, signal, bump, RenderMan network, and node wording while preserving parameter labels. |
| 2 | `REN27/542224612-PxrRemap.html` | 14/low | Translate remap/clamp/channel prose while preserving Bias, Gain, input/output names, and parameter labels. |
| 3 | `REN27/542225110-PxrTileManifold.html` | 14/low | Translate manifold, shading graph, grout, object, seed, and color-output prose while preserving node names, parameter labels, and attribute identifiers. |
| 4 | `REN27/542229435-PxrIntMultLightFilter.html` | 14/low | Translate light-filter, multiplier, diffuse/specular contribution, saturation, tint, and combine-mode prose while preserving node and parameter labels. |
| 5 | `RFH27/544640429-Solaris.html` | 14/low | Translate Solaris overview/navigation title fragments while preserving Solaris, USD, Hydra Renderer Delegate, husk, and product names. |
| 6 | `RFH27/544640572-Solaris Geometry Workflow.html` | 14/low | Translate geometry attribute/opinion/object node/spare parameter prose while preserving LOP and UI choice labels. |
| 7 | `RFH27/544647152-Installation.html` | 14/low | Correct HDA expansion to Houdini Digital Asset and translate Asset menu/install-button prose while preserving Kaboom Box and filename labels. |

## Results

- `REN27/542220045-LamaSheen.html`: 14/low -> 5/low. Translated specular-lobe, procedural-texture, roughness, signal, bump, RenderMan network, and node wording while preserving Sheen, Fresnel, parameter labels, and node names.
- `REN27/542224612-PxrRemap.html`: 14/low -> 7/low. Translated remap, clamp, Gamma/channel prose while preserving Bias, Gain, input/output names, and parameter labels.
- `REN27/542225110-PxrTileManifold.html`: 14/low -> 0/low. Translated manifold, shading graph, grout, object, seed, and color-output prose while preserving node names, parameter labels, and attribute identifiers.
- `REN27/542229435-PxrIntMultLightFilter.html`: 14/low -> 0/low. Translated light-filter, multiplier, diffuse/specular contribution, saturation, tint, and combine-mode prose while preserving node and parameter labels.
- `RFH27/544640429-Solaris.html`: 14/low -> 8/low. Translated Solaris navigation/title fragments and added readable Hydra render delegate explanation while preserving Solaris, USD, Hydra Renderer Delegate, husk, and product names.
- `RFH27/544640572-Solaris Geometry Workflow.html`: 14/low -> 5/low. Translated geometry attribute/opinion/object node/spare parameter prose while preserving RenderGeometrySettings, LOP, RfH, and UI choice labels.
- `RFH27/544647152-Installation.html`: 14/low -> 13/low. Corrected HDA expansion to Houdini Digital Asset and translated Asset menu/install-button prose while preserving Kaboom Box, Install Asset Library, and filename labels.

Batch 070 total progress contribution: 7 / 7 pages complete. Overall terminology review progress is now 636 / 816 = 77.94%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2730 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
