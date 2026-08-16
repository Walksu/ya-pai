# 主题组件库（ya-pai 维度驱动设计系统）

> **使用说明**：本文件是 ya-pai 的「设计语言」——组件按**族（Family）**组织，每个族有多个**变体（Variant）**，由用户选定的 8 维度（气质/色板/字体/版式/疏密/装饰/背景/功能）驱动选型。装配时**一律从这里取组件**，把 `{{占位}}` 替换为所选 token 的具体值，不凭记忆手写、不复制其它主题的成品。**用几个、放哪里、值不值得用**先读 references/editorial-principles.md（组件预算 + 节奏 + 替换不追加）。
>
> **变量来源**：色值 → tokens/color-palettes.md；字体栈 → tokens/font-pairings.md；宽度/间距 → tokens/layouts.md + tokens/density.md；背景 → tokens/backgrounds.md。
>
> **平台红线（与 scripts/validate_gzh_html.py 一致）**：禁 `<style>/<script>/<div>`、`class/id`、`position:fixed/absolute/sticky`、`float`、`@media/@keyframes`、`display:grid`、CSS 变量、外部字体；样式全内联；**所有文字节点用 `<span leaf="">` 包裹**；装饰性空元素内放 `<span leaf=""><br></span>`。

## 一、审美原理（排版纪律，全文通用）

这些是设计「为什么好看」的底层规则，比具体组件更重要：

1. **三层视觉层级**：锚点层（全篇 ≤3–5 处：accent 加粗、深底白字引用）→ 标记层（每段 1–3 处下划线关键词，高频）→ 容器层（卡片/引用/提示，按需）。三层频率递减，视线有秩序。
2. **色彩纪律**：一篇只用一个 accent；accent 面积 <10% 版面；accent-soft 只做容器底色；黄色只做高亮/警告；红色只做否定对比；正文色不花。
3. **字体纪律**：≤2 个字体族 + 等宽点缀（编号/眉题/代码）；字重阶梯 400→600→700→900；`font-size` ≤24px；同一个 `<p>` 不多字号；`font-size`/`border-bottom` 不打在 `<strong>` 上。
4. **留白纪律**：间距全部由疏密档位统一取值；同一元素全篇同距；标题「上大下小」挂住正文；不同疏密不混用。
5. **组件一致性**：一篇只选一族的一个变体（如引用选左竖线就全篇左竖线），不跨变体混搭。
6. **封面双层标题**：正文标题在公众号平台设置；封面引导语视角**错开**——封面卖「里面讲什么」，不原样复述标题关键词。
7. **目录精选**：导读/目录只取 3–6 个 `##` 章节标题原文，不铺全量、不编造、不加锚点。
8. **骨架顺序**：封面 → 引言 → 目录 → 编号章节 → 结尾；一篇文章只有一条骨架线。
9. **每段标记**：正文每段主动找 1–2 个关键短语做下划线标记（即使原文没有加粗也要标）；过渡段/整段无要点可不标；同一短语不重复标。
10. **不做的事**：不用虚线框包标题/强调（占位板块除外）、不用 `width:100%` 拉伸小图、不整段划线、不虚构图注与 CTA。

## 二、设计变量速查表

```
page-bg / content-bg   页面底 / 内容底
text / text-secondary  正文 / 次要文字
heading                标题色
accent / accent-soft   强调色 / 强调浅底
divider                分隔线 / 边框
quote-bar              引用竖线
code-bg                代码底
body-font / heading-font / mono-font
content-width / container-padding / para-gap / section-gap / body-lh
background-style        B1–B5（tokens/backgrounds.md）
decoration-level        L0–L3（本文件「维度→变体选择表」）
```

## 三、组件族与变体

### F1 封面族（文章开头，2 选 1）

**F1a 书卷封面**（人文书卷 / 安静编辑，L1–L2）：上下细线 + 等宽眉题 + 引言金句 + 可选署名。金句按「审美原理 6」视角错开，从文章核心论点提炼一句，不重复标题关键词。

```html
<section style="margin:0 0 32px;padding:30px 24px 24px;border-top:1px solid {{DIVIDER}};border-bottom:1px solid {{DIVIDER}};text-align:center;">
  <p style="margin:0 0 18px;font-size:11px;letter-spacing:3px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
    <span leaf="">{{眉题，如：TUTORIAL · 系列 01}}</span>
  </p>
  <p style="margin:0 0 12px;font-size:19px;font-weight:700;color:{{HEADING}};line-height:1.7;letter-spacing:1px;">
    <span leaf="">{{引言金句}}</span>
  </p>
  <p style="margin:0;font-size:12px;color:{{TEXT_SECONDARY}};letter-spacing:1px;">
    <span leaf="">—— {{作者名，未知则整行删}}</span>
  </p>
</section>
```

**F1b 快讯卡**（冷冽理性 / 现代极简，L2–L3；教程/工具类信息密度高时）：白卡圆角 + 顶部标签条 + 双行大标题 + 底部 accent 色带。

```html
<section style="margin:0 0 32px;background:#fff;border:1px solid {{DIVIDER}};border-radius:16px;overflow:hidden;">
  <section style="padding:26px 24px 22px;">
    <p style="margin:0 0 14px;font-size:11px;font-weight:700;letter-spacing:2px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
      <span leaf="">{{顶部标签}}</span>
    </p>
    <p style="margin:0;font-size:22px;font-weight:900;color:{{HEADING}};line-height:1.25;letter-spacing:0;">
      <span leaf="">{{主标题行 1}}</span><span style="color:{{ACCENT}};"><span leaf="">{{高亮词}}</span></span>
    </p>
    <p style="margin:0 0 14px;font-size:22px;font-weight:900;color:{{ACCENT}};line-height:1.25;letter-spacing:0;">
      <span leaf="">{{主标题行 2}}</span>
    </p>
    <p style="margin:0;font-size:13px;color:{{TEXT_SECONDARY}};line-height:1.7;">
      <span leaf="">{{副标题关键词，用 · 分隔}}</span>
    </p>
  </section>
  <section style="background:linear-gradient(135deg,{{ACCENT}},{{ACCENT}}cc);padding:11px 24px;">
    <p style="margin:0;font-size:12px;color:#fff;font-weight:600;letter-spacing:0.5px;">
      <span leaf="">{{底部品牌/系列名}}</span>
    </p>
  </section>
</section>
```

**F1c 极简眉题**（现代极简 / 冷冽理性，L0–L1）：眉题 + 1px 细线，无色块。

```html
<p style="margin:0 0 10px;font-size:11px;letter-spacing:3px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
  <span leaf="">{{眉题}}</span>
</p>
<section style="height:1px;background:{{DIVIDER}};margin:0 0 28px;"><span leaf=""><br></span></section>
```

**F1d 杂志封面**（温暖纸感 / L4 卡片式，L3）：大图卡 + 色块标题带。

```html
<section style="margin:0 0 28px;border-radius:16px;overflow:hidden;border:1px solid {{DIVIDER}};">
  <section style="text-align:center;background:{{CONTENT_BG}};padding:6px;">
    <span leaf=""><img src="{{封面图URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:12px;"></span>
  </section>
  <section style="background:{{ACCENT_SOFT}};padding:20px 22px;">
    <p style="margin:0 0 8px;font-size:11px;letter-spacing:2px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
      <span leaf="">{{眉题}}</span>
    </p>
    <p style="margin:0;font-size:18px;font-weight:800;color:{{HEADING}};line-height:1.6;">
      <span leaf="">{{引言金句}}</span>
    </p>
  </section>
</section>
```

**F1e 编辑部眉批封面**（人文书卷 / 温暖纸感，L2–L3）：色点 + `EDITORIAL NOTE` 眉题 + 短横线 + 标题 + 摘要 + 底部 accent 窄条，像杂志内刊的卷首语。眉题/系列名可用 `VOL. 01` / `FIELD NOTE` 等杂志感标签。

```html
<section style="margin:0 0 32px;background:{{CONTENT_BG}};border:1px solid {{DIVIDER}};border-radius:6px;overflow:hidden;">
  <section style="padding:26px 22px 20px;">
    <section style="display:flex;align-items:center;margin-bottom:16px;">
      <span style="width:8px;height:8px;background:{{ACCENT}};border-radius:50%;display:inline-block;"><span leaf=""><br></span></span>
      <p style="margin:0 9px;font-size:9px;font-weight:700;letter-spacing:3px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">EDITORIAL NOTE</span></p>
      <section style="flex:1;height:1px;background:{{DIVIDER}};"><span leaf=""><br></span></section>
    </section>
    <p style="margin:0 0 12px;font-size:22px;font-weight:800;color:{{HEADING}};line-height:1.4;"><span leaf="">{{标题或引言金句}}</span></p>
    <p style="margin:0;font-size:13px;color:{{TEXT_SECONDARY}};line-height:1.85;"><span leaf="">{{副标/摘要}}</span></p>
  </section>
  <section style="background:{{ACCENT}};padding:10px 22px;">
    <p style="margin:0;font-size:11px;color:#fff;font-weight:600;letter-spacing:1px;"><span leaf="">{{系列名/品牌句}}</span></p>
  </section>
</section>
```

**F1f 深色开场**（冷冽理性 / 现代极简，L2–L3；深色板）：深底卡起手有重量，正文回浅底，整篇不压。深色板上 `{{CONTENT_BG}}` 即深底、`{{HEADING}}` 即浅色标题，直接套 token 即可。

```html
<section style="margin:0 0 34px;padding:30px 22px 26px;background:{{CONTENT_BG}};border-radius:10px;">
  <p style="margin:0 0 14px;font-size:10px;font-weight:700;letter-spacing:3px;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{眉题，如 DEEP DIVE}}</span></p>
  <p style="margin:0 0 14px;font-size:23px;font-weight:750;line-height:1.45;color:{{HEADING}};"><span leaf="">{{标题或引言金句}}</span></p>
  <p style="margin:0;font-size:14px;line-height:1.9;color:{{TEXT_SECONDARY}};"><span leaf="">{{摘要}}</span></p>
</section>
```

### F2 导读/目录族

**F2a 静态目录卡**（L6 侧栏式的公众号静态版；3–6 条）：accent-soft 底卡 + mono 编号。

