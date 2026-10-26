# Agent Task Prompts
*Copy-paste prompts for running each pipeline stage with Claude Code from the repo root. The creative/production prompts themselves (research, script, voice, music, thumbnails) live in the root `PROMPT LIBRARY.md`; research-only prompts in `Research System/Research Prompt Libraries/`. This file is the **operator layer**: what to ask the agent to do.*

## Session start
> Read `CLAUDE MASTER BOOTSTRAP PROMPT.md`, `CHANNEL BIBLE.md`, `EPISODE TRACKER.md` and `SOP - EPISODE PRODUCTION.md`. Tell me the next unfinished step for the current series and what you need from me.

## New series
> Using `Research System/Research Prompt Libraries/Research Prompts.md` §1–3, research a new series hazard for [season/setting]. Save the brief in `Research System/Source Gathering Workflow/`, then draft a series framework in `Script Frameworks/Narrative Arcs for Documentaries/` following the S01 framework structure (concept, 5 rules, 12 clues, HUD table, 6 parts, thumbnail and title formulas).

## Script a Part
> Write `Productions/[series]/parts/part[N].json` from the series framework. Follow the hook playbook, the tension map and the cliffhanger playbook in `Script Frameworks/`. Plant clues [list]. Only use the allowed scenes, SFX and music moods from the SOP. Then run the fact-check SOP on every real-world claim and show me the claims table.

## Produce a Part
> Run SOP steps 4–5 for Part [N]: voice + mix, loudness check, QA stills at 5,30,60,90, show me the stills, then full render. Report duration, LUFS and any warnings.

## Thumbnails
> Run SOP step 6 for Part [N] with these poses [..] and texts [..]. Run the impeccable QA gate and show me the 3 best at 320 px wide.

## Upload package
> Create `output/part[N]_UPLOAD.md` with: 2 title options (Title Hooks Library), description (SEO checklist template), chapters from timeline.json, tags, pinned comment, end-card question, and the A/B test plan.

## Shorts
> Cut 3 Shorts from Part [N] with `make_shorts.py`: pick the 3 moments with the strongest standalone hook, each ending "Part [N] is on the channel." Update the Shorts table in EPISODE TRACKER.

## Weekly review
> Here are my Studio numbers: [paste]. Update EPISODE TRACKER, compare against `Growth Engine/Analytics That Matter/Analytics Dashboard Guide.md`, and give me the one change to make next week.

## Translation
> Translate `parts/part[N].json` VO lines and on-screen text to [es/pt-br] following the 30-Day Scaling Plan second-channel steps. Keep timings, localise units and the emergency number, and produce a review sheet for a native speaker.

## Maintenance rule
When a prompt produces shipped output, log it in `PROMPT LIBRARY.md` with ✅, the date and the series.
