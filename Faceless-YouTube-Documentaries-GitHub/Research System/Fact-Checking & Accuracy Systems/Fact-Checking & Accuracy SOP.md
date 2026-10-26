# Fact-Checking & Accuracy SOP
*Every series has a real-science twist. If the science is wrong, the channel loses its "documentary" identity, advertiser trust and, for safety topics, could hurt someone. This SOP runs before voice recording.*

## Source tiers
| Tier | Accept for | Examples |
|---|---|---|
| **A: primary/official** | Any on-screen fact or number | CDC (MMWR), CPSC, NOAA/NWS, NIH/PubMed, FEMA, WHO, peer-reviewed papers |
| **B: reputable secondary** | Context, history, quotes | Major newspapers, university pages, Wikipedia *only to find* the primary source |
| **C: not acceptable** | Nothing on screen | Forums, AI answers without links, content farms, other YouTube videos |

Every number on screen needs a **Tier A** source. Two independent sources for anything surprising.

## Workflow (30–45 min per series, 10 min per Part)
1. **Extract claims.** From the script/shot list (`parts/partN.json`) list every factual claim: VO lines, rule cards, HUD values with real units (e.g. `CO: 410 PPM`), end cards, the science segment.
2. **Classify.** Story claim (fiction, no check) vs. real-world claim (must check). Anything in the real-science segment, end cards and Shorts explainers is real-world.
3. **Verify.** Find a Tier A source for each real-world claim. Write it in the claims table below in the series research brief (`Research System/Source Gathering Workflow/`).
4. **Safety check.** Does any line imply unsafe advice? (e.g. "open a window and you're fine"). Rewrite to the correct guidance.
5. **Plausibility check of the fiction.** Symptoms, timelines and visuals must match reality (e.g. CO symptoms shown in a plausible order).
6. **Sign-off.** Mark the Part's Script column in `EPISODE TRACKER.md` ✅ only after this table is complete.

## Claims table template
| # | Claim (as written) | Where | Source (Tier A link) | Status | Fix |
|---|---|---|---|---|---|
| 1 | "~85 US deaths a year from generator CO" | P6 science | CPSC 2022 report | ✅ | — |
| 2 | "Opening a window fixes it" | — | CPSC: a cracked window is NOT enough | ❌ | Say "generator off, get out, call 911" |

## Safety language rules (health/safety twists)
- Resolution always = **remove the source → get to fresh air → call emergency services → install/test detector.**
- No diagnostic claims ("cherry-red skin means CO"). Use "can", "often", "may".
- No medical advice beyond official guidance. Add on-screen: "Source: [agency]".
- Real tragedies are referenced with numbers, never mocked or dramatised with real victims' names.

## Common AI-research errors to catch
- Invented statistics or wrong years. Open the link and find the number.
- Mixing up US and other-country figures.
- Outdated guidance (check the source's date; prefer the newest edition).
- Citation links that point to a different document than claimed.

## After publishing
- If a viewer reports an error: verify within 24 h. If it's real, pin a correction comment, fix the description, and fix the source file for re-uploads/translations.
- Log corrections in the series research brief under "Corrections".
