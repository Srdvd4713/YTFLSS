# THE WALL AT ASHFORD — Adaptation & Replication Guide
**Source channels:** @IFOLOGYFILMS · @Final_Sight · @IfverseTales
**Original prompt by:** @OnlySainted (X) · CC BY 4.0
**Raw prompt file:** WALL AT ASHFORD Master Prompt.txt (same folder)

---

## What This Is

A complete code-only 6-part animated YouTube Shorts series.
No stock footage. No video models. No actors.
Pure SVG + HTML + JS rendered to MP4 via Playwright + ffmpeg.

**The channels using this:** @IFOLOGYFILMS, @Final_Sight, @IfverseTales

---

## What You Need to Run It

### Required Software
| Tool | Purpose | Install |
|------|---------|---------|
| Node.js 18+ | Runtime | nodejs.org |
| Python 3.10+ | Voice pipeline (voice.py) | python.org |
| Playwright | Headless Chromium renderer | `npm i -D playwright` + `npx playwright install chromium` |
| ffmpeg | Frame assembly + audio mux | ffmpeg.org (or ffmpeg-skill) |
| Kokoro-82M ONNX | Local TTS voice engine | github.com/hexgrad/kokoro |
| espeak-ng | Phoneme timing for captions | espeak.sourceforge.net |

### Required Fonts
- **Oswald 700** (Google Fonts) — all captions and rule cards
- **Monospace** (system) — HUD overlay

### Required Python Packages
```
pip install kokoro-onnx espeak-ng numpy scipy soundfile
```

### Optional (Higher Quality)
| Tool | Replaces | Quality |
|------|---------|---------|
| ElevenLabs | Kokoro TTS | ?? Better voice |
| GPT-4o | Claude (character sheets) | Comparable |
| CapCut | Manual SFX timing | Easier but manual |

---

## File Structure Claude Needs to Build

```
project/
+-- parts/
¦   +-- part1.json    ? shot list (Claude builds this from prompt)
¦   +-- part2.json
¦   +-- part3.json
¦   +-- part4.json
¦   +-- part5.json
¦   +-- part6.json
+-- render/
¦   +-- index.html    ? SVG art engine (Claude builds this)
+-- voice.py          ? TTS + timeline pipeline (Claude builds this)
+-- render.js         ? Playwright frame capture (Claude builds this)
+-- output/
    +-- part1.mp4
    +-- part2.mp4
    ...
```

---

## How to Run (Step-by-Step)

```bash
# 1. Paste the master prompt into Claude Code
# 2. Claude builds all the files above
# 3. Generate voice + timeline
python voice.py --part 1

# 4. Render frames + assemble video
node render.js --part 1

# 5. Repeat for parts 2–6
# 6. Output: part1.mp4 through part6.mp4
```

---

## What Might Need Fixing (Known Gaps)

### 1. Kokoro Voice Availability
Some voices in the prompt (am_adam, bm_george, af_sky) may not be in your Kokoro build.
**Fix:** Check available voices with `kokoro --list-voices`. Substitute closest match or use ElevenLabs.

### 2. espeak-ng on Windows
espeak-ng can be tricky on Windows.
**Fix:** Use WSL2 (Ubuntu) or run the voice pipeline in Docker.
```bash
docker run -it python:3.10 bash
pip install kokoro-onnx espeak-ng
```

### 3. SFX Synthesis
The prompt says "synthesize or use CC0 samples." Claude will generate basic SFX in code.
Quality varies. **Fix:** Replace generated SFX with real CC0 samples from:
- freesound.org
- mixkit.co/free-sound-effects
- zapsplat.com

### 4. Playwright Memory on Long Renders
1080×1920 at 30fps × 80 seconds = 2,400 frames per part.
**Fix:** Increase Playwright timeout and memory:
```javascript
const browser = await chromium.launch({
  args: ['--disable-dev-shm-usage', '--no-sandbox']
});
```

### 5. Motion Blur Sub-frames
The prompt specifies 3 sub-frame motion blur on fast shots.
**Fix:** If Claude skips this, add manually in ffmpeg:
```
-vf minterpolate=fps=90,tmix=frames=3,fps=30
```

### 6. Audio Loudnorm Target
The prompt targets -14 LUFS (YouTube standard).
**Fix:** If not auto-applied, add in ffmpeg post-render:
```
ffmpeg -i part1_raw.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 part1.mp4
```

---

## How to Adapt for a New Story (Documentary Version)

This is the replication formula. Use this structure for any new animated series.

### Story Requirements Checklist
- [ ] **Unreliable narrator** — the protagonist believes something wrong
- [ ] **Twist in Part 5** — everything recontextualised
- [ ] **12 planted clues** — must work on rewatch (Part 5 replays them all)
- [ ] **Emotional core** — a relationship (siblings, parent/child, friends)
- [ ] **Rules system** — 5-6 rules shown as cards, one broken in finale
- [ ] **HUD tracker** — a live stat that changes and creates tension
- [ ] **Sequel hook** — ends with a new location doing the same thing

