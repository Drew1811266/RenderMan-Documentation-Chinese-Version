# Review Batch 044: Low-Risk Prose Polish

Status: completed
Created: 2026-07-02

## Scope

Continue post-T1 low-risk prose polish after Batch 043. This batch targets Katana denoising, holdout, geometry, and error-handling pages plus Houdini/Solaris bindings, grouping, and lighting workflow pages.

Preserve exact product names, node names, macro names, menu paths, UI labels, parameter names, enum values, attribute names, file formats, shader names, scenegraph literals, and acronyms. Translate ordinary prose terms such as interactive denoising option, first pass, heuristic, quality, denoised result, time interval, browser/video element, macro, parameters, render, holdout image, composite, background image, render directory, pipeline, custom, render procedurals, scene recipe, fatal error, attribute function, string field, float field, scatter data, multiplier, base color, velocities, grouping membership, trace set, shadow subset, bundle/grouping, light linking, stage view, light shapes, scope, mute, and solo when they are not exact identifiers.

## Pages

| Order | Page | Starting Risk | Primary Cleanup |
|---:|---|---:|---|
| 1 | `RFK27/546179198-Interactive Denoiser.html` | 34/low | Translate denoiser option, first-pass, heuristic, quality, convergence, interval, sample, preference, browser, and video-element prose while preserving UI labels. |
| 2 | `RFK27/546179038-Holdouts in Katana.html` | 34/low | Translate holdout macro, parameter, render/composite/background, AOV, directory, Filename, group, and sample-filter prose while preserving macro names and enum values. |
| 3 | `RFK27/546177458-Geometry in Katana.html` | 34/low | Translate geometry-type, pipeline/custom, render-procedural, VDB/box-volume, attribute, and Scenegraph prose while preserving node names and format names. |
| 4 | `RFK27/546177430-Error Handling.html` | 34/low | Translate scenegraph traversal, warn/abort, scene recipe, fatal error, override handler, attribute-function, error-code, and error-message prose while preserving attribute literals. |
| 5 | `RFH27/544646865-Bindings.html` | 34/low | Translate volume-binding, string/float field, scatter data, multiplier, base-color, intensity, density, velocity, and shader prose while preserving parameter labels. |
| 6 | `RFH27/544643653-Grouping Membership.html` | 34/low | Translate grouping membership, trace set, shadow subset, token, bundle/grouping, caret, sphere/rect-light, and shadow prose while preserving UI labels and token syntax. |
| 7 | `RFH27/544641395-Solaris Lighting Workflow.html` | 34/low | Translate Solaris lighting workflow, stage view, Light Mixer, light linking, Rules, on/off, light shape, scope, texture-conversion, and visibility prose while preserving node/UI labels. |

## Results

Edited 65 visible article text-node update operations across 7 pages, including a follow-up pass on the Bindings page to translate one remaining ordinary `shader` occurrence. Tag fingerprints were checked before and after each page edit and remained unchanged.

| Order | Page | Final Risk | Notes |
|---:|---|---:|---|
| 1 | `RFK27/546179198-Interactive Denoiser.html` | 9/low | Translated interactive-denoising, first-pass, heuristic, quality, convergence, interval, sample, preference, browser, and video-element prose while preserving UI labels. |
| 2 | `RFK27/546179038-Holdouts in Katana.html` | 7/low | Translated holdout macro, parameter, render/composite/background, image-name, render-directory, group, and sample-filter prose while preserving macro names, enum values, and output filenames. |
| 3 | `RFK27/546177458-Geometry in Katana.html` | 18/low | Translated geometry-type, render-procedural, pipeline/custom, USD-format, VDB/box-volume, and attribute prose while preserving node names, format names, URLs, and Scenegraph terminology. |
| 4 | `RFK27/546177430-Error Handling.html` | 6/low | Translated scenegraph traversal, warn/abort, scene recipe, fatal-error, override-handler, attribute-function, error-code, and error-message prose while preserving attribute literals and abort enum values. |
| 5 | `RFH27/544646865-Bindings.html` | 16/low | Translated string/float field, scatter data, multiplier, base-color, intensity, density, velocity, and shader prose while preserving volume and parameter labels. |
| 6 | `RFH27/544643653-Grouping Membership.html` | 12/low | Translated grouping membership, trace set, shadow subset, token, bundle/grouping, caret, sphere/rect-light, and shadow prose while preserving token syntax and UI labels. |
| 7 | `RFH27/544641395-Solaris Lighting Workflow.html` | 20/low | Translated stage-view, Light Mixer, light-linking, on/off, RfH-difference, light-shape, scope, texture, and visibility prose while preserving node/UI labels. |

## Validation

- `python3 -m py_compile tools/audit_terminology.py tools/translate_html_docs.py tools/audit_official_layout_alignment.py` passed.
- `python3 tools/audit_terminology.py scan-pages` reports 0 high / 1 medium / 814 low pages, 40 flagged terms, and 3112 residual term candidates.
- `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pages passed and 816/816 browser-sampled pages passed.
