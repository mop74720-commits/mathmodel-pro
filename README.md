# mathmodel-pro v0.3.2

数学建模竞赛 Coach 层。v0.3.2 根据 2020C 全系统演练把顶层决策正式改为 **State-first**。

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
