# mathmodel-pro v0.3.0

数学建模竞赛“教练层”：负责比赛大方向、阶段推进、时间策略、质量底线、协作约定、项目模板和专项 Skill 路由。

## 三层架构

- `mathmodel-pro`：教练 / Playbook / Strategy / Templates
- `mathmodel-skills`：具体小情景的 Router + Skill Library
- `CUMCM-YYYY-X`：三人真实 Git 协作仓库

## 本版吸收内容

### 来自 ll2010650-coder/mathmodel-pro（MIT）

保留并通用化了：

- 六阶段“输入→步骤→产物→验收”纪律；
- 题面六要素、模糊表述预检、分题型建模规范；
- 最小步骤运行、约束回代、随机算法复现、灵敏度/收敛检查；
- 图表三问、流程图和视觉检查原则；
- 文档处理规则、两个历史案例、训练论文扣分经验、获奖论文结构观察；
- Word/Pandoc 生产线和公式/表格后处理工具。

去掉或降级为可选：个人用户画像、固定本机路径、MATLAB-only、强制 Obsidian、最低页数/图数等私人 KPI。

### 来自 chenboshuo/cumcm_template（设计参考）

重新实现了：

- `reference / src / paper` 职责分离；
- 论文 section 分文件；
- draft/release 两种构建模式；
- 支撑材料文件树自动生成；
- Windows / Make 构建入口。

未复制其旧 `cumcmthesis.cls` 或其他未明确授权源码；最终版式必须按当届官方规则更新。

## 主流程

`READ -> FREEZE -> MODEL -> IMPLEMENT -> VERIFY -> WRITE -> AUDIT -> SUBMIT`

只保留四个关键 Gate：`MODEL / MVP / FINAL RESULT / PAPER`。

## 目录

- `playbooks/`：赛时阶段手册
- `references/`：方法论、文档、图表、历史经验
- `tools/word/`：Word/Pandoc 后处理
- `assets/word/`：Pandoc reference.docx 等静态资产
- `templates/competition-repo/`：真实比赛 Git 仓库模板
- `UPSTREAM_NOTICE.md`：上游来源和许可边界

## 使用

1. 赛前维护 `mathmodel-pro` 和 `mathmodel-skills`。
2. 开赛后复制 `templates/competition-repo/` 为新的比赛仓库并 `git init`。
3. 三人只在比赛仓库协作；教练/Skill 仓库视为只读工具。
4. 比赛开始时在 `paper/` 中选择 Word 或 LaTeX 一条生产线。
