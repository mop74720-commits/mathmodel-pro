# Historical Experience Memory Extension — 2026-09-10

本次提交不改变 v0.4.1 的 State-first / Outcome-first 主架构，而是补足案例级历史经验检索。

## 新增

- `experience/index.yaml`
  - 14 个历史案例卡；
  - 9 个获奖论文案例；
  - 4 个训练论文 + 教师评审案例；
  - 1 个 2001 CUMCM B 经典图像/几何案例。
- `experience/patterns.yaml`
  - progressive modeling；
  - prove-before-compute；
  - dimensionality reduction；
  - hierarchical optimization；
  - independent cross-check；
  - degeneracy validation；
  - network compression；
  - inspect-data-first 等。
- `experience/failures.yaml`
  - model-code drift；
  - error magnitude misread；
  - sensitivity mismatch；
  - result-version drift；
  - step-size under-justification；
  - enumeration/Monte-Carlo confusion；
  - probability mass loss；
  - parameter-variable confusion；
  - heuristic global-optimum overclaim；
  - assumed data shape。
- `scripts/validate_experience.py`
  - 检查案例数量、ID 唯一性、prior-not-evidence 边界和 route integration。

## 路由变化

`references/selection-route-decision.md` 增加 Historical experience prior：

```text
current structure
→ historical retrieval
→ candidate prior
→ cheap probe / refutation
→ current evidence
→ route decision
```

历史经验只改变候选优先级、probe、fallback 和 validation，不直接成为当前题证据。

## 上游边界

本次主要对 `ll2010650-coder/mathmodel-pro` 进行第二轮案例粒度吸收。保留其历史案例中的结构经验；仍拒绝恢复固定六阶段状态机、固定 MATLAB/LINGO/Origin、固定页数/字数/图数、固定敏感性比例和其他环境/篇幅硬编码。
