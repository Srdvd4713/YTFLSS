# A/B Testing System (Thumbnails & Titles)
*How to test packaging without guessing. Uses YouTube Studio's built-in **Test & Compare** (up to 3 thumbnails, and titles where available) plus a manual log.*

## What to test, in order of impact
1. **Thumbnail concept** (different scene/pose), not small tweaks.
2. **Thumbnail text** (two imperative words, e.g. "KEEP IT SHUT." vs "DON'T ANSWER.").
3. **Title formula** (formula 1 vs 2 in `Title Hooks That Work/Title Hooks Library.md`).
4. Small details (colour of line 2, crop) only once the concept is settled.

## Process per upload
1. Produce 5 thumbnail variants (SOP step 6: `gen_thumbs.py` + `thumbs.js`), run the impeccable QA gate, then pick 3 by eye at 320 px wide.
2. Upload with Test & Compare enabled, 3 variants.
3. Don't touch title/thumbnail while the test runs (Studio picks the winner by **watch time share**, which also accounts for retention, not just CTR).
4. When the test finishes (usually days to two weeks depending on traffic), log the result below.
5. Low-traffic channel? If the test is inconclusive after 14 days, keep the leader and test again on the next Part.

## Test log
| Date | Video | Variable | A | B | C | Winner | Watch-time share | Note |
|---|---|---|---|---|---|---|---|---|
| — | S01P1 | thumb text | #5 "KEEP IT SHUT." | #1 "DON'T ANSWER." | — | — | — | Planned (EPISODE TRACKER) |

## Hypothesis format (write before testing)
"I believe **[variant B]** will beat **[A]** because **[audience reason]**. I'll know if watch-time share is higher by a clear margin."

## Turning results into rules
- 3 wins in a row for the same pattern → add it to the series framework thumbnail formula and to PROMPT LIBRARY (✅).
- A pattern that loses 3 times → remove it from the variant pool.
- Keep a "loser gallery" folder per series (`output/thumbs/losers/`) so you don't test the same idea twice.

## Metrics to watch outside the test
- Impressions CTR in the first 24 h vs channel average.
- Average view duration: a CTR win with a retention drop means the packaging overpromised.
- Traffic source: browse vs suggested vs search behave differently. Compare like with like.
