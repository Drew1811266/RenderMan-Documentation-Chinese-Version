# Review Batch 007: Tractor UI, Maya Overview, Scheduling, Best Practices, and Mesh Lights Cleanup

Status: complete
Created: 2026-06-30

## Scope

Seventh manual terminology cleanup batch. This batch starts from the current highest-risk pages after Batch 006 and keeps the faster workflow: script-assisted residual detection first, then Codex context review and text-node-safe correction.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| Tractor UI / dashboard / menu items | Translate ordinary UI-tour prose for panels, queues, blades, jobs, filters, and actions; preserve literal menu labels, command names, config keys, and example strings. |
| Blade capability advertisements / scheduling modes | Translate scheduling, allocation, capability, advertisement, dispatch, and resource prose; preserve service keys, profile keys, env keys, and example expressions. |
| RenderMan for Maya overview / best practices | Translate workflow prose for scene units, intersection priority, render settings, materials, lights, and bridge behavior; preserve Maya/RfM UI labels and parameter names when literal. |
| Mesh lights in Maya | Translate mesh light, geometry light, emission, samples, visibility, linking, and shading prose; preserve node names and UI/parameter labels. |
| Layered materials / shading network / layer mask | 着色网络 / 层遮罩 in prose; preserve shader names, node names, and parameter identifiers. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `TRA/22184218-Tractor UI Tour.html` | 289 -> 45 / low | Reviewed Dashboard prose; translated ordinary UI-tour wording for queues, jobs, blades, panels, filters, browser/session/window descriptions, and preserved literal UI labels. |
| 2 | `RFM27/544538625-RenderMan 27 for Maya.html` | 288 -> 32 / low | Reviewed RfM overview prose; translated workflow, plugin, imaging, interactive rendering, lights, GI, volume, surface, material, output, shader, procedural, pipeline, Tractor, and RPS descriptions while preserving product/feature/API names. |
| 3 | `TRA/22184324-Advanced Blade Capability Advertisement.html` | 287 -> 28 / low | Reviewed service-key capability advertisement prose; translated job/blade/capability/counting/slot/required-key descriptions while preserving `Provides`, `Slots`, suffixes, service keys, and command examples. |
| 4 | `TRA/22184302-Scheduling Modes.html` | 282 -> 10 / low | Reviewed scheduling-mode prose; translated queue, tier, priority, blade assignment, ATCL/RR behavior, checkpoint processing, and allocation descriptions while preserving mode names and config keys. |
| 5 | `RFM27/544543262-Introduction to Best Practices.html` | 277 -> 40 / low | Reviewed Maya best-practices prose; translated scene units, intersection priority, modeling, subdivision surfaces, texture maps, material lobes, lighting, and look-development wording while preserving shader/node/parameter names where needed. |

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
- Overall page review progress: 38 / 816 = 4.66%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 35 high / 287 medium / 493 low pages after `RFM27/544543262-Introduction to Best Practices.html`.
- Structure validation for `TRA/22184218-Tractor UI Tour.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544538625-RenderMan 27 for Maya.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184324-Advanced Blade Capability Advertisement.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `TRA/22184302-Scheduling Modes.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Structure validation for `RFM27/544543262-Introduction to Best Practices.html`: tag-count diff is limited to the expected offline theme injection (`link`: 0 -> 1, `script`: 0 -> 2).
- Full layout validation: `python3 tools/audit_official_layout_alignment.py` passes 816 / 816 static pages and 816 / 816 browser-sampled pages.
- Throughput adjustment: keep page-level review, but use script-assisted exact replacements for obvious prose-level residual English first, then manually inspect only ambiguous protected terms and UI labels.
