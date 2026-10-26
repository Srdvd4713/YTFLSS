# 30-Day Scaling Plan — S01 launch
*Day 1 = the day Part 1 goes live. Production capacity measured this session: one Part ≈ 3 min of voice/mix + 4 min of render on this PC, plus writing time.*

## Calendar
| Day | Long-form | Shorts (3 per episode) | Other |
|---|---|---|---|
| 1 | **Part 1** The Day The World Went Quiet | P1 short 1 | pin "WOULD YOU ANSWER?" |
| 2 | **Part 2** They Know Our Names | P1 short 2 · P2 short 1 | |
| 3 | **Part 3** Biscuit Won't Wake Up | P1 short 3 · P2 short 2 | stickman explainer #1 |
| 4 | **Part 4** June Opened The Window | P2 short 3 · P3 short 1 | |
| 5 | **Part 5** The Word Was OPEN (twist) | P3 shorts 2–3 | members get P5 24 h early (once eligible) |
| 6 | **Part 6** I Opened The Door + real CO facts | P4 shorts | stickman explainer #2 |
| 7 | **"Did you catch all 12 clues?"** compilation (re-cut of P1–2 with clue callouts + P5 replay cards) | P5 shorts | Podcastfy ep 1: "The Silent Killer in Every Blackout" |
| 8–13 | — (produce S02) | P6 shorts, then best-performer re-cuts | stickman explainers #3–#5 |
| 14 | **S02 concept drop**: teaser, "THE HUM UNDER DRY CREEK" (sequel sting from P6 + Rule 1 card) | teaser short | community post poll: "Which rule will break first?" |
| 15–20 | S02 Parts 1–6 daily | 3/day | stickman explainers #6–#8 |
| 21 | S02 clue compilation | | Podcastfy ep 2 |
| 22–30 | S03 pre-production; re-cut a 25-min "full series" movie of S01 (watch-time play) | 3/week explainer shorts | 2nd-language channel launch (below) |

**Stickman explainer shorts (3/week):** 30–45 s, real science from each series ("Why your headache goes away outside", "Why dogs get sick first", "Where a generator actually goes"). Made in the same engine with a `diagram`-style scene. These are advertiser-safe and link to the series.

**Podcastfy ×2:** feed the series framework + research brief. 2 hosts, journalistic tone, 15–20 min. Upload to Spotify, then clip 3 audiograms.

## Second channel (same series, second market, near-zero cost)
1. Translate `parts/partN.json` VO lines (LLM translation + one native-speaker review pass). Keep the shot timings; `voice.py` re-times everything automatically.
2. Voices: Spanish `em_alex` / `ef_dora`, Portuguese-BR `pm_alex` / `pf_dora`. Add `lang` to the voices block (`es`, `pt-br`).
3. Translate on-screen text: rule cards, note, HUD labels, end card (all strings live in `part*.json` / `index.html`).
4. Same render command. Spanish first (largest YouTube market after EN); Brazil second.

## Brand ad pipeline
After S01 Part 6 is live and the channel has a portfolio:
- Offer **animated 30–60 s explainers** in this exact style to safety brands (CO alarms, generators, outdoor gear), local utilities, and insurers.
- Pricing: $500 (30 s, existing assets) → $5K (60 s, custom characters + scenes).
- The safety-science angle of S01 is the pitch: "we already make people care about CO alarms."
