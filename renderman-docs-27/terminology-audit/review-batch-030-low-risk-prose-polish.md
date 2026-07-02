# Review Batch 030: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish on the next highest-ranked pages. This batch covers RenderMan light reference prose, instancing attributes, RenderMan University metallic workflow and cheat-sheet entries, and Maya Alembic workflow prose. Edits should translate ordinary English words in Chinese sentences while preserving node names, UI labels, command/file literals, project names, and artist names.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `REN27/542227947-PxrDistantLight.html` | 47/low -> 13/low | Completed; translated light/geometry/manifold prose while preserving PxrUnified, Integrator, trace-set, and parameter labels. |
| 2 | `REN27/542226975-PxrDomeLight.html` | 47/low -> 7/low | Completed; translated dome-light prose around light amounts, geometry, maps, diffuse/specular, objects, and portals while preserving UI/parameter labels. |
| 3 | `REN27/542213293-Instancing.html` | 47/low -> 17/low | Completed; normalized prototype/visibility/procedural prose while preserving attribute-category concepts and archive/procedural identifiers. |
| 4 | `RU/619741326-PxrSurface - Metallic Workflow.html` | 46/low -> 18/low | Completed; translated metallic workflow prose around maps, nodes, roughness, diffuse/specular, and texturing software while preserving PxrMetallicWorkflow and exact channel names. |
| 5 | `RU/384368745-RenderMan CheatSheet.html` | 46/low -> 15/low | Completed; translated cheat-sheet category/entry prose where ordinary words remained, while preserving concise table labels and node names. |
| 6 | `RFM27/544540223-Alembic Workflows.html` | 46/low -> 31/low | Completed; translated cache/export/edit prose while preserving Alembic, file/path labels, sample file names, and artist/model names. |

## Validation

- Edited 107 visible article text nodes through the HTML text-node replay pipeline.
- Per-page edit pass preserved each page's pre-edit tag fingerprint.
- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 61 flagged terms, and 3340 residual term candidates after this batch.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pass and 816/816 browser-sampled pass after this batch.