```html
<section style="margin:0 0 28px;padding:18px 20px;background:{{ACCENT_SOFT}};border-radius:12px;">
  <p style="margin:0 0 10px;font-size:11px;letter-spacing:2px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
    <span leaf="">目录</span>
  </p>
  <section style="padding:8px 0;border-bottom:1px solid {{DIVIDER}};">
    <p style="margin:0;font-size:14px;color:{{TEXT}};line-height:1.6;">
      <span style="color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">01</span></span><span leaf="">　{{章节标题原文}}</span>
    </p>
  </section>
  <!-- 每章一段，末条去掉 border-bottom -->
</section>
```

**F2b 三列看点**（导读，章节 ≥3；现代极简/冷冽理性）：三栏线框卡，精选 3 个看点。

```html
<section style="margin:0 0 28px;">
  <section style="display:flex;">
    <section style="flex:1;border-top:2px solid {{ACCENT}};padding:14px 10px;margin-right:8px;">
      <p style="margin:0 0 6px;font-size:10px;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">01</span></p>
      <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};line-height:1.5;"><span leaf="">{{看点一}}</span></p>
    </section>
    <section style="flex:1;border-top:2px solid {{DIVIDER}};padding:14px 10px;margin-right:8px;">
      <p style="margin:0 0 6px;font-size:10px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">02</span></p>
      <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};line-height:1.5;"><span leaf="">{{看点二}}</span></p>
    </section>
    <section style="flex:1;border-top:2px solid {{DIVIDER}};padding:14px 10px;">
      <p style="margin:0 0 6px;font-size:10px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">03</span></p>
      <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};line-height:1.5;"><span leaf="">{{看点三}}</span></p>
    </section>
  </section>
</section>
```

**F2c 横向滚动目录**（教程/盘点，信息密度高；L2–L3）：首卡 accent 高亮，末卡「写在最后」。

```html
<section style="margin:0 0 28px;">
  <p style="margin:0 0 10px;font-size:10px;color:{{TEXT_SECONDARY}};letter-spacing:2px;font-weight:600;"><span leaf="">📦 {{N}} Parts</span></p>
  <section style="overflow-x:scroll;-webkit-overflow-scrolling:touch;white-space:nowrap;padding-bottom:8px;">
    <section style="display:inline-block;white-space:normal;vertical-align:top;width:112px;background:{{ACCENT}};border-radius:12px;padding:12px;margin-right:8px;">
      <p style="font-size:9px;font-weight:700;color:rgba(255,255,255,0.75);margin:0 0 5px;"><span leaf="">PART 01</span></p>
      <p style="font-size:13px;font-weight:800;color:#fff;margin:0;"><span leaf="">{{章节名}}</span></p>
    </section>
    <section style="display:inline-block;white-space:normal;vertical-align:top;width:112px;background:{{CONTENT_BG}};border:1px solid {{DIVIDER}};border-radius:12px;padding:12px;margin-right:8px;">
      <p style="font-size:9px;font-weight:700;color:{{TEXT_SECONDARY}};margin:0 0 5px;"><span leaf="">PART 02</span></p>
      <p style="font-size:13px;font-weight:800;color:{{HEADING}};margin:0;"><span leaf="">{{章节名}}</span></p>
    </section>
    <!-- 按需重复白卡；末卡为「写在最后」 -->
  </section>
</section>
```

**F2d 细线目录**（低噪音气质，L0–L1；L6 侧栏式的公众号静态版）：编号 + 标题竖排成一份目录，细线分隔，无色块——适合安静编辑、人文书卷、墨线气质。

```html
<section style="margin:0 0 32px;">
  <p style="margin:0 0 8px;font-size:11px;letter-spacing:2px;color:{{TEXT_SECONDARY}};"><span leaf="">本文看点</span></p>
  <section style="border-top:1px solid {{DIVIDER}};">
    <section style="padding:9px 0;border-bottom:1px solid {{DIVIDER}};">
      <span style="font-size:11px;font-weight:800;color:{{ACCENT}};letter-spacing:1px;margin-right:10px;font-family:{{MONO_FONT}};"><span leaf="">01</span></span>
      <span style="font-size:13.5px;font-weight:600;color:{{HEADING}};"><span leaf="">{{章节标题原文}}</span></span>
    </section>
    <!-- 每章一段，末条去掉 border-bottom -->
  </section>
</section>
```

### F3 章节标题族（`##`，自动编号 01/02/03…，末章可用 ∞）

**F3a 编号 + 细线**（人文书卷 / 安静编辑，L1；默认）：mono 编号 + 中文标题 + 底部 1px 细线。

```html
<section style="margin:{{SECTION_GAP}} 0 22px;padding-bottom:12px;border-bottom:1px solid {{DIVIDER}};">
  <p style="margin:0 0 6px;font-size:12px;color:{{ACCENT}};font-family:{{MONO_FONT}};letter-spacing:2px;">
    <span leaf="">{{01}}</span><span leaf="">　{{ENGLISH TAG}}</span>
  </p>
  <h3 style="margin:0;font-size:19px;font-weight:700;color:{{HEADING}};line-height:1.4;letter-spacing:1px;">
    <span leaf="">{{中文章节标题}}</span>
  </h3>
</section>
```

**F3b 水印大编号**（现代极简，L0–L1）：48px 浅色大数字叠底 + 标题。

```html
<section style="margin:{{SECTION_GAP}} 0 28px;">
  <p style="margin:0;font-size:46px;font-weight:900;color:{{DIVIDER}};line-height:1;letter-spacing:-2px;"><span leaf="">{{01}}</span></p>
  <h3 style="margin:2px 0 0;font-size:20px;font-weight:800;color:{{HEADING}};line-height:1.4;"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

**F3b·叠底版（讲义，L2–L3）**：浅色大数字 + 标题负 margin 叠在数字下缘，像讲义页码叠在标题后面（公众号兼容：不用 absolute/mask，靠负 margin 实现叠压）。

```html
<section style="margin:{{SECTION_GAP}} 0 26px;">
  <p style="margin:0;font-size:60px;font-weight:900;color:{{SURFACE_B}};line-height:1;letter-spacing:-2px;font-family:{{HEADING_FONT}};"><span leaf="">{{01}}</span></p>
  <h3 style="margin:-0.46em 0 0;font-size:23px;font-weight:900;color:{{HEADING}};line-height:1.4;letter-spacing:1px;"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

**F3c PART 标签 + 竖线**（冷冽理性 / 教程盘点，L1–L2）：大数字 + 竖线 + 标题 + 英文小标。

```html
<section style="margin:{{SECTION_GAP}} 0 28px;display:flex;align-items:center;gap:14px;">
  <section style="text-align:center;flex-shrink:0;">
    <p style="margin:0;font-size:24px;font-weight:900;color:{{ACCENT}};line-height:1;"><span leaf="">{{01}}</span></p>
    <p style="margin:0;font-size:8px;font-weight:700;color:{{TEXT_SECONDARY}};letter-spacing:2px;"><span leaf="">PART</span></p>
  </section>
  <span style="width:1px;height:34px;background:{{DIVIDER}};flex-shrink:0;"><span leaf=""><br></span></span>
  <section>
    <p style="margin:0 0 2px;font-size:17px;font-weight:900;color:{{HEADING}};"><span leaf="">{{中文章节标题}}</span></p>
    <p style="margin:0;font-size:11px;font-weight:600;color:{{TEXT_SECONDARY}};letter-spacing:1.5px;"><span leaf="">{{ENGLISH · 副标}}</span></p>
  </section>
</section>
```

**F3d 色块章头**（温暖纸感 / L4 卡片式，L2–L3）：accent-soft 底 + 编号药丸。

```html
<section style="margin:{{SECTION_GAP}} 0 24px;background:{{ACCENT_SOFT}};border-radius:12px;padding:16px 18px;display:flex;align-items:center;gap:12px;">
  <span style="display:inline-block;background:{{ACCENT}};color:#fff;font-size:12px;font-weight:700;padding:3px 10px;border-radius:999px;font-family:{{MONO_FONT}};"><span leaf="">{{01}}</span></span>
  <h3 style="margin:0;font-size:18px;font-weight:800;color:{{HEADING}};line-height:1.4;"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

**F3e 墨线章头**（人文书卷 / 安静编辑 衬线气质，L1）：实心黑方块编号 + 标题 + 细线收尾，像纸质书内页。编号底色用 `{{HEADING}}`（墨线气质下即墨色）。

```html
<section style="margin:{{SECTION_GAP}} 0 22px;">
  <section style="margin-bottom:12px;">
    <span style="display:inline-block;padding:5px 9px;background:{{HEADING}};color:#fff;font-size:12px;font-weight:700;letter-spacing:1px;font-family:{{MONO_FONT}};"><span leaf="">{{01}}</span></span>
  </section>
  <h3 style="margin:0 0 10px;font-size:19px;font-weight:700;line-height:1.5;color:{{HEADING}};"><span leaf="">{{中文章节标题}}</span></h3>
  <section style="height:1px;background:{{DIVIDER}};"><span leaf=""><br></span></section>
</section>
```

**F3f 反白色带章头**（观点文 / 判断明确，L2–L3）：章节标题整条反白压在主色上，通栏出血，是「色块」主题的核心识别点；全篇只允许这一个「大」元素时用它。

```html
<section style="margin:{{SECTION_GAP}} 0 22px;background:{{ACCENT}};padding:11px 16px;">
  <section style="display:flex;align-items:center;">
    <span style="display:inline-block;background:#fff;color:{{ACCENT}};font-size:12px;font-weight:800;padding:3px 9px;margin-right:11px;font-family:{{MONO_FONT}};"><span leaf="">{{01}}</span></span>
    <span style="font-size:17px;font-weight:800;color:#fff;line-height:1.4;"><span leaf="">{{中文章节标题}}</span></span>
  </section>
</section>
```

**F3g 渐变圆角徽标**（活泼 / 现代 / 观点，L2–L3）：渐变底圆角数字徽标 + 加粗标题，视觉重量集中在徽标上。渐变只用 accent 单色系（`{{ACCENT}} → {{ACCENT}}99`），不引入第二强调色。

```html
<section style="margin:{{SECTION_GAP}} 0 24px;display:flex;align-items:center;gap:12px;">
  <span style="display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;background:linear-gradient(135deg,{{ACCENT}},{{ACCENT}}99);color:#fff;font-size:16px;font-weight:900;border-radius:14px;font-family:{{MONO_FONT}};flex-shrink:0;"><span leaf="">{{01}}</span></span>
  <h3 style="margin:0;font-size:19px;font-weight:800;color:{{HEADING}};line-height:1.4;"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

