# Channel Research & Niche Scoring — 2026-10-24

Data pulled live with `yt-dlp` on 2026-10-24 (view counts, upload dates, top comments, thumbnails).
Raw method: `python -m yt_dlp --flat-playlist --print "%(view_count)s %(duration)s %(title)s" https://www.youtube.com/@CHANNEL/videos`

## Headline findings

1. **None of the three reference channels is a documentary channel.** Two are "What If [superpower]" stickman stories, one is rule-based horror. All three use flat-vector code-drawable art (the Ashford/Stickman stack can reproduce it).
2. **All three are < 3 weeks old and upload daily.** Ifverse hit 4.4M views on a video posted Oct 7. Speed + daily cadence is the game.
3. **The views are in 6–10 minute 16:9 long-form, not Shorts.** Their Shorts top out at ~45K. Long-form = 200K–4.4M. Shorts are a funnel, not the product.
4. **The audience's favourite comment is the twist reversal.** Final Sight's top comments: *"That deer saved our lives"*, *"The deer wasn't killing people, he was protecting the people."* This is exactly the Ashford mechanic (protector misread as threat).
5. **Serialized day-count survival is the fastest-growing format found.** Beanie Survives: 93.5K subs from 12 videos in 12 days. Titles carry a day number like a HUD stat.

---

## Reference channels (8-point analysis)

### @IfverseTales — 52.5K subs
| # | Point | Finding |
|---|---|---|
| 1 | Niche | Sci-fi "What If" — one impossible ability followed to its consequences (speed, IQ, time loops) |
| 2 | Format | 6–12 min 16:9, flat-vector black-head stickman, single deadpan male narrator, 2nd person ("you"). Multi-part ("Part 1 of 3") |
| 3 | Top 5 | What If Your Reaction Time Was 10x Faster? (4.4M) · What If You Had 500 IQ? (1.3M) · What If One Second Felt Like Ten? (642K) · What If You Used 500 IQ to Disappear? (466K) · What If One Second Felt Like Forever? (364K). Hook: mundane benefit → "Sounds amazing. It's also kind of awful." |
| 4 | Cadence | ~5/week long-form + Shorts |
| 5 | Thumbnail | Dark navy night gradient, stickman (black head, coloured hoodie) at 1/3, one hero prop (bullet, IQ meter), 1–2 words: white + yellow/red ("TOO SLOW.", "TEST BROKE.") |
| 6 | Comments | Jokes riffing on premise ("If I had 500 IQ I'd still procrastinate"), timestamp callouts, "what next?" sequel requests |
| 7 | Our stack | Stickman SOP + Kokoro + Playwright render; thumbnails = same SVG engine |
| 8 | Difficulty | **Easy–Medium** |

### @IFOLOGYFILMS — 38.2K subs
| # | Point | Finding |
|---|---|---|
| 1 | Niche | Identical "What IF You Could [power]" superpower premise (clear copy of Ifverse) |
| 2 | Format | 5–22 min 16:9, same stickman style, deadpan narrator |
| 3 | Top 5 | What IF You Were 10x Faster? (770K) · Could Stop Time? (561K) · Could Teleport? (294K) · Could Shapeshift? (273K) · 100x Stronger? (229K) |
| 4 | Cadence | Daily, sometimes 2/day |
| 5 | Thumbnail | Same formula — close-up stickman face + one word ("PAUSED.") yellow |
| 6 | Comments | Premise jokes, power-ranking debates |
| 7 | Our stack | Stickman SOP |
| 8 | Difficulty | **Easy** — but proves the niche is already being cloned (saturating) |

