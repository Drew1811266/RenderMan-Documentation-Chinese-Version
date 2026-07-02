# Review Batch 002: Tractor Scheduling, Access, and Limits Cleanup

Status: complete
Created: 2026-06-30

## Scope

Second manual terminology cleanup batch for high-risk Tractor pages. This batch continues the Tractor area while the terminology context is fresh, focusing on scheduling policy, access/authentication, query APIs, limits, and login management.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| NIMBY | Preserve `NIMBY`; translate explanatory prose as 不接收作业 / 暂停接收新工作 depending on context. |
| blade | Blade（执行节点） on first concept use; later `Blade` is acceptable for the Tractor component. |
| job / task / command | 作业 / 任务 / 命令 in prose; preserve code/API labels. |
| owner / user / login | 所有者 / 用户 / 登录名, unless literal account fields. |
| password / authentication | 密码 / 身份验证. |
| query / clause / predicate | 查询 / 子句 / 谓词 or 条件, depending on sentence. |
| limit / limit counter | 限制 / 限制计数器; preserve `Limit Counters` when naming the UI page or feature. |
| crew / service / profile | crew（分组） or 作业组 contextually; 服务; 配置档. |
| allocation / slot / capacity | 分配 / 槽位 / 容量. |
| active / blocked / ready / done / error | Preserve exact status values when naming status literals; translate surrounding prose. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `TRA/22184284-NIMBY.html` | 468 -> 27 | Reviewed and corrected. Localized scheduling/Blade availability, NIMBY modes, active-job ejection, profile settings, URL state changes, and authentication prose while preserving `NIMBY`, exact UI mode labels, command options, config fields, URL values, and path literals. |
| 2 | `TRA/22184252-Alternative Authentication.html` | 400 -> 30 | Reviewed and corrected. Localized challenge-response hashing, password validation, login credential handling, server/client encoding, `/etc/passwd` comparison, and validator-program prose while preserving scheme labels, file names, function names, config keys, example values, and hash terminology where useful. |
| 3 | `TRA/22184266-Query Python API.html` | 391 -> 44 | Reviewed and corrected. Localized query/list/operation explanations, search clauses, columns, sorting, limiting, archive costs, affiliation attributes, and Engine session prose while preserving Python identifiers, keyword parameters, field names, examples, function names, and query literals. |
| 4 | `TRA/22184308-Limits Configuration.html` | 364 -> 39 | Reviewed and corrected. Localized limit counters, allocation policy, project shares, dispatch behavior, and Blade/resource-capacity prose while preserving config keys, JSON examples, feature labels, literal field names, and intentional UI/table headings. |
| 5 | `TRA/22184322-Login Management.html` | 361 -> 49 | Reviewed and corrected. Localized login/password/account, PAM, credential transfer, challenge-token, external-script, monitor-login, and JSON response prose while preserving config literals, PAM policy values, function names, URLs, JSON fields, and `crew` concept usage. |

## Exit Criteria

- Each page is reviewed against the English source page and the current Tractor term rules.
- Prose is natural Chinese and avoids unnecessary English fragments.
- Product names, command names, config keys, API identifiers, status literals, and code examples remain exact.
- Only visible text nodes are changed; HTML structure and official layout remain intact.
- Re-run `python3 tools/audit_terminology.py scan-pages` after each page.
- Re-run `python3 tools/audit_official_layout_alignment.py` before marking the batch complete.

## Current Progress

- Reviewed pages: 5 / 5.
- Batch completion: 100.00%.
- Overall page review progress: 13 / 816 = 1.59%.
- Latest validation: `python3 tools/audit_terminology.py scan-pages` reports 73 high / 312 medium / 430 low pages. `TRA/22184322-Login Management.html` moved from 361/high to 49/low; quick article tag-count check shows no HTML structure delta against the English source.
- Batch layout validation: `python3 tools/audit_official_layout_alignment.py` reports 816 / 816 pass.
