# Competition Repository Template

这是 `mathmodel-pro` 用来初始化真实比赛 Git 仓库的模板。

目标：让三名队员围绕同一个事实源、模型合同、Run 记录和论文工程协作，而不是把 Skill/知识库混入比赛仓库。

## 目录

```text
.
├── problem/        # 题面事实、假设
├── models/         # 各问模型合同
├── src/            # 可复现代码
├── runs/           # 实验/正式 Run 记录
├── results/        # 表格与正式结果
├── figures/        # 代码生成的正式图片
├── reference/      # BibTeX / 文献元数据
├── paper/          # 分章节论文工程
├── audit/          # Claim-Evidence / 决策记录
└── ai/             # AI 使用留痕
```

## 使用原则

- `main` 保持当前可提交状态；具体任务用短生命周期 `work/*` / `fix/*` 分支。
- `problem/FACTS.md` 是题面事实基线。
- `models/qN/METHOD_CONTRACT.md` 描述“数学模型与真实实现”的合同。
- `runs/RUN_LEDGER.csv` 记录所有会影响正式结论的运行；每问只能指定一个当前 `FINAL` Run。
- `paper/` 只引用已进入 `results/` / `figures/` 且能追溯到 Run 的证据。
- 最终格式以当届官方规则为准；模板中的 LaTeX 仅提供结构骨架。
