# Upstream notice

`mathmodel-pro` v0.3.0 is a refactored contest-coach layer that absorbs useful material from two public GitHub projects.

## 1. ll2010650-coder/mathmodel-pro

- Upstream: https://github.com/ll2010650-coder/mathmodel-pro
- Baseline inspected: commit `66b3bfa6a773b2763950f88acc5d646337466ac7` (2026-07-27, v1.1.0 line).
- License: MIT. A copy is retained in `licenses/ll2010650-mathmodel-pro-MIT.txt`.
- Absorbed and adapted: six-stage operating discipline, modeling norms, document handling, visualization discipline, Word/Pandoc production lessons, historical case notes, training-paper lessons, award-paper structural observations, and the Word post-processing scripts.
- Deliberately generalized or removed: named-user profile, fixed local paths, MATLAB-only requirement, mandatory Obsidian, and private quality targets such as minimum page/figure counts.

## 2. chenboshuo/cumcm_template

- Upstream: https://github.com/chenboshuo/cumcm_template
- Baseline inspected: commit `06372c777e88301113f14cc2f7e9e1ed3dfd44b6` (2021-09-10).
- The repository root did not expose an explicit license during inspection. Therefore this project does **not** redistribute its `cumcmthesis.cls`, original Makefile, or other source files verbatim.
- Absorbed as design ideas only: `reference/src/thesis` responsibility separation, sectionized paper source, draft-vs-release builds, generated support-file tree, and cross-platform build entry points. Those mechanisms are reimplemented from scratch here.

## Rule priority

Official rules for the current contest edition always override upstream defaults, templates, examples, or historical practices.
