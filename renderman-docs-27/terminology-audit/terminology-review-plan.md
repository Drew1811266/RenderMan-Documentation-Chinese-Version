# RenderMan 27 Chinese Documentation Terminology Review Plan

Status: active goal
Created: 2026-06-30

## Objective

Review the translated RenderMan 27 documentation for professional terminology accuracy and readability. The review must catch both directions of terminology risk:

- Wrong or inconsistent Chinese translations of real RenderMan/CG/VFX terms.
- Over-preservation of English words where normal Chinese prose would read better.

The target result is not "translate every English token". Product names, node names, APIs, parameter identifiers, file paths, command examples, UI labels, and official acronyms must remain exact where required. Explanatory prose should be natural Simplified Chinese, using English only where it improves precision.

## Current Baseline

- Translated HTML pages: 816.
- Existing glossary: `renderman-docs-27/glossary/renderman_terminology.json`.
- Existing glossary term count: 5282.
- Existing entries marked `preserve: true`: 2917.
- Initial high-risk over-preserve candidates: 620 entries.
- Main content output: `renderman-docs-27/html-zh`.
- Source HTML: `renderman-docs-27/html`.

The initial over-preserve candidate count is only a triage signal. Some candidates are legitimate UI labels or page titles, but many must be reclassified as translatable prose terms, bilingual first-use terms, or context-dependent labels.

## Source Priority

Use sources in this order when deciding terminology:

1. RenderMan 27 official documentation and local downloaded source pages.
2. Pixar RenderMan public pages, especially product, fundamentals, release, and technical pages.
3. Upstream official specifications used by RenderMan: Open Shading Language, MaterialX, OpenUSD, OpenEXR, OpenVDB, OpenColorIO, Cryptomatte.
4. Official DCC documentation only when reviewing bridge-specific UI/workflow terms for Maya, Houdini, Katana, Blender, and Solaris.
5. Common Chinese CG/VFX usage, used only to choose readable Chinese phrasing after the technical meaning is confirmed.

Online access already verified for:

- https://renderman.pixar.com/tech-specs
- https://renderman.pixar.com/fundamentals-materials
- https://rmanwiki-27.pixar.com/space/REN27/542213836/PxrSurface
- https://open-shading-language.readthedocs.io/en/latest/

## Term Decision Classes

Every important term should be assigned one of these classes.

| Class | Meaning | Examples |
|---|---|---|
| preserve | Must stay English/exact. | RenderMan, PRMan, XPU, RIS, PxrSurface, Rix, Ri, RMANTREE, txmake |
| translate | Should normally be Chinese in prose. | rendering -> 渲染, shading -> 着色, material -> 材质, displacement -> 置换 |
| bilingual-first-use | First use should be Chinese plus acronym or English. Later uses may use acronym. | 任意输出变量（AOV）, 光路表达式（LPE）, 开放着色语言（OSL） |
| context-ui-label | Keep exact English only when referring to the UI/control label; translate surrounding prose. | Enable Manifold Walk, Trace Light Paths, Shadow Mode |
| context-title | Page, paper, asset, video, or project titles may stay English, but descriptive prose should be Chinese. | The Open Chess Set, Layered Materials, Schlick approximation |
| review-required | Meaning depends on page context and must be manually adjudicated. | User lobe, Pattern nodes, procedural noise, display line |

## Translation Style Rules

- Preserve exact identifiers beginning with `Pxr`, `Rix`, `Ri`, `RfM`, `RfH`, `RfK`, `RfB`, `PRMan`, `RMAN`, and similar prefixes.
- Preserve file paths, environment variables, command names, JSON keys, Python/C++ identifiers, parameter names, code blocks, and literal UI labels.
- Translate ordinary explanatory nouns and verbs into Chinese even if they are common CG terms.
- Prefer Chinese core terms when they are established: 渲染, 着色, 材质, 纹理, 采样, 积分器, 光路, 合成, 置换, 体积, 次表面散射, 法线, 反照率, 噪声, 降噪.
- Use bilingual phrasing where a term is both technical and likely useful for search, such as `光路表达式（LPE）`.
- Do not leave sentences with dense English fragments unless those fragments are identifiers, UI labels, command examples, or official product names.

## Review Phases

