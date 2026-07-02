# Review Batch 091: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 090. This batch targets low-score Tractor utility pages, Solaris/Blender advanced pages, and selected RenderMan node-reference pages.

Preserve exact API names, UI labels, config keys, product names, node names, parameter names, and command/query keywords. Translate ordinary prose terms such as engine communication, help text, node/context/pane explanations, stats panel wording, customizing labels, and mix/clamp prose where they are not protected identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `TRA/22191840-brikit.mobile.html` | 2/low | Review Theme Press as protected product/template wording. |
| 2 | `TRA/22184358-Upgrading to 2.1.html` | 2/low | Review Query API and `columns` keyword prose. |
| 3 | `TRA/22184341-APIs.html` | 2/low | Translate engine/query prose while preserving API labels. |
| 4 | `TRA/22184320-Administration.html` | 2/low | Translate administration/help prose while preserving Engine/blade component names. |
| 5 | `RFH27/564199461-Stylized Looks in Solaris.html` | 2/low | Translate node/filter prose while preserving exact node names. |
| 6 | `RFH27/544642250-Live Stats in Solaris.html` | 2/low | Translate stats-panel prose while preserving `Attach Render` UI label. |
| 7 | `RFH27/544640896-Converting Textures.html` | 2/low | Translate Solaris context/pane prose while preserving Texture Manager UI label. |
| 8 | `RFB27/544640056-Advanced.html` | 2/low | Translate Blender advanced navigation labels where appropriate. |
| 9 | `REN27/542225088-PxrThinFilm.html` | 2/low | Review `Thickness` parameter wording while preserving parameter labels. |
| 10 | `REN27/542224229-PxrMix.html` | 2/low | Translate mix/clamp prose while preserving parameter labels. |

## Results

Completed 10 / 10 pages. Eight pages received targeted text-node edits; two pages were reviewed and left unchanged because the remaining candidates are preserved product/API/keyword terms.

| Order | Page | Result |
|---:|---|---|
| 1 | `TRA/22191840-brikit.mobile.html` | 2/low -> 2/low; remaining candidates are preserved `Theme Press` product/template wording. |
| 2 | `TRA/22184358-Upgrading to 2.1.html` | 2/low -> 2/low; remaining candidates are preserved `Query API` and `columns` keyword wording. |
| 3 | `TRA/22184341-APIs.html` | 2/low -> 0/low. |
| 4 | `TRA/22184320-Administration.html` | 2/low -> 0/low. |
| 5 | `RFH27/564199461-Stylized Looks in Solaris.html` | 2/low -> 0/low. |
| 6 | `RFH27/544642250-Live Stats in Solaris.html` | 2/low -> 1/low; remaining candidate is preserved `Attach Render` UI label. |
| 7 | `RFH27/544640896-Converting Textures.html` | 2/low -> 0/low. |
| 8 | `RFB27/544640056-Advanced.html` | 2/low -> 0/low. |
| 9 | `REN27/542225088-PxrThinFilm.html` | 2/low -> 0/low. |
| 10 | `REN27/542224229-PxrMix.html` | 2/low -> 2/low; remaining candidates are preserved `Mixer` and `Output` parameter/group labels. |

## Validation

Passed after Batch 091:

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2558 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`
- `python3 tools/audit_official_layout_alignment.py`: 816 / 816 static pages pass, 816 / 816 browser-sampled pages pass, 0 unrewritten Confluence links.

Overall terminology review progress: 813 / 816 = 99.63%.
