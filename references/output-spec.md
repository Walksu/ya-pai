# 输出要求（平台规范，公众号）

## 产物格式

- **纯 `<section>…</section>` 正文片段**：从全局容器开始，**不要包 `<!DOCTYPE>`/`<html>`/`<head>`/`<body>`**——公众号编辑器只接受正文片段，多余的文档外壳会被丢弃或干扰粘贴。
- 样式全部内联在元素的 `style` 属性；**所有文字节点用 `<span leaf="">文字</span>` 包裹**（否则粘贴后样式丢失）。
- 可用标签：`section / p / h3 / span / strong / em / img / table / a`；**禁 `<div>`**（微信会改写，用 `<section>`）。

## 命名与位置

- 命名：`{原文文件名}_排版_{气质英文标识或预设标识}.html`（标识取自 tokens/aesthetics.md 的条目 id 或 tokens/presets.md）。
- 存放：与原文同目录；原文是粘贴文本时存当前工作目录。
- 预览页：`scripts/wrap_preview.py <正文.html>` 产出 `{...}_预览.html`（右上角「复制到公众号」按钮）。

## 平台红线（与 scripts/validate_gzh_html.py 一致）

**禁止**：`<style>` / `<script>` / `<div>` / `<link>`、`class` / `id` 属性、`position:fixed/absolute/sticky`、`float`、`@media` / `@keyframes` / `@import`、`display:grid`、CSS 变量 `var(--x)`、外部字体/CSS。

**必须**：样式全部内联；文字节点全部 `<span leaf="">` 包裹；正文中文标点全角（代码/URL/英文内部保持半角）。

**可用**：`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`position:relative`。

## WeChat 兼容铁律（实际踩坑总结）

- `font-size` ≤ 24px；同一个 `<p>` 内不要混多个不同 `font-size`（微信会自动「纠正」导致样式被重写）。
- 不要把 `font-size` / `border-bottom` 打在 `<strong>` 上；高亮样式统一挂在外层 `<span>` 上。
- 装饰性空元素（细线、圆点、色带）内部必须放 `<span leaf=""><br></span>`，否则微信剥掉样式。
- 不用四周虚线框（dashed）包标题/强调；仅「待补素材占位」可用虚线框（通用库 2c）。
- 图片一律 `max-width:100%;height:auto;display:block;margin:0 auto`，**不用 `width:100%`**（小图会被拉伸变糊）。
- 不用 `position:absolute` 做划线/高亮。
- **整篇只一个根 `<section>`，正文区单一背景**：相邻兄弟 `<section>` 各带底色直接相贴会在微信里插白缝，底色块之间用 margin / 内边距隔开。
- **表格只写 `<table><tr><th/td>` 三层**：禁 `<thead>/<tbody>/<caption>`（微信会把它们渲染成独立空表）。
- **结构组件嵌套 ≤3 层**；标题类组件优先「单层 `<p>` + `<span>`」实现。
- 禁 `position:absolute`、`writing-mode`、`transform:rotate`（公众号会剥）。
- 相对宽度优先（`%` / `auto`）；只有小元素（圆点、色条、编号块）才用固定 px。
- **长文体积**：产物 > 200KB（或 > 1.2 万字）时，交付提示公众号编辑器可能卡顿，建议拆成系列篇或压缩重复样式（同一样式尽量复用同一条规则）。

## 生成时的智能处理（必须做）

1. 章节自动编号：按 `##` 出现顺序 01/02/03…；末章若为结语/总结类用 `∞` + `THE END`，中间章节不得用。
2. 英文标签：据中文章节标题生成（BASICS / WORKFLOW / TUTORIAL / SUMMARY…），章节标题组件有槽位时使用。
3. **正文关键词下划线（核心特色）**：每个正文段落主动找 1–2 个关键短语（4–15 字）用 `border-bottom:2px solid {ACCENT}` 标记；即使原文无加粗也要主动标；过渡段/整段无要点可不标；同一短语不重复标。
4. 引言关键词高亮：开头金句核心词用高亮组件标记。
5. 目录/导读：从 `##` 取前 3–6 个作目录条目，只取原文标题、不编造、不加锚点。
6. 开头引言卡署名：有作者写「—— 作者名」，没有则省略，不固定写死。
7. 尾部签名区（**强制，每篇末尾必有一处**）：用 F11c 作者签名卡（mono AUTHOR 标签 + 简介行）；**作者名 + 一句话简介在提问阶段（design-system §10 第 4 步）向用户获取**，用户提供则直接填入；用户明确不提供才用 `{{作者名}}` / `{{简介}}` 占位，交付时必须提示用户替换；原文末尾已有署名段 → 并入该卡，不重复生成。
8. 中文全角标点：正文一律全角（，。！？：；""''（）——……），生成时直接写弯引号；代码、URL、英文专名内部保持原样。