### Documentary-Adapted Niches That Work
| Niche | Twist Concept | Example |
|-------|--------------|---------|
| True Crime | The "criminal" was protecting someone | Cold case reveal |
| History | The "heroes" were the real villains | Colonial rewrite |
| Conspiracy | The conspiracy was actually true | Government cover-up |
| Science | The "cure" was the disease | Medical experiment |
| Cult | The leader believed they were saving people | Tragedy not evil |
| War | The "enemy" was fighting the same enemy | Friendly fire truth |

### Prompt Variables to Replace
```
[TOWN NAME]        ? Your setting
[POPULATION]       ? Your group size
[THE THREAT]       ? What they fear
[THE TRUTH]        ? What it really is
[THE NARRATOR]     ? Your protagonist (age, role, look)
[THE RULES]        ? 5 rules they follow wrongly
[THE CLUES]        ? 12 misread details ? real meaning
[THE RELATIONSHIP] ? Emotional core (who do they protect?)
[THE SEQUEL STING] ? New location, same mistake
```

### New Story Template Prompt for Claude
```
You are building a 6-part animated YouTube Shorts series using the same
engine and format as "The Wall at Ashford" by @OnlySainted.

STORY BRIEF:
- Setting: [YOUR SETTING]
- Narrator: [NAME, AGE, ROLE]
- The fear: [WHAT THEY THINK IS HAPPENING]
- The truth: [WHAT IS ACTUALLY HAPPENING]
- Emotional core: [THE RELATIONSHIP]
- Rules: [5 RULES, last one broken in finale]
- Clues (12): [LIST WHAT IS MISREAD AND WHAT IT REALLY IS]
- Twist timing: Part 5
- Sequel hook: [NEW LOCATION, SAME MISTAKE]

Use the same technical spec as The Wall at Ashford:
- 1080×1920, 30fps, H.264 MP4, AAC audio
- SVG drawn in code (no stock assets)
- Kokoro-82M TTS (or ElevenLabs)
- Playwright + ffmpeg render pipeline
- Survival HUD tracker
- 3D Rule Cards (lime metal, spring-physics flip)
- Clue replay split-cards in Part 5
- -14 LUFS mastered audio

Build all 6 part JSON shot lists, the SVG art engine, voice.py, and render.js.
```

---

## 12-Clue System (The Core of What Makes It Viral)

The reason these videos get mass rewatches is the **12-clue structure**.
Every clue must:
1. Feel completely normal in context (Parts 1–4)
2. Be obviously meaningful in retrospect (Part 5 reveals)
3. Be planted in the first 2 parts

### Clue Planting Framework
| Clue | Planted In | Revealed In | Why It Works |
|------|-----------|-------------|-------------|
| Gray water | Part 1 | Part 5 | Feels like world-building |
| They always come in pairs | Part 1 | Part 5 | Feels like threat behaviour |
| Scout's bandage | Part 4 | Part 5 | Feels like mystery |
| Toby's drawings | Part 4 | Part 5 | Feels like trauma |
| The voice at 9PM | Part 4 | Part 5 | Feels like horror |

**Rule:** Plant clues EARLY. Reveal them LATE. The audience should feel smart, not cheated.

---

## HUD System Design for New Stories

The HUD is what creates real-time tension. Design yours around:
- **A countdown** (time, resources, something running out)
- **A number that drops** (survivors, days, supplies)
- **A secret counter** (things hidden, lies told)
- **A rewrite in Part 5** (old label ? truth label, same as SURVIVORS ? PATIENTS)

---

## Channel Strategy for This Format

| Upload | Content |
|--------|---------|
| Day 1 | Part 1 (the hook — ends on a mystery) |
| Day 2 | Part 2 (escalation — ends on a choice) |
| Day 3 | Part 3 (twist deepens — ends on a question) |
| Day 4 | Part 4 (everything accelerates — ends on cliffhanger) |
| Day 5 | Part 5 (THE TWIST — ends with "count the clues") |
| Day 6 | Part 6 (resolution + sequel hook) |
| Day 7 | "Did you catch all 12 clues?" compilation |

**Comments strategy:** Each end card asks a specific question (TELL / HIDE, WHO IS BITTEN, etc.) — this drives engagement that YouTube's algorithm reads as retention signals.

---

## Cost Breakdown (Replication)

| Item | Cost |
|------|------|
| Claude Code (1 month) | ~$20 |
| Kokoro TTS | Free (local) |
| ElevenLabs (upgrade) | $5–$22/mo |
| Playwright + Node | Free |
| ffmpeg | Free |
| SFX sources | Free (CC0) |
| **Total per series** | **~$20–$42** |

---

*Source: @OnlySainted (X) · Channels: @IFOLOGYFILMS @Final_Sight @IfverseTales*
*Saved: October 2026*
