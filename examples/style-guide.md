# 示例效果说明（style-guide）

`sample-article.md` → `sample-quiet.html` 演示了一套完整组合，供排其他文章时对齐「气质与手感」，但**不要复制配色**（每篇按用户选择重新取 token）。

> 注意：`sample-quiet.html` 是旧版整页格式示例。当前产物标准为**纯 `<section>` 片段 + 全部文字 `<span leaf="">` 包裹 + 禁 `<div>/class/id`**（见 references/output-spec.md 与 references/component-library.md）；最新合规范例见 `examples/Codex 完整指南：…_排版_humanistic.html` 及其 `_预览.html`。

## 本示例的组合

| 维度 | 选择 | 理由 |
|---|---|---|
| 气质 | 安静编辑 | 随笔题材，克制、留白、编辑感 |
| 色板 | 暖米 | 纸感底色，温暖不抢眼 |
| 字体 | 衬线标题 + 无衬线正文 | 标题庄重、正文易读，经典编辑组合 |
| 版式 | L1 单栏流（窄，560–600px） | 短小随笔，沉浸阅读 |
| 疏密 | 中 | 段距 16px、章节距 40px、行高 1.8 |
| 装饰 | L1 细线 | 眉题 + 1px 分隔线 + 引用左竖线，无大面积色块 |
| 功能 | 图注居中灰字 | 图片说明清晰，不喧宾夺主 |

## 排版决策映射

- 眉题「随笔 · 阅读」：12px + letter-spacing 2px + accent 色，制造编辑感。
- h1 衬线 25px/600，正文无衬线 16px：层级靠字体家族 + 字重，不靠放大字号。
- 引语用左竖线 3px（quote-bar 色），正文段两端对齐。
- 强调每段仅 1 处：第一段「失去了完整读完一段话的能力」、结尾「从今晚开始」，均 accent 色加粗。
- 列表 marker 用次要色，条目正文用正文色。
- 行内代码浅底圆角；代码块浅米底 + 等宽 + 每行一个 `<p>`（公众号兼容）。
- 图片 `display:block;max-width:100%;height:auto;margin:0 auto`，图注居中灰字。
- 结尾 1px 细线收尾，不虚构 CTA；文章末尾强制附作者签名卡（见 references/component-library.md 的 F11c，colophon 排版：上下细线 + 等宽 AUTHOR 标签 + 大字距作者名 + 1px accent 点睛线），作者信息未知时保留 `{{作者名}}` 占位并提醒用户替换。

## 如何改成其他组合

- 换色板：把全文 `#F7F2EA/#FFFDF8/#3D362C/...` 换成目标色板的 token 值（tokens/color-palettes.md）。
- 换字体：替换 h1/h2 的 `font-family` 与正文 `font-family`（tokens/font-pairings.md）。
- 换密度：按 tokens/density.md 调整 padding、段距、章节距、行高。
- 换版式：容器宽度 + 组件顺序按 tokens/layouts.md；加目录用 partials/toc.html。
- 加装饰：引用改浅底卡片、章节加色点编号（references/typography.md 引用卡片写法）。

## 验证方式

用浏览器打开 `sample-quiet.html`，分别检查 375px（手机）与桌面宽度：无横向滚动、无孤儿标题、图片不拉伸、强调不泛滥。然后全选复制，粘贴进公众号编辑器确认样式不丢。