## 校验（强制，交付前必跑）

```bash
<SKILL_ROOT>/scripts/validate_gzh_html.py <生成的正文.html>
```

- ERROR 清零才算完成；报 ERROR 就回到组装步骤修。
- **半角标点 WARNING 同样修复到 0 再交付**（最高频返工点）。
- **审美类 WARNING**（连续 4+ 段纯文字 / AI 默认色 / font-size 超限）能修则修；确因原文结构无法修的，在交付说明中注明人工确认（水印大数字的 font-size 例外属正常）。
- 通过后再跑 `<SKILL_ROOT>/scripts/wrap_preview.py <正文.html>` 生成预览页。
- **发布前必跑** `<SKILL_ROOT>/scripts/publish_audit.py <正文.html>`：占位符残留 / 本地图片 / 产物体积 / 预览页；❌ 项清零才算可发布（`{{作者名}}`、`{{一句话简介}}` 未替换时会直接挡下）。

## 自检清单

1. 文件是纯 `<section>` 片段，无 doctype/html/head/body。
2. 每个文字节点都被 `<span leaf="">` 包裹（校验脚本 WARNING = 0）。
3. 无 `<style>/<script>/<div>/<link>/class/id`、无 fixed/absolute/sticky/float/@media/grid/CSS 变量。
4. 无占位符残留（`{{` / `}}`，除签名占位 {{作者名}} 需在交付时提示）。
5. 中文标点全角；代码、URL、英文内部半角。
6. 章节编号按 `##` 顺序不跳号；结语变体只用于末章。
7. 每段 ≤2 处下划线标记，无整段划线；过渡段不标不视为漏标。
8. 原文每个段落、图片、列表、表格都在产物里，无增删。
9. 图片全部 `max-width:100%;height:auto`；图注只写原文提供的信息。
10. 目录条目只取 `##` 标题原文，不编造。
11. `font-size` ≤ 24px；正文行高 ≥ 1.6；段间距在所选疏密档位内。
12. 对比度：正文 ≥ 4.5:1，标题 ≥ 3:1，小字号次要文字 ≥ 3:1；强调色锚点 ≥3.5:1 且 ≤3 处可确认。
13. 文件名符合命名规则；与原文同目录。
14. 无连续 4+ 段纯文字、无连续 2 个重组件紧挨（见 references/editorial-principles.md）。
15. 表格无 `<thead>/<tbody>/<caption>`；根容器唯一；底色块之间留 margin。
16. 结构组件嵌套 ≤3 层；组件总数落在所选密度档预算内（standard 3–6）。

## 交付话术

- 产物绝对路径（干净正文 + 预览页）
- 组合说明：九维度最终选择（均经用户确认）+ 一句话理由
- 粘贴指引：**打开 `{...}_预览.html` → 点右上角「复制到公众号」→ 公众号编辑器 Ctrl/⌘+V**
- 提示：本地图片需先上传公众号素材库并替换 `src`；标题在公众号后台设置，正文不重复放。
- 长文（产物 > 200KB）附一句「建议拆篇」提示。
