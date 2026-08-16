#!/usr/bin/env python3
"""微信公众号 HTML 合规校验器。

把 SKILL.md 里"必须遵守的平台限制"从模型自觉变成确定性兜底。
排版生成后必跑：检查禁用标签/属性/样式，并核查文字节点是否用
<span leaf=""> 包裹（公众号编辑器粘贴后保持样式的关键）。
除平台红线外，还做一层「审美自检」（WARNING，参考 editorial-principles.md）：
连续 4+ 段纯文字阅读墙、疑似 AI 默认渐变/高饱和色、font-size 超限。
另做 WCAG 对比度检查：正文 ≥4.5:1、大字号/小字号次要文字 ≥3.0:1（纯计算，不依赖浏览器）。

用法:
    validate_gzh_html.py <file.html>
    validate_gzh_html.py --stdin < file.html

退出码: 1 = 有 ERROR（会被公众号过滤或粘贴后样式丢失）; 0 = 通过。
"""

import argparse
import math
import re
import sys
from html.parser import HTMLParser

# (正则, 级别, 说明) —— ERROR 会被公众号编辑器过滤掉或导致样式失效
FORBIDDEN = [
    (re.compile(r"<style[\s>]", re.I), "ERROR", "<style> 标签会被过滤，样式必须内联"),
    (re.compile(r"<script[\s>]", re.I), "ERROR", "<script> 标签会被过滤"),
    (re.compile(r"</?div[\s>]", re.I), "ERROR", "<div> 会被改写，请用 <section>"),
    (re.compile(r"<link[\s>]", re.I), "ERROR", "外部 <link>（CSS/字体）会被过滤"),
    (re.compile(r"\sclass\s*=", re.I), "ERROR", "class 属性会被剥离，请用内联 style"),
    (re.compile(r"\sid\s*=", re.I), "ERROR", "id 属性会被剥离"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I), "ERROR",
     "position fixed/absolute/sticky 不被支持"),
    (re.compile(r"float\s*:", re.I), "ERROR", "float 不被支持"),
    (re.compile(r"@media", re.I), "ERROR", "@media 媒体查询不被支持"),
    (re.compile(r"@keyframes", re.I), "ERROR", "@keyframes 动画不被支持"),
    (re.compile(r"@import", re.I), "ERROR", "@import 不被支持"),
    (re.compile(r"display\s*:\s*grid", re.I), "ERROR", "display:grid 不被支持，请用 flex"),
    (re.compile(r"var\s*\(\s*--", re.I), "ERROR", "CSS 变量 var(--x) 不被支持，请写死值"),
    (re.compile(r"url\s*\(\s*['\"]?https?://[^)]*\.(woff2?|ttf|otf|eot)", re.I),
     "ERROR", "外部字体不被支持"),
]

CJK = re.compile(r"[一-鿿㐀-䶿]")
SKIP_TAGS = {"head", "title", "style", "script"}  # 不参与公众号正文粘贴的区域
# 中文字后紧跟半角逗号/分号/叹号/问号（应改全角）；只查"中文在前"避免中英混排误伤
HALF_PUNCT = re.compile(r"[一-鿿㐀-䶿][,;!?]")
ASCII_QUOTE = re.compile(r"[\"']")
# 代码区特征：等宽字体或 white-space:pre —— 其内半角符号是正常的
CODE_STYLE = re.compile(r"monospace|white-space\s*:\s*pre|courier|consolas|sf mono", re.I)
# 常见 AI 默认渐变/高饱和色（出现即提示检查，通常与「优雅低调」冲突）
AI_DEFAULT_COLORS = [
    "#667eea", "#764ba2", "#7f00ff", "#e100ff", "#00c6ff", "#0072ff",
    "#00f2fe", "#4facfe", "#f093fb", "#f5576c", "#ee9ca7", "#ffdde1",
    "#fa709a", "#fee140", "#f83600", "#6a11cb", "#2575fc", "#30cfd0",
    "#330867", "#ff512f", "#dd2476", "#00b09b", "#96c93d", "#fc4a1a",
    "#f7b733", "#1a2980", "#26d0ce", "#ff9966", "#ff5e62", "#8e2de2",
    "#4a00e0", "#f12711", "#f5af19", "#12c2e9", "#c471ed", "#f64f59",
    "#e96443", "#904e95", "#9be15d", "#00e3ae", "#ff758c", "#ff7eb3",
]
FONT_SIZE = re.compile(r"font-size\s*:\s*(\d{2,3})px", re.I)
COLOR_VALUE = re.compile(
    r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?(?:[0-9a-fA-F]{2})?"
    r"|rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+\s*)?\)"
)
COLOR_STYLE = re.compile(r"(?:^|;)\s*color\s*:\s*(" + COLOR_VALUE.pattern + r")")
BG_STYLE = re.compile(
    r"(?:^|;)\s*background(?:-color)?\s*:\s*("
    + COLOR_VALUE.pattern
    + r"|linear-gradient\([^)]*\)|transparent)"
)
GRADIENT_RE = re.compile(r"gradient", re.I)
RGBA_RE = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)")
FONT_SIZE_ANY = re.compile(r"font-size\s*:\s*(\d+(?:\.\d+)?)px", re.I)
FONT_WEIGHT_ANY = re.compile(r"font-weight\s*:\s*(bold|(\d{3}))", re.I)


