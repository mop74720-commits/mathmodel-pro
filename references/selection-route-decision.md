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

### Probe type 必须服务于 deciding unknown

不要把“做实验”本身当进度。按当前决定性未知选择最小证据动作：

- `analytical_check`：量纲、极限、小实例、可辨识性、闭合性；
- `data_probe`：字段、质量、切分、泄漏、最小 baseline；
- `literature_check`：核验方法前提、变量需求、验证方式与迁移边界；
- `solver_probe`：最小可行模型、规模、收敛与数值风险；
- `pilot_run`：真实竞争候选在同一数据/切分/指标/预算下做小规模比较；
- `sensitivity_probe`：只针对可能翻转当前结论的关键参数或假设。

`pilot_run` 是 Coach 的 probe 类型，不新增同名 Skill；通常组合 SkillHub 的 `model-comparison + implementation + experiment-manager`。

## Historical experience prior

当当前题或候选路线存在明显结构特征时，先读取 `experience/index.yaml`，按**问题结构而不是题目名称**检索少量历史案例。历史经验的作用是改变 candidate prior，而不是替代当前题证据。

历史经验只能作为 prior：

- 可以把过去有效的 baseline / decomposition / validation 提前放入 shortlist；
- 可以把过去出现过的 failure mode 提前变成 refutation test；
- 可以提示哪个 cheap probe 最可能快速淘汰错误路线；
- 不可以把历史模型名机械绑定到当前题型；
- 不可以把历史结果、参数、阈值或“获奖论文做法”写成当前事实；
- deciding evidence 必须来自当前赛题本身。

每次实际借用一个案例，至少记录：

- `case_id`
- matched structure
- mismatch
- transfer risk
- candidate effect
- deciding probe

默认只检索 Top-3，必要时扩展到 Top-5。若没有可信的数值相似度模型，使用 high/medium/low 或 pairwise evidence，不制造伪精确分数。

跨案例模式可进一步查 `experience/patterns.yaml`，已知失败模式查 `experience/failures.yaml`。

## Evidence reconciliation：题意也允许被证据修正

第一次问题解释不是永久冻结。若数据审计、可靠文献、官方来源、用户纠正或当前题可复现 probe / Pilot 暴露了会改变 deliverable、输入输出、约束、切分、验证口径或跨问依赖的新事实，Coach 应重新核对：

`题面原文 -> 当前解释 -> 新证据 -> 是否修正解释/假设/路线`

修正时只更新真正受影响的 `INTERPRETATIONS / QUESTION_MAP / ASSUMPTIONS / Route / Model Contract`，并把原因写入 Decision Log。历史经验与文献方法只能提供 prior/条件信息，不能未经当前题核验直接写入 `FACTS.md`。

完整规则见 `references/evidence-reconciliation.md`。

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

## High-stakes independent challenge

当路线选择影响多个小问、核心结论或大量后续工作，且存在可信替代结构时，可临时使用：

`incumbent proposal -> independent alternative -> blind challenge -> deciding evidence`

这里描述的是审查职责，不要求固定多个 Agent。若问题低风险、替代路线没有具体机制优势或验证成本过高，则不要机械触发。

## Engineering feasibility

重点看输入是否可得、solver 是否可迭代、能否验证、失败后能否保住完整答案，以及结果能否形成评委可见证据。

“尽早 baseline”是启发，不是固定时间门槛。若最重要的是先证明可辨识性、核实参数或修正题意，就先做这些。

## Differentiation priority

`correct → executable → verifiable → explainable → differentiated`

不要为了不同而选择证据更差的路线。

## Targeted rollback / staleness

若上游题意解释、关键假设或模型合同发生实质变化，不整场重来，也不删除旧产物。沿真实依赖关系把受影响链标为 `STALE`：

`Interpretation -> Model Contract -> Run -> Result/Figure -> Claim -> Paper Section`

未依赖该变化的分支保持有效；旧产物保留用于审计和回滚，但 `STALE` 产物不得继续支撑 Final Claim。人工纠正应累计记录，避免后续重算把先前反馈丢掉。

## Reopen selection

只有 route-level blocker 才值得重新打开 selection，例如关键输入不可得、核心结构不可辨识/不可行、solver 风险不可承受且无局部 fallback、当前题无法形成可验证核心交付。局部模型失败通常由 SkillHub 修复。

## Upstream inspiration

选择性吸收 `y3519712124-ui/math-modeling-contest-route-selection` 的 route-led selection、engineering feasibility、refutation、flip condition 与 fallback 思想；固定评分权重、固定分差、固定 Day-One gate 与强制多路线规则未采用。MIT 许可见 `THIRD_PARTY_NOTICES.md`。

2026-09-10 对 `ll2010650-coder/mathmodel-pro` 做第二轮案例级吸收：恢复其获奖论文、训练论文和经典题中可迁移的结构经验，但只进入 `experience/` 作为 historical prior，不恢复固定六阶段工作流和环境/篇幅硬编码。

2026-09-10 选择性参考 `zhou2030109-glitch/Remit`：吸收“数据/文献/当前实验证据可回头校正题意”、Pilot 作为 route probe、高影响选型的独立 challenge、累计人工反馈与定点回滚思想；不复制固定四角色 Agent 流程，不采用固定 `20%/30%/50%` 方法检索权重，也不把 checkpoint 等同于科学质量。许可说明见 `THIRD_PARTY_NOTICES.md`。
