# Review Batch 029: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish on the next highest-ranked pages. This batch mixes RenderMan core shader/integrator pages, RenderMan University project prose, Maya UI references, and Katana light workflow prose. Edits should translate ordinary English words in Chinese sentences while preserving shader/node names, UI labels, parameter labels, person names, paper titles, and exact technical identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542220743-PxrDisneyBsdf.html` | 48/low -> 8/low | Completed; translated shader parameter prose around specular, diffuse, sheen, clearcoat, maps, bump, and dielectric while preserving Disney/Burley names and parameter labels. |
| 2 | `RU/611680257-SciTech Scene.html` | 47/low -> 31/low | Completed; translated art challenge, hardware, denoise, hybrid-processing, model-credit, and EULA prose while preserving person names, award names, and proper project titles. |
| 3 | `RFM27/544542444-Features.html` | 47/low -> 45/low | Completed conservatively; normalized Maya render-feature prose around Motion Blur, Sampling tab, max samples, denoiser pass, and beauty pass while preserving UI labels. |
| 4 | `RFM27/544542112-Tilt-Shift in Maya.html` | 47/low -> 43/low | Completed conservatively; translated Tilt-Shift explanatory prose while preserving camera/menu/control labels and Maya menu paths. |
| 5 | `RFK27/546178440-PxrAovLight in Katana.html` | 47/low -> 12/low | Completed; translated AOV light/linking prose while preserving PxrAovLight, Light Filter UI label, and Katana node context. |
| 6 | `REN27/542232083-PxrUnified.html` | 47/low -> 29/low | Completed; normalized integrator prose around manifold walk, sampling, user attribute, lights, spatial/query trees, photon targeting, and developer-option wording while preserving paper citations and identifiers. |

## Validation

- Edited 65 visible article text nodes through the HTML text-node replay pipeline.
- Per-page edit pass preserved each page's pre-edit tag fingerprint.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 62 flagged terms, and 3345 residual term candidates after this batch.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pass and 816/816 browser-sampled pass after this batch.