**F3h 衬线居中大字**（书卷 / 杂志 / 仪式感，L2–L3）：英文眉题 + 居中衬线大字 + 宽字距，靠字体与留白制造庄重感，不靠色块。

```html
<section style="margin:{{SECTION_GAP}} 0 26px;text-align:center;">
  <p style="margin:0 0 6px;font-size:11px;letter-spacing:3px;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{ENGLISH TAG}}</span></p>
  <h3 style="margin:0;font-size:22px;font-weight:600;color:{{HEADING}};line-height:1.5;letter-spacing:2px;font-family:{{HEADING_FONT}};"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

**F3i 终端标签**（冷冽理性 / 技术向，L1–L2）：等宽 `▸ 01 / TAG` 标签 + 加粗标题，代码感强。

```html
<section style="margin:{{SECTION_GAP}} 0 22px;">
  <p style="margin:0 0 10px;font-size:12px;font-weight:700;color:{{ACCENT}};font-family:{{MONO_FONT}};letter-spacing:1px;"><span leaf="">▸ {{01}} / {{ENGLISH TAG}}</span></p>
<h3 style="margin:0;font-size:18px;font-weight:800;color:{{HEADING}};line-height:1.4;"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

**F3j 报章方块编号**（报章式 L8，L1–L2）：实心方块编号 + 大号标题 + 底部栏线，像报纸版面分区的小版头；编号底色用 `{{ACCENT}}`，报章气质时 `font-family:{{HEADING_FONT}}`。

```html
<section style="margin:{{SECTION_GAP}} 0 24px;border-bottom:2px solid {{DIVIDER}};padding-bottom:14px;">
  <section style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
    <span style="display:inline-block;background:{{ACCENT}};color:#fff;font-size:13px;font-weight:900;padding:4px 10px;font-family:{{MONO_FONT}};letter-spacing:1px;"><span leaf="">{{01}}</span></span>
    <p style="margin:0;font-size:10px;letter-spacing:2px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{ENGLISH TAG}}</span></p>
  </section>
  <h3 style="margin:0;font-size:21px;font-weight:900;color:{{HEADING}};line-height:1.45;font-family:{{HEADING_FONT}};"><span leaf="">{{中文章节标题}}</span></h3>
</section>
```

### F4 子标题族（`###` / `####`）

**F4a 左竖条**（默认，L1）：`border-left:3px solid {{ACCENT}};padding-left:12px;font-size:16px;font-weight:700;color:{{HEADING}};margin:26px 0 12px;`（`<p><span leaf="">{{标题}}</span></p>`）

**F4b 高亮下划线**（L2，教程/盘点）：`background:linear-gradient(180deg,transparent 65%,{{ACCENT_SOFT}} 65%)` 包标题。

**F4c 药丸标签**（L2–L3）：`<span style="display:inline-block;background:{{ACCENT}};color:#fff;font-size:12px;font-weight:700;padding:4px 12px;border-radius:999px;"><span leaf="">{{标题}}</span></span>` 独立成 `p`。

**F4d 纯加粗**（L0）：`font-size:16px;font-weight:700;color:{{HEADING}};` 无装饰。

### F5 正文与标记族

段落（默认）：`<p style="margin:0 0 {{PARA_GAP}};font-size:15px;line-height:{{BODY_LH}};text-align:justify;color:{{TEXT}};letter-spacing:0.5px;">…</p>`

标记变体（每段 ≤2 处，混用 ≤2 种；过渡段可不标）：

- **M1 下划线关键词**（默认标记）：`<span style="border-bottom:2px solid {{ACCENT}};font-weight:600;color:{{HEADING}};"><span leaf="">{{短语}}</span></span>`
- **M2 accent 加粗**（锚点，全篇 ≤3 处）：`<strong style="color:{{ACCENT}};font-weight:700;"><span leaf="">{{文字}}</span></strong>`
- **M3 浅底高亮**（`==文字==`）：`<span style="background:{{ACCENT_SOFT}};border-radius:3px;padding:1px 5px;color:{{HEADING}};"><span leaf="">{{文字}}</span></span>`
- **M4 行内代码**：`<span style="background:{{CODE_BG}};color:{{ACCENT}};padding:1px 6px;border-radius:4px;font-family:{{MONO_FONT}};font-size:13px;"><span leaf="">{{code}}</span></span>`
- **M5 否定/对比**（仅否定语义，红色系）：`<span style="border-bottom:2px solid #FECACA;color:{{HEADING}};"><span leaf="">{{文字}}</span></span>`
- **M6 整句高亮条**（讲义 / 结论，L2）：独立一行的浅底高亮条，用于「一句话结论」，比 M3 更醒目；全篇 ≤2 处。

```html
<p style="margin:0 0 24px;"><span style="display:inline-block;background:{{HIGHLIGHT}};padding:8px 18px;font-size:16px;line-height:1.8;color:{{HEADING}};font-weight:700;"><span leaf="">{{整句结论}}</span></span></p>
```

### F6 引用族（`> 引用`）

**F6a 左竖线**（L0/L1）：`<section style="border-left:3px solid {{QUOTE_BAR}};padding:12px 0 12px 18px;margin:0 0 20px;"><p style="margin:0;font-size:15px;font-weight:700;color:{{HEADING}};line-height:1.8;"><span leaf="">{{内容}}</span></p></section>`

**F6b 浅底引用卡**（L2/L3）：`<section style="background:{{ACCENT_SOFT}};border-left:3px solid {{ACCENT}};border-radius:0 10px 10px 0;padding:16px 18px;margin:0 0 20px;">…</section>`

**F6c 居中金句分隔**（杂志/章节过渡）：`<p style="font-size:15px;margin:0 0 24px;text-align:center;color:{{ACCENT}};font-weight:700;border-top:1px solid {{DIVIDER}};border-bottom:1px solid {{DIVIDER}};padding:12px 0;"><span leaf="">{{金句}}</span></p>`

**F6d 拉引文**（书卷 / 杂志，L2–L3）：居中衬线大字 + 上下细线，全篇 ≤2 处；只摘原文原句。

```html
<section style="margin:0 0 24px;padding:22px 0;text-align:center;border-top:1px solid {{DIVIDER}};border-bottom:1px solid {{DIVIDER}};">
  <p style="margin:0;font-size:17px;font-weight:600;color:{{HEADING}};line-height:1.9;font-family:{{HEADING_FONT}};"><span leaf="">{{原文金句}}</span></p>
</section>
```

**F6e 大引号引用**（讲义 / 书卷，L2–L3）：浅色大引号 + 楷体正文，中文「斜体感」用楷体族实现，不用 `font-style:italic`。配合面色板 `{{QUOTE_BAR}}` 做引号色。

```html
<section style="margin:0 0 26px;display:flex;align-items:flex-start;">
  <span style="font-family:Georgia,serif;font-size:52px;line-height:1;color:{{QUOTE_BAR}};flex-shrink:0;margin:-8px 14px 0 0;opacity:0.55;"><span leaf="">“</span></span>
  <p style="margin:0;flex:1;font-size:17px;line-height:1.9;color:{{HEADING}};font-family:'KaiTi','STKaiti','BiauKai','Noto Serif SC',serif;"><span leaf="">{{金句原文}}</span></p>
</section>
```

### F7 提示族（注意/警告/旁注）

- **F7a 左竖条提示**（L1）：`<section style="border-left:3px solid {{ACCENT}};padding:12px 0 12px 16px;margin:0 0 20px;"><p style="margin:0;font-size:14px;color:{{TEXT}};line-height:1.8;"><span leaf="">{{提示}}</span></p></section>`
- **F7b 踩坑**（负面/风险）：同 F7a，竖条 `rgb(255,76,0)`，首行小标「！踩坑」。
- **F7c 黄色警告框**（L2/L3）：`<section style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:10px;padding:12px 16px;margin:0 0 20px;"><p style="margin:0;font-size:13px;color:#92400E;font-weight:700;"><span leaf="">{{警告}}</span></p></section>`
- **F7d 信息框**（L2/L3）：`<section style="background:{{ACCENT_SOFT}};border:1px solid {{DIVIDER}};border-radius:10px;padding:12px 16px;margin:0 0 20px;">…</section>`
- **F7e SUMMARY 结论卡**（讲义 / 报告，L2/L3）：label + 衬线标题 + 正文 + ✦ 强调行，低对比无阴影；用于章节小结或全文结论。

```html
<section style="margin:0 0 26px;padding:22px 26px 22px 30px;background:{{SUMMARY_BG}};border-left:3px solid {{DIVIDER}};">
  <p style="margin:0 0 8px;font-size:12px;letter-spacing:3px;color:{{TEXT_SECONDARY}};font-weight:600;font-family:{{MONO_FONT}};"><span leaf="">SUMMARY · 小结</span></p>
  <p style="margin:0 0 12px;font-size:19px;font-weight:900;color:{{HEADING}};line-height:1.5;font-family:{{HEADING_FONT}};"><span leaf="">{{小结标题}}</span></p>
  <p style="margin:0 0 12px;font-size:15px;line-height:1.85;color:{{TEXT}};"><span leaf="">{{小结正文，多行用 br 换行}}</span></p>
  <p style="margin:0;font-size:14px;line-height:1.7;color:{{ACCENT}};font-weight:700;"><span leaf="">✦ {{一句话强调}}</span></p>
</section>
```

### F8 列表族

- **F8a 圆点列表**（L0–L2）：flex 行，accent 圆点（内部 `<span leaf=""><br></span>`）+ 文字。
- **F8b 编号圆标**（有序）：`<span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:{{ACCENT}};color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;"><span leaf="">1</span></span>` + 文字 `p`（flex）。
- **F8c 药丸胶囊**（L2–L3，短条目）：`<span style="display:inline-block;font-size:13px;font-weight:700;color:{{ACCENT}};background:{{ACCENT_SOFT}};padding:3px 12px;border-radius:999px;">…</span>` 每条独立 `p`。
- **F8d 时间线**（L3 时间线式，L2–L3）：竖向圆点 + 竖线 + 节点标题/说明；末节点不要竖线。
- **F8e 方块列表**（报章式 L8 / 讲义，L1）：方形实心标记 + 等宽小序号，像报纸条目；与圆点列表（F8a）同一篇不混用。

