# mathmodel-pro v0.5.0-alpha

## v0.5.0-alpha — Route Selection contract

在 v0.4.1 的 Selection Workspace / State-first 架构上，加入结构化 route
record、decision record、外部 adapter 边界和不自动晋升 FACT 的 validator。
这不是新的 Router、Decision Engine 或 Freeze Engine；评分只能作为
`proxy_only` 证据，最终全局裁决仍属于 Coach。

## v0.4.1 — Outcome / Competitiveness repair

在 v0.4.0 Selection/State-first 架构上，修复“可复现就过早冻结”和“系统闭环替代成果质量”的目标漂移。新增 Outcome-first 目标层级，并显式区分 `REPRODUCIBLE` 与 `COMPETITIVE_ENOUGH`；只有存在具体高信息量 challenge 时才继续挑战 incumbent，不引入固定搜索次数或模型数量。


## v0.4.1 — Selection Workspace / Route-led decision

本版把多题/多路线尚未确定建模为临时 Selection Workspace，而不是新增长期 Router 层。Coach 使用 `candidate → decisive unknown → cheap probe → evidence → flip/fallback` 循环；正式选题后只把确认过的证据晋升到 Competition Repo。数值评分降级为可选 proxy。

数学建模竞赛 Coach 层。v0.4.1 根据完整三层系统演练与集成审计，把顶层决策正式改为 **State-first**。

## 三层关系

```text
mathmodel-pro          = Coach：现在最值得做什么
mathmodel-skills       = SkillHub：这个局部问题怎么做
competition-template   = Competition Repo：本场比赛唯一事实源
```

## 核心变化

- 不再把 READ→MODEL→CODE→WRITE 等当全局状态机；
- 不再用固定小时数自动触发冻结/写作/提交；
- playbook/time window 只作情景参考；
- 四个 Gate 只描述某个问题或产物的质量成熟度；
- Skill 路径不由 Coach 硬编码，必须读取 SkillHub `registry.yaml`；
- 独立 `competition-template` 是唯一比赛仓库模板。

Coach 默认从 Competition Repo 的 `PROJECT_STATUS.md`、FACTS、QUESTION_MAP、模型合同、Run、Claim-Evidence 和 Decision Log 重新判断优先级。

发布检查：

```bash
python scripts/validate_coach.py
```


## v0.4.1 Official-Rules Closure

- 正式竞赛开始后主动核验当届官方规则，不再把“用户未上传规则”视为可忽略的外部事项。
- 规则未核验不阻塞前期建模，但硬性禁止 `SUBMISSION_READY`。
- 将 `rules/RULE_PROFILE.json` 作为 Competition Repo 内当前届次规则状态的机器伴随文件；人类可读来源仍保存在 `rules/OFFICIAL_RULES.md`。
- AI 使用与支撑材料要求被纳入提交判断，但不得虚构 AI 日志或人工核验。
