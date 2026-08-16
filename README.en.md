# ya-pai · Combinatorial WeChat Article Layout Skill

> Turn a Markdown article into a **single self-contained HTML snippet that pastes cleanly into the WeChat Official Account editor** — with a genuinely different "first impression" per style, not just a color swap.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agents](https://img.shields.io/badge/Codex%20·%20Claude%20Code%20·%20Cursor-supported-8b5cf6.svg)](#-quick-start)
[![Skeletons](https://img.shields.io/badge/layouts-10-059669)](tokens/layouts.md)
[![Presets](https://img.shields.io/badge/presets-12-3b82f6)](tokens/presets.md)
[![Gallery](https://img.shields.io/badge/gallery-11-9a5f32)](examples/gallery/index.html)

**ya-pai** is an AI-agent skill for WeChat article layout. You write Markdown; it renders a fully inline-styled HTML snippet that survives pasting into the WeChat editor — automatic chapter numbering, keyword underlines, quotes, TOC, code blocks, author signature — with deterministic validation scripts that enforce the platform's quirks.

## ✨ Highlights

- **9 combinable dimensions**: aesthetic × palette × typography × layout skeleton × density × decoration × background × feature modules × heading style. Every dimension is an independent atom.
- **10 layout skeletons**: single column / guided / timeline / cards / poster / sidebar / lecture notes / **newspaper** / **letter** / **terminal** — each with its own opening, section entry, quote & list treatment, and closing.
- **12 one-click presets** and an **11-piece gallery**: the same short article rendered 11 different ways, so you choose by looking, not by parameter.
- **Preference-first Q&A flow**: gallery → confirm recommendation → single-dimension tweaks → author signature. The agent recommends but never chooses for you; both preset options and free-form input are open.
- **Deterministic quality gates**: `validate_gzh_html.py` (platform red lines + WCAG contrast + aesthetic self-check) and `publish_audit.py` (placeholders / local images / size).
- **Zero format loss**: pure `<section>` output, all styles inline, every text node wrapped in `<span leaf="">`.

## 🚀 Quick Start

### Via npx (recommended)

```bash
npx skills add https://github.com/walksu/ya-pai
```

### Manual install (Codex)

```bash
git clone https://github.com/walksu/ya-pai.git "$HOME/.codex/skills/ya-pai"
```

### Manual install (Claude Code / Cursor, etc.)

```bash
git clone https://github.com/walksu/ya-pai.git "$HOME/.claude/skills/ya-pai"
```

Works with any agent runtime that loads `SKILL.md` (Codex, Claude Code, Cursor, OpenCode, …).

## 📝 Usage

1. Tell the agent "**use $ya-pai to layout this article**" and pass a `.md` path (or paste Markdown).
2. The agent opens the **gallery** (`examples/gallery/index.html`) for you to pick a first impression — or recommends a full combination based on the article's *topic and tone* (a lighthearted tech article should get a lighthearted layout).
3. Fine-tune one dimension at a time ("rounded gradient headings", "poster layout", "yellow-white-blue palette"), or just say "follow recommendations / auto".
4. Provide the **author name + one-line bio** (required for the closing signature card).
5. HTML is generated, validated, and audited; open the preview page, click "复制到公众号" (copy to WeChat), and paste into the editor.

## 🖼️ Gallery

Interactive gallery with copy buttons: [examples/gallery/index.html](examples/gallery/index.html).

| g01 bookish | g02 tech-doc | g03 cool-report | g04 magazine |
|---|---|---|---|
| ![g01](assets/screenshots/g01.png) | ![g02](assets/screenshots/g02.png) | ![g03](assets/screenshots/g03.png) | ![g04](assets/screenshots/g04.png) |

| g05 poster | g06 minimal | g07 lecture | g08 timeline |
|---|---|---|---|
| ![g05](assets/screenshots/g05.png) | ![g06](assets/screenshots/g06.png) | ![g07](assets/screenshots/g07.png) | ![g08](assets/screenshots/g08.png) |

| g09 newspaper | g10 letter | g11 terminal |
|---|---|---|
| ![g09](assets/screenshots/g09.png) | ![g10](assets/screenshots/g10.png) | ![g11](assets/screenshots/g11.png) |

## 📁 Repository Layout

```
ya-pai/
├── SKILL.md                     # Skill definition + main workflow (agent entry)
├── README.md / README.en.md     # Docs (CN / EN)
├── LICENSE                      # MIT
├── agents/openai.yaml           # Agent UI metadata
├── references/                  # Rules the agent reads on demand
├── tokens/                      # Combinable design atoms + presets
├── templates/                   # HTML/CSS skeletons
├── examples/gallery/            # 11-piece gallery with interactive previews
├── scripts/                     # validate / wrap-preview / publish-audit
└── assets/                      # Preview template + gallery screenshots
```

## 🛡️ Quality Gates

- **Validation**: `scripts/validate_gzh_html.py <output.html>` — flags everything the WeChat editor strips or breaks (`<style>`, `<div>`, `class/id`, `position`, `grid`, CSS variables, external fonts…), checks `<span leaf="">` wrapping, and runs WCAG contrast + aesthetic checks.
- **Preview**: `scripts/wrap_preview.py <body.html>` — wraps the body in a preview page with a "copy to WeChat" button.
- **Publish audit**: `scripts/publish_audit.py <body.html>` — placeholders, local images, size, missing preview.

## 📄 License

[MIT](LICENSE) © 2026 Walksu