```html
<section style="margin:0 0 22px;">
  <section style="display:flex;align-items:flex-start;margin:0 0 10px;">
    <span style="flex-shrink:0;width:10px;height:10px;background:{{ACCENT}};display:inline-block;margin:7px 12px 0 2px;"><span leaf=""><br></span></span>
    <p style="margin:0;flex:1;font-size:14.5px;line-height:1.8;color:{{TEXT}};"><span leaf="">{{条目文字}}</span></p>
  </section>
  <!-- 每项一段 -->
</section>
```

```html
<section style="margin:0 0 24px;">
  <section style="display:flex;align-items:flex-start;margin:0 0 22px;">
    <section style="flex-shrink:0;width:26px;display:flex;flex-direction:column;align-items:center;margin-right:14px;">
      <span style="width:12px;height:12px;border-radius:50%;background:{{ACCENT}};display:inline-block;margin-top:5px;"><span leaf=""><br></span></span>
      <span style="width:1px;flex:1;background:{{DIVIDER}};display:inline-block;margin-top:4px;"><span leaf=""><br></span></span>
    </section>
    <section style="flex:1;min-width:0;">
      <p style="margin:0 0 4px;font-size:11px;letter-spacing:2px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{01}}</span></p>
      <p style="margin:0;font-size:15px;font-weight:800;color:{{HEADING}};line-height:1.6;"><span leaf="">{{节点标题}}</span></p>
      <p style="margin:4px 0 0;font-size:13.5px;line-height:1.75;color:{{TEXT}};"><span leaf="">{{节点说明}}</span></p>
    </section>
  </section>
  <!-- 末节点去掉竖线 span -->
</section>
```

### F9 卡片族（条目/数据/流程）

- **F9a 工具/条目卡**（细线框，L1）：`<section style="border:1px solid {{DIVIDER}};border-radius:12px;padding:14px 18px;margin:0 0 16px;">` 内放 `<p style="font-size:14px;color:{{TEXT}};line-height:1.8;">…</p>`。卡顶可用 mono 小标签 `{{TOOL 01}}`（`<span style="font-size:10px;font-weight:700;color:{{ACCENT}};font-family:{{MONO_FONT}};letter-spacing:1px;"><span leaf="">…</span></span>`）。
- **F9b 高亮卡**（L2/L3）：`background:{{ACCENT_SOFT}}` + 圆角 12px + 内边距 16px 18px。
- **F9c 数据卡**（两列/三列）：flex 均分，线框 + 大数字 + 说明（数字 28px/900 accent）。
- **F9d 流程卡**（三步横排）：首卡 accent 实底、中间白卡、末卡 accent 描边，箭头 `→` 连接。
- **F9e 重叠圆对比**（讲义 / 科普，L2–L3）：两个半透明圆重叠，交叠处自然混色，表达「A 与 B 的张力/交集」。微信用 opacity + 负 margin 实现，禁 absolute。

```html
<section style="margin:0 0 28px;">
  <section style="display:flex;justify-content:center;align-items:flex-start;">
    <section style="width:200px;height:200px;border-radius:50%;background:{{SURFACE_A}};opacity:0.88;display:flex;align-items:center;justify-content:center;text-align:center;padding:22px;">
      <section><p style="margin:0 0 6px;font-size:16px;font-weight:800;color:{{HEADING}};"><span leaf="">{{概念A}}</span></p><p style="margin:0;font-size:12px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{说明A}}</span></p></section>
    </section>
    <section style="width:200px;height:200px;border-radius:50%;background:{{SURFACE_B}};opacity:0.88;display:flex;align-items:center;justify-content:center;text-align:center;padding:22px;margin-left:-64px;margin-top:44px;">
      <section><p style="margin:0 0 6px;font-size:16px;font-weight:800;color:{{HEADING}};"><span leaf="">{{概念B}}</span></p><p style="margin:0;font-size:12px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{说明B}}</span></p></section>
    </section>
  </section>
</section>
```

### F10 图片族

- **F10a 细线框卡**（L1+，默认）：`<section style="margin:0 0 16px;border:1px solid {{DIVIDER}};border-radius:10px;padding:6px;"><section style="border-radius:8px;overflow:hidden;"><span leaf=""><img src="{{URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span></section></section>`
- **F10b 无框圆角**（L0/封面）：`<section style="margin:0 0 20px;text-align:center;"><span leaf=""><img src="{{URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:10px;"></span></section>`
- 图注（有真说明才加）：`<p style="font-size:12px;color:{{TEXT_SECONDARY}};text-align:center;margin:0 0 20px;"><span leaf="">— {{图注}}</span></p>`
- **F10c 占位板块**（待补素材）：居中虚线框 + 图标 + 「待补素材」说明（唯一允许 dashed 的场景）。

### F11 结尾族

- **F11a 细线收尾**（书卷/极简）：`<section style="height:1px;background:{{DIVIDER}};margin:28px 0 0;"><span leaf=""><br></span></section>`
- **F11b END 线**（编辑风）：细线 + 居中 mono `END`。
- **F11c 作者签名卡（强制，每篇末尾必有一处）**：编辑风「colophon 署名」——上下细线框 + 等宽小标签 + 大字距作者名 + 1px accent 点睛线 + 次要色简介；层级靠字号/字距/留白，不靠色块。**作者名 + 一句话简介在提问阶段（design-system §10 第 4 步）向用户获取**，用户提供则直接填入；用户明确不提供才用 `{{作者名}}` / `{{简介}}` 占位并在交付时提醒替换；原文末尾已有署名段 → 并入此卡，不重复生成。

居中版（默认，优雅低调）：

```html
<section style="margin:40px 0 0;padding:30px 26px 26px;border-top:1px solid {{DIVIDER}};border-bottom:1px solid {{DIVIDER}};text-align:center;">
  <p style="margin:0 0 16px;font-size:10px;letter-spacing:5px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
    <span leaf="">AUTHOR · 作者</span>
  </p>
  <p style="margin:0 0 12px;font-size:20px;font-weight:600;color:{{HEADING}};letter-spacing:4px;line-height:1.5;">
    <span leaf="">{{作者名}}</span>
  </p>
  <section style="width:32px;height:1px;background:{{ACCENT}};margin:0 auto 14px;"><span leaf=""><br></span></section>
  <p style="margin:0;font-size:13px;color:{{TEXT_SECONDARY}};letter-spacing:1px;line-height:1.9;">
    <span leaf="">{{一句话简介}}</span>
  </p>
</section>
```

左对齐版（副刊/内刊风，可选）：

```html
<section style="margin:40px 0 0;padding:28px 0 24px;border-top:1px solid {{DIVIDER}};">
  <p style="margin:0 0 10px;font-size:10px;letter-spacing:4px;color:{{ACCENT}};font-family:{{MONO_FONT}};">
    <span leaf="">AUTHOR</span>
  </p>
  <p style="margin:0 0 6px;font-size:20px;font-weight:600;color:{{HEADING}};letter-spacing:3px;line-height:1.4;">
    <span leaf="">{{作者名}}</span>
  </p>
  <p style="margin:0;font-size:13px;color:{{TEXT_SECONDARY}};line-height:1.9;">
    <span leaf="">{{一句话简介}}</span>
  </p>
</section>
```

设计要点：锐角（0 圆角，印刷感）；accent 只作 1px 点睛线与标签色；作者名用宽字距制造庄重感，简介保持小号次要色——优雅、克制、有细节，但不繁杂。

- **F11d CTA 卡**（原文有互动引导才用）：浅底卡 + 「点赞在看转发」图标组。

### F13 文末留存族（可选，默认关）

**F13a 完读卡**（仅在用户明确要 CTA、或原文自带互动引导时用；全篇只 1 个）：accent-soft 底 + 左竖线 + 等宽「写在最后」标签 + 一句完读肯定（从原文结语提炼，不改原意）。

```html
<section style="margin:36px 0 0;background:{{ACCENT_SOFT}};border-left:3px solid {{ACCENT}};border-radius:0 10px 10px 0;padding:16px 18px;">
  <p style="margin:0 0 8px;font-size:10px;font-weight:800;letter-spacing:3px;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">写在最后</span></p>
  <p style="margin:0;font-size:14px;line-height:1.85;color:{{TEXT}};"><span leaf="">{{完读肯定句}}</span></p>
</section>
```

注意：F13 与 F11c 签名卡不冲突——收尾顺序为 F11a 收尾线 → F11c 签名卡 →（可选）F13。

### F14 图解族（Diagram，F14a–F14z）

把「关系、张力、结构、流程、度量」画出来，让抽象概念一眼可见。全部用微信兼容的 HTML/CSS 实现（flex / 圆角 / 半透明 / 负 margin / 渐变 / 边框，**禁 SVG / absolute / grid**），颜色全部 token 化（面色板 surface-a/b、highlight、summary-bg 参与，保持低饱和 + 单 accent）。

**规则**：图解是重组件，**每篇 ≤2 处**，计入组件预算；同一篇尽量保持同一视觉语言（同色系、同圆角、同粗细），不贪多。选择按**内容语义**，不按气质：权衡→天平/光谱，分层→同心圆，循环→闭环环，数据→条形，评价→星级。

#### F14a 天平 / 跷跷板（seesaw）——权衡、此消彼长

```html
<section style="margin:0 0 28px;">
  <section style="display:flex;justify-content:center;align-items:flex-end;">
    <section style="text-align:center;width:150px;">
      <p style="margin:0 0 6px;font-size:14px;font-weight:800;color:{{HEADING}};"><span leaf="">{{概念A}}</span></p>
      <section style="width:54px;height:54px;border-radius:50%;background:{{SURFACE_A}};margin:0 auto;"><span leaf=""><br></span></section>
    </section>
    <section style="width:110px;height:6px;background:{{DIVIDER}};border-radius:3px;margin:0 8px 24px;"><span leaf=""><br></span></section>
    <section style="text-align:center;width:150px;">
      <p style="margin:0 0 6px;font-size:14px;font-weight:800;color:{{HEADING}};"><span leaf="">{{概念B}}</span></p>
      <section style="width:54px;height:54px;border-radius:50%;background:{{SURFACE_B}};margin:0 auto;"><span leaf=""><br></span></section>
    </section>
  </section>
  <section style="width:0;height:0;border-left:9px solid transparent;border-right:9px solid transparent;border-bottom:12px solid {{ACCENT}};margin:0 auto;"><span leaf=""><br></span></section>
  <p style="margin:8px 0 0;font-size:12px;color:{{TEXT_SECONDARY}};text-align:center;"><span leaf="">{{权衡说明}}</span></p>
</section>
```

