# Review Batch 006: Crews, PxrLayer, PxrLayerSurface, tq, and Hair Cleanup

Status: complete
Created: 2026-06-30

## Scope

Sixth manual terminology cleanup batch. This batch starts from the current highest-risk pages after Batch 005 and keeps the faster workflow: script-assisted residual detection first, then Codex context review and text-node-safe correction.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| Tractor crews / crew membership | 工作组 / 工作组成员 in prose; preserve config keys, command options, service names, and literal values such as `crews`. |
| tq / query / filter / columns | Preserve the `tq` command, options, field names, and examples; translate ordinary prose around querying, filtering, columns, jobs, blades, tasks, and output. |
| PxrLayer / PxrLayerSurface | Preserve shader and parameter names; translate layer, lobe, blend, mask, material, diffuse, specular, subsurface, clearcoat, and artistic-control prose. |
| indirect bounces / shading network | 间接反弹 / 着色网络 in prose; preserve renderer tokens and UI labels when they are literal labels. |
| PxrMarschnerHair / hair shading | Preserve shader/node names and scientific model names; translate hair, color, melanin, glint, lobe, roughness, tint, and lighting prose where they are descriptive text. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `TRA/22184294-Crews.html` | 324 -> 47 | Reviewed and corrected. Localized Tractor crew prose for access control, login permissions, site override directories, crew definitions, reserved and meta crew names, user names, recursive crew expansion, membership removal, job edit permissions, edit policies, password validation, PAM authentication, Dashboard sessions, clear-text password handling, transport protection, and custom validators while preserving config keys, command/service names, literal values, reserved crew names, permission keywords, and code examples. |
| 2 | `REN27/542217837-PxrLayer.html` | 320 -> 31 | Reviewed and corrected. Localized PxrLayer prose for shader parameters, diffuse reflection, roughness, bump mapping, transmission, specular reflection, artistic/physical reflection controls, IOR prose, anisotropy, layer thickness, attenuation/coating, iridescence color ranges, fuzz retroreflection, subsurface scattering, single scattering, glow indirect bounces, incandescence, glass reflection/refraction, and bump normals while preserving shader names, parameter labels, UI modes, presets, model names, and renderer terminology. |
| 3 | `REN27/542216714-PxrLayerSurface.html` | 319 -> 23 | Reviewed and corrected. Localized PxrLayerSurface prose for reflection models, layer pattern nodes, diffuse exponent behavior, specular/Fresnel modes, energy compensation, iridescence controls, fuzz retroreflection, subsurface scattering, trace subsets, single scattering, scattering globals, glass refraction/attenuation, indirect bounces, cached presence, shading networks, and shadow opacity while preserving shader names, parameter labels, model names, mode values, and trace-control enum values. |
| 4 | `TRA/22184306-tq- Tractor Query tool.html` | 309 -> 41 | Reviewed and corrected. Localized `tq` query-tool prose for command-line usage, built-in help, subcommands, jobs/tasks/commands/invocations/blades, search clauses, boolean expressions, columns, widths, sorting, limits, affiliations, operations, prompts, global options, authentication, archived jobs, deleted-job searches, undelete, examples, help topics, usage, and option descriptions while preserving command examples, flags, field names, aliases, user/host placeholders, and literal query expressions. |
| 5 | `RFM27/544541101-PxrMarschnerHair in Maya.html` | 304 -> 21 | Reviewed and corrected. Localized Maya hair-shader prose for hair texturing, hair/fur presets, PxrMarschner material behavior, artist-friendly controls, diffuse models, diffuse color/gain, Marschner specular lobes, R/TRT/TT transport paths, energy conservation, wet hair, transmission/refraction, volume attenuation, glints, cone angles, refractive index, Fresnel attenuation, eccentricity, glow, global controls, presence masks, shadow color, rays, global illumination, and named/user lobes while preserving shader names, parameter labels, model names, paper title, author names, primvars, lobe identifiers, and code/asset labels. |

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
- Overall page review progress: 33 / 816 = 4.04%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 40 high / 287 medium / 488 low pages. `RFM27/544541101-PxrMarschnerHair in Maya.html` moved from 304/high to 21/low with no flagged terms; quick article tag-count check shows no HTML structure delta against the English source except the expected local `script`/`link` assets.
- Batch layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816 / 816 static pages and 816 / 816 browser-sampled pages.
