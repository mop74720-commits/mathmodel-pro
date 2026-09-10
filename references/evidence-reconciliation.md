# Evidence Reconciliation & Targeted Rollback

> 这是 Coach 的决策知识。它允许新证据修正题意与路线，但不建立新的固定阶段，也不复制固定多 Agent 工作流。

## 1. 为什么需要 reconciliation

第一次读题得到的是当前最合理的解释，不是不可修改的真理。真实数据画像、可靠文献、当前题的 probe / Pilot 或官方规则，可能暴露原解释中的数据不可得、分组/时间结构、单位、约束、验证口径或任务依赖错误。

因此 Coach 在出现**会改变问题合同或路线选择的高信息量新证据**时，应重新核对：

`题面原文 -> 当前解释 -> 新证据 -> 是否需要修正解释/假设/路线`

不要因为“流程已经往后走”而保留已失效解释；也不要因为拿到一篇新论文就反复重写题意。

## 2. 可触发 reconciliation 的证据

优先级不是固定分数，而看其是否能改变当前决策：

- 题面、附件、官方勘误或当届规则中的直接证据；
- 数据审计发现的真实结构：时间、分组、重复测量、缺失、字段不可得、单位/范围；
- 已核验文献中的方法成立条件或变量要求；
- 当前题可复现 probe / Pilot 暴露的不可辨识、不可行、泄漏、边界或数值问题；
- 用户对题意/业务语义的明确纠正。

历史案例只能提供 prior 和 refutation test，不能单独改写当前事实。

## 3. Reconciliation 输出

只有确实受影响的对象才更新：

- `problem/INTERPRETATIONS.md`：记录旧解释、新解释、触发证据与未决冲突；
- `problem/QUESTION_MAP.md`：若 deliverable、输入输出或跨问依赖改变则同步；
- `problem/ASSUMPTIONS.md`：新增、削弱或撤销受影响假设；
- Route / Model Contract：若结构改变，重新检查 incumbent；
- `audit/DECISION_LOG.md`：记录为什么改变、什么证据触发、哪些下游产物受影响。

不得把文献建议、历史经验或模型生成文本直接晋升为 `problem/FACTS.md`。

## 4. Probe taxonomy

Coach 选择 probe 时先问“哪个未知最可能改变路线”，再从下面选最低成本的证据动作：

- `analytical_check`：量纲、极限、小实例、可辨识性、闭合性；
- `data_probe`：字段、质量、切分、泄漏、最小 baseline；
- `literature_check`：核验方法前提、变量需求、验证方式与可迁移边界；
- `solver_probe`：最小可行模型、规模、收敛、数值稳定性；
- `pilot_run`：对真实竞争候选用同一数据/切分/指标/预算做小规模真实比较；
- `sensitivity_probe`：只扰动当前决定性参数/假设，观察结论或排名是否翻转。

`pilot_run` 不是新的 Skill。它通常组合 SkillHub 的 `model-comparison + implementation + experiment-manager`，必要时再加对应算法 Skill。

## 5. High-stakes independent challenge

当一次路线选择对多个小问、核心结论或大量剩余工作具有高影响，而且仍存在可信替代结构时，可以临时采用：

`incumbent proposal -> independent alternative -> blind challenge -> deciding evidence`

这里的“independent / blind”描述审查职责，不要求固定三个 Agent。低风险、低不确定问题不要机械触发，以免浪费时间和 token。

## 6. Targeted rollback / staleness

上游解释、假设或模型合同发生实质变化时，不删除旧产物，也不整场重来。沿依赖关系把真正受影响的下游标为 `STALE`：

`Interpretation -> Model Contract -> Run -> Result/Figure -> Claim -> Paper Section`

未依赖该变化的其他问题、Run 和论文段落继续保持有效。旧产物保留用于审计、回滚和比较，但 `STALE` 产物不得继续支撑 Final Claim。

## 7. 累计人工反馈

用户/队员在审批节点提出的纠正应追加记录，而不是覆盖掉此前意见。后续重算应能回答：

- 本次从哪个对象回退；
- 哪条累计反馈触发；
- 哪些依赖项被置为 STALE；
- 哪些对象保持 VALID；
- 何种新证据才能重新通过。

## 8. 边界

- 不引入固定 Coordinator / Modeler / Coder / Writer 状态机；
- 不采用固定候选数量或领域/子领域/方法的硬编码权重；
- 不把 checkpoint 当作科学质量证明；
- 不用 reconciliation 制造无限反复，只有能改变高影响决策的新证据才值得重新打开。

设计启发参考 `zhou2030109-glitch/Remit` 的 evidence feedback、Pilot、human rollback 与 recoverability 思想；本文为本项目架构下的独立改写。许可说明见 `THIRD_PARTY_NOTICES.md`。
