# ?? Design & Motion Studio — Master Tool Reference
> 10 open-source repos (550K+ stars) to build a full visual production stack

---

## Quick Map

| # | Tool | Stars | Stage | Folder |
|---|------|-------|-------|--------|
| 1 | impeccable | 85K | Design Quality Control | Visual Storytelling\Scene Composition Rules |
| 2 | UI UX Pro Max | 139K | Design System Generation | Thumbnails & Titles |
| 3 | MCP for Blender | 32K | 3D Modeling + Scenes | Visual Storytelling\AI Image + Video Generation |
| 4 | img2threejs | 19K | Image ? 3D Web Animation | Visual Storytelling\AI Image + Video Generation |
| 5 | video-shotcraft | 13K | Promo Video Rendering | Editing & Packaging\Documentary Editing Templates |
| 6 | HyperFrames | 70K | HTML ? MP4 Agent Video | Editing & Packaging\Text Overlays & Motion Graphics |
| 7 | Penpot | 62K | Open-Source Figma + MCP | Thumbnails & Titles\Curiosity-Driven Thumbnails |
| 8 | Remotion | 67K | React-Based Video Engine | Editing & Packaging\Text Overlays & Motion Graphics |
| 9 | lemo-opuscar | 6K | 59 Cinematic Film Styles | Editing & Packaging\Color Grading Styles |
| 10 | diagram-design | 60K | Brand Diagrams as SVG/HTML | Visual Storytelling\Scene Composition Rules |

---

## ?? Stress-Test Priority (For Documentary Channels)

| Priority | Tool | Why |
|----------|------|-----|
| ?? 1st | **Remotion** | Videos in React — animated titles, intros, lower thirds, chapter cards |
| ?? 2nd | **HyperFrames** | Write HTML ? render MP4 — agent-native, /figma brand token pull |
| ?? 3rd | **Penpot** | Free Figma with MCP — agents can read your design files for thumbnails |
| 4th | **impeccable** | 62 rule-based checks — kills AI-slop in every visual before it ships |
| 5th | **lemo-opuscar** | 59 film styles in code — instant cinematic grade, no model needed |

---

## ?? Full Tool Breakdowns

---

### 1. impeccable (85K ?)
**GitHub:** https://github.com/pbakaus/impeccable
**Stage:** Design Quality Control — anti AI-slop enforcement

#### What It Does
62 rule-based checks that catch and fix design problems AI tools commonly produce:
- Spacing inconsistencies
- Misaligned type hierarchies
- Color contrast failures
- Layout ratio violations

#### Use for Documentary Channel
- Run every thumbnail through impeccable before publishing
- Check AI-generated scene images for quality before they go in the edit
- Enforce consistent visual standards across all channel art

#### Workflow
1. Generate thumbnail / graphic (FLUX.2, Penpot, etc.)
2. Run impeccable checks
3. Fix flagged issues
4. Publish clean, professional output

#### Notes
- Treat this as your **design QA gate** — nothing ships without passing it
- Store your custom rule configs in `Scene Composition Rules`

---

### 2. UI UX Pro Max (139K ?)
**GitHub:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
**Stage:** Full Design System Generation

#### What It Does
From a single project brief, generates a complete design system:
- Color palette
- Typography scale
- Component patterns
- Layout grid

#### Use for Documentary Channel
- Generate your **channel brand system** once — use forever
- Feed to HyperFrames and diagram-design for auto-branded video assets
- Consistent palette across thumbnails, end screens, community posts

#### Workflow
1. Write channel brief: tone, niche, target audience, mood
2. Tool generates: palette + type + patterns
3. Export tokens ? feed into HyperFrames /figma skill
4. All future assets auto-branded

#### Prompt Template
> "Design system for a faceless documentary YouTube channel. Tone: authoritative, cinematic, investigative. Primary audience: 25–45, curious adults. Style: dark mode, high contrast, editorial."

---

### 3. MCP for Blender (32K ?)
**GitHub:** https://github.com/ahujasid/blender-mcp
**Stage:** 3D Scene Modeling via LLM Prompts

