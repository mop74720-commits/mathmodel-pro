# Historical Experience Memory

`experience/` 是 `mathmodel-pro` 的历史经验层。它保存“过去哪些问题结构出现过、哪些路线有效、哪些路线失败、什么验证最有信息量”，用于帮助 Coach 生成候选路线和 cheap probe。

它不是当前比赛的事实源，也不是算法教程库。

## 1. 核心边界

历史经验只能作为 **prior**：

- 可以提高某条候选路线进入 shortlist 的优先级；
- 可以提示最值得先验证的失败模式；
- 可以提示 baseline、fallback、validation 和 judge-visible evidence；
- 不可以因为过去某题用了某模型，就直接决定当前题也用该模型；
- 不可以把历史参数、结论、阈值或最优结果写入当前 `problem/FACTS.md`；
- 当前赛题的 deciding evidence 必须来自当前题面、附件、官方来源或当前可复现实验。

简写：

```text
current structure
    ↓
historical retrieval
    ↓
candidate prior
    ↓
cheap probe / refutation
    ↓
current evidence
    ↓
route decision
```

## 2. 如何检索

默认先读 `index.yaml`，按“结构相似”而不是“题目名字相似”检索。优先比较：

1. deliverable：最终要预测、优化、排序、重建、解释还是制定策略；
2. problem family：优化、统计、机理、网络、几何、仿真等；
3. data modality：表格、时序、图像、图网络、参数型；
4. variable / constraint structure：连续、整数、分层、时变、守恒、碰撞、边界；
5. dynamics / uncertainty：静态、动态、随机、重复测量、参数不确定；
6. validation opportunity：是否可退化、守恒、独立互验、小规模精确解；
7. engineering risk：solver、计算规模、参数可得性、实现复杂度。

默认取 Top-3；只有候选高度相近时扩展到 Top-5。

## 3. 每次借用历史案例必须记录

至少明确：

- `case_id`
- 匹配了哪些结构；
- 哪些结构不匹配；
- 迁移风险；
- 该案例只改变了什么：候选优先级 / probe / fallback / validation；
- 当前题真正的 deciding probe 是什么。

不要输出虚假的“相似度 92.7%”。如果没有可靠可校准的距离模型，使用 high / medium / low 或 pairwise evidence 即可。

## 4. 文件

- `index.yaml`：案例卡索引，面向检索和路由；
- `patterns.yaml`：跨案例可复用的成功模式；
- `failures.yaml`：高频失败模式与最小反证动作；
- `references/selection-route-decision.md`：Coach 如何把历史 prior 接入 Selection / route decision。

## 5. 当前种子案例

v0.4.1 后的 experience seed 共 14 个：

- 9 个国赛获奖论文案例：A016、A053、A196、B060、B157、C023、C132、D037、E030；
- 4 个训练论文 + 教师评审案例：TR-T01 ~ TR-T04；
- 1 个 2001 CUMCM B 血管三维重建经典案例。

来源主要来自 `ll2010650-coder/mathmodel-pro` 中的公开案例提炼。当前仓库只保留结构化、可迁移的摘要，不恢复上游固定六阶段状态机、固定 MATLAB、固定页数/字数/图数或固定扰动比例等规则。
