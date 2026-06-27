# MPV + yt-dlp: Distraction-Free YouTube & Media Viewing

**Source:** `07-mpv-ytdlp.md` · **Phase 1** · Cleaned & annotated

## Overview

A lightweight, open-source combo for watching YouTube and online video without ads, sidebars, comments, or algorithmic rabbit holes. MPV is the minimal player, yt-dlp fetches the video stream — together they form a "focus mode" for video consumption.

## Core Content

### 1. The Elevator Pitch

Drag a YouTube link into a clean player window. No ads, no "Up Next," no comment section, no algorithm. You watch what you intended to watch, then stop. That's it. Free, cross-platform, and light enough your laptop battery won't notice.

### 2. Why This Matters

- **Attention sovereignty:** YouTube's business model is designed to keep you clicking. MPV strips away the engagement traps.
- **Compound focus:** Distraction-free viewing = deeper comprehension from tutorials, cleaner analysis as a creator.
- **"Aha!" moment:** Dragging a link into a tiny player window and realizing there's no login, no pre-roll, no subscribe pop-up.

### 3. Reality Check

- **Overrated when:** You enjoy YouTube's discovery engine — MPV kills serendipitous recommendations. It's a viewer, not an explorer.
- **Opportunity cost:** A browser extension like Enhancer for YouTube or DF Tube achieves ~70% of the benefit with 5% of the effort.
- **Not for:** CLI-phobes, people who rely on timestamp comments, or users who need subtitles (MPV supports them but it's clunkier).

### 4. Core Concepts

| Component | What It Does | Analogy |
|-----------|-------------|---------|
| **MPV** | Minimalist media player — plays anything, weighs almost nothing | The "notes app" of video players |
| **yt-dlp** | Fetches video streams from YouTube (and 1000+ sites) | Invisible delivery driver |
| **Drag-and-drop** | Grab URL, drop on MPV — zero friction | Tossing clothes in a hamper |
| **No algorithm** | No sidebar, no recommendations, no dopamine hijack | Reading with the TV off |
| **Local + online** | One player for your FLAC collection and Python tutorials | Universal remote that works |

### 5. AI Leverage

**Use AI for:** Config file generation (`mpv.conf`), yt-dlp command crafting (download flags), troubleshooting when yt-dlp breaks.

**Don't outsource:** Your viewing habits (self-awareness required), the initial setup friction (building confidence).

**One AI workflow:** *"Give me the exact terminal commands to install MPV and yt-dlp on [my OS]. Then write a config that makes MPV always start in fullscreen, skip sponsor segments, and use hardware decoding."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Install both, drag a YouTube link into MPV. Experience the silence. |
| **Foundation** | 1 hr | 3 principles: MPV plays, yt-dlp fetches; keyboard shortcuts > mouse (`f` fullscreen, `space` pause, `]` speed up); `mpv.conf` is where the magic lives |
| **Application** | 1–2 hr | Build a "Watch Later" workflow: text file of URLs + one-line script to feed them sequentially |
| **Deep Dive** | Optional | Lua scripts (sponsorblock, auto-save position), advanced yt-dlp flags (format selection, metadata embedding) |

### 7. Go/No-Go

| Situation | Verdict |
|-----------|---------|
| Distraction-free learning from tutorials | 🟢 **Learn this NOW** |
| Discovering new content > watching specific videos | ⏳ Stick to YouTube Premium + extensions |
| Zero CLI tolerance | ⚠️ Use Invidious/Piped in browser instead |
| Frequent offline video downloads | 🟢 **Learn this NOW** — yt-dlp is the gold standard |
| Mobile/tablet primary viewing | 🔴 Skip — MPV is desktop-first. Use NewPipe on Android |

## Key Takeaways

1. The 20% effort — install both, drag a link — gives 80% of the reward: your attention back.
2. MPV and yt-dlp are separate tools with a clear division of labor: one plays, one fetches.
3. Keyboard shortcuts are the real interface: `f` (fullscreen), `space` (pause), `]` (speed up), `q` (quit).
4. This combo is a power-user's antidote to attention capitalism — not for everyone, but transformative if YouTube feels like a casino designed to take your time.
