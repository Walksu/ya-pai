#!/usr/bin/env python3
"""ya-pai 作者信息记忆（author-info）。

用户首次提供作者名 + 一句话简介后写入 ~/.ya-pai/author.json，
之后排版不再重复询问，直接沿用。存储位置在 skill 目录之外：
三处安装（.codex / .dsh / WorkBuddy）共享同一份，同步不覆盖。

用法:
    author_info.py get
    author_info.py set --name 张三 --bio "写点 AI 与产品"
    author_info.py path
"""

import argparse
import json
import os
import sys

DEFAULT_FILE = os.path.join(os.path.expanduser("~"), ".ya-pai", "author.json")


def load(path):
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(data, dict):
        return {}
    return data


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description="ya-pai 作者信息记忆")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("get", help="读取已保存的作者信息")
    sub.add_parser("path", help="显示存储路径")

    ap_set = sub.add_parser("set", help="保存/覆盖作者信息（--bio 可留空）")
    ap_set.add_argument("--name", required=True)
    ap_set.add_argument("--bio", default="")

    args = ap.parse_args()
    path = DEFAULT_FILE
    if args.cmd == "path":
        print(path)
        return 0
    if args.cmd == "get":
        data = load(path)
        if data.get("name"):
            print(f"name: {data['name']}")
            print(f"bio: {data.get('bio', '')}")
        else:
            print("（未保存作者信息）")
        return 0
    if args.cmd == "set":
        data = load(path)
        data["name"] = args.name
        data["bio"] = args.bio
        save(path, data)
        print(f"✓ 已保存作者信息：{args.name} / {args.bio or '（简介留空）'} → {path}")
        print("  之后排版将直接沿用，不再询问；要更换随时说一声。")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
