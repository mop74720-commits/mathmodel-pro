# Upstream overlap selection

目标：只比较“本仓库已有且上游也有”的同功能内容，选择更优版本或融合，而不是按缺失项把上游整包搬入。

## ll2010650-coder/mathmodel-pro

| 重叠项 | 选择 | 原因 |
|---|---|---|
| `SKILL.md` / 全流程职责 | 以 coach v0.2 架构为主 | 当前三层架构边界更清晰；上游完整但把算法、软件、Word、个人偏好耦合进一个大 Skill |
| 审题阶段 | 融合 | 上游“实际查看数据、六要素、歧义闭环”更强；当前 FACTS/ASSUMPTIONS、Baseline、比赛时序更强 |
| 建模阶段 | 融合 | 上游分题型纪律更丰富；当前 Baseline、模型-实现合同、验证前置更合理 |
| 实现阶段 | 融合 | 保留上游小实例、回代约束、记录中间产物；删除“核心计算必须 MATLAB”等环境绑定 |
| 验证阶段 | 融合 | 上游给出更多验证类型；删除固定阈值和固定重复次数，改为风险/精度驱动 |
| 论文阶段 | 以当前 coach 为主并吸收细节 | 保留证据链、同步写作；吸收图证闭环、摘要定量、模型表达纪律；拒绝固定章节/页数/图数/创新条数 |
| `modeling-norms.md` | 融合重写 | 上游覆盖面胜出，但其算法决策树和固定阈值过度刚性；当前原则正确但过薄 |
| `award-winning-papers.md` | 融合压缩 | 上游案例证据丰富但过长且含本机路径；当前过薄。保留跨案例共性，不保留路径和“照模板”倾向 |
| `training-papers-lessons.md` | 融合压缩 | 上游历史评审信息很有价值，但不适合把数万字案例直接放 coach；提炼成高频失败模式 |
| `word-paper-pipeline.md` | 融合重写 | 上游自动化经验强，但绑定固定 docx、脚本、COM、MathType 环境；改为 Word/LaTeX 双轨通用生产纪律 |

明确拒绝升级为通用规则的上游内容：固定软件（MATLAB/LINGO/Origin）、固定本机路径、固定文献数量、固定页数/字数/图数、固定敏感性扰动比例、固定 Monte Carlo 次数、固定随机算法重复次数、固定章节小节数量。

### 2026-09-10 第二轮：案例粒度恢复

第一次融合把长案例压缩成了通用规则，适合常驻 Coach，但损失了“过去遇到过什么结构、什么方法成功/失败、什么验证最有信息量”的可检索粒度。

本轮新增 `experience/`：

- `experience/index.yaml`：14 个结构化案例卡；
- `experience/patterns.yaml`：跨案例成功模式；
- `experience/failures.yaml`：高频失败模式；
- `experience/README.md`：prior-not-evidence 边界与检索协议。

这不是恢复上游固定六阶段工作流，而是恢复**案例级 prior**。历史案例只用于候选生成、probe、refutation、fallback 与 validation；当前题的 deciding evidence 必须来自当前赛题。

## chenboshuo/cumcm_template

| 重叠项 | 选择 | 原因 |
|---|---|---|
| `main.tex` | 保留当前版本 | 上游绑定历史 `cumcmthesis` 与 2020 字段；当前骨架对当届官方模板保持中立，并增加 Q4/validation/AI statement |
| 分章节结构 | 当前版本 | 两者思想相同；当前 `model/solution/validation` 与证据链更匹配 |
| `Makefile` | 保留当前版本 | 当前 clean 更安全、依赖更少；上游依赖 `timeout/tree/awk`，且 `git clean -fXd` 风险更高 |
| `make.ps1` | 保留当前版本 | 当前按 target 构建且非阻塞；上游一次生成多个版本并 `Read-Host` 阻塞 |
| `reference.bib` | 保留当前版本 | 当前只允许真实核验条目，避免示例条目被误提交 |
| `notations.tex` | 保留当前版本 | 上游 glossary 自动化依赖旧 class/package；当前模板更轻、兼容性更高 |
| 支撑材料目录 | 保留当前实现 | 当前用 Git tracked files 生成，不依赖系统 `tree` 命令 |

因此，chen 上游在“分文件 + 自动构建”的设计思想上值得保留，但同功能具体实现不替换当前版本。

## Route-selection upstream (v0.4.0)

`y3519712124-ui/math-modeling-contest-route-selection` 的 route-led selection、engineering feasibility、refutation、flip condition、fallback 被选择性吸收为 Coach decision knowledge。未采用固定评分公式、固定 near-tie 阈值、固定 Day-One gate 或强制多路线。Selection 被实现为临时 workspace，而不是新增长期 Router/Agent。
