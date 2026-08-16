# 背景样式（backgrounds）

九维度之一。全部内联实现、公众号兼容：不用外部背景图片；`linear-gradient` 可用但只放页底，不压在文字下。

## B1 纯色（默认）

- body = 色板的 page-bg；内容区 = content-bg。
- `<body style="margin:0;background:#EEF1F3;">`，内容 `<section style="...;background:#FBFCFC;">`。
- 适用：所有气质默认；最稳。

## B2 微渐变

- body 用同色系上下微渐变（明度差 ≤ 5%，克制）。
- `<body style="margin:0;background:linear-gradient(180deg,#EEF1F3,#E3E8EC);">`。
- 适用：冷静报告、科技极简的柔和变体；禁止高饱和渐变。

## B3 顶部色带

- 内容区最上方一条 accent-soft 色带（高 8px，可配圆角），作为文章「书脊」。
- `<div style="height:8px;background:#F3E7D5;border-radius:4px 4px 0 0;"></div>` 放在容器内标题区之前。
- 适用：温暖故事、书卷墨绿等暖气质。

## B4 深浅分层

- body 用加深的 page-bg（或深色板的深底），内容区卡片式浮起：圆角 8px + 上下 padding 加大。
- `<body style="margin:0;background:#17191C;">` + `<section style="...;border-radius:8px;background:#1F2226;">`。
- 适用：深色板、深夜终端、冷冽理性。

## B5 细边框留白

- 内容区 1px `solid` divider 细边框（不是虚线）+ 内边距加大 8px，报纸卡感。
- `<section style="...;border:1px solid #DDE3E8;border-radius:8px;">`。
- 适用：现代极简、冷静报告的克制变体。

## B6 三色分区

- 全文分「顶带 / 正文 / 尾带」三段统合配色（如黄白蓝：顶部米黄 = 栏目眉题、正文白/浅底、尾部浅蓝 = 签名收束）。它让版式看起来是「一套整体设计」，而不是换了个背景。
- 实现：顶带与尾带各自是一个浅色色块容器（`border-radius:8px` + padding 14–18px），正文区保持单一浅底；色带之间用 margin 分隔，**不连续相贴**（避免微信插白缝）。
- 规则：
  - 三色全部取低饱和；正文/次要文字与各自底色的对比度仍 ≥ 4.5:1。
  - 三色里**只允许一个 accent 做文字强调**，其余两色只做背景层，不出现第二个强调色。
  - 一条色带只承担一个功能：顶部 = 眉题/栏目，尾部 = 签名/收束；不做装饰性纯色块。
  - 深色板不用三色分区（对比度难达标）。

```html
<section style="margin:0 0 24px;background:#F6EBD3;padding:14px 18px;border-radius:8px;">
  <p style="margin:0;font-size:11px;letter-spacing:3px;color:#7A5E2E;font-weight:700;"><span leaf="">栏目眉题</span></p>
</section>
<!-- 正文区：单一浅底，正常排版 -->
<section style="margin:24px 0 0;background:#E3EBF2;padding:16px 18px;border-radius:8px;">
  <p style="margin:0;font-size:13px;color:#3E4C5A;line-height:1.8;"><span leaf="">签名/收束语</span></p>
</section>
```

## 规则

- 一篇只用一个背景样式；选 B2–B6 时正文对比度仍须 ≥ 4.5:1。
- 渐变、色带、边框都属于背景层，不叠加使用（B3 与 B5 互斥；B6 与 B3 同为「分区」，二选一）。
