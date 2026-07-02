# Review Batch 043: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 042. This batch targets content-heavy RenderMan University pages plus MatteID, Cryptomatte, and light-filter explanation pages where ordinary English words remain in Chinese prose.

Preserve exact product names, node names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, scene/project names, and acronyms. Translate ordinary prose terms such as truck, main character, model, ice cream truck, van, backstory, geometry, radar dishes, CCTV cameras, off-road wheels, roof rack, tracking equipment, workflow, pass, pattern, connection, light filter, intensity, physical/analytic mode, online material library, texturing software, process, maps, model, textures, plugin, mask, per-object/per-material output, and shape node when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RU/563118083-The Hunted Van.html` | 36/low | Translate narrative asset-building prose while preserving UFO and project naming. |
| 2 | `RFM27/544543508-MatteID in Maya.html` | 36/low | Translate MatteID workflow prose, pass/pattern/connection wording, and user-attribute wording while preserving node and UI names. |
| 3 | `REN27/542228334-Light Filters.html` | 35/low | Translate light-filter overview and filter-type descriptions while preserving filter class names and deprecated product identifiers. |
| 4 | `RU/608436284-Lac d'Annecy.html` | 34/low | Translate HDRI resource usage and overview prose while preserving place/license names. |
| 5 | `RU/606208122-Lama Metallic Workflow.html` | 34/low | Translate PBR-map/Lama workflow, material-library, texture, model, UV, and menu prose while preserving node names and product names. |
| 6 | `RU/598901006-Lighting Path.html` | 34/low | Translate course-card prose where English is ordinary descriptive wording, preserving lesson titles. |
| 7 | `RFM27/544543618-Cryptomatte in Maya.html` | 34/low | Translate Cryptomatte workflow, plugin/output/mask/token and ID assignment prose while preserving identifiers and file examples. |

## Results

Edited 59 visible article text-node update operations across 7 pages, including a focused follow-up correction on the Lighting Path page to avoid introducing a new `Light Filters` audit flag. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RU/563118083-The Hunted Van.html` | 0/low | Translated asset-building and story prose such as truck, main character, model, backstory, geometry, radar dishes, CCTV cameras, roof rack, tracking equipment, initial renders, monitors, and desks while preserving UFO and media filenames. |
| 2 | `RFM27/544543508-MatteID in Maya.html` | 4/low | Translated workflow, material ID, shape, render-pass, pattern, connection, manifold, and user-attribute prose while preserving MatteID/Pxr node and UI labels. |
| 3 | `REN27/542228334-Light Filters.html` | 0/low | Translated light-filter overview, integrator, intensity/exposure, physical/analytic mode, blocker, rod, ramp, and filter descriptions while preserving filter class names. |
| 4 | `RU/608436284-Lac d'Annecy.html` | 9/low | Translated HDRI resource labels, usage text, location prose, sunny-day description, license wording, and credit wording while preserving place and license names. |
| 5 | `RU/606208122-Lama Metallic Workflow.html` | 7/low | Translated online-material-library, PBR-map, texture-software, workflow, process, map, model, triplanar, texture, UV, material-network, and normal-connection prose while preserving node names and product/UI names. |
| 6 | `RU/598901006-Lighting Path.html` | 32/low | Translated ordinary description text and corrected the Light Filters course label to Chinese-only where it was not needed as an identifier, while preserving lesson/project titles. |
| 7 | `RFM27/544543618-Cryptomatte in Maya.html` | 16/low | Translated Cryptomatte workflow, plugin, mask, per-object/per-material output, token/padding prose, user-string-attribute wording, LPE-group wording, and shape-node wording while preserving identifiers and file examples. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 40 flagged terms, and 3129 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
