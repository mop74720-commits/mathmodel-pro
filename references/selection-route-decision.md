# Selection & Route Decision Knowledge

> 这是 Coach 的策略知识，不是强制 Stage，也不是独立 Agent。

## 核心对象

选题时比较的不是题目名称，而是：`candidate problem × executable route × validation path × failure recovery`。

## Information-gain loop

对仍有竞争力的候选，先问哪个未知最可能改变选择，再设计最低成本 probe。典型 probe：

- 机理：单位/边界/参数可得性、小实例方程闭合；
- 优化：最小 LP/MILP/greedy 可行性、变量规模、约束一致性、solver 预跑；
- 数据：字段、缺失率、标签质量、泄漏风险、最简单 baseline；
- 几何：可辨识性、镜像解、条件数、小案例逆验；
- 仿真：规则可校准性、确定性极限。

## Problem Card（按需）

- deliverable clarity
- data / parameter reality
- structural difficulty
- validation opportunity
- engineering risk
- paper expressibility
- team-fit dependency（软信号）
- current decisive unknown

数字评分只能是 proxy；必须同时保留证据与 flip condition。

## Route Card（按需）

- deliverable
- baseline / minimal witness
- primary route
- binding constraints
- engineering risk
- deciding probe / deciding evidence
- rejected alternative（仅真实竞争时）
- refutation test
- flip condition
- fallback trigger + action
- judge-visible evidence

低不确定性时只需 baseline + primary；不要为了形式制造第二路线。

## Engineering feasibility

重点看输入是否可得、solver 是否可迭代、能否验证、失败后能否保住完整答案，以及结果能否形成评委可见证据。

“尽早 baseline”是启发，不是固定时间门槛。若最重要的是先证明可辨识性、核实参数或修正题意，就先做这些。

## Differentiation priority

`correct → executable → verifiable → explainable → differentiated`

不要为了不同而选择证据更差的路线。

## Reopen selection

只有 route-level blocker 才值得重新打开 selection，例如关键输入不可得、核心结构不可辨识/不可行、solver 风险不可承受且无局部 fallback、当前题无法形成可验证核心交付。局部模型失败通常由 SkillHub 修复。

## Upstream inspiration

选择性吸收 `y3519712124-ui/math-modeling-contest-route-selection` 的 route-led selection、engineering feasibility、refutation、flip condition 与 fallback 思想；固定评分权重、固定分差、固定 Day-One gate 与强制多路线规则未采用。MIT 许可见 `THIRD_PARTY_NOTICES.md`。
