# Git 协作约定

## 最小分支模型

- `main`：当前稳定、可运行、可继续提交的版本。
- `work/*`：任务分支，例如 `work/q2-baseline`。
- `fix/*`：修复分支，例如 `fix/q2-capacity-constraint`。
- `paper/*`：必要时用于论文集中修改。

## Commit 原则

Commit 要说明“改变了什么以及结果是否变化”。

推荐：

`fix(q2): add capacity constraint; objective 153.82 -> 148.67; supersede R014`

## 必须 Review 的改动

- 核心模型；
- 最终算法；
- Final Run；
- 摘要；
- 最终提交文件。
