# Multi-Channel Operations SOP
*How the same pipeline feeds several channels (EN main + ES + PT-BR) without doubling the work. Business gates and revenue tracking: `Monetization/Scaling to Multiple Doc Channels/Multi-Channel Revenue Plan.md`.*

## Folder convention
```
Productions/S01 Kestrel Lake/
  parts/part1.json            # EN master (source of truth for shots + timing)
  parts/es/part1.json         # ES: same shots, translated vo + on-screen text, "lang": "es"
  parts/pt-br/part1.json
  output/part1.mp4            # EN
  output/es/part1.mp4
  output/pt-br/part1.mp4
```
Only **text and voices** change between languages. Scenes, music and SFX are shared.

## Per-language pipeline (per Part, ~2 h)
1. Translate VO + on-screen strings (Agent Task Prompts → Translation).
2. Native-speaker review (Outsourcing Rules checklist).
3. `voice.py` with the language voices (ES `em_alex`/`ef_dora`, PT-BR `pm_alex`/`pf_dora`) → mix + SRT.
4. Render with the same command, output to the language folder.
5. Thumbnails: same art, translated text (2 imperative words still).
6. Upload package in the language (titles re-written for the market, not literally translated).

## Weekly schedule (once 3 channels run)
| Day | EN | ES | PT-BR |
|---|---|---|---|
| Mon–Sat | New Part / Shorts (during a series) | Translated Part from the previous EN series | Same, one week behind ES |
| Sun | Review + script next | Review | Review |
Keep a fixed posting time per channel in that market's time zone.

## Tracker
Add columns per language to `EPISODE TRACKER.md` or a separate table:
| EP | Part | EN upload | ES translate | ES review | ES upload | PT translate | PT review | PT upload |
|---|---|---|---|---|---|---|---|---|

## Automation opportunities
- One command per language: a small wrapper script that runs voice.py + render.js for `--lang es`.
- Batch renders overnight (one GPU/CPU job at a time — the GPU rule in the SOP still applies).
- Use YouTube Studio scheduling to queue a week of uploads per channel.

## Account management
- Each channel as a Brand Account under one Google account, 2-Step Verification on.
- Channel permissions for helpers per channel, lowest role needed.
- Shared assets (music, scenes) stay in the main series folder; never duplicate them per language.

## Quality guardrails
- A language channel ships only complete series (all 6 Parts ready before Part 1 goes live).
- Safety lines localised and fact-checked (units, emergency number).
- If a language channel misses its schedule, pause it. Don't let it delay the EN main channel.
