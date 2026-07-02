# Review Batch 087: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 086. This batch targets remaining low-score release/home pages, RenderMan overview and subdivision pages, RenderMan University resource metadata pages, Kickstarter prose, and Solaris integrator prose.

Preserve exact product names, renderer names, bridge names, node names, parameter names, UI labels, RIB/API identifiers, resource titles, artist names, and proper nouns. Translate generic metadata labels, prose nouns, workflow wording, and page-navigation labels where English is not acting as an identifier.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFB27/544640279-RenderMan for Blender Release Notes.html` | 5/low | Translate release/source-code labels while preserving URLs and copyright/title names. |
| 2 | `RFB27/544374874-Blender 27 Home.html` | 5/low | Translate remaining Confluence template labels without changing page structure. |
| 3 | `REN27/542213016-Subdivision Surfaces.html` | 5/low | Review subdivision scheme names and face-varying terminology while preserving exact scheme/tag names. |
| 4 | `REN27/542212717-RenderMan.html` | 5/low | Review RenderMan product/interface prose and aliasing terminology. |
| 5 | `REN27/542212097-RenderMan 27 Documentation.html` | 5/low | Translate Early Access/lookdev/support-forum prose while preserving feature names and external package labels. |
| 6 | `RU/608337921-Stirling.html` | 4/low | Translate resource metadata labels while preserving project, artist, and feature names. |
| 7 | `RU/608305219-Crocostrich.html` | 4/low | Translate resource metadata labels while preserving project, artist, and feature names. |
| 8 | `RU/608272385-Cookies & Milk.html` | 4/low | Translate resource metadata labels while preserving project, artist, and feature names. |
| 9 | `RU/599359489-RenderMan Kickstarters.html` | 4/low | Translate Kickstarter prose around quick-start/tutorial wording while preserving product/tutorial titles. |
| 10 | `RFH27/575569950-Integrators in Solaris.html` | 4/low | Translate integrator/workflow prose while preserving LOP names, attributes, and Scene Graph UI wording. |

## Results

Completed 10 / 10 pages. Generic metadata labels, release labels, workflow prose, and integrator wording were translated; preserved remaining English consists of product names, feature/resource names, artist/title names, scheme names, UI labels, attributes, and API/package labels.

| Order | Page | Result |
|---:|---|---|
| 1 | `RFB27/544640279-RenderMan for Blender Release Notes.html` | 5/low -> 3/low; remaining candidates are preserved title/copyright/source proper names such as `Inside Out 2`, `Disney/Pixar`, and repository text. |
| 2 | `RFB27/544374874-Blender 27 Home.html` | 5/low -> 1/low; remaining candidate is preserved `Confluence` product name. |
| 3 | `REN27/542213016-Subdivision Surfaces.html` | 5/low -> 4/low; remaining candidates are preserved subdivision scheme/tag names such as `Catmull-Clark`, `Loop`, and `facevarying`. |
| 4 | `REN27/542212717-RenderMan.html` | 5/low -> 5/low; remaining candidates are preserved product/interface/proper terms such as `RenderMan Pro Server`, `Autodesk`, `RenderMan Interface`, and `aliasing` bilingual terminology. |
| 5 | `REN27/542212097-RenderMan 27 Documentation.html` | 5/low -> 1/low; remaining candidate is preserved `Doxygen` package label. |
| 6 | `RU/608337921-Stirling.html` | 4/low -> 0/low. |
| 7 | `RU/608305219-Crocostrich.html` | 4/low -> 1/low; remaining candidate is preserved `Displacement` feature label. |
| 8 | `RU/608272385-Cookies & Milk.html` | 4/low -> 1/low; remaining candidate is preserved `Pixar Surface` feature label. |
| 9 | `RU/599359489-RenderMan Kickstarters.html` | 4/low -> 0/low. |
| 10 | `RFH27/575569950-Integrators in Solaris.html` | 4/low -> 2/low; remaining candidates are preserved `Scene Graph` and `outputs:ri:integrator` attribute wording. |

## Validation

Passed after Batch 087:

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2568 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`
- `python3 tools/audit_official_layout_alignment.py`: 816 / 816 static pages pass, 816 / 816 browser-sampled pages pass, 0 unrewritten Confluence links.

Overall terminology review progress: 773 / 816 = 94.73%.