class LeafChecker(HTMLParser):
    """检查每个非空文本节点是否处于 <span leaf> 内。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []           # [(tag, is_leaf, is_code)]
        self.leaf_depth = 0       # 处于 span[leaf] 内的嵌套计数
        self.code_depth = 0       # 处于代码区（等宽/pre）内的嵌套计数
        self.span_leaf_count = 0  # 全文 span leaf 总数
        self.unwrapped = []       # (文本片段, 父标签) —— 未被 leaf 包裹的中文文本
        self.half_punct = []      # 正文里疑似半角标点的片段

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        is_leaf = tag == "span" and "leaf" in ad
        is_code = bool(CODE_STYLE.search(ad.get("style", "") or ""))
        if is_leaf:
            self.span_leaf_count += 1
            self.leaf_depth += 1
        if is_code:
            self.code_depth += 1
        self.stack.append((tag, is_leaf, is_code))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, was_leaf, was_code in self.stack[i:]:
                    if was_leaf:
                        self.leaf_depth -= 1
                    if was_code:
                        self.code_depth -= 1
                del self.stack[i:]
                break

    def handle_data(self, data):
        text = data.strip()
        if not text or not CJK.search(text):
            return
        if any(t in SKIP_TAGS for t, _, _ in self.stack):
            return  # <head>/<title>/<style>/<script> 内文字不进公众号正文
        if self.leaf_depth == 0:
            parent = self.stack[-1][0] if self.stack else "(root)"
            snippet = text[:24] + ("…" if len(text) > 24 else "")
            self.unwrapped.append((snippet, parent))
        if self.code_depth == 0 and (HALF_PUNCT.search(text)
                                     or ASCII_QUOTE.search(text)):
            snippet = text[:24] + ("…" if len(text) > 24 else "")
            self.half_punct.append(snippet)


class AestheticChecker(HTMLParser):
    """粗略的结构扫描，供审美 WARNING 使用（只统计块级标签的嵌套深度）。"""

    BLOCK = {"section", "p", "h3", "img", "table"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.blocks = []  # (tag, style, depth)

    def handle_starttag(self, tag, attrs):
        if tag not in self.BLOCK:
            return
        ad = dict(attrs)
        style = ad.get("style", "")
        if tag == "img":  # 自闭合，不留深度
            self.blocks.append((tag, style, self.depth + 1))
            return
        self.depth += 1
        self.blocks.append((tag, style, self.depth))

    def handle_endtag(self, tag):
        if tag in self.BLOCK and tag != "img":
            self.depth -= 1


def parse_color(text):
    """把 #hex / rgb() / rgba() 解析成 (r,g,b)；带透明度的返回 None（无法可靠计算）。"""
    s = text.strip().lower()
    if s.startswith("#"):
        h = s[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        elif len(h) == 4:
            h = "".join(c * 2 for c in h[:3]) + h[3] * 2
        if len(h) in (6, 8):
            if len(h) == 8 and int(h[6:8], 16) < 255:
                return None
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
        return None
    m = RGBA_RE.match(s)
    if m:
        if m.group(4) is not None and float(m.group(4)) < 0.99:
            return None
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def _channel_lum(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    r, g, b = rgb
    return (0.2126 * _channel_lum(r) + 0.7152 * _channel_lum(g)
            + 0.0722 * _channel_lum(b))


def contrast_ratio(fg, bg):
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


VOID_TAGS = {"img", "br", "hr", "input", "meta", "link"}
TEXT_TAGS = {"section", "p", "h3", "span", "strong", "a", "em"}


class ContrastChecker(HTMLParser):
    """收集「显式设了 color 的元素」与其生效背景，做 WCAG 对比度检查。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []           # 祖先元素 style 文本
        self.pairs = set()        # (fg, bg, need)
        self.skipped_gradient = 0
        self.unknown_bg = 0

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        style = ad.get("style", "")
        if tag not in VOID_TAGS:
            self.stack.append(style)
        if tag not in TEXT_TAGS:
            return
        m = COLOR_STYLE.search(style)
        if not m:
            return
        fg = parse_color(m.group(1))
        if fg is None:
            return
        bg = None
        bm = BG_STYLE.search(style)
        if bm:
            if GRADIENT_RE.search(bm.group(1)):
                self.skipped_gradient += 1
                return
            if bm.group(1).lower() != "transparent":
                bg = parse_color(bm.group(1))
        if bg is None:
            for ancestor in reversed(self.stack[:-1]):
                am = BG_STYLE.search(ancestor)
                if am:
                    if GRADIENT_RE.search(am.group(1)):
                        self.skipped_gradient += 1
                        return
                    if am.group(1).lower() != "transparent":
                        bg = parse_color(am.group(1))
                        break
        if bg is None:
            self.unknown_bg += 1
            return
        fm = FONT_SIZE_ANY.search(style)
        size = float(fm.group(1)) if fm else 15.0
        if size >= 40:
            return  # 水印大数字/大引号等背景级装饰元素，不做对比度检查
        wm = FONT_WEIGHT_ANY.search(style)
        weight = 700 if (wm and (wm.group(1) == "bold" or (wm.group(2) and int(wm.group(2)) >= 700))) else 400
        if size >= 24 or (size >= 18.66 and weight >= 700):
            need = 3.0
        elif size < 14 and weight < 700:
            need = 3.0   # 小字号次要文字（眉题/图注/页码）
        else:
            need = 4.5   # 正文
        self.pairs.add((fg, bg, need))

    def handle_endtag(self, tag):
        if tag not in VOID_TAGS and self.stack:
            self.stack.pop()


def contrast_warnings(html):
    warns = []
    checker = ContrastChecker()
    try:
        checker.feed(html)
    except Exception:
        return warns
    bad = []
    for fg, bg, need in checker.pairs:
        ratio = contrast_ratio(fg, bg)
        if ratio < need:
            bad.append((fg, bg, need, ratio))
    if bad:
        def hex6(c):
            return "#%02x%02x%02x" % c
        sample = "；".join(
            f"{hex6(f)} 配 {hex6(b)}（{r:.2f}:1 < {n}:1）"
            for f, b, n, r in sorted(bad, key=lambda x: x[3])[:6]
        )
        warns.append(
            f"{len(bad)} 组文字/背景对比度不达标（WCAG）：{sample}…"
            "正文须 ≥4.5:1、大字号/小字号次要文字须 ≥3.0:1；"
            "强调色锚点若 ≥3.5:1 且全篇 ≤3 处可人工确认"
        )
    if checker.skipped_gradient:
        warns.append(
            f"{checker.skipped_gradient} 处渐变背景未做对比度检查"
            "（渐变两端都需与文字保持足够反差）"
        )
    return warns


def aesthetic_checks(html):
    """审美层 WARNING：不阻断粘贴，但交付前应处理（修复或人工确认）。"""
    warnings = []
    checker = AestheticChecker()
    try:
        checker.feed(html)
    except Exception:
        return warnings

    # 1) 连续 ≥4 段纯文字（阅读墙，见 editorial-principles 节奏公式）
    run, walls = 0, 0
    for tag, style, depth in checker.blocks:
        if tag == "p" and depth == 2 and "background" not in style:
            run += 1
        else:
            run = 0
        if run >= 4:
            walls += 1
            run = 0
    if walls:
        warnings.append(
            f"检测到 {walls} 处连续 ≥4 段纯文字（阅读墙）；"
            "应回到原文按事实/判断/机制/例子/行动拆段，或用图片/引用/卡片做呼吸点"
        )

    # 2) 疑似 AI 默认渐变/高饱和色（与 anti-slop 的「默认紫蓝渐变」一致）
    low = html.lower()
    hits = sorted({h for h in AI_DEFAULT_COLORS if h in low})
    if hits:
        sample = "、".join(hits[:6])
        warnings.append(
            f"疑似 AI 默认渐变/高饱和色 {len(hits)} 处（{sample}…）；"
            "通常与「优雅低调」冲突，除非用户明确指定否则应换面色板/低饱和色"
        )

    # 3) font-size 超限（仅背景级水印数字例外）
    sizes = [int(m.group(1)) for m in FONT_SIZE.finditer(html)]
    over = [s for s in sizes if s > 24]
    if over:
        warnings.append(
            f"{len(over)} 处 font-size>24px（最大 {max(over)}px）；"
            "正文/标题必须 ≤24px，仅水印大数字（F3b/F3b叠，极浅色叠底）例外"
        )

    return warnings


def validate(html, name="<input>"):
    errors, warnings = [], []

    for rx, level, msg in FORBIDDEN:
        hits = len(rx.findall(html))
        if hits:
            (errors if level == "ERROR" else warnings).append(
                f"{msg}（命中 {hits} 处）")

    checker = LeafChecker()
    try:
        checker.feed(html)
    except Exception as e:  # 容错：解析失败不致命，只提示
        warnings.append(f"HTML 解析中断: {e}")

    has_cjk = bool(CJK.search(html))
    if has_cjk and checker.span_leaf_count == 0:
        errors.append("全文没有任何 <span leaf=\"\"> 包裹——"
                      "粘贴到公众号后样式会大面积丢失")
    elif checker.unwrapped:
        sample = "；".join(f"「{s}」(在 <{p}> 内)"
                           for s, p in checker.unwrapped[:5])
        warnings.append(
            f"{len(checker.unwrapped)} 处中文文本未被 <span leaf> 包裹，"
            f"样式可能丢失。例：{sample}")

    if checker.half_punct:
        sample = "；".join(f"「{s}」" for s in checker.half_punct[:5])
        warnings.append(
            f"{len(checker.half_punct)} 处正文疑似半角标点/英文引号，应改中文全角"
            f"（代码块内不计）。例：{sample}")

    warnings.extend(aesthetic_checks(html))
    warnings.extend(contrast_warnings(html))

    return errors, warnings, checker.span_leaf_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", help="HTML 文件路径")
    ap.add_argument("--stdin", action="store_true", help="从标准输入读取")
    args = ap.parse_args()

    if args.stdin or not args.file:
        html = sys.stdin.read()
        name = "<stdin>"
    else:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            html = f.read()
        name = args.file

    errors, warnings, leaf_n = validate(html, name)

    print(f"📋 公众号 HTML 合规校验: {name}")
    print(f"   span leaf 包裹: {leaf_n} 处")
    if errors:
        print(f"\n❌ ERROR ×{len(errors)}（必须修复，否则粘贴后失效）:")
        for e in errors:
            print(f"   • {e}")
    if warnings:
        print(f"\n⚠️  WARNING ×{len(warnings)}（建议检查）:")
        for w in warnings:
            print(f"   • {w}")
    if not errors and not warnings:
        print("\n✅ 完全合规，可直接粘贴到公众号编辑器")
    elif not errors:
        print("\n✅ 无致命问题，可粘贴（warning 请人工确认）")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
