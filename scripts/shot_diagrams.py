#!/usr/bin/env python3
"""Extract each diagram card from diagram-demo.html and screenshot them individually."""
import re
import os
import sys
import subprocess
import tempfile

DEMO = r"D:\万寰\ya-pai-repo\Walksu-ya-pai-0fd7632\examples\gallery\diagram-demo.html"
OUT_DIR = r"D:\万寰\ya-pai-repo\Walksu-ya-pai-0fd7632\assets\screenshots\diagrams"
CHROME = r"C:\Users\36523\AppData\Local\ms-playwright\chromium-1234\chrome-win64\chrome.exe"
TMP = tempfile.mkdtemp(prefix="diagshot_")

html = open(DEMO, encoding="utf-8").read()

# extract all demo cards: <div class="demo">...</div> blocks
cards = re.findall(r'<div class="demo">(.*?)</div>\s*</div>', html, re.S)
# fallback pattern if above fails: match from '<div class="demo">' to the next '<div class="demo">' or '<div class="group">'
if not cards:
    parts = re.split(r'<div class="demo">', html)[1:]
    for p in parts:
        cards.append(p.split('</div></div>')[0] + '</div>')

# extract titles
titles = re.findall(r'<h3>(.*?)</h3>', html)

os.makedirs(OUT_DIR, exist_ok=True)

print(f"Found {len(cards)} cards, {len(titles)} titles")
for i, card in enumerate(cards):
    title = titles[i] if i < len(titles) else f"F14-{i}"
    # sanitize filename: keep ascii + digits
    name = re.sub(r'[^\w\-]+', '', title.replace(' ', '-'))
    if not name:
        name = f"diagram-{i}"
    page = os.path.join(TMP, f"card-{i}.html")
    with open(page, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<style>
  body{{margin:0;background:#fff;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;}}
  .wrap{{width:400px;min-height:240px;display:flex;align-items:center;justify-content:center;box-sizing:border-box;padding:24px 20px;background:#fff;}}
</style></head>
<body><div class="wrap">{card}</div></body></html>""")
    out = os.path.join(OUT_DIR, f"{name}.png")
    r = subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--window-size=400,400", "--virtual-time-budget=3000",
                        f"--screenshot={out}", f"file:///{page}"],
                       capture_output=True, text=True)
    if os.path.exists(out):
        print(f"OK  {name}.png  ({os.path.getsize(out)} bytes)")
    else:
        print(f"FAIL {name}.png  {r.stderr[-200:]}")

print("DONE", TMP)