#### F14b 拉锯条（slider）——当前偏哪一边

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;justify-content:space-between;margin:0 0 8px;">
    <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};"><span leaf="">{{左标签}}</span></p>
    <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};"><span leaf="">{{右标签}}</span></p>
  </section>
  <section style="position:relative;height:10px;background:{{ACCENT_SOFT}};border-radius:5px;">
    <section style="width:30%;height:10px;background:{{ACCENT}};border-radius:5px;"><span leaf=""><br></span></section>
  </section>
  <p style="margin:6px 0 0;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{偏向说明}}</span></p>
</section>
```

#### F14c 光谱条（spectrum）——连续谱，不是二选一

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;justify-content:space-between;margin:0 0 8px;">
    <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};"><span leaf="">{{左端}}</span></p>
    <p style="margin:0;font-size:13px;font-weight:700;color:{{HEADING}};"><span leaf="">{{右端}}</span></p>
  </section>
  <section style="height:12px;border-radius:6px;background:linear-gradient(90deg,{{SURFACE_A}},{{SURFACE_B}});"><span leaf=""><br></span></section>
  <p style="margin:6px 0 0;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{谱系说明}}</span></p>
</section>
```

#### F14d 分水岭（watershed）——表面 vs 本质 / 旧 vs 新

```html
<section style="margin:0 0 26px;">
  <section style="border-left:3px solid {{ACCENT}};padding:12px 14px;border-bottom:1px solid {{DIVIDER}};">
    <p style="margin:0 0 4px;font-size:12px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{上标签}}</span></p>
    <p style="margin:0;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{上说明}}</span></p>
  </section>
  <section style="border-left:3px solid {{TEXT_SECONDARY}};padding:12px 14px;">
    <p style="margin:0 0 4px;font-size:12px;font-weight:800;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{下标签}}</span></p>
    <p style="margin:0;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{下说明}}</span></p>
  </section>
</section>
```

#### F14e 镜像 vs（mirror-vs）——直接对立

```html
<section style="margin:0 0 26px;display:flex;align-items:stretch;">
  <section style="flex:1;border-top:2px solid {{ACCENT}};border-right:1px solid {{DIVIDER}};padding:14px 12px;">
    <p style="margin:0 0 4px;font-size:14px;font-weight:800;color:{{HEADING}};"><span leaf="">{{甲}}</span></p>
    <p style="margin:0;font-size:12px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{甲说明}}</span></p>
  </section>
  <section style="flex:0 0 44px;display:flex;align-items:center;justify-content:center;">
    <p style="margin:0;font-size:14px;font-weight:900;color:{{ACCENT}};"><span leaf="">vs</span></p>
  </section>
  <section style="flex:1;border-top:2px solid {{TEXT_SECONDARY}};border-left:1px solid {{DIVIDER}};padding:14px 12px;">
    <p style="margin:0 0 4px;font-size:14px;font-weight:800;color:{{HEADING}};"><span leaf="">{{乙}}</span></p>
    <p style="margin:0;font-size:12px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{乙说明}}</span></p>
  </section>
</section>
```

#### F14f 漏斗（funnel）——层层收敛 / 筛选

```html
<section style="margin:0 0 26px;">
  <section style="width:88%;background:{{SURFACE_A}};border-radius:8px;padding:9px 14px;margin:0 auto 6px;"><p style="margin:0;font-size:13px;font-weight:800;color:{{HEADING}};"><span leaf="">{{第1层}}</span></p></section>
  <section style="width:72%;background:{{ACCENT_SOFT}};border-radius:8px;padding:9px 14px;margin:0 auto 6px;"><p style="margin:0;font-size:13px;font-weight:800;color:{{HEADING}};"><span leaf="">{{第2层}}</span></p></section>
  <section style="width:56%;background:{{SURFACE_B}};border-radius:8px;padding:9px 14px;margin:0 auto 6px;"><p style="margin:0;font-size:13px;font-weight:800;color:{{HEADING}};"><span leaf="">{{第3层}}</span></p></section>
  <section style="width:40%;background:{{ACCENT}};border-radius:8px;padding:9px 14px;margin:0 auto;"><p style="margin:0;font-size:13px;font-weight:800;color:#fff;"><span leaf="">{{最终层}}</span></p></section>
</section>
```

#### F14g 同心圆（onion）——核心 / 中间层 / 外层

```html
<section style="margin:0 0 26px;text-align:center;">
  <section style="width:220px;height:220px;border-radius:50%;background:{{SURFACE_A}};margin:0 auto;display:flex;align-items:center;justify-content:center;">
    <section style="width:150px;height:150px;border-radius:50%;background:{{SURFACE_B}};display:flex;align-items:center;justify-content:center;">
      <section style="width:84px;height:84px;border-radius:50%;background:{{ACCENT}};display:flex;align-items:center;justify-content:center;">
        <p style="margin:0;font-size:12px;font-weight:800;color:#fff;text-align:center;line-height:1.4;"><span leaf="">{{核心}}</span></p>
      </section>
    </section>
  </section>
  <p style="margin:10px 0 0;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{外层 · 中间层 · 核心说明}}</span></p>
</section>
```

#### F14h 层叠卡（stack）——多级体系 / 版本演进

```html
<section style="margin:0 0 26px;">
  <section style="border:1px solid {{DIVIDER}};border-radius:10px;padding:12px 14px;background:{{SUMMARY_BG}};"><p style="margin:0;font-size:13px;font-weight:700;color:{{TEXT_SECONDARY}};"><span leaf="">{{底层}}</span></p></section>
  <section style="border:1px solid {{DIVIDER}};border-radius:10px;padding:12px 14px;background:{{SURFACE_A}};margin:-8px 12px 0;"><p style="margin:0;font-size:13px;font-weight:700;color:{{TEXT}};"><span leaf="">{{中层}}</span></p></section>
  <section style="border:1px solid {{ACCENT}};border-radius:10px;padding:12px 14px;background:{{CONTENT_BG}};margin:-8px 24px 0;"><p style="margin:0;font-size:13px;font-weight:800;color:{{HEADING}};"><span leaf="">{{顶层}}</span></p></section>
</section>
```

#### F14i 金字塔（pyramid）——底座支撑上层

```html
<section style="margin:0 0 26px;">
  <section style="width:44%;background:{{ACCENT}};border-radius:8px;padding:9px 14px;margin:0 auto 6px;"><p style="margin:0;font-size:12px;font-weight:800;color:#fff;text-align:center;"><span leaf="">{{核心/少数}}</span></p></section>
  <section style="width:62%;background:{{ACCENT_SOFT}};border-radius:8px;padding:9px 14px;margin:0 auto 6px;"><p style="margin:0;font-size:12px;font-weight:800;color:{{HEADING}};text-align:center;"><span leaf="">{{支撑层}}</span></p></section>
  <section style="width:80%;background:{{SURFACE_A}};border-radius:8px;padding:9px 14px;margin:0 auto 6px;"><p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};text-align:center;"><span leaf="">{{基础层}}</span></p></section>
  <section style="width:94%;background:{{SURFACE_B}};border-radius:8px;padding:9px 14px;margin:0 auto;"><p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};text-align:center;"><span leaf="">{{底座/大量}}</span></p></section>
</section>
```

#### F14j 中心辐射（hub-spoke）——一个主节点 + 多个分支

```html
<section style="margin:0 0 26px;">
  <section style="width:120px;background:{{ACCENT}};border-radius:12px;padding:12px 10px;margin:0 auto 0;">
    <p style="margin:0;font-size:13px;font-weight:800;color:#fff;text-align:center;"><span leaf="">{{中心}}</span></p>
  </section>
  <section style="width:1px;height:14px;background:{{DIVIDER}};margin:0 auto;"><span leaf=""><br></span></section>
  <section style="display:flex;justify-content:center;gap:8px;">
    <section style="flex:1;max-width:130px;border:1px solid {{DIVIDER}};border-radius:10px;padding:10px 8px;text-align:center;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{分支1}}</span></p></section>
    <section style="flex:1;max-width:130px;border:1px solid {{DIVIDER}};border-radius:10px;padding:10px 8px;text-align:center;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{分支2}}</span></p></section>
    <section style="flex:1;max-width:130px;border:1px solid {{DIVIDER}};border-radius:10px;padding:10px 8px;text-align:center;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{分支3}}</span></p></section>
  </section>
</section>
```

#### F14k 包含框（containment）——整体包含局部

```html
<section style="margin:0 0 26px;border:1px solid {{DIVIDER}};border-radius:12px;padding:14px;">
  <p style="margin:0 0 10px;font-size:12px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{大集合}}</span></p>
  <section style="display:flex;flex-wrap:wrap;gap:8px;">
    <section style="flex:1;min-width:110px;background:{{SURFACE_A}};border-radius:8px;padding:10px;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{子集1}}</span></p></section>
    <section style="flex:1;min-width:110px;background:{{ACCENT_SOFT}};border-radius:8px;padding:10px;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{子集2}}</span></p></section>
    <section style="flex:1;min-width:110px;background:{{SURFACE_B}};border-radius:8px;padding:10px;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{子集3}}</span></p></section>
  </section>
</section>
```

#### F14l 堆栈塔（stack-tower）——分层架构 / Agent 层级

```html
<section style="margin:0 0 26px;">
  <section style="background:{{SURFACE_B}};border:1px solid {{DIVIDER}};border-radius:8px;padding:8px 12px;"><p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};"><span leaf="">{{顶层}}</span></p></section>
  <section style="background:{{ACCENT_SOFT}};border:1px solid {{DIVIDER}};border-radius:8px;padding:8px 12px;margin:4px 10px 0;"><p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};"><span leaf="">{{中间层}}</span></p></section>
  <section style="background:{{SURFACE_A}};border:1px solid {{DIVIDER}};border-radius:8px;padding:8px 12px;margin:4px 20px 0;"><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{底层}}</span></p></section>
</section>
```