### @Final_Sight — 9.1K subs
| # | Point | Finding |
|---|---|---|
| 1 | Niche | Analog-horror "survival guide" — *If You See [ordinary thing]… [COMMAND]* |
| 2 | Format | 6–8 min 16:9, flat vector, numbered rules ("There are 7 rules. Most people break the fourth.") |
| 3 | Top 5 | If You See A Deer In Your Window… LEAVE THE HOUSE (837K) · If Your Dog Ever Stops Moving… DONT PET IT (412K) · Dog Scream At 3AM… HIDE (269K) · Mom Smiles At Your Doorbell… DO NOT OPEN IT (247K) · Everyone In Your Class Stops Writing… NEVER LOOK UP (214K) |
| 4 | Cadence | Daily |
| 5 | Thumbnail | Red/white split: huge command word left, framed creature-in-window right, white arrow |
| 6 | Comments | **Twist-reversal ("the deer was protecting them")**, "last video before bed", rule-lawyering |
| 7 | Our stack | Ashford engine (rules cards + twist) |
| 8 | Difficulty | **Easy** |

## Additional channels (100K-class / fast-growing, similar method)

| Channel | Subs | Niche | Top video (views) | Length | Cadence | Thumb/notes | Stack | Diff. |
|---|---|---|---|---|---|---|---|---|
| Beanie Survives | 93.5K (12 vids) | Serialized zombie survival, day counter | 30 Days Trapped On The 30th Floor (2.6M); Ep.5 "You Got Them Out (Day 121)" 456K | 8–10 min | Daily | Episode + day number in title = HUD | Ashford engine | Medium |
| Nobody Gets In | 30.7K (10 vids) | Same, location-swap ("Supermarket", "School", "Mega Mall") | 30 Days Locked Inside a Supermarket (1.7M) | 8–11 min | ~Daily | Location-swap = sequel-hook formula | Ashford engine | Medium |
| Bradikinin | 45K (9 vids) | Rule-horror | If Your Dog Ever Stands On Two Legs… ACT NORMAL (2.7M) | 4.5–6.5 min | Daily | Shorter runtime still hits millions | Ashford engine | Easy |
| Dusk Broadcast | 62K | Analog horror broadcasts | How to Safely Visit Abandoned Places (297K) | 8–9 min | Weekly | Crowded, lower ceiling | Ashford engine | Medium |
| True Doc | 8.4K | 2D-animated **true** business/crime stories (India) | India's ₹550 Crore Heist (1.1M) | 7–11 min | ~Weekly | The only real "documentary" in the set; high CPM topics | Stickman + LDR research | Medium |
| Textify | 529K | Long analog-horror compilations | Do Not Fall Asleep (179K) | 35–60 min | 2–3/week | Big but flat views — saturated | — | Hard |

---

## Phase 3 — Niche scoring (1–10)

| Niche | Rewatch | Series | Emotion | Gap | CPM | Speed | Clues | Evergreen | **Total /80** |
|---|---|---|---|---|---|---|---|---|---|
| **A. Serialized survival + rules + science twist** (Beanie / Nobody Gets In / Ashford) | 8 | 10 | 9 | 7 | 6 | 8 | 10 | 9 | **67** |
| B. Rule-horror "If You See X… DO Y" (Final Sight / Bradikinin) | 8 | 6 | 9 | 5 | 4 | 9 | 8 | 8 | **57** |
| C. 2D animated true-story documentary (True Doc) | 5 | 6 | 7 | 8 | 9 | 5 | 5 | 10 | **55** |
| D. "What If" superpower stickman (Ifverse / IFOLOGY) | 6 | 7 | 7 | 4 | 5 | 8 | 4 | 9 | **50** |
| E. Analog horror broadcast (Dusk / Textify) | 7 | 7 | 8 | 3 | 3 | 7 | 7 | 8 | **50** |
| F. Live-research mystery doc (Nexpo / LEMMiNO) | 5 | 4 | 8 | 3 | 9 | 2 | 3 | 10 | **44** |

### Top 5: A (67) · B (57) · C (55) · D (50) · E (50)

### Recommendation: **A — serialized survival series with a real-science twist**
- Takes Beanie Survives' proven *day-count serial* + Final Sight's *rules packaging* + the *protector-reversal* comments the audience loves.
- The twist is a **real, documentable hazard** (carbon monoxide poisoning). That keeps the "Documentaries" identity, raises advertiser-friendliness above pure horror (CPM), and gives every series a free spin-off: a stickman explainer of the real science.
- Long-form 16:9 (5–9 min) is the product; 3 vertical Shorts per episode are the funnel.
