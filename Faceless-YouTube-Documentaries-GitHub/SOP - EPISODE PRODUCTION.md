# SOP — EPISODE PRODUCTION
*One episode (one Part) from blank page to upload. All commands run from `Productions\S01 Kestrel Lake\` in a terminal (Git Bash or PowerShell). Everything is local and free.*

## 0. One-time setup (already done on this PC — 2026-10-24)
Node 24 · Playwright + Chromium · Python 3.14 + `kokoro-onnx` · ffmpeg 9 · Kokoro models in `tools\kokoro-models\` · ACE-Step 1.5 in `tools\ACE-Step-1.5\` (own `.venv`, Python 3.12) · FLUX.2 Klein 4B via `diffusers` (weights auto-download to the HF cache on first run).
> **GPU rule:** run only ONE GPU job at a time (ACE-Step **or** FLUX). The 8 GB card can't hold both.

## 1. Research (15 min)
1. Open the series framework (`Script Frameworks\Narrative Arcs for Documentaries\`) and the research brief (`Research System\Source Gathering Workflow\`).
2. For a new series, run the research prompt from `PROMPT LIBRARY.md → Research` through Local Deep Research (or a web-search session until LDR + Ollama is configured). Save the brief in `Research System\Source Gathering Workflow\`.
3. Check the "accuracy guardrails" section before writing anything factual.

## 2. Script → shot list (45–90 min)
1. Copy `parts\part1.json` to `parts\partN.json`.
2. Edit each shot: `scene`, `params`, `vo` lines, `sfx`, `music`, `hud`. Wrap caption keywords in `*stars*`.
3. Keep the 12-clue table open. Every clue planted must be **visible but natural**.
4. Allowed scenes: `window_pov, title, ext_cabin, int_cabin, shed, note, rule_card, alarm, woodpile, door, black, end_card` (add new ones in `render\index.html → S.<name>`).
5. Allowed SFX: `wind hum heartbeat boom snore static paper pencil flip ring crunch door chirp click riser knock`.
6. Music moods: `cabin tension rules dread drone sting silence`.

## 3. Music (once per series, 10 min) — ACE-Step 1.5
```
..\..\tools\ACE-Step-1.5\.venv\Scripts\python.exe gen_music.py
```
Writes `assets\music\<mood>.wav`. `voice.py` picks them up automatically; with no file there, it falls back to a synthesized bed. To redo one mood: `... gen_music.py dread`.

## 4. Voice + mix (2 min)
```
python voice.py --part N
```
Outputs `build\partN\timeline.json`, `build\partN\mix.wav` (VO + SFX + music ducked -10 dB, **-14 LUFS / -1.5 dBTP**), `output\partN.srt`.
Check loudness: `ffmpeg -i build\partN\mix.wav -af ebur128 -f null -` → "I: -14.0 LUFS".

## 5. QA stills, then render (10–25 min)
```
node render.js --part N --still 5,30,60,90      # look at build\partN\stills\*.png
node render.js --part N --workers 6             # full render -> output\partN.mp4
```
Partial re-render for fixes: `node render.js --part N --from 40 --to 55`.

## 6. Thumbnail (15 min)
1. Edit the pose list in `gen_thumbs.py` and the text list in `thumbs.js` (formula: 2 imperative words, line 2 amber).
2. `python gen_thumbs.py` → `build\thumbs\art_1..5.png` (FLUX.2 Klein, ~2 min each).
3. `node thumbs.js` → `output\thumbs\thumb_1..5.html/.jpg`.
4. **impeccable QA gate:** `..\..\tools\impeccable\.agent\skills\impeccable\scripts\impeccable detect --json output\thumbs`. Fix anything flagged. Then pick the winner by eye at phone size (resize to 320 px wide). Max 3 dominant colours, text readable at 320 px.

## 7. Final check (5 min) — ffmpeg-skill standards
- Watch the whole MP4 once.
- `ffprobe output\partN.mp4` → H.264, yuv420p, 1920×1080, 30 fps, AAC.
- Loudness already -14 LUFS (step 4). Do **not** re-normalize.
- Captions are burned in by the engine. Upload `output\partN.srt` as closed captions too (SEO).

## 8. Shorts ×3 (10 min)
`python make_shorts.py --part N` → `output\shorts\partN_short1..3.mp4` (9:16, blurred-fill background, built from the 3 strongest beats listed in the script).

## 9. Upload
- Title: one of the 3 title formulas (PROMPT LIBRARY → Titles). Description: 2-line hook + "Part N of 6" + chapter list + real-science sources (Part 6).
- Thumbnail: the step 6 winner. End screen: next Part + subscribe.
- Pin a comment with the end-card question.
- Shorts: upload with "#shorts", link the full Part in the related video.

## 10. Distribute + log
- Social Media Agent (`langchain-ai/social-media-agent`, not yet installed — see PROMPT LIBRARY → Distribution for the post templates to paste meanwhile).
- Update `EPISODE TRACKER.md`. Log any new prompt that worked in `PROMPT LIBRARY.md`.
