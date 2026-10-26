# Script-to-Voice Alignment Guide
*How narration, captions and pictures stay in sync. In this pipeline the voice drives the timing: `voice.py` measures each generated line and re-times the shots, then `render.js` draws the frames against `timeline.json`.*

## The flow
```
parts/partN.json  →  voice.py  →  build/partN/timeline.json  →  render.js  →  output/partN.mp4
   (shots + vo)       (TTS + timing)   (start/end of every shot,        (frames)
                                        line, caption word, sfx)
                     ↘ output/partN.srt (captions)
```

## Writing lines that align well
- **1–2 sentences per shot.** A shot's length = its VO length + padding, so long lines make long static shots.
- **Visual first, words second:** the clue appears on screen ~0.5 s before the narrator mentions it (or he never mentions it at all).
- **Keywords in `*stars*`** become the amber caption words. Max 1–2 per line.
- **Pauses:** use a separate shot with no VO (or `music: silence`) instead of writing "…" and hoping TTS pauses.
- **Numbers:** write them how they should be spoken ("four hundred ten" vs "410") if TTS reads them wrong.

## Timing targets
| Element | Target |
|---|---|
| Narration speed | ~150–165 words/min (Kokoro `am_michael` at 0.98) |
| Padding after a line | 0.3–0.6 s (longer before a scare) |
| Caption line | ≤ 42 characters, ≤ 2 lines |
| Rule card hold | 2.5–3.5 s even if the VO is shorter |

## QA steps
1. After voice.py, open `output/partN.srt` and skim: every line present, no overlaps.
2. Render stills at key seconds: `node render.js --part N --still 5,30,60,90` and check the caption matches the image.
3. Watch the full render once with sound. Mark any line that lands before its visual.
4. Fix in `partN.json` (split the line, move it to the next shot, add a silent shot), re-run voice.py and a partial render: `node render.js --part N --from A --to B`.

## Translations (Spanish / Portuguese channels)
- Translated lines run ~15–25% longer. voice.py re-times automatically, but check the Part's total length and the rule-card holds.
- Shorten translations to match the meaning, not word count. The native-speaker review pass (see `Automation & Systems/Outsourcing Rules/`) approves this.
- Re-generate the SRT per language and upload it as that language's caption track.

## Captions for YouTube
Upload `output/partN.srt` as the English caption track on every upload, even with burned-in keywords. It improves accessibility and gives YouTube the transcript for search.