#### F14m 闭环环（loop）——循环 / 飞轮

```html
<section style="margin:0 0 26px;text-align:center;">
  <section style="display:flex;justify-content:space-between;margin:0 0 6px;">
    <section style="width:88px;background:{{SURFACE_A}};border-radius:10px;padding:8px 6px;"><p style="margin:0;font-size:11px;font-weight:700;color:{{HEADING}};"><span leaf="">{{节点1}}</span></p></section>
    <section style="width:88px;background:{{SURFACE_B}};border-radius:10px;padding:8px 6px;"><p style="margin:0;font-size:11px;font-weight:700;color:{{HEADING}};"><span leaf="">{{节点2}}</span></p></section>
  </section>
  <p style="margin:6px 0;font-size:13px;font-weight:800;color:{{ACCENT}};"><span leaf="">{{中心：循环/飞轮}}</span></p>
  <section style="display:flex;justify-content:space-between;">
    <section style="width:88px;background:{{SURFACE_B}};border-radius:10px;padding:8px 6px;"><p style="margin:0;font-size:11px;font-weight:700;color:{{HEADING}};"><span leaf="">{{节点4}}</span></p></section>
    <section style="width:88px;background:{{SURFACE_A}};border-radius:10px;padding:8px 6px;"><p style="margin:0;font-size:11px;font-weight:700;color:{{HEADING}};"><span leaf="">{{节点3}}</span></p></section>
  </section>
  <p style="margin:8px 0 0;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{循环说明}}</span></p>
</section>
```

#### F14n 管道流水线（pipeline）——输入 → 处理 → 输出

```html
<section style="margin:0 0 26px;display:flex;align-items:stretch;">
  <section style="flex:1;background:{{SURFACE_A}};border-radius:10px 0 0 10px;padding:12px 8px;text-align:center;"><p style="margin:0 0 4px;font-size:11px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">01</span></p><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{输入}}</span></p></section>
  <p style="margin:0;flex:0 0 20px;text-align:center;color:{{ACCENT}};font-weight:900;font-size:15px;line-height:52px;"><span leaf="">→</span></p>
  <section style="flex:1;background:{{ACCENT_SOFT}};padding:12px 8px;text-align:center;"><p style="margin:0 0 4px;font-size:11px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">02</span></p><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{处理}}</span></p></section>
  <p style="margin:0;flex:0 0 20px;text-align:center;color:{{ACCENT}};font-weight:900;font-size:15px;line-height:52px;"><span leaf="">→</span></p>
  <section style="flex:1;background:{{ACCENT}};border-radius:0 10px 10px 0;padding:12px 8px;text-align:center;"><p style="margin:0 0 4px;font-size:11px;font-weight:800;color:#FFFFFFB3;font-family:{{MONO_FONT}};"><span leaf="">03</span></p><p style="margin:0;font-size:12px;font-weight:700;color:#fff;"><span leaf="">{{输出}}</span></p></section>
</section>
```

#### F14o 阶梯上升（stairs）——成长 / 爬坡 / 阶段跃迁

```html
<section style="margin:0 0 26px;">
  <section style="width:70%;background:{{SURFACE_B}};border-radius:8px;padding:9px 12px;"><p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};"><span leaf="">{{阶段1}}</span></p></section>
  <section style="width:84%;background:{{ACCENT_SOFT}};border-radius:8px;padding:9px 12px;margin:6px 0 0 auto;"><p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};"><span leaf="">{{阶段2}}</span></p></section>
  <section style="width:94%;background:{{SURFACE_A}};border-radius:8px;padding:9px 12px;margin:6px 0 0 auto;"><p style="margin:0;font-size:12px;font-weight:800;color:{{HEADING}};"><span leaf="">{{阶段3}}</span></p></section>
</section>
```

#### F14p 回形迭代（feedback-loop）——行为 → 反馈 → 优化

```html
<section style="margin:0 0 26px;">
  <section style="border:1px solid {{DIVIDER}};border-radius:10px;padding:12px 14px;"><p style="margin:0;font-size:13px;font-weight:800;color:{{HEADING}};"><span leaf="">{{动作/行为}}</span></p></section>
  <p style="margin:4px 0;text-align:center;color:{{ACCENT}};font-weight:900;font-size:14px;"><span leaf="">↓</span></p>
  <section style="border:1px solid {{DIVIDER}};border-radius:10px;padding:12px 14px;background:{{SURFACE_A}};"><p style="margin:0;font-size:13px;font-weight:700;color:{{TEXT}};"><span leaf="">{{数据/反馈}}</span></p></section>
  <p style="margin:4px 0;text-align:center;color:{{ACCENT}};font-weight:900;font-size:14px;"><span leaf="">↑</span></p>
  <section style="border:1px solid {{ACCENT}};border-radius:10px;padding:12px 14px;background:{{CONTENT_BG}};"><p style="margin:0;font-size:13px;font-weight:800;color:{{HEADING}};"><span leaf="">{{优化/再投入}}</span></p></section>
</section>
```

#### F14q 里程碑（milestones）——阶段规划：已到 / 当前 / 未来

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;justify-content:space-between;">
    <p style="margin:0;font-size:11px;font-weight:800;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{2024}}</span></p>
    <p style="margin:0;font-size:11px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{2025}}</span></p>
    <p style="margin:0;font-size:11px;font-weight:800;color:{{HEADING}};font-family:{{MONO_FONT}};"><span leaf="">{{2026}}</span></p>
  </section>
  <section style="height:3px;background:linear-gradient(90deg,{{DIVIDER}},{{ACCENT}});border-radius:2px;margin:6px 0 8px;"><span leaf=""><br></span></section>
  <section style="display:flex;justify-content:space-between;">
    <p style="margin:0;font-size:11px;color:{{TEXT_SECONDARY}};"><span leaf="">{{已发生}}</span></p>
    <p style="margin:0;font-size:11px;color:{{ACCENT}};font-weight:700;"><span leaf="">{{当前}}</span></p>
    <p style="margin:0;font-size:11px;color:{{TEXT}};"><span leaf="">{{未来}}</span></p>
  </section>
</section>
```

#### F14r 条形对比（growth-bars）——同一指标的量差

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;align-items:center;margin:0 0 8px;">
    <p style="margin:0;flex:0 0 90px;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{标签1}}</span></p>
    <section style="flex:1;height:8px;background:{{ACCENT_SOFT}};border-radius:4px;"><section style="width:30%;height:8px;background:{{ACCENT}};border-radius:4px;"><span leaf=""><br></span></section></section>
    <p style="margin:0 0 0 8px;font-size:12px;font-weight:800;color:{{HEADING}};"><span leaf="">{{值1}}</span></p>
  </section>
  <section style="display:flex;align-items:center;margin:0 0 8px;">
    <p style="margin:0;flex:0 0 90px;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{标签2}}</span></p>
    <section style="flex:1;height:8px;background:{{ACCENT_SOFT}};border-radius:4px;"><section style="width:55%;height:8px;background:{{ACCENT}};border-radius:4px;"><span leaf=""><br></span></section></section>
    <p style="margin:0 0 0 8px;font-size:12px;font-weight:800;color:{{HEADING}};"><span leaf="">{{值2}}</span></p>
  </section>
  <section style="display:flex;align-items:center;">
    <p style="margin:0;flex:0 0 90px;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{标签3}}</span></p>
    <section style="flex:1;height:8px;background:{{ACCENT_SOFT}};border-radius:4px;"><section style="width:78%;height:8px;background:{{ACCENT}};border-radius:4px;"><span leaf=""><br></span></section></section>
    <p style="margin:0 0 0 8px;font-size:12px;font-weight:800;color:{{HEADING}};"><span leaf="">{{值3}}</span></p>
  </section>
</section>
```

#### F14s 双条镜像（mirror-bars）——A vs B 量级对比

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;align-items:center;margin:0 0 6px;">
    <section style="flex:1;display:flex;justify-content:flex-end;"><section style="width:40%;height:10px;background:{{ACCENT}};border-radius:4px 0 0 4px;"><span leaf=""><br></span></section></section>
    <p style="margin:0 8px;font-size:11px;font-weight:800;color:{{TEXT_SECONDARY}};"><span leaf="">vs</span></p>
    <section style="flex:1;"><section style="width:55%;height:10px;background:{{SURFACE_A}};border-radius:0 4px 4px 0;"><span leaf=""><br></span></section></section>
  </section>
  <section style="display:flex;justify-content:space-between;">
    <p style="margin:0;font-size:11px;color:{{TEXT}};"><span leaf="">{{甲 40%}}</span></p>
    <p style="margin:0;font-size:11px;color:{{TEXT_SECONDARY}};"><span leaf="">{{乙 55%}}</span></p>
  </section>
</section>
```

#### F14t 星级（stars）——评价 / 强度

```html
<section style="margin:0 0 26px;text-align:center;">
  <p style="margin:0 0 6px;font-size:16px;letter-spacing:3px;"><span style="color:{{ACCENT}};"><span leaf="">★★★★</span></span><span style="color:{{DIVIDER}};"><span leaf="">★</span></span></p>
  <p style="margin:0;font-size:12px;color:{{TEXT_SECONDARY}};"><span leaf="">{{评分说明}}</span></p>
</section>
```

#### F14u 色阶热力（ladder）——程度档位：低 → 中 → 高

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;gap:6px;">
    <section style="width:28px;height:28px;border-radius:8px;background:{{SURFACE_B}};"><span leaf=""><br></span></section>
    <section style="width:28px;height:28px;border-radius:8px;background:{{ACCENT_SOFT}};"><span leaf=""><br></span></section>
    <section style="width:28px;height:28px;border-radius:8px;background:{{SURFACE_A}};"><span leaf=""><br></span></section>
    <section style="width:28px;height:28px;border-radius:8px;background:{{ACCENT}};"><span leaf=""><br></span></section>
  </section>
  <section style="display:flex;justify-content:space-between;margin:6px 0 0;">
    <p style="margin:0;font-size:11px;color:{{TEXT_SECONDARY}};"><span leaf="">{{低}}</span></p>
    <p style="margin:0;font-size:11px;color:{{TEXT}};"><span leaf="">{{中}}</span></p>
    <p style="margin:0;font-size:11px;color:{{HEADING}};"><span leaf="">{{高}}</span></p>
  </section>
</section>
```

