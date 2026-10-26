# Research Prompts
*Prompts for each research stage, ready for Local Deep Research (`tools/local-deep-research`), a Claude web-search session, or any LLM with search. Proven prompts are also logged in the root `PROMPT LIBRARY.md`. Mark them ✅ there once they produce shipped output.*

## 1. Find a twist hazard (new series)
> List 10 real, well-documented household or outdoor hazards whose symptoms or warning signs are commonly misread as something supernatural or as someone else's threat. For each: the misreading, the real cause, 3 visible signs a cartoon could show, and an authoritative source (CDC, CPSC, NOAA, NIH).

## 2. Score the hazard
> For the hazard [X], score 1–10 and justify: (a) how visual its warning signs are, (b) how surprising the real cause is to a 13–24 audience, (c) how strong the official safety data is, (d) whether a safe, correct resolution exists that a teenager could perform, (e) advertiser safety. Return a table plus a one-line verdict.

## 3. Documentary research brief (main brief)
> Produce a detailed research report on [TOPIC]. Include: verified facts, historical timeline, key figures, turning points, conflicting accounts, and shocking lesser-known details. Format as a documentary research brief. Every fact must have a link to a primary source (government agency, peer-reviewed paper, or official report). Flag anything you could not verify.

Save as `Research System/Source Gathering Workflow/Research Brief - [Topic] (S0X).md` with sections: Verified facts · Lesser-known details (story fuel) · Accuracy guardrails · Gaps.

## 4. Clue generator
> The real hazard is [X]. The narrator believes [false reality]. Generate 15 clues that are visible in a flat 2D cartoon, each with: what the narrator thinks it is, what it really is, and the real-world fact behind it (with source). The clues must be fair: a careful viewer could solve the twist from them.

## 5. Symptom/timeline realism check
> In a story, characters are exposed to [hazard] for [N] days in [conditions]. List the realistic progression of signs and symptoms by time and severity, which signs would show first in a small child, an adult and a dog, and what would make them improve. Cite sources. Mark anything uncertain.

## 6. Setting research
> Describe realistic details of [place] during [event/season]: weather, sounds, emergency response (who comes, how, what equipment), typical homes and heating. Focus on details a cartoon could show. Cite sources.

## 7. Real-science segment script
> Write a 45–60 second calm, factual documentary narration explaining [hazard] for a 13–24 audience: what it is, why it happens, the 3 warning signs, and the 3 correct actions. Every sentence must map to a source in this list: [paste brief sources]. No fear-mongering, no medical advice beyond official guidance.

## 8. Explainer Shorts batch
> From this research brief, write 6 explainer Short scripts (30–45 s each). Each starts with a counter-intuitive hook line, gives one fact with its source, and ends with "This is why [Part title] happened." Paste brief: [...]

## 9. Competitor and topic validation
Run the `yt-dlp` commands in `PROMPT LIBRARY.md → Research` with `ytsearch15:[hazard] story` and `ytsearch15:[hazard] animated` to check whether the twist is already used and how it performed.

## Prompt hygiene
- Always ask for sources and for "flag what you could not verify".
- Paste the output into the Fact-Checking claims table before using any fact (`Research System/Fact-Checking & Accuracy Systems/`).
- Never use an LLM's numbers without opening the link.
