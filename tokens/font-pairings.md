# 字体组合（font pairings）

全部使用**系统字体栈**（公众号不支持 web 字体）。中文渲染优先级：iOS 用苹方/宋体，Android 用思源系列，桌面用微软雅黑/宋体。

## 公共字体栈

- 无衬线正文：`-apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", Arial, sans-serif`
- 衬线正文：`"Noto Serif SC", "Source Han Serif SC", "Songti SC", "SimSun", "Times New Roman", serif`
- 英文衬线标题：`Georgia, "Times New Roman", "Noto Serif SC", "Songti SC", serif`
- 等宽：`"SF Mono", "Cascadia Code", Consolas, "Courier New", monospace`

## P1 衬线标题 + 无衬线正文（经典编辑）

- 标题：`Georgia, "Noto Serif SC", "Songti SC", "SimSun", serif`，600–700，letter-spacing 1px。
- 正文：无衬线栈，400，letter-spacing 0.5px。
- 气质：安静编辑、温暖纸感。
- 注意：中文标题落回宋体，庄重；别给标题加斜体。

## P2 全无衬线（现代极简）

- 标题与正文都用无衬线栈；标题 600–700，正文 400。
- 气质：现代极简、冷冽理性。
- 注意：全部无衬线时靠字重与字号分层，标题字重 ≥ 600，否则扁平无层次。

## P3 中文友好衬线（书卷）

- 标题与正文都用衬线栈：`"Noto Serif SC", "Source Han Serif SC", "Songti SC", "SimSun", serif`。
- 标题 600，正文 400；行高 1.9 以上。
- 气质：人文书卷。
- 注意：正文衬线 + 两端对齐时控制行宽（≤ 40 字/行），否则观感拥挤。

## P4 无衬线标题 + 衬线正文（人文杂志）

- 标题：无衬线栈 700；正文：衬线栈 400。
- 气质：温暖纸感、现代杂志。
- 注意：反差感强，标题可加大字号（22–24px）压住正文。

## P5 等宽点缀（技术向）

- 正文/标题用无衬线栈；代码、眉题标签、序号用等宽栈。
- 气质：冷冽理性、现代极简（技术变体）。
- 注意：眉题等宽 + letter-spacing 2px 有工程感；正文不要用等宽。

## P6 宋体标题 + 黑体正文（报章）

- 标题：`"Songti SC", "SimSun", "Noto Serif SC", serif`，700；正文：无衬线栈。
- 气质：温暖纸感、人文书卷（报纸/深度报道感）。
- 注意：宋体标题字号 21–23px 即可，再大显笨；正文行高 1.85。

## P7 等宽点缀·终端风（技术向）

- 标题与代码用等宽栈 `"SF Mono", "Cascadia Code", Consolas, "Courier New", monospace`（中文标题自动落回系统黑体），正文用无衬线栈。
- 气质：冷冽理性（终端/命令行变体）。
- 注意：等宽感主要来自数字、英文与代码；正文不用等宽；眉题、章节编号可用等宽制造工程感。

## P8 楷体引用（讲义/书卷）

- 正文与标题照常（无衬线或衬线）；**引用/金句专用楷体族** `'KaiTi','STKaiti','BiauKai','Noto Serif SC',serif`。
- 中文没有斜体，「斜体感」的正确实现是换楷体族，不是 `font-style:italic`。
- 配合 F6e 大引号引用、讲义骨架 L7 使用；引用字号可比正文大 1–2px。
- 气质：安静编辑、人文书卷（讲义/技术讲解变体）。

## 通用字重与字号

- 正文 400；强调 600；标题 600–700；眉题 400–500 + letter-spacing。
- 标题字号：h1 24–26、h2 19–20、h3 17–18；正文 15–16；图注/眉题 12–13。
- **讲义档（L7 讲义式）**：正文 17px、行高 1.9、标题 23px、引用 18px、图注 13px——讲解/课程内容更舒展；其余骨架仍按 15–16px 正文。
