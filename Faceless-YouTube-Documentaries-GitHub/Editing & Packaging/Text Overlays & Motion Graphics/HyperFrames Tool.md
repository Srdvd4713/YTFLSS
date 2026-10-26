# HyperFrames (70K ?)
**GitHub:** https://github.com/heygen-com/hyperframes
**Stage:** HTML ? MP4 Agent-Native Video Engine

## What It Does
Write HTML ? render as a finished MP4 video.
Built specifically for AI agents with:
- /figma skill: pulls brand tokens from Figma/Penpot files
- Programmatic video composition
- Agent-driven pipeline (no manual editing)

## Use for Documentary Channel
- **Animated intro/outro** — write HTML, render video
- **Title cards** and chapter headers, auto-branded
- **Quote overlays** with animated typography
- **Source citation lower thirds**

## /figma Skill Setup
1. Build brand in Penpot (open-source Figma)
2. Export design tokens (colors, fonts, spacing)
3. Run: `/figma pull [your-file-url]`
4. HyperFrames automatically applies brand to all video assets

## HTML ? Video Template Examples

### Documentary Intro Card
```html
<div class="intro-card dark-bg">
  <h1 class="doc-title">[EPISODE TITLE]</h1>
  <p class="subtitle">A [CHANNEL NAME] Investigation</p>
  <div class="progress-bar animate-in"></div>
</div>
```

### Source Citation Lower Third
```html
<div class="lower-third slide-up">
  <span class="source-name">Source: [Name]</span>
  <span class="source-detail">[Title / Date]</span>
</div>
```

## Notes
- Store your HTML templates in this folder
- Every template is reusable across all episodes
- Pair with Remotion for full motion pipeline
