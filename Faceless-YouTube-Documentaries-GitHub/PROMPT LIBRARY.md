# PROMPT LIBRARY
*Every prompt used in production, by stage. ✅ = produced shipped output. 🧪 = used but not yet validated against real results. Add new winners with date + series.*

## RESEARCH
**✅ Competitor pull (yt-dlp, 2026-10-24)** — real numbers, no API key:
```
python -m yt_dlp --flat-playlist --playlist-end 80 --print "%(view_count)s	%(duration)s	%(title)s" "https://www.youtube.com/@CHANNEL/videos"
python -m yt_dlp --skip-download --write-comments --extractor-args "youtube:max_comments=60,all,0;comment_sort=top" --write-info-json "https://youtu.be/ID"
python -m yt_dlp --flat-playlist --print "%(channel)s	%(channel_url)s	%(view_count)s	%(title)s" "ytsearch15:QUERY"
```
**✅ Topic research brief (S01, via web search; re-run in Local Deep Research once configured):**
> Produce a detailed research report on [TOPIC]. Include: verified facts, historical timeline, key figures, turning points, conflicting accounts, and shocking lesser-known details. Format as a documentary research brief.

**🧪 Twist-hazard finder (for new series):**
> List 10 real, well-documented household or outdoor hazards whose symptoms or warning signs are commonly misread as something supernatural or as someone else's threat. For each: the misreading, the real cause, 3 visible signs a cartoon could show, and an authoritative source (CDC, CPSC, NOAA, NIH).

## SCRIPT
**✅ Series template (Wall at Ashford formula, from the Adaptation Guide):** see `Script Frameworks/AI Script Prompts for Docs/WALL AT ASHFORD Adaptation Guide.md → New Story Template Prompt`. Filled version: S01 framework file.

**✅ Narration voice rules (S01):** first-person teen, deadpan, short sentences, never explains the irony; the HUD and the visuals carry it. Each shot holds 1–2 sentences. Caption keywords in `*stars*`. Each part ends on a sound/line from outside plus a binary end-card question.

**✅ Hook line pattern:** "On the first night of [EVENT], [N] of them [ACTION]. [One-word beat]. [What they were doing to us]."

## VOICE (Kokoro-82M)
| Role | Voice | Speed | Notes |
|---|---|---|---|
| ✅ Narrator (teen boy) | `am_michael` | 0.98 | calm deadpan |
| ✅ Child (June, 8) | `af_sky` | 1.08 | |
| ✅ Voice through the door | `bm_george` | 0.88 | lowpass 900 Hz + 60 ms echo (`muffle`) |
| 🧪 Spanish channel | `em_alex` / `ef_dora` | — | |
| 🧪 Portuguese channel | `pm_alex` / `pf_dora` | — | |

## MUSIC (ACE-Step 1.5 turbo, instrumental, 90 s, bpm 70)
Template: `[NICHE TONE] cinematic, [MOOD], no lyrics, documentary score`
- cabin: `winter survival cinematic, quiet unease, sparse felt piano and soft strings, slow, minor key, no lyrics, documentary score`
- tension: `winter survival cinematic, creeping tension, low string tremolo, ticking pulse, minor key, no lyrics, documentary score`
- rules: `winter survival cinematic, steady determined pulse, low drums and cello ostinato, dark, no lyrics, documentary score`
- dread: `winter horror cinematic, deep dread, dark ambient drone, sub bass, distant metallic textures, no melody, no lyrics, documentary score`
- drone: `dark ambient, subtle tension, drone bass, mysterious, cinematic, no melody, no lyrics`

## VISUALS
**✅ Engine:** `Productions/S01 Kestrel Lake/render/index.html`. Scenes are code. To add one, copy an `S.<scene>` function. Style rules: flat vector, black round heads, white deadpan eyes, coloured hoodies, snow on every exterior, clues visible but never highlighted.

**✅ Thumbnail art (FLUX.2 Klein 4B, 4 steps, guidance 1.0, 1280×720, seed 100+n, text added after).** ⚠️ "stickman with a black round head" alone gives anime faces 4/5 times. The *no skin, no hair, no nose* wording below fixed it 5/5:
```
flat 2D vector illustration, YouTube thumbnail, 16:9. A cartoon boy whose head is a perfectly round solid pitch-black circle
with no skin, no hair, no nose and no ears, only two big white oval eyes (silhouette stickman style), wearing a red hoodie, [POSE], inside a dark log cabin at night. Behind him a frosted window shows a snowy pine treeline where
two very tall dark figures stand, each with a single glowing white light for an eye. Deep navy and warm amber palette, strong rim
light, clean bold shapes, high contrast, empty space top-left for text, no text, no watermark.
```
Poses used: facing viewer, wide frightened eyes, back to window · pressed against the door · flashlight at the window · face close-up left third · kneeling to shield the little sister.

**Thumbnail text:** 2 imperative words, line 2 amber: `DON'T / ANSWER.` · `NEVER / OPEN IT.` · `KEEP IT / SHUT.` · `THEY'RE / WATCHING.`

## EDIT (ffmpeg-skill standards)
```
# loudness (2-pass, done in voice.py)      loudnorm=I=-14:TP=-1.5:LRA=11
# final video encode                        -vf "scale=in_range=pc:out_range=tv,format=yuv420p" -color_range tv -c:v libx264 -crf 20 -preset slow -movflags +faststart
# check loudness                            ffmpeg -i in.mp4 -af ebur128=peak=true -f null -
# contact sheet for review                  ffmpeg -i in.mp4 -vf "fps=1/8,scale=384:216,tile=6x4" -frames:v 1 contact.jpg
```

## TITLES
1. `If [ordinary thing]… [COMMAND]` → **If Two Lights Watch Your Cabin At Night… DON'T ANSWER**
2. `[N] Days [Trapped] [Place] With [Unknown Threat] (Day X)` → **Snowed In: 5 Days With Something Outside The Cabin (Day 1)**
3. `We Followed Every Rule. [Twist clause].` → **We Followed Every Rule. That Was The Mistake.**

## DISTRIBUTION (paste until Social Media Agent is installed)
**X:**
> On the first night, two of them stood at the edge of the trees. Perfectly still. Watching our window.
> We made 5 rules to survive. Part 1 → [LINK]

**LinkedIn (for the science episodes):**
> Most people don't know that ~85 Americans die every year from portable-generator carbon monoxide, often during blackouts. We turned that into a 6-part animated survival story. Part 1: [LINK]

**Pinned comment:** `WOULD YOU ANSWER? Reply YES or NO 👇 (and if you spotted a clue, don't spoil it… yet)`
