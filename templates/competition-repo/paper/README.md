# Paper Engineering Template

本目录吸收 `chenboshuo/cumcm_template` 的三个核心工程思想：

1. `main.tex` 只负责总装，正文按 `sections/` 拆分；
2. 草稿版允许显示 TODO，发布版自动隐藏 TODO；
3. 代码、文献、图片与论文正文分目录维护，并可自动生成支撑材料文件树。

## 重要边界

这里**不内置旧版 `cumcmthesis.cls`**。仓库中的结构源自历史模板经验，但最终提交必须切换/适配到当届官方允许的版式与模板。

默认 `main.tex` 使用 `ctexart` 作为可编译的结构草稿。正式提交前必须根据当届规则完成版式替换与 PDF 目检。

## 构建

Linux/macOS：

```bash
make draft
make release
make tree
make clean
```

Windows PowerShell：

```powershell
./make.ps1 draft
./make.ps1 release
./make.ps1 tree
```

- `draft`：显示 `\coachTODO{}` 提示；
- `release`：隐藏 TODO，生成发布候选 PDF；
- `release` 只表示“无 TODO 的论文候选”，**不等价于官方格式审计通过**。
