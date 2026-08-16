# 中英文排版细则

本文件定义逐元素的内联样式基准。所有数值都应按所选「疏密」档位（tokens/density.md）与「字体」组合（tokens/font-pairings.md）微调，这里给的是「中」密度、通用字体的基准。

## 字号阶梯

| 元素 | 字号 | 说明 |
|---|---|---|
| 文章标题 h1 | 24–26px | 全篇唯一 |
| 章节标题 h2 | 19–20px | 字重 600–700 |
| 子节标题 h3 | 17–18px | 字重 600 |
| 正文 p | 15–16px | 公众号正文惯例 |
| 次要/眉题 | 12–13px | 眉题加 letter-spacing 1–2px |
| 图注/说明 | 12–13px | 灰色 |
| 行内代码 | 13–14px | 等宽族 |
| 代码块 | 13–14px | 等宽族 |

## 行高与字距

- 正文：`line-height 1.7–2.0`（中文 1.8 为基准）；`letter-spacing 0–1px`。
- 标题：`line-height 1.3–1.5`；`letter-spacing 1–2px`（大标题 0.5–1px 即可）。
- 眉题/英文小标签：`letter-spacing 2px` 上限，再大就是灾难。
- 全角中文与数字/英文混排时，正文 `letter-spacing` 统一即可，不逐字调整。

## 标题层级

- 一篇文章只有一个 h1（即文章大标题）。
- 章节用 h2，子节用 h3，**不跳级**（h1 → h3 是错误）。
- 章节编号（若开）：按 `##` 出现顺序 01/02/03，不跳号；结尾总结类章节可用「结语」等文字替代编号，中间章节不得用。
- 标题不换行不截断，超过两行时重新断句。

## 段落

- 公众号惯例：**无首行缩进 + 段间距**。`<p style="margin:0 0 16px;text-align:justify;...">`。
- 书卷风可改用「首行缩进 2em + 无段距」（人文书卷气质时），但同一篇内只选一种。
- `text-align:justify` 让中文两端对齐；长英文单词所在行可能被拉松，此时该段改 `text-align:left`。
- 段落内强调 ≤ 1 处（加粗、高亮、着色三选一）。

## 强调

- **加粗**（语义强调）：正文默认色或 accent 色，`font-weight:600` 即可，不必 700。
- **高亮**：`background:accent-soft` 浅底 + 正文色文字，圆角 2–3px、padding 1px 4px。每段 ≤ 1 处。
- **下划线**：只用于链接，不用下划线强调正文。
- **颜色强调**：accent 色加粗，仅用于关键短语；与背景对比度 ≥ 4.5:1。

## 引用

- 短引用（≤ 2 行）：左竖线 + 次要色文字：`<blockquote style="margin:24px 0;padding:2px 0 2px 16px;border-left:3px solid {quote-bar};color:{secondary};line-height:1.8;">`
- 长引用（≥ 3 行）或关键点：L2 起用浅底卡片：`background:{accent-soft};border-radius:6px;padding:18px 20px;border-left:3px solid {accent};`
- 引用内不要嵌套第二层引用。

## 列表

- 无序列表：圆点或方形 marker，`color:{secondary}`（L0/L1）；L2+ 可用 accent 色点。
- 有序列表：数字保持原文顺序，`padding-left:1.4em`。
- 列表项间距 8–14px；长条目换行时第二行与首字对齐（悬挂缩进，简单做法：`padding-left:1.2em;text-indent:-1.2em` 或直接整块缩进）。
- 列表项内的强调同样每项 ≤ 1 处。

## 代码

- 行内代码：`<code style="font-family:{mono};background:{code-bg};border-radius:4px;padding:2px 6px;font-size:14px;color:{text};">`
- 代码块：整块 `<section style="background:{code-bg or 深色};border-radius:6px;padding:16px 18px;margin:24px 0;">`，**每行一个 `<p style="margin:0;font-family:{mono};font-size:14px;line-height:1.6;color:{code-text};white-space:normal;">`**，禁用 `white-space:pre`（会吃掉缩进/换行）。
- 代码块内保留半角标点与原始缩进（缩进用全角空格 `　` 或原样空格，勿用 CSS 缩进）。
- 中文注释照常显示，字号可稍大（14px）。

## 表格

- `<table style="width:100%;border-collapse:collapse;font-size:14px;line-height:1.7;">`
- 表头 `<th style="background:{accent-soft};padding:10px 12px;text-align:left;font-weight:600;border:1px solid {divider};">`
- 单元格 `<td style="padding:10px 12px;border:1px solid {divider};text-align:left;">`
- 超过 5 列建议转列表/卡片式呈现；表格内不放大段文字。

## 图片与图注

- 图片一律：`display:block;max-width:100%;height:auto;margin:0 auto;` 不强制 `width:100%`（小图会被拉伸变形；仅封面/流程类大图可 100%）。
- 图注：`<figcaption style="margin-top:10px;text-align:center;font-size:13px;color:{secondary};line-height:1.6;">`；风格可选：居中灰 / 左对齐灰 / 编号（图 1｜说明）。
- 图注只写原文提供的信息；空 alt 不编图注。

## 分隔线

- 1px 细线：`<div style="height:1px;background:{divider};margin:{density} 0;"></div>`。
- 或纯留白分隔（L0）；禁用 emoji、`***`、波浪线分隔。

## 链接

- `<a style="color:{accent};text-decoration:underline;text-underline-offset:3px;">`；无 hover 效果（公众号无 hover）。
- 外链保留原文 URL；页内锚点在公众号不可用，不生成 `href="#..."`。

## 中西文混排

- 中文与英文/数字之间留一个半角空格（视觉更透气）：「使用 Notion 管理」。
- 中文标点一律全角：`，。！？：；“”‘’（）——……`。
- 代码、URL、英文专名内部保持半角，不做全角替换。
