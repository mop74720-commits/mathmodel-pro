# mathmodel-pro

数学建模竞赛“教练层”仓库。

定位：负责比赛大方向、阶段推进、时间管理、质量底线、协作约定和通用模板；不负责具体算法实现，不内置庞大的专项 Skill 集合。

## 三层生态中的位置

- `mathmodel-pro`：教练 / Playbook / Strategy
- `mathmodel-skills`：专项 Skill Router + Skill Library
- `CUMCM-YYYY-X`：真实比赛 Git 协作仓库

依赖方向：`mathmodel-pro -> mathmodel-skills -> competition repo outputs`。

## 核心原则

1. 题面事实优先于一切推断。
2. 大框架稳定，小问题按需调用 Skill。
3. 比赛仓库始终保持“当前可提交”状态。
4. 先 Baseline，再改进；先 MVP，再全量计算。
5. 模型、实现、结果、论文必须一致。
6. 48 小时后原则上冻结核心模型，只允许低风险改进。
7. 论文中的关键结论必须能追溯到真实 Run / 图 / 表 / 代码。
8. AI 只做辅助，关键判断必须人工核验并留痕。

## 主流程

READ -> FREEZE -> MODEL -> IMPLEMENT -> VERIFY -> WRITE -> AUDIT -> SUBMIT

详见 `SKILL.md` 与 `playbooks/`。


## Competition template

`templates/competition-repo/` 是真实比赛 Git 仓库初始化骨架。其论文部分借鉴 `chenboshuo/cumcm_template` 的分文件与多构建模式思想，但不继承旧版版式规则。

## Upstream overlap selection

v0.3.0 对 `ll2010650-coder/mathmodel-pro` 和 `chenboshuo/cumcm_template` 中与本仓库重叠的能力进行了逐项对比，而不是直接复制。选择依据见 `UPSTREAM_COMPARISON.md`。