#### F14v 比例条（ratio-split）——占比拆分

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;height:14px;border-radius:7px;overflow:hidden;">
    <section style="flex:0 0 65%;background:{{ACCENT}};"><span leaf=""><br></span></section>
    <section style="flex:1;background:{{SURFACE_A}};"><span leaf=""><br></span></section>
  </section>
  <section style="display:flex;justify-content:space-between;margin:6px 0 0;">
    <p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{A 65%}}</span></p>
    <p style="margin:0;font-size:12px;font-weight:700;color:{{TEXT}};"><span leaf="">{{B 35%}}</span></p>
  </section>
</section>
```

#### F14w 角色链路（chain）——带角色名的环节链

```html
<section style="margin:0 0 26px;display:flex;align-items:stretch;">
  <section style="flex:1;border-top:2px solid {{ACCENT}};border-right:1px solid {{DIVIDER}};padding:10px 8px;text-align:center;"><p style="margin:0 0 4px;font-size:10px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{角色1}}</span></p><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{环节1}}</span></p></section>
  <p style="margin:0;flex:0 0 18px;text-align:center;color:{{ACCENT}};font-weight:900;font-size:14px;line-height:46px;"><span leaf="">→</span></p>
  <section style="flex:1;border-top:2px solid {{ACCENT}};border-right:1px solid {{DIVIDER}};padding:10px 8px;text-align:center;"><p style="margin:0 0 4px;font-size:10px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{角色2}}</span></p><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{环节2}}</span></p></section>
  <p style="margin:0;flex:0 0 18px;text-align:center;color:{{ACCENT}};font-weight:900;font-size:14px;line-height:46px;"><span leaf="">→</span></p>
  <section style="flex:1;border-top:2px solid {{TEXT_SECONDARY}};padding:10px 8px;text-align:center;"><p style="margin:0 0 4px;font-size:10px;font-weight:800;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{角色3}}</span></p><p style="margin:0;font-size:12px;font-weight:700;color:{{HEADING}};"><span leaf="">{{环节3}}</span></p></section>
</section>
```

#### F14x 映射双列（mapping）——问题 → 解法 / 旧 → 新

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;align-items:flex-start;">
    <section style="flex:1;min-width:0;">
      <p style="margin:0 0 8px;font-size:12px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{左列标题}}</span></p>
      <p style="margin:0 0 8px;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{左项1}}</span></p>
      <p style="margin:0 0 8px;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{左项2}}</span></p>
      <p style="margin:0;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{左项3}}</span></p>
    </section>
    <p style="margin:0 10px;font-size:16px;font-weight:900;color:{{ACCENT}};line-height:32px;"><span leaf="">→</span></p>
    <section style="flex:1;min-width:0;">
      <p style="margin:0 0 8px;font-size:12px;font-weight:800;color:{{ACCENT}};font-family:{{MONO_FONT}};"><span leaf="">{{右列标题}}</span></p>
      <p style="margin:0 0 8px;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{右项1}}</span></p>
      <p style="margin:0 0 8px;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{右项2}}</span></p>
      <p style="margin:0;font-size:13px;line-height:1.7;color:{{TEXT}};"><span leaf="">{{右项3}}</span></p>
    </section>
  </section>
</section>
```

#### F14y 状态迁移（state）——就绪 → 运行 → 完成

```html
<section style="margin:0 0 26px;display:flex;align-items:flex-start;justify-content:center;">
  <section style="text-align:center;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:{{ACCENT}};color:#fff;font-size:12px;font-weight:800;"><span leaf="">{{S1}}</span></span>
    <p style="margin:4px 0 0;font-size:11px;color:{{TEXT}};"><span leaf="">{{就绪}}</span></p>
  </section>
  <p style="margin:8px 8px 0;color:{{ACCENT}};font-weight:900;font-size:14px;"><span leaf="">→</span></p>
  <section style="text-align:center;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:{{ACCENT_SOFT}};color:{{ACCENT}};font-size:12px;font-weight:800;"><span leaf="">{{S2}}</span></span>
    <p style="margin:4px 0 0;font-size:11px;color:{{TEXT}};"><span leaf="">{{运行}}</span></p>
  </section>
  <p style="margin:8px 8px 0;color:{{ACCENT}};font-weight:900;font-size:14px;"><span leaf="">→</span></p>
  <section style="text-align:center;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:{{SURFACE_A}};color:{{HEADING}};font-size:12px;font-weight:800;"><span leaf="">{{S3}}</span></span>
    <p style="margin:4px 0 0;font-size:11px;color:{{TEXT}};"><span leaf="">{{完成}}</span></p>
  </section>
</section>
```

#### F14z 关键词云（tag-cloud）——并列概念的权重

```html
<section style="margin:0 0 26px;">
  <section style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;">
    <span style="background:{{ACCENT}};color:#fff;border-radius:999px;padding:6px 14px;font-size:14px;font-weight:800;"><span leaf="">{{核心词}}</span></span>
    <span style="background:{{ACCENT_SOFT}};color:{{HEADING}};border-radius:999px;padding:5px 12px;font-size:12px;font-weight:700;"><span leaf="">{{次核心}}</span></span>
    <span style="background:{{SURFACE_A}};color:{{TEXT}};border-radius:999px;padding:4px 10px;font-size:11px;"><span leaf="">{{外围词}}</span></span>
    <span style="background:{{SURFACE_B}};color:{{TEXT}};border-radius:999px;padding:4px 10px;font-size:11px;"><span leaf="">{{并列词}}</span></span>
  </section>
</section>
```




### F15 报章 / 信笺族（L8 报章式 · L9 信笺式的骨架签名组件）

这两个家族只在对应骨架里用，是「第一眼」的识别点：报章式靠报头眉线与栏线，信笺式靠信头与落款。其余正文组件仍从 F4–F14 取。

**F15a 报头眉线**（L8 报章式）：刊名 + 刊号·日期·栏目，上下双栏线，等宽小字；像报纸报头的窄版。

```html
<section style="margin:0 0 22px;border-top:3px solid {{HEADING}};border-bottom:1px solid {{DIVIDER}};padding:14px 2px 10px;text-align:center;">
  <p style="margin:0 0 8px;font-size:24px;font-weight:900;color:{{HEADING}};letter-spacing:6px;line-height:1.3;font-family:{{HEADING_FONT}};"><span leaf="">{{刊名}}</span></p>
  <p style="margin:0;font-size:10px;letter-spacing:2px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{刊号 · 日期 · 栏目}}</span></p>
</section>
```

**F15b 日期戳**（L8/L9 通用）：等宽小字块 + 细线，给文章一个「写下于何时」的时间锚点。

```html
<section style="margin:0 0 18px;">
  <section style="display:inline-block;border:1px solid {{DIVIDER}};padding:5px 12px;">
    <p style="margin:0;font-size:11px;letter-spacing:1px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{YYYY.MM.DD · 地点/栏目}}</span></p>
  </section>
</section>
```

**F15c 此致 / 落款行**（L9 信笺式收尾）：右对齐「此致」+ 敬礼 + 落款名/日期，替代常规收尾线的仪式感结尾。

```html
<section style="margin:34px 0 0;text-align:right;">
  <p style="margin:0 0 4px;font-size:15px;color:{{TEXT}};line-height:1.8;"><span leaf="">此致</span></p>
  <p style="margin:0 0 16px;font-size:15px;color:{{TEXT}};line-height:1.8;"><span leaf="">敬礼！</span></p>
  <p style="margin:0 0 4px;font-size:16px;font-weight:700;color:{{HEADING}};letter-spacing:2px;"><span leaf="">{{落款名}}</span></p>
  <p style="margin:0;font-size:11px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{YYYY.MM.DD}}</span></p>
</section>
```

**F15d 信头**（L9 信笺式开篇）：称呼 + 问候语，像一封信的第一行；之后接引言正文。

```html
<section style="margin:0 0 26px;">
  <p style="margin:0 0 8px;font-size:17px;font-weight:700;color:{{HEADING}};line-height:1.7;font-family:{{HEADING_FONT}};"><span leaf="">{{称呼，如：亲爱的读者：}}</span></p>
  <p style="margin:0 0 4px;font-size:14px;line-height:1.9;color:{{TEXT}};"><span leaf="">{{问候语，如：见字如面。这篇文章想和你聊聊……}}</span></p>
</section>
```



### F16 终端族（L10 终端式的骨架签名组件）

只在 L10 终端式里用。终端式的关键是把整篇文章「框」进一个终端窗口——顶栏给出窗口感，提示符给出「对话感」，代码块与正文同底融为一体。

**F16a 窗口顶栏**（L10）：圆角深底卡 + 红黄绿三圆点 + 居中 mono 窗口标题；圆点用固定安全色（`#FF5F57` / `#FEBC2E` / `#28C840`），不随 accent 换色。

```html
<section style="margin:0 0 24px;background:{{CONTENT_BG}};border-radius:12px;overflow:hidden;border:1px solid {{DIVIDER}};">
  <section style="display:flex;align-items:center;padding:9px 14px;background:{{SURFACE_B}};border-bottom:1px solid {{DIVIDER}};">
    <span style="width:11px;height:11px;border-radius:50%;background:#FF5F57;display:inline-block;margin-right:6px;"><span leaf=""><br></span></span>
    <span style="width:11px;height:11px;border-radius:50%;background:#FEBC2E;display:inline-block;margin-right:6px;"><span leaf=""><br></span></span>
    <span style="width:11px;height:11px;border-radius:50%;background:#28C840;display:inline-block;margin-right:12px;"><span leaf=""><br></span></span>
    <p style="margin:0;flex:1;font-size:11px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};letter-spacing:1px;"><span leaf="">{{窗口标题，如：ya-pai — article.md}}</span></p>
  </section>
  <section style="padding:16px 16px 14px;">
    <p style="margin:0;font-size:21px;font-weight:900;color:{{HEADING}};line-height:1.45;font-family:{{MONO_FONT}};"><span leaf="">{{文章大标题}}</span></p>
    <p style="margin:8px 0 0;font-size:12px;color:{{TEXT_SECONDARY}};font-family:{{MONO_FONT}};"><span leaf="">{{副行，如：read · {{N}} min · {{日期}}}}</span></p>
  </section>
</section>
```