#### What It Does
Connect Blender to any LLM (Claude, GPT, Gemini). Prompt-driven:
- 3D object modeling
- Scene composition
- Lighting setup
- Animation

#### Use for Documentary Channel
- Generate **custom 3D scene art** for documentaries (instead of stock footage)
- Recreate historical environments, crime scenes, or space scenes from text
- Build animated logo intros and end screens

#### Prompt Examples
- `"Create a 1940s war room interior with dim lighting and a large map table"`
- `"Model a dark forest clearing at night with volumetric fog"`
- `"Build a simple animated logo reveal for [Channel Name]"`

#### Notes
- Requires Blender + LLM API
- Learning curve — start with simple scene compositions
- Huge upside for unique B-roll no one else has

---

### 4. img2threejs (19K ?)
**GitHub:** https://github.com/img2threejs/img2threejs
**Stage:** Image ? Animation-Ready 3D Web Object

#### What It Does
Give it a reference image ? get back a Three.js code object:
- Fully code-based (no video model)
- Animation-ready from the start
- Runs in browser / embeds in web

#### Use for Documentary Channel
- Convert key visual assets into animated web components
- Embed interactive 3D elements in channel website or Patreon
- Generate animated thumbnail elements

#### Workflow
1. Input: reference image of key documentary element
2. Tool outputs: Three.js code
3. Animate: add rotation, hover effects, timeline scrub
4. Export as video clip or use in web embed

---

### 5. video-shotcraft (13K ?)
**GitHub:** https://github.com/Vincentwei1021/video-shotcraft
**Stage:** Promo Video Rendering

#### What It Does
- Captures screenshots of your real pages/content
- Picks from 150+ shot recipes (angles, transitions, compositions)
- Renders a finished promo video using Remotion

#### Use for Documentary Channel
- Auto-generate **channel trailers** from your content pages
- Create episode preview clips for social media
- Build promo reels for Patreon / membership pitches

#### 150 Shot Recipe Categories
- Hero reveals
- Split-screen comparisons
- Zoom-in focus pulls
- Text-driven transitions
- Mockup device frames

---

### 6. HyperFrames (70K ?)
**GitHub:** https://github.com/heygen-com/hyperframes
**Stage:** HTML ? MP4 Agent-Native Video Engine

#### What It Does
Write HTML ? render as MP4 video. Built natively for AI agents:
- /figma skill pulls brand tokens directly from your design files
- Agent-driven video composition
- Used by HeyGen for AI video production

#### Use for Documentary Channel
- **Animated title cards** and chapter headers
- Auto-branded intro/outro sequences pulled from your Penpot/Figma
- AI agent generates the HTML ? renders the video ? no manual editing

#### /figma Skill Workflow
1. Set up brand in Penpot or Figma
2. /figma skill extracts: colors, fonts, component styles
3. HyperFrames uses tokens to auto-brand all video assets
4. Every new video is on-brand automatically

#### Notes
- Pairs perfectly with Remotion for full video pipeline
- Store your HTML templates in `Text Overlays & Motion Graphics`

---

### 7. Penpot (62K ?)
**GitHub:** https://github.com/penpot/penpot
**Stage:** Open-Source Figma Alternative + MCP Server

#### What It Does
Full design tool with an MCP server so AI agents can:
- Read your design files programmatically
- Extract brand tokens, colors, and components
- Feed design data into HyperFrames, diagram-design, etc.

#### Use for Documentary Channel
- **Thumbnail design hub** — build templates, reuse for every episode
- MCP server lets your agent auto-pull brand colors into video assets
- Host locally or self-host — no subscription fees

#### Workflow
1. Build thumbnail templates in Penpot
2. Connect MCP server to your AI agent
3. Agent reads brand tokens ? feeds into HyperFrames
4. Every video asset is auto-branded from source of truth

#### Notes
- Self-hosted = full control, no data sent to third parties
- Best free alternative to Figma for teams/solo creators

---

