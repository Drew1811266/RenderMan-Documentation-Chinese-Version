# Review Batch 081: Low-Risk Prose Polish

Status: complete
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 080. This batch targets Tractor upgrade/overview pages, RenderMan University resource/project prose, and RenderMan geometry/camera pages where ordinary English remains in Chinese explanatory text.

Preserve exact product names, component names, API/tool names, UI labels, page titles, artist names, project names, URL text, file names, command-line options, license names, and proper nouns. Translate ordinary prose terms such as job queue, work distribution system, pipeline, farm, private installation, stock config, engine config, live-action VFX, plate, look development, digital double, micro displacement detail, resource labels, captured by, use, overview, copyright, trimmed NURBS, trimcurve, projection plugins, sphere, torus, cylinder, and More Information when they are explanatory wording rather than exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `TRA/22184350-Upgrading from Tractor 1.x.html` | 14/low | Translate Tractor upgrade prose around private PostgreSQL installs, stock config, and engine config while preserving commands, config names, and component names. |
| 2 | `TRA/22183944-Tractor 2.html` | 9/low | Translate Tractor overview prose around job queue, work distribution, pipeline customization, farm tools, APIs, and release notes while preserving product/tool labels. |
| 3 | `RU/608567297-Luxo Jr.html` | 12/low | Translate resource metadata labels and license prose while preserving HDRI, PxrDomeLight, names, and license title. |
| 4 | `RU/604438600-Stirling VFX.html` | 12/low | Translate Stirling VFX prose around live-action VFX, plate footage, HDRI capture, and license wording while preserving project names and artist names. |
| 5 | `RU/608305153-Louise.html` | 11/low | Translate Louise asset-credit prose around digital double and micro displacement detail while preserving artist, vendor, URL, and feature names. |
| 6 | `RU/604438529-Making a Toy F1 Car.html` | 10/low | Translate Toy F1 prose around look development and license wording while preserving project title and artist names. |
| 7 | `REN27/542212954-NURBS.html` | 9/low | Translate NURBS prose around trimmed NURBS, trimcurve, and Sphere wording while preserving NURBS/RIS/XPU identifiers. |
| 8 | `REN27/542231085-Cameras.html` | 8/low | Translate camera prose around depth of field, bokeh, projection plugins, built-in projections, and More Information while preserving page links and projection names where useful. |

## Results

- `TRA/22184350-Upgrading from Tractor 1.x.html`: 14/low -> 10/low. Translated upgrade prose around private PostgreSQL installs, stock config, and engine config while preserving commands, config names, and component names.
- `TRA/22183944-Tractor 2.html`: 9/low -> 3/low. Translated Tractor overview prose around job queue, work distribution, pipeline customization, farm tools, APIs, and release notes while preserving product/tool labels.
- `RU/608567297-Luxo Jr.html`: 12/low -> 7/low. Translated resource metadata labels while preserving HDRI, PxrDomeLight, names, and license title.
- `RU/604438600-Stirling VFX.html`: 12/low -> 7/low. Translated Stirling VFX prose around live-action VFX, plate footage, HDRI capture, and license wording while preserving project and artist names.
- `RU/608305153-Louise.html`: 11/low -> 0/low. Translated Louise asset-credit prose around digital double and micro displacement detail while preserving artist, vendor, URL, and feature names.
- `RU/604438529-Making a Toy F1 Car.html`: 10/low -> 2/low. Translated Toy F1 prose around look development and license wording while preserving project title and artist names.
- `REN27/542212954-NURBS.html`: 9/low -> 5/low. Translated NURBS prose around trimmed NURBS, trimcurve, and Sphere wording while preserving NURBS/RIS/XPU identifiers.
- `REN27/542231085-Cameras.html`: 8/low -> 4/low. Translated camera prose around depth of field, bokeh, projection plugins, built-in projections, and More Information while preserving page links and projection names.

Batch 081 total progress contribution: 8 / 8 pages complete. Overall terminology review progress is now 714 / 816 = 87.50%.

## Validation

- `python3 tools/audit_terminology.py scan-pages`: 0 high / 1 medium / 814 low pages, 17 flagged terms, 2614 residual term candidates.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py`: pass.
- `python3 tools/audit_official_layout_alignment.py`: 816/816 static pages pass and 816/816 browser-sampled pages pass.