**F16b 提示符行**（L10）：`$` 提示符 + 文字，用于引言与过渡行；首字母 `>` 可作续行。

```html
<p style="margin:0 0 14px;font-size:14.5px;line-height:1.85;color:{{TEXT}};font-family:{{MONO_FONT}};">
  <span style="color:{{ACCENT}};font-weight:800;"><span leaf="">$ </span></span><span leaf="">{{提示符文字}}</span>
</p>
```

**F16c 终端收束行**（L10 收尾）：`$ done` + 光标方块（静态即可），替代「END 线」的收尾。

```html
<p style="margin:30px 0 0;font-size:14px;font-family:{{MONO_FONT}};color:{{TEXT_SECONDARY}};">
  <span style="color:{{ACCENT}};font-weight:800;"><span leaf="">$ </span></span><span leaf="">done</span><span style="display:inline-block;width:8px;height:14px;background:{{ACCENT}};vertical-align:-2px;margin-left:4px;"><span leaf=""><br></span></span>
</p>
```

### F12 代码族

- **F12a 深色代码块**（默认）：深底圆角卡 + 顶栏（三色圆点 + 语言名）+ 每行一个 `<p style="margin:0;font-family:{{MONO_FONT}};font-size:13px;line-height:1.6;color:#E2E8F0;">`，**禁 `white-space:pre`**，缩进用全角空格。
- **F12b 浅色代码块**：`background:{{CODE_BG}}` + `border-left:3px solid {{ACCENT}}`，每行一个 `p`。
- **F12c 行内代码**：同 M4。

## 四、维度 → 变体选择表

| 装饰档位 | 封面 | 章节标题 | 子标题 | 引用 | 提示 | 列表 | 卡片 | 图片 |
|---|---|---|---|---|---|---|---|---|
| L0 | F1c | F3b | F4d | F6a | F7a | F8a/F8b | — | F10b | — |
| L1 | F1a/F1c | F3a/F3c/F3e/F3i/F3j | F4a | F6a | F7a/F7b | F8a/F8b/F8e | F9a | F10a | F14b/F14c |
| L2 | F1a/F1b/F1e | F3c/F3d/F3f/F3g/F3i/F3b叠 | F4b/F4c | F6b/F6d/F6e | F7c/F7d/F7e | F8c/F8d | F9b/F9e | F10a | F14 族（≤2 处） |
| L3 | F1b/F1d/F1e/F1f | F3d/F3f/F3g/F3h/F3b叠 | F4c | F6b/F6c/F6d/F6e | F7c/F7d/F7e | F8c/F8d | F9b/F9d/F9e | F10a | F14 族（≤2 处） |

目录行（L6 侧栏式的公众号静态版）：L0–L1 用 F2d 细线目录；L2–L3 用 F2a 静态目录卡或 F2b 三列看点。
注：L2–L3 的 `F3b叠` 指水印大数字叠底版（讲义）；F6e/F7e/F9e/F8d 是讲义与图解配套组件，只在对应骨架（L7/L3）或用户指定时使用；F14 图解族按「内容语义」选型（见下方图解选型表），与装饰档位联动但不被气质锁定；F15 报章/信笺族只在 L8/L9 骨架使用、F16 终端族只在 L10 骨架使用，不参与档位表。

气质签名（同档位下的偏好）：

| 气质 | 封面 | 章节标题 | 引用 | 卡片 |
|---|---|---|---|---|
| 人文书卷 | F1a/F1e | F3a/F3e/F3h | F6a/F6d/F6e | F9a/F9e |
| 安静编辑 | F1a | F3a/F3e | F6a/F6e | F9a/F9e |
| 现代极简 | F1c/F1b | F3b/F3g | F6a | F9a |
| 冷冽理性 | F1b/F1c/F1f | F3c/F3f/F3i | F6a | F9a/F9c |
| 温暖纸感 | F1d/F1a/F1e | F3d/F3h | F6b | F9b |

## 五、完整文章模板骨架

```html
<section style="max-width:{{CONTENT_WIDTH}};margin:0 auto;{{背景样式}}font-family:{{BODY_FONT}};color:{{TEXT}};line-height:{{BODY_LH}};letter-spacing:0.5px;box-sizing:border-box;padding:{{CONTAINER_PADDING}};overflow-x:hidden;">

  <!-- 1. 封面（F1 族一选一；封面图放最前用 F10b） -->
  <!-- 2. 引言金句（F6 族；原文开头有 > 引用时） -->
  <!-- 3. 前言正文（F5 段落 × N） -->
  <!-- 4. 导读/目录（F2 族；L6 侧栏式必放 F2a/F2d，L2 导读式章节 ≥3 可 F2b，教程可 F2c） -->
  <!-- 5. 第一～N 章（F3 章节标题 + 章内 F4–F12 组件） -->
  <!-- 6. 结语章（F3 变体：编号 ∞） -->
  <!-- 7. 结尾（F11a 收尾线 + F11c 作者签名卡【强制】；F13 CTA 可选默认关） -->

</section>
```

**骨架铁律**：开篇 → 正文 → 结尾；具体形状（开篇进法、章节进场、引用/列表/图片处理、收尾）由 L1–L10 版式骨架决定——一篇文章只走一条骨架线、只用一套变量与一族变体，不跨骨架混搭。

骨架的具体形状（开篇怎么进、章节怎么进场、引用/列表/图片怎么处理、怎么收尾）由 tokens/layouts.md 的 **L1–L10 版式骨架**决定——不同的骨架是不同的「第一眼印象」，不是只换宽窄。选好骨架后，本库的组件按「维度 → 变体选择表」填入；同一篇内不得跨骨架混搭。

## 六、文章类型 → 组件组合配方

| 文章类型 | 核心组件 | 点缀组件 |
|---|---|---|
| 教程/操作指南 | F5 正文 + F4 子标题 + F8b 编号 + F12 代码 | F7b 踩坑、F9d 流程、F2c 目录 |
| 盘点/工具清单 | F5 正文 + F9a 工具卡 + F8a 列表 | F2a 目录、F6b 引用 |
| 观点/深度分析 | F5 正文 + F6a 引用 + M1 下划线 | F7a 提示、F6c 金句 |
| 访谈/人物特稿 | F5 正文 + F6a 引用（引语）+ F8d 时间线 | F6c 金句、F9b 高亮卡 |
| 数据复盘/报告 | F5 正文 + F9c 数据卡 + F8b 编号 | F2b 看点、M5 否定 |
| 生活/情感随笔 | F5 正文 + F6a 引用 + M3 高亮 | F2a 目录（章节多时） |
| 案例实战 | F5 正文 + F8b 编号 + F9a 卡片 | F7b 踩坑、F9d 流程 |
| 讲义/技术讲解 | F5 正文 + F3b叠底章头 + F6e 大引号 + F7e SUMMARY | M6 高亮条、F9e 重叠圆、F8d 时间线（演进内容） |

### 图解选型表（F14 族，按内容语义）

| 内容语义 | 优先图解 |
|---|---|
| 权衡 / 此消彼长 / 二选一 | F14a 天平、F14b 拉锯条、F14c 光谱条、F14e 镜像 vs |
| 表面 vs 本质 / 旧 vs 新 | F14d 分水岭、F14e 镜像 vs |
| 层层收敛 / 筛选 | F14f 漏斗、F14i 金字塔 |
| 分层 / 嵌套 / 架构层级 | F14g 同心圆、F14h 层叠卡、F14l 堆栈塔、F14k 包含框 |
| 中心 + 分支 | F14j 中心辐射 |
| 循环 / 飞轮 / 反馈回路 | F14m 闭环环、F14p 回形迭代 |
| 流程 / 流水线 / 环节链 | F14n 管道流水线、F14w 角色链路 |
| 阶段 / 里程碑 / 成长 | F14q 里程碑、F14o 阶梯上升 |
| 数据量差 / 占比 | F14r 条形对比、F14s 双条镜像、F14v 比例条 |
| 评价 / 强度档位 | F14t 星级、F14u 色阶热力 |
| 映射 / 对应 / 状态流转 | F14x 映射双列、F14y 状态迁移 |
| 并列概念 / 关键词 | F14z 关键词云 |

## 七、Markdown → 组件映射规则表

| Markdown 元素 | 组件 |
|---|---|
| `# 标题` | 不进正文（平台设置）；封面引导语按「审美原理 6」视角错开 |
| 开头 `> 引言` | F6 引用族（或并入 F1 封面金句） |
| `## 章节` | F3 章节标题族（自动编号，末章 ∞） |
| `### / #### 子标题` | F4 子标题族 |
| 普通段落 | F5 段落（每段 1–3 处 M1 下划线） |
| `**加粗**` | M2 accent 加粗（全篇 ≤3）/ 深字加粗 |
| `==高亮==` | M3 浅底高亮 |
| `<u> / ++…++` | M1 下划线 |
| `~~删除~~` | 删除线 + 次要色 |
| 行内 `` `code` `` | M4 行内代码 |
| `> 引用` | F6 引用族 |
| ` ``` 代码 ``` ` | F12a 深色 / F12b 浅色代码块 |
| `- 项` | F8a 圆点列表 |
| `1. 项` | F8b 编号圆标 |
| `![说明](URL)` | F10 图片族（有真说明才加图注） |
| `![](xxx.gif)` | F10 + GIF 角标 |
| `---` | 分隔线（细线，装饰空元素内放 `<span leaf=""><br></span>`） |
| 表格 | 表格组件（偶数行 accent-soft 浅底） |
| 注意/警告 | F7 提示族 |
| 时间线/演进内容 | F8d 时间线 |
| 章节小结/结论段 | F7e SUMMARY 结论卡 |
| 一句话结论（独立行） | M6 整句高亮条（全篇 ≤2） |
| 概念张力/权衡/分层/循环/流程/度量关系 | F14 图解族（按内容语义选型，见图解选型表；每篇 ≤2 处） |
| 文末 | F11a 收尾线 + F11c 作者签名卡（**强制**；F11d CTA 仅原文有互动引导时加） |