### 8. Remotion (67K ?)
**GitHub:** https://github.com/remotion-dev/remotion
**Stage:** React-Based Programmatic Video Engine

#### What It Does
Create videos using React code:
- Animated intros and outros
- Dynamic lower thirds and title cards
- Data-driven motion graphics
- Official skills repo teaches agents how to use it

#### Use for Documentary Channel
- **Animated chapter cards** generated from script outline
- Dynamic title sequences with episode metadata
- Lower thirds with source citations
- Stats and data visualizations animated automatically

#### Component Ideas for Docs
```jsx
// Chapter card component
<ChapterCard number={3} title="The Cover-Up" timestamp="14:23" />

// Lower third
<LowerThird name="Dr. Sarah Chen" title="Forensic Expert, MIT" />

// Stat reveal
<StatReveal value="2.3M" label="People affected" />
```

#### Notes
- **#1 stress-test recommendation** for documentary channels
- Huge ecosystem, great docs, agent skill repo is excellent
- Output: MP4, GIF, image sequences

---

### 9. lemo-opuscar (6K ?)
**GitHub:** https://github.com/lemomo-ai/lemo-opuscar
**Stage:** Cinematic Film Style Engine

#### What It Does
59 distinct film styles rendered entirely in code — no video model required:
- Film grain and color science simulations
- Noir, neo-realist, new wave, modern cinematic
- Apply to any video or image sequence

#### Use for Documentary Channel
- Apply **cinematic grades** to AI-generated or stock footage
- Instant visual identity — pick 1–2 styles and stick with them
- No licensing, no GPU-heavy video model needed

#### 59 Style Categories (Examples)
| Style | Best For |
|-------|----------|
| Noir Classic | Crime / Investigation docs |
| Cold Blue | Science / Tech docs |
| Warm Amber | History / Culture docs |
| Desaturated Green | Military / Conspiracy docs |
| High Contrast B&W | Archive-style docs |
| Golden Hour | Nature / Geography docs |

#### Notes
- Pick your channel's **signature 2–3 styles** and document them here
- Consistency = instant brand recognition

---

### 10. diagram-design (60K ?)
**GitHub:** https://github.com/cathrynlavery/diagram-design
**Stage:** Brand-Aware Diagram Generation (HTML + SVG)

#### What It Does
Agent skill that outputs diagrams as a single HTML+SVG file:
- Auto-applies your brand colors and fonts
- No design tool required — pure code output
- Works with any agent workflow

#### Use for Documentary Channel
- **Timeline diagrams** for historical documentaries
- **Org charts** showing power structures / conspiracies
- **Flow diagrams** for complex processes or events
- **Map overlays** as static SVG infographics

#### Prompt Template
> "Create a timeline diagram of [EVENT] from [YEAR] to [YEAR]. Use dark background, white text, red accent color. Include: [5 KEY EVENTS]. Output as single HTML+SVG file."

#### Notes
- Feed your Penpot/UI UX Pro Max brand tokens in for auto-branding
- Store diagram templates in `Scene Composition Rules`

---

## ??? Full Visual Production Stack

```
BRAND FOUNDATION
    ¦
    +--? [UI UX Pro Max] ----------? Design System (palette, type, patterns)
    +--? [Penpot] -----------------? Thumbnail Templates + Brand File
              ¦
              +-- MCP ? [HyperFrames] --? Auto-Branded Video Assets
                         ¦
                         +--? [Remotion] ------? Motion Graphics + Title Cards
                                    ¦
                                    +--? [video-shotcraft] -? Promo Renders

VISUAL ASSETS
    ¦
    +--? [MCP for Blender] --------? Custom 3D Scenes + B-Roll
    +--? [img2threejs] ------------? Animated 3D Web Objects
    +--? [diagram-design] ---------? Infographics + Timelines

QUALITY & STYLE
    ¦
    +--? [impeccable] -------------? Design QA (62-rule checker)
    +--? [lemo-opuscar] -----------? Cinematic Film Style Grades
```

---

*Last updated: October 2026 | 550K+ combined stars*
