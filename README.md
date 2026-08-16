# 雅排 ya-pai · 组合式公众号文章排版 Skill

> 把一篇 Markdown 文章，排版成 **单个自包含、可直接粘贴进微信公众号编辑器的 HTML** —— 不是换颜色，而是「第一眼」就不同。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agents](https://img.shields.io/badge/Codex%20·%20Claude%20Code%20·%20Cursor-supported-8b5cf6.svg)](#-快速开始)
[![Skeletons](https://img.shields.io/badge/版式骨架-10-059669)](tokens/layouts.md)
[![Presets](https://img.shields.io/badge/预设组合-12-3b82f6)](tokens/presets.md)
[![Gallery](https://img.shields.io/badge/组合画廊-11%20套-9a5f32)](examples/gallery/index.html)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/walksu/ya-pai/pulls)

**ya-pai（雅排）** 是一个给 AI Agent 用的公众号排版 Skill：你写完 Markdown，它按你选定的组合，生成**样式全内联、粘贴到公众号编辑器不掉格式**的 HTML —— 自动章节编号、关键词下划线、引用与目录、代码块、作者签名，并用校验脚本确定性兜住公众号平台的各种限制。

## ✨ 核心特性

- **九维度自由组合**：气质 × 色板 × 字体 × 版式骨架 × 疏密 × 装饰 × 背景样式 × 功能模块 × 标题风格。每个维度都是可独立更换的「原子」，组合空间是无限的。
- **10 套版式骨架**：单栏流 / 导读+章节流 / 时间线式 / 卡片式 / 海报式 / 侧栏式 / 讲义式 / **报章式** / **信笺式** / **终端式** —— 决定整篇文章的第一眼印象，不只是换宽窄。
- **12 套一键预设**：经典编辑 / 科技极简 / 深夜终端 / 书卷墨绿 / 温暖故事 / 冷静报告 / 侧栏版 / 海报观点 / 讲义纸感 / 报章观察 / 信笺致读者 / 终端窗口版。
- **11 套组合画廊**：同一篇短文渲染出 11 种完全不同的排版，先看图、再选型，每套标注九维度取值。
- **效果优先的提问流程**：看画廊 → 确认 Agent 推荐 → 单点微调 → 作者署名，Agent 只推荐、不替用户选定；每个维度同时开放「预设选项」与「自由填写」两条路。
- **确定性质量门禁**：`validate_gzh_html.py` 检查平台红线（禁 `<style>/<div>/class/id`、样式全内联、文字 `<span leaf="">` 包裹）+ WCAG 对比度 + 审美自检；`publish_audit.py` 做发布前审计（占位符残留 / 本地图片 / 体积）。
- **零格式丢失**：产物是纯 `<section>` 片段，所有样式内联、所有文字用 `<span leaf="">` 包裹，粘贴进公众号编辑器后样式完整保留。

## 🚀 快速开始

### 方式一：npx 安装（推荐）

```bash
npx skills add https://github.com/walksu/ya-pai
```

### 方式二：手动安装（Codex）

```bash
git clone https://github.com/walksu/ya-pai.git "$HOME/.codex/skills/ya-pai"
# Windows PowerShell：
# git clone https://github.com/walksu/ya-pai.git "$env:USERPROFILE\.codex\skills\ya-pai"
```

### 方式三：手动安装（Claude Code / Cursor 等）

```bash
git clone https://github.com/walksu/ya-pai.git "$HOME/.claude/skills/ya-pai"
```

任何能加载 `SKILL.md` 的 Agent 运行时（Codex、Claude Code、Cursor、OpenCode 等）都可使用。

## 📝 用法

1. 对 Agent 说「**用 $ya-pai 排版这篇文章**」，并提供 `.md` 文件路径或直接粘贴 Markdown。
2. Agent 打开**组合画廊**（`examples/gallery/index.html`）让你先看第一眼；也可以让它按文章的「题材 × 文风」推荐整组（不只题材——技术文章写得轻松就该推轻松的组合）。
3. 单选微调：「标题换渐变圆角那种」「版式换海报式」「色板用黄白蓝」；或直接说「全部按推荐 / 自动」。
4. 提供**作者名 + 一句话简介**（用于文末签名卡，必问）。
5. 生成 HTML → 自动跑校验与发布审计 → 打开预览页 → 点「复制到公众号」→ 粘贴进公众号编辑器。

## 🖼️ 组合画廊

同一篇短文，11 种第一眼。完整可交互画廊（带「复制到公众号」按钮）在 [examples/gallery/index.html](examples/gallery/index.html)。

| g01 书卷长文 | g02 科技文档 | g03 冷静报告 | g04 杂志封面 |
|---|---|---|---|
| ![g01](assets/screenshots/g01.png) | ![g02](assets/screenshots/g02.png) | ![g03](assets/screenshots/g03.png) | ![g04](assets/screenshots/g04.png) |
| 纸页感·窄读·墨线章头 | 终端感·目录·结构块 | 论文感·大数字竖线 | 内刊卷首语·衬线大字 |

| g05 海报观点 | g06 极简留白 | g07 讲义纸感 | g08 时间线式 |
|---|---|---|---|
| ![g05](assets/screenshots/g05.png) | ![g06](assets/screenshots/g06.png) | ![g07](assets/screenshots/g07.png) | ![g08](assets/screenshots/g08.png) |
| verdict 页·黄白蓝 | 空气感·水印数字 | 纸面讲义·叠底数字 | 演进轴·圆点竖线 |

| g09 报章式 | g10 信笺式 | g11 终端式 | |
|---|---|---|---|
| ![g09](assets/screenshots/g09.png) | ![g10](assets/screenshots/g10.png) | ![g11](assets/screenshots/g11.png) | |
| 报纸版面·方块编号 | 一封手写信·此致落款 | 终端窗口·提示符 | |

## 🧩 九维度组合

| 维度 | 可选值 | 作用 |
|---|---|---|
| 气质 | 安静编辑 / 现代极简 / 人文书卷 / 冷冽理性 / 温暖纸感 | 决定整体感觉 |
| 色板 | 暖米 / 冷灰 / 深色 / 高对比 / 低饱和 / 墨绿 / 黛蓝 / 奶油 / 纸绿 / 纸蓝 / 陶土 | 背景 + 文字 + 强调色 |
| 字体 | 衬线标题+无衬线正文 / 全无衬线 / 中文友好衬线 / 等宽点缀 / 宋体报章 等 | 最影响「高级感」 |
| 版式骨架 | L1–L10（见下） | **决定第一眼印象** |
| 疏密 | 松 / 中 / 紧 | 控制呼吸感 |
| 装饰 | 几乎无装饰 / 细线 / 轻微色块 / 强调引用 | 避免繁杂 |
| 背景样式 | 纯色 / 微渐变 / 顶部色带 / 深浅分层 / 细边框留白 / 三色分区 | 页面与内容区的底 |
| 功能 | 目录 / 折叠 / 代码增强 / 图注 / 章节编号 / 结尾签名（强制）/ 文末 CTA | 按内容开关 |
| 标题风格 | 编号细线 / 水印数字 / 大数字+竖线 / 色块章头 / 墨线方块 / 反白通栏 / 渐变圆角徽标 / 衬线居中大字 / 终端标签 / 报章方块 | 章节标题的独立变体 |

## 📐 版式骨架速览

| 骨架 | 第一眼 | 适用 |
|---|---|---|
| L1 单栏流 | 干净文字流 | 随笔、书评、观点、长文 |
| L2 导读+章节流 | 先看导航卡 | 教程、清单、方法论 |
| L3 时间线式 | 一条演进轴 | 演进史、案例复盘、编年 |
| L4 卡片式 | 一张张卡片 | 盘点、测评、知识整理 |
| L5 海报式 | 大色块强冲击 | 观点、趋势判断、评测结论 |
| L6 侧栏式 | 目录 + 正文 | 长教程、参考手册 |
| L7 讲义式 | 一页页纸面讲义 | 技术讲解、课程、深度教程 |
| L8 报章式 | 一张报纸版面 | 深度评论、行业观察、新闻解读 |
| L9 信笺式 | 一封手写信 | 致读者、随笔、品牌信 |
| L10 终端式 | 一个终端窗口 | 技术长文、命令教程、工具文档 |

## 📁 目录结构

```
ya-pai/
├── SKILL.md                     # 技能定义 + 主流程指令（Agent 入口）
├── README.md / README.en.md     # 仓库说明（中 / 英）
├── LICENSE                      # MIT
├── agents/
│   └── openai.yaml              # Agent UI 元数据
├── references/                  # Agent 按需读取的详细规则
│   ├── design-system.md         # 九维度组合逻辑 + 提问流程
│   ├── component-library.md     # 维度驱动组件库（F1–F16 家族）
│   ├── editorial-principles.md  # 组件预算 + 节奏 + 编辑心态
│   ├── layout-patterns.md       # 10 套骨架的组件排列顺序
│   ├── anti-slop.md             # 禁止项（字体/装饰/密度/AI 味）
│   ├── typography.md            # 中英文排版细则
│   └── output-spec.md           # 输出要求（单文件 HTML、命名、结构）
├── tokens/                      # 可组合的设计零件
│   ├── aesthetics.md            # 气质定义
│   ├── color-palettes.md        # 11 套色板（含面色板）
│   ├── font-pairings.md         # 字体组合
│   ├── layouts.md               # 10 套版式骨架
│   ├── density.md               # 疏密档位
│   ├── backgrounds.md           # 背景样式
│   └── presets.md               # 12 套一键预设
├── templates/                   # HTML/CSS 骨架
├── examples/                    # 示例（md → html → 效果说明）
│   └── gallery/                 # 组合画廊（11 套，含可交互预览）
├── scripts/                     # 校验 + 预览包装 + 发布审计
│   ├── validate_gzh_html.py     # 强制校验（ERROR/WARNING 清零）
│   ├── wrap_preview.py          # 生成带「复制到公众号」按钮的预览页
│   └── publish_audit.py         # 发布前审计（占位符/本地图片/体积）
└── assets/                      # 预览模板 + 画廊截图
```

## 🛡️ 质量保障

- **合规校验**：`scripts/validate_gzh_html.py <输出.html>` —— 检查公众号会过滤/改写的一切（`<style>`、`<div>`、`class/id`、`position`、`grid`、CSS 变量、外部字体…），并核查文字是否用 `<span leaf="">` 包裹；另做 WCAG 对比度计算与审美自检（连续 4+ 段纯文字阅读墙、AI 默认渐变、font-size 超限）。
- **预览包装**：`scripts/wrap_preview.py <正文.html>` —— 生成带「复制到公众号」按钮的浏览器预览页，一键复制富文本。
- **发布审计**：`scripts/publish_audit.py <正文.html>` —— 占位符残留 / 本地图片未传 / 体积过大 / 预览页缺失，❌ 项清零才可发布。

## 🔧 扩展

- 加新色板 → `tokens/color-palettes.md`；加新字体 → `tokens/font-pairings.md`；加新气质 → `tokens/aesthetics.md`；加新骨架 → `tokens/layouts.md` + `references/layout-patterns.md`；加新组件 → `references/component-library.md` 组件族；加新预设 → `tokens/presets.md`。
- 每套新骨架必须有一组独立的骨架签名组件（如报章式的 F15、终端式的 F16），而不是只换颜色。

## 📄 License

[MIT](LICENSE) © 2026 Walksu
