# Review Batch 031: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish on the next highest-ranked pages. This batch focuses on DCC UI/workflow pages and one camera reference page. Because these pages contain many UI labels, edits should translate ordinary explanatory prose and leave exact menu, preference, parameter, and button labels intact unless the surrounding prose clearly needs a Chinese gloss.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFM27/544539259-RenderMan Menu.html` | 46/low | Translate RenderMan menu prose around script editor logging, output logs, previews, globals, utilities, and help labels. |
| 2 | `RFH27/544645926-Output.html` | 46/low | Translate output/display prose around display drivers, options, images, bit depth, compression, and quantized renders. |
| 3 | `RFH27/544640927-Preset Browser in Solaris.html` | 46/low | Translate preset/material/domelight import prose while preserving exact import command labels and Solaris node names. |
| 4 | `RFB27/544639958-Denoiser in Blender.html` | 46/low | Translate denoiser prose around viewport, passes, compositor, batch style, sample filters, and layer properties. |
| 5 | `RFB27/544639612-Batch Rendering in Blender.html` | 46/low | Translate batch-render prose around batch/spool style, compositor, queue, recovery, frame chunking, and persistent data. |
| 6 | `REN27/542231487-Aperture.html` | 46/low | Translate aperture/bokeh explanatory prose while preserving camera parameter labels and lens terms where useful. |

## Results

Edited 73 visible article text nodes. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFM27/544539259-RenderMan Menu.html` | 36/low | Translated menu/output/logging prose while preserving exact UI labels and command names. |
| 2 | `RFH27/544645926-Output.html` | 7/low | Translated display-driver, image, bit-depth, compression, and quantized-render prose; preserved file-format and driver identifiers. |
| 3 | `RFH27/544640927-Preset Browser in Solaris.html` | 26/low | Translated preset/material/domelight import prose; preserved import command labels and Solaris node names. |
| 4 | `RFB27/544639958-Denoiser in Blender.html` | 27/low | Translated denoiser, render-pass, compositor, and properties prose; preserved Blender UI labels. |
| 5 | `RFB27/544639612-Batch Rendering in Blender.html` | 46/low | Translated batch/spool, compositor, queue, recovery, and frame-chunking prose; remaining English is mainly UI labels. |
| 6 | `REN27/542231487-Aperture.html` | 22/low | Translated aperture/bokeh explanatory prose while preserving parameter labels such as `Sides`, `Roundness`, and `Density`. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 61 flagged terms, and 3328 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
