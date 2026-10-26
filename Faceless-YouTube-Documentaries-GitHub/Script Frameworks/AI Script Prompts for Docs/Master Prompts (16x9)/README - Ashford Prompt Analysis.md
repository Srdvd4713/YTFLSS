# Master Prompts (16:9): analysis of the Ashford model + 4 adaptations
*Model: `../WALL AT ASHFORD Master Prompt.md` (by @OnlySainted, CC BY 4.0). Each file in this folder is a standalone master prompt: paste the whole file into Claude Code inside an empty folder and it builds and renders the video(s).*

## Why the Ashford prompt works
| # | Section | What it does | Why it matters for an agent |
|---|---|---|---|
| 0 | **Deliverable spec** | Exact resolution, fps, codec, duration, number of files | No guessing; the agent knows when it's done |
| 1 | **Story bible** | Setup, rules, *seen → truth* clue table, characters with hex colours | Consistency across parts; the twist is planned before a frame is drawn |
| 2 | **Art direction** | Layer stack, tight palette, reusable props, lighting, 2D camera | The agent builds an art *kit*, not one-off drawings |
| 3 | **Text on screen** | Caption markup (`*lime*`, `_orange_`, `~red~`), HUD semantics (`hud_at`, null resets), rule cards, tags, title/end cards | Signature graphics become data-driven components |
| 4 | **Voice** | Kokoro voices per role, speeds, text normalisation, timing model | Free, local, repeatable narration; no "tilde" read aloud |
| 5 | **Sound** | Music moods, SFX vocabulary, `[name, at, dur]`, ducking, -14 LUFS | Sound is scriptable per shot, like visuals |
| 6 | **Engine** | JSON schema, `voice.py` → `timeline.json`, `renderAt(t)` pure function, Playwright → ffmpeg, QA | Deterministic, parallel, re-renderable |
| 7 | **Tone rules** | Scary not gory, emotional core, fair clues | Guardrails for platform safety and quality |
| 8 | **Verbatim shot lists** | Every shot: scene, description, VO, HUD, card, SFX, music, transition | The agent executes; it doesn't improvise the story |

**Key mechanics to keep in any adaptation:** a false belief the viewer can disprove from fair clues · a persistent HUD that tells the story in numbers · signature cards · one emotional line delivered in silence · a replay section (*what I saw → what it was*) · an end card with one clear call to action · a sequel/next hook.

## The 4 adaptations (all 16:9, 1920×1080, long-form)
| File | Content type | Length | Twist mechanism | HUD | Signature card |
|---|---|---|---|---|---|
| `01 Animated True Documentary - The Silent Lake.md` | Real event documentary (Lake Nyos, 1986) | 3 parts × 6–8 min | Rumours/theories → the real science | DATE · TIME · CO₂ · DISTANCE | EVIDENCE #N |
| `02 Rule-Horror One-Shot - The Rules of Kalani Bay.md` | "If You See X… DO Y" rule horror | 1 × 7–8 min | The feared figure is the protector; the real hazard is natural | TIME · SEA LEVEL · RULES BROKEN | RULE #N |
| `03 What-If Stickman - Never Sleep Again.md` | "What If…?" 2nd-person stickman | 1 × 8–10 min | Benefit → escalating cost → the thing you'd trade back for | HOURS AWAKE · FREE HOURS · etc. | WHAT IF LOG / DAY N |
| `04 Educational Explainer - Quicksand.md` | Myth-busting science explainer | 1 × 6–8 min | Movie myth → 5 clues → the true danger | MYTH METER · CLUES n/5 | CLUE #N / MYTH vs FACT |

## How the adaptations differ from Ashford
- **Canvas 1920×1080**: captions in the lower third (y ≈ 880–980), HUD top-left, cards centred at ~60% height; wider sets allow horizontal parallax and two-shot compositions.
- **Pacing for long-form**: shots 3–6 s, chapters every 60–90 s, a mid-roll-safe break (black + silence) in videos ≥ 8 min.
- **Facts gate**: prompts 01 and 04 (and the science outros of 02) contain real-world claims. Each prompt includes a mandatory fact-check step: every number must be verified against a primary source before voice recording (see `Research System/Fact-Checking & Accuracy Systems/`).
- **Brand**: the prompts are neutral (no channel name on end cards), so a friend can reuse them.

## Credit
Derived from "The Wall at Ashford" master prompt by @OnlySainted (CC BY 4.0). Keep the credit line at the bottom of each file if you publish derivatives.
