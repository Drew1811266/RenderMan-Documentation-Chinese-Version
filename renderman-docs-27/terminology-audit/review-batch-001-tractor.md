# Review Batch 001: Tractor Terminology Cleanup

Status: complete
Created: 2026-06-30

## Scope

First manual terminology cleanup batch for high-risk Tractor pages. This batch focuses on reducing unnecessary English fragments in explanatory prose while preserving exact Tractor product names, command names, config keys, API identifiers, and literal examples.

## Why Tractor First

The current page risk report identifies 90 high-risk pages. Tractor accounts for 34 of them, the largest single product area. The samples show real readability issues, not just scanner noise:

- `job`, `task`, `command`, `file`, `config`, `process`, `server`, `profile`, and `database` are often left as English in Chinese prose.
- Exact identifiers such as `tractor-engine`, `tractor-blade`, command-line options, and config filenames must remain unchanged.
- Component names such as Tractor Engine, Blade, and Dashboard need consistent context rules.

## Term Rules For This Batch

| English | Preferred Chinese / Rule |
|---|---|
| Job / job | 作业, unless it is literal code/API syntax. |
| Task / task | 任务, unless it is a class/API label. |
| Command / command | 命令, unless it is literal command syntax. |
| script | 脚本. |
| spool / spooled / spooler | 提交 / 已提交 / 提交器, unless part of `tractor-spool`. |
| blade | Blade（执行节点） on first concept use; later `Blade` is acceptable for the Tractor component. Translate generic lowercase prose where possible. |
| engine | Engine（调度引擎） on first component use; preserve `tractor-engine`. |
| Dashboard | Dashboard（仪表板） on first concept use; later preserve `Dashboard` for the UI product. |
| config / configuration | 配置, except config filenames and keys. |
| profile | 配置档 / profile label depending on context. |
| server | 服务器. |
| host | 主机. |
| database | 数据库. |
| process | 进程. |
| file | 文件. |
| service | 服务. |
| log | 日志. |
| key | 键. |
| list | 列表. |
| string / integer / boolean / float | Preserve in schema/type tables; translate as 字符串 / 整数 / 布尔值 / 浮点数 in prose. |

## Pages

| Order | Page | Risk score | Notes |
|---:|---|---:|---|
| 1 | `TRA/22184270-Glossary.html` | 701 -> 115 | Reviewed and corrected. Establishes Tractor term definitions before correcting other pages. |
| 2 | `TRA/22184352-Release Notes.html` | 2904 -> 294 | Reviewed and corrected. Remaining residual English is mostly literal UI labels, status names, command options, config keys, and release-note feature titles; no concentrated high-risk chunks remain. |
| 3 | `TRA/22184254-Job Scripting.html` | 1110 -> 195 | Reviewed and corrected. Prose terms such as job/script/command/task/file/key/blade/server/profile/expression were localized while preserving script operators, command examples, service keys, substitutions, and environment variables. |
| 4 | `TRA/22184316-Engine.html` | 1008 -> 69 | Reviewed and corrected. Established Engine/component wording; localized prose terms around configuration, scheduling, logging, retry behavior, URLs, and SMTP while preserving config keys, command names, status values, account names, and literal examples. |
| 5 | `TRA/22184312-Server Profiles.html` | 830 -> 32 | Reviewed and corrected. Localized server profile prose around profile matching, Hosts/Access/Provides/Capacity, EnvKeys, VersionPin, NIMBY, and GPU filtering while preserving config keys, JSON examples, mode values, and literal examples. |
| 6 | `TRA/22184250-Logging.html` | 656 -> 10 | Reviewed and corrected. Localized logging prose around Engine/Blade logs, log rotation, command output logs, central fileserver logging, web retrieval, and CORS while preserving command options, paths, logrotate/systemd/journald literals, and UI menu labels. |
| 7 | `TRA/22184256-Job Scripting Operators.html` | 615 -> 36 | Reviewed and corrected. Localized operator descriptions around Job/Task/RemoteCmd/Cmd/Instance/Assign/Iterate while preserving operator syntax, option names, placeholders, command examples, service expressions, and literal mode names. |
| 8 | `TRA/22184276-tractor-spool.html` | 588 -> 10 | Reviewed and corrected. Localized command-help prose around job submission, ranges, iteration, runtime bounds, status output, authentication, and review output while preserving command syntax, placeholders, examples, `RemoteCmd`/`Cmd` literals, and option values. |

## Exit Criteria

- Each page is reviewed against the English source page and current term rules.
- Only visible text nodes are changed; HTML structure and official layout remain intact.
- Code blocks, command examples, filenames, config keys, API identifiers, and command names are preserved.
- Re-run `python3 tools/audit_terminology.py scan-pages`.
- Re-run `python3 tools/audit_official_layout_alignment.py`.
- Record before/after risk scores and corrected term decisions.

## Current Progress

- Reviewed pages: 8 / 8.
- Batch completion: 100.00%.
- Overall page review progress: 8 / 816 = 0.98%.
- Latest validation: `python3 -m py_compile tools/audit_terminology.py` passes; `python3 tools/audit_terminology.py scan-pages` reports 78 high / 312 medium / 425 low pages. `python3 tools/audit_official_layout_alignment.py` reports 816/816 static pass and 816/816 browser-sampled pass. `TRA/22184276-tractor-spool.html` moved from 588/high to 10/low.
