#!/usr/bin/env python3
"""ya-pai 用户自定义预设管理（my-presets）。

用户在第 3 步最终确认时勾选「确认并保存为我的预设」，Agent 用本脚本把当前
九维度组合快照写入 ~/.ya-pai/presets.json（Windows: %USERPROFILE%\.ya-pai\presets.json）。

存储位置刻意放在 skill 目录之外：
- .codex / .dsh / WorkBuddy 三处安装共享同一份用户预设；
- skill 安装同步（/MIR）不会覆盖用户预设。

用法:
    user_presets.py list
    user_presets.py path
    user_presets.py add --name 我的墨绿窄读 --aesthetic 人文书卷 --palette 墨绿 \
        --font "中文友好衬线" --layout "L1 单栏流（窄）" --density 松 \
        --decoration 细线 --background 纯色 --features "章节编号 + 结尾签名" \
        --heading F3e --note "书评/随笔专用"
    user_presets.py delete <id|name>
"""

import argparse
import json
import os
import sys
from datetime import date

DEFAULT_DIR = os.path.join(os.path.expanduser("~"), ".ya-pai")
DEFAULT_FILE = os.path.join(DEFAULT_DIR, "presets.json")

DIMS = ["aesthetic", "palette", "font", "layout", "density",
        "decoration", "background", "features", "heading"]


def load(path):
    if not os.path.isfile(path):
        return {"presets": []}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        print(f"✗ 预设文件损坏或不可读: {path}（备份后删除重建即可）", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data, dict) or not isinstance(data.get("presets"), list):
        data = {"presets": []}
    return data


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def cmd_list(path):
    data = load(path)
    presets = data["presets"]
    if not presets:
        print("（暂无用户预设。在最终确认时选「确认并保存为我的预设」即可创建。）")
        return 0
    print(f"共 {len(presets)} 个用户预设（{path}）：")
    for p in presets:
        dims = p.get("dims", {})
        summary = " × ".join(str(dims.get(k, "?")) for k in DIMS if dims.get(k))
        note = f"（{p.get('note', '')}）" if p.get("note") else ""
        print(f"- [{p.get('id', '?')}] {p.get('name', '未命名')}：{summary}{note}")
    return 0


def cmd_add(path, args):
    data = load(path)
    presets = data["presets"]
    name = args.name or f"我的预设 {len(presets) + 1}"
    for p in presets:
        if p["name"] == name:
            print(f"✗ 已存在同名预设「{name}」；先 delete 旧的再新增，或用 --name 换名字。",
                  file=sys.stderr)
            return 1
    dims = {k: getattr(args, k, "") for k in DIMS}
    missing = [k for k in DIMS if not dims[k]]
    if missing:
        print(f"✗ 缺少维度参数: {', '.join(missing)}"
              "（九维度最好都填；Agent 应先用已确认的推荐值补齐再保存）", file=sys.stderr)
        return 1
    pid = f"p{date.today().strftime('%Y%m%d')}-{len(presets) + 1:03d}"
    entry = {"id": pid, "name": name, "created": date.today().isoformat(),
             "dims": dims, "note": args.note or ""}
    presets.append(entry)
    save(path, data)
    print(f"✓ 已保存用户预设「{name}」（{pid}）→ {path}")
    print(f"  下次排版直接说「用我的预设 {name}」即可。")
    return 0


def cmd_delete(path, target):
    data = load(path)
    presets = data["presets"]
    hit = [p for p in presets if p["id"] == target or p["name"] == target]
    if not hit:
        print(f"✗ 找不到预设「{target}」。可用 list 查看已有预设。", file=sys.stderr)
        return 1
    if len(hit) > 1:
        print(f"✗ 「{target}」匹配多个预设，请用精确 id 删除。", file=sys.stderr)
        return 1
    p = hit[0]
    presets.remove(p)
    save(path, data)
    print(f"✓ 已删除用户预设「{p['name']}」（{p['id']}）。")
    return 0


def main():
    ap = argparse.ArgumentParser(description="ya-pai 用户自定义预设管理")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="列出全部用户预设")
    sub.add_parser("path", help="显示预设文件路径")

    ap_add = sub.add_parser("add", help="新增一个用户预设")
    ap_add.add_argument("--name", default="")
    for k in DIMS:
        ap_add.add_argument(f"--{k}", default="")
    ap_add.add_argument("--note", default="")

    ap_del = sub.add_parser("delete", help="删除用户预设（按 id 或名称）")
    ap_del.add_argument("target")

    args = ap.parse_args()
    path = DEFAULT_FILE
    if args.cmd == "path":
        print(path)
        return 0
    if args.cmd == "list":
        return cmd_list(path)
    if args.cmd == "add":
        return cmd_add(path, args)
    if args.cmd == "delete":
        return cmd_delete(path, args.target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
