# Review Batch 008: Mesh Lights, Layered Materials, Noise, Tractor Menus, and Installation Cleanup

Status: completed
Created: 2026-06-30

## Scope

Eighth terminology cleanup batch. This batch starts from the current highest-risk pages after Batch 007 and continues the faster workflow: text-node-safe bulk normalization for obvious residual English first, then Codex context review for ambiguous UI labels, shader/node names, parameters, and examples.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| Mesh lights in Maya | Translate mesh light, geometry light, emission, sampling, visibility, light linking, and shading prose; preserve node names, UI/parameter labels, and literal menu names when needed. |
| Layered materials / patina | Translate layered material, shading network, layer mask, coating, oxidation/patina, color/roughness prose; preserve shader names, node names, and parameter identifiers. |
| PxrPhasorNoise | Translate noise, fractal, frequency, amplitude, phase, feature-size, displacement, and pattern prose; preserve shader name and parameter labels. |
| Tractor custom menu items | Translate Dashboard/custom menu/action prose; preserve config keys, JSON-like snippets, command names, and literal menu labels. |
| Tractor installation | Translate install/service/profile/license/networking prose; preserve paths, command flags, config keys, product names, platform names, and example values. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `RFM27/544541535-Mesh Lights in Maya.html` | 276 -> 44 / low | Reviewed mesh-light workflow prose; translated geometry/light-source/emission/sampling/visibility/linking/temperature/near-distance descriptions while preserving `Mesh Light`, `PxrMeshLight`, `PxrBlack`, editor names, and parameter labels where useful. |
| 2 | `RFK27/546179628-Copper Patina with Layered Materials.html` | 275 -> 20 / low | Reviewed layered-material/patina prose; translated layered material, shading network, layer mask, copper/bronze/patina, bump, roughness, weathering, and masking descriptions while preserving shader/node/port names. |
| 3 | `REN27/542224343-PxrPhasorNoise.html` | 274 -> 17 / low | Reviewed phasor-noise prose; translated noise, phasor wave, kernel, frequency, direction, phase, octave, fractal, harmonic, falloff, amplitude-space, filtering, and convergence descriptions while preserving shader name, parameter names, and enum-like labels. |
| 4 | `TRA/22184304-Custom Menu Items.html` | 271 -> 39 / low | Reviewed Tractor Dashboard custom-menu prose; translated context menu, custom item, script, configuration directory, job/task/user, browser/response, command-line, exception, and troubleshooting prose while preserving attribute keys, JSON payload fields, paths, example values, and command literals. |
| 5 | `TRA/22184336-Installation.html` | 268 -> 21 / low | Reviewed Tractor installation prose; translated host, installer, package, license, storage, queue, hostname alias, network, command-line, and blade-service descriptions while preserving paths, service names, platform names, environment variables, command options, and literal config values; corrected `tractor.conf` file-name drift from the previous Chinese text. |

## Exit Criteria

- Each page is reviewed against the English source page and the current batch term rules.
- Prose is natural Chinese and avoids unnecessary English fragments.
- Product names, shader/node names, UI labels, API identifiers, parameter names, renderer tokens, code examples, command options, paths, and literal values remain exact.
- Only visible text nodes are changed; HTML structure and official layout remain intact.
- Re-run `python3 tools/audit_terminology.py scan-pages` after each page.
- Re-run `python3 tools/audit_official_layout_alignment.py` before marking the batch complete.

## Current Progress

- Reviewed pages: 5 / 5.
- Batch completion: 100.00%.
- Overall page review progress: 43 / 816 = 5.27%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 30 high / 287 medium / 498 low pages after `TRA/22184336-Installation.html`.
- Full layout validation: `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pass and 816/816 browser-sampled pass.
- Structure validation for `RFM27/544541535-Mesh Lights in Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFK27/546179628-Copper Patina with Layered Materials.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `REN27/542224343-PxrPhasorNoise.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184304-Custom Menu Items.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184336-Installation.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
