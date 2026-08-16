#!/usr/bin/env python3
"""发布态审计：发布到公众号之前跑一遍，把「发出去才后悔」的问题挡下来。

先跑 validate_gzh_html.py（平台红线 + 审美），再跑本脚本（发布前状态）：

    publish_audit.py <生成的正文.html>

检查项：
  ❌ 必须修复：占位符残留（{{作者名}} 等没替换）；本地图片 src（需上传素材库后替换）
  ⚠️  建议处理：文件体积 > 200KB（长文拆篇提示）
  ℹ️  提示：正文不含 H1（标题在公众号后台设置）；预览页是否已生成

退出码：1 = 有必须修复项；0 = 可以发布。
"""

import os
import re
import sys

PLACEHOLDER = re.compile(r"\{\{[^}]+\}\}")
IMG_SRC = re.compile(r'<img[^>]*\bsrc\s*=\s*"([^"]+)"', re.I)
IMG_ALT = re.compile(r'<img[^>]*\balt\s*=\s*"([^"]*)"', re.I)
REMOTE = ("http://", "https://", "//", "data:")


def main():
    if len(sys.argv) < 2:
        print("用法: publish_audit.py <生成的正文.html>")
        sys.exit(2)
    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"✗ 找不到文件: {path}")
        sys.exit(2)

    html = open(path, encoding="utf-8").read()
    must_fix = []
    suggestions = []
    infos = []

    # 1) 占位符残留
    ph = sorted(set(PLACEHOLDER.findall(html)))
    if ph:
        must_fix.append("占位符残留，发布后会把 {{…}} 原文显示出来：" + "、".join(ph[:6]))

    # 2) 本地图片路径
    local = [src for src in IMG_SRC.findall(html)
             if not src.startswith(REMOTE)]
    if local:
        sample = "；".join(local[:4])
        must_fix.append(
            f"{len(local)} 张本地图片未上传素材库（src 不是 http/data）：{sample}…"
        )

    # 3) alt 仍是占位「本地图片」
    alt_ph = [a for a in IMG_ALT.findall(html) if a in ("", "本地图片")]
    if alt_ph:
        infos.append(f"{len(alt_ph)} 张图 alt 仍是占位/为空（图注未补，仅提示）")

    # 4) 体积
    size = os.path.getsize(path)
    if size > 200 * 1024:
        suggestions.append(
            f"产物 {size // 1024}KB > 200KB，公众号编辑器可能卡顿，建议拆篇或压缩重复样式"
        )
    else:
        infos.append(f"产物体积 {size // 1024}KB（<200KB，正常）")

    # 5) 标题
    if "<h1" not in html.lower():
        infos.append("正文不含 H1（符合规范：标题在公众号后台设置，不在正文重复放）")

    # 6) 预览页
    preview = os.path.splitext(path)[0] + "_预览.html"
    if os.path.isfile(preview):
        infos.append(f"预览页已生成：{os.path.basename(preview)}")
    else:
        suggestions.append("预览页未生成——先跑 wrap_preview.py 再交付")

    print(f"📦 发布态审计: {path}\n")
    for item in must_fix:
        print(f"  ❌ {item}")
    for item in suggestions:
        print(f"  ⚠️  {item}")
    for item in infos:
        print(f"  ℹ️  {item}")

    if must_fix:
        print(f"\n❌ 有 {len(must_fix)} 项必须修复，发布前处理")
        sys.exit(1)
    print("\n✅ 可以发布（建议先把预览页发给作者人工看一眼）")
    sys.exit(0)


if __name__ == "__main__":
    main()