### Phase T0: Baseline and Plan

Goal: establish review criteria, sources, and measurable audit targets.

Tasks:

- Record current glossary/page baseline.
- Identify preserve-heavy glossary entries.
- Define decision classes and review rules.
- Create first audit plan document.

Exit criteria:

- This plan exists.
- Baseline counts are recorded.
- Next phase inputs are clear.

### Phase T1: Source Research and Termbase Recalibration

Goal: recalibrate the glossary against official and high-confidence references.

Tasks:

- Build `source-research.md` with official source links and term notes.
- Split `renderman_terminology.json` concepts into decision classes without losing original entries.
- Generate `overpreserve-candidates.tsv`.
- Generate `term-decision-overrides.json` for reclassified terms.

Exit criteria:

- All top-level RenderMan domains have source-backed term decisions: rendering, materials/shading, lights, volumes, geometry, sampling/filtering, color, stylized looks, DCC bridges, Tractor.
- High-risk preserve candidates are either confirmed, reclassified, or marked review-required.

### Phase T2: Automated Page Triage

Goal: find pages most likely to contain terminology problems or too much English in prose.

Tasks:

- Extract visible prose text from `html-zh` while ignoring code, preformatted blocks, scripts, styles, hidden downloader metadata, and exact UI label contexts where detectable.
- Score pages by English residual density after applying the approved preserve allowlist.
- Report dense mixed-language sentences.
- Detect protected terms that were accidentally translated or damaged.
- Detect glossary terms with inconsistent Chinese translations.

Exit criteria:

- `page-risk-report.json` and `page-risk-report.md` exist.
- Every page receives a risk tier: high, medium, low, or exempt.

### Phase T3: Manual Terminology Review by Domain

Goal: review and correct high-risk pages in controlled batches.

Suggested batch order:

1. RenderMan core rendering and outputs.
2. Materials, shading, PxrSurface, Lama, MaterialX, OSL.
3. Lighting, light filters, cameras, sampling, filtering, integrators.
4. Geometry, displacement, volumes, OpenVDB, subdivision, curves.
5. Stylized Looks and NPR terms.
6. DCC bridge workflows: Maya, Houdini/Solaris, Katana, Blender.
7. RenderMan University pages and project pages.
8. Tractor pages and developer/API pages.

Exit criteria per batch:

- Batch pages reviewed against source English and calibrated glossary.
- Corrections applied through text-node-safe mechanisms.
- Layout/tag audit still passes.
- Batch report records reviewed page count, corrected terms, remaining decisions, and total progress.

### Phase T4: Final Consistency Audit

Goal: prove the terminology pass is complete and does not damage layout.

Tasks:

- Re-run terminology scanner across all 816 pages.
- Re-run existing layout audit.
- Review final high-risk English fragments.
- Update glossary and README status.

Exit criteria:

- 816/816 pages have terminology review status.
- No high-risk unreviewed mixed-language prose remains.
- Protected identifiers remain intact.
- Final report documents known acceptable English residues.

## Progress Accounting

Use two progress metrics:

- Page progress: reviewed pages / 816.
- Termbase progress: decided high-risk terms / high-risk candidate terms.

Every completed phase report should include both metrics, even if one metric has not changed.

## Initial Risk Signals

The existing glossary contains many likely valid preserved identifiers, but the following kinds of entries need review:

- English category phrases marked preserve, such as `pattern nodes`, `texture nodes`, and `procedural noise`.
- UI labels mixed into prose, such as `Enable Manifold Walk`, `Trace Light Paths`, and `Shadow Mode`.
- Page-title or section-title phrases that should stay English in navigation but may need Chinese in body prose.
- Technical labels where English is useful for precision, but surrounding explanation should be Chinese, such as `User lobe`, `display line`, and `LPE accessible lobe`.

Initial page scan also shows that simple English-density scoring is noisy because it counts hidden download metadata and page titles. The Phase T2 extractor must ignore those regions before using the score for review decisions.

## Safety Requirements

- Do not edit HTML structure when fixing terms.
- Prefer pipeline-compatible text-node updates or controlled DOM text replacement.
- After fixes, compare source and target tag fingerprints.
- Preserve official layout and navigation assets.
- Record every batch correction in a phase report.
