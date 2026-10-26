Master prompt adapted from "The Wall at Ashford" by @OnlySainted (CC BY 4.0). Paste this whole file into a coding agent (Claude Code, or any agent that can run code, Node/Python, Playwright and ffmpeg). It researches, fact-checks, builds and renders a 3-part animated documentary series about a REAL event, "The Silent Lake" (Lake Nyos, Cameroon, 1986), with no stock assets. Everything is drawn in code, voiced with a free local TTS, and scored with synthesized or CC0 sound.

0. WHAT YOU ARE BUILDING
A 3-part horizontal (16:9) animated documentary series for YouTube:
Format: 1920×1080, 30 fps, H.264 MP4 with AAC audio, one file per part (part1.mp4 … part3.mp4). Each part runs ≈ 6–8 minutes.
Genre: true-event mystery documentary. Structure: Part 1 = the mystery (what the world found), Part 2 = the wrong theories, Part 3 = the real science and what it means today. The "twist" is the scientific answer, and every early detail must make sense on a second viewing.
Look: flat-vector 2D illustration (SVG drawn in code), lush green highland palette that drains to grey-blue during the disaster, documentary map and diagram graphics, cinematic gradients, vignette, mist.
Every frame is a pure function of time renderAt(t). No Date.now(), no unseeded Math.random().
Deliver: the 3 MP4s, a contact sheet per part, an SRT per part, the source code, and sources.md (every fact with its primary source).

0.5 MANDATORY FACT-CHECK GATE (do this BEFORE writing any VO to audio)
This is a real disaster with real victims. The numbers and details in this prompt are a starting brief, not verified truth.
1. Extract every factual claim from section 1 and section 8 into facts.md (claim · part/shot · status).
2. Verify each claim against primary or authoritative sources (peer-reviewed papers on the 1986 Lake Nyos limnic eruption, USGS, Smithsonian Global Volcanism Program, government/UN reports, reputable science journalism that cites those). Use web search.
3. If a number differs between sources, use the most authoritative figure and phrase it with "about" or "an estimated".
4. Correct the VO in the part JSON files. Mark anything unverifiable and remove or soften it.
5. Never invent quotes from real survivors or scientists. Survivor experiences are voiced as "survivors later described…" paraphrases of documented accounts, or by clearly labelled COMPOSITE characters.
6. Write sources.md and put on-screen source chips (bottom-left, small monospace) on every statistic.

1. THE STORY BIBLE (brief, to be verified)
Setting: Lake Nyos, a deep crater lake in the highlands of north-west Cameroon. Villages in the valleys below (Nyos, Kam, Cha, Subum and others). Farming and cattle-herding communities.
Event: on the night of 21 August 1986 (around 9:30 pm), the lake released an enormous cloud of carbon dioxide. CO₂ is heavier than air, so the cloud flowed down the valleys, displacing the oxygen. About 1,700+ people and thousands of cattle died, most in their sleep, some many kilometres from the lake.
Mystery details (seen → truth):
| Shown early | Truth |
|---|---|
| Morning silence: no birds, no insects | The gas killed every breathing animal low in the valleys |
| People found dead in their homes, no wounds | Asphyxiation by CO₂; no fire, no poison in the usual sense |
| Survivors woke hours later, confused | They were at the edge of the cloud's concentration |
| The beautiful blue lake turned rusty red-brown | Iron-rich deep water had been churned to the surface |
| Water level near the shore had dropped; vegetation flattened on one side | A surge of water/gas had swept the shoreline |
| Higher ground survived, valleys didn't | Heavy gas flows downhill like water |
| Some described a smell (rotten eggs / gunpowder) | Reported in accounts; CO₂ itself is odourless (explain carefully, verify) |
| A smaller similar event at Lake Monoun (1984) | Same mechanism, warning sign that was missed |
Wrong theories (Part 2): a chemical-weapon test or bomb, a volcanic eruption with poisonous gas, local beliefs about the lake's spirits, a gas leak from the earth near the villages. Present local beliefs respectfully, never as superstition to mock.
The answer (Part 3): a LIMNIC ERUPTION. CO₂ from volcanic sources below seeped into the deep, cold, stratified lake water and dissolved under pressure, like a sealed soda bottle. Something (a landslide, rainfall, wind, or slow overturn: still debated, verify) disturbed the layers; the water rose, pressure dropped, the gas came out of solution all at once. Afterwards: degassing pipes installed (from 2001; more later) that let the gas out slowly. Lake Kivu (Rwanda/DR Congo) holds gas too and is monitored.
Characters (consistent across parts):
| Name | Role | Look (flat vector) |
|---|---|---|
| Narrator | Calm documentary voice (no on-screen body) | — |
| Composite herder "Ama" (label: COMPOSITE CHARACTER) | Guides the human experience in Part 1 | Round head #6b4228 skin, dark outline, dot eyes, green wrap #3f7d4e, red headscarf #b2392f |
| Composite boy "Ngum" (COMPOSITE) | Ama's son, runs to the hill | Orange shirt #d07a2e, shorts #34495e |
| The investigators | Scientists arriving in Part 2 (no real names unless verified and needed) | Khaki field shirts, sample bottles, boat |
| The lake | A character in itself: blue → red-brown → calm with a pipe fountain | — |
People: round heads with dark outline, dot eyes, brows, simple mouths, stroke-limbs with round hands, soft ground shadow, procedural breathing/blinking/walk. Victims are never shown in detail: use empty doorways, still silhouettes at distance, cattle silhouettes lying in grass, a dropped bowl. No faces of the dead.

2. ART DIRECTION
Canvas 1920×1080 SVG, recomposed every frame. Layers: sky gradient → far volcanic ridges → highland hills with terraces → mid-ground village (round huts with thatched roofs, rectangular tin-roof houses) → characters → foreground grass with slight blur → weather (mist bands, drifting gas as translucent ground-hugging layer) → vignette → film grain 6%.
Palette: grass #4f8a3f / #79a85a, earth #a8754a, lake blue #2f6f8f, lake rust #9a4a2a, mist #d7dccf, night #0a0f18 → #1d2a3a, dawn #e9c79a, gas tint #9fb3b8 at 25–45% opacity.
Signature props as reusable functions: crater lake (cross-section and top view), huts and houses, cattle, cooking fire, oil lamp, bicycle, boat, sample bottle, map of Cameroon with the lake marker, cross-section diagram of lake layers, CO₂ molecule icon, soda bottle, degassing pipe with fountain.
Lighting: night scenes lit by lamps and moonlight; the gas scene desaturates everything it touches (apply a saturation mask that follows the gas layer).
Camera in 2D: slow push-ins, lateral drifts along the valley, map zooms (country → region → lake), split-screen comparisons.

3. TEXT ON SCREEN
Captions: Oswald 700, ALL CAPS, 1–4 words per chunk, centred low (y ≈ 900–990). Thick black stroke, soft shadow, spring pop per word. Markup: *word* = amber #ffc23d, _word_ = teal #49c6b8, ~word~ = red #ff4a3d. Strip markup before TTS.
Documentary HUD (top-left, monospace): DATE 21 AUG 1986 · TIME 21:30 · LOCATION LAKE NYOS · CO₂ CLOUD — · DISTANCE 0 KM · LIVES LOST (only after verification, shown once, never as a ticking counter). Values pop when they change; hud_at = fraction of the shot where the change lands; HUD null hides and resets.
EVIDENCE CARD: a manila evidence tag (paper texture, string hole, red "EVIDENCE #N" stamp) flips in with 3D perspective and spring physics, sheen sweep, impact SFX. Variant "THEORY #N" (blue stamp, later struck through in red). Variant "SCIENCE #N" (teal, clean).
Source chip: bottom-left, Consolas 22 px, 75% white: "Source: …" on every statistic, ≥ 2 s.
Composite label: under any composite character the first time they appear: "COMPOSITE CHARACTER · BASED ON SURVIVOR ACCOUNTS".
Title card (each part): night map of the lake at the centre, mist drifting, a pulsing ring around the lake. Text "THE SILENT LAKE" + "PART N" chip + subtitle.
End card: "NEXT: PART N+1 · SUBTITLE" + CTA line + the lake silhouette breathing mist. No "follow @channel".

4. VOICE
Kokoro-82M (ONNX) + espeak-ng. Narrator = bm_george at 0.96 (calm British documentary register). Composite Ama = af_heart at 1.0 (short paraphrased lines only), Ngum = af_sky at 1.08, investigators = am_michael at 0.98.
Normalise text before TTS: "1986" → "nineteen eighty-six", "CO₂" → "carbon dioxide", "km" → "kilometres", "21:30" → "nine thirty at night", strip * _ ~, remove abbreviation full stops.
Timing: synthesise each shot's line, trim silence, place caption chunks by phoneme weight snapped to silences. Shot length = lead (≈0.25 s) + speech + tail (≈0.5 s, longer where noted).

5. SOUND & MUSIC (original only)
Moods: village (soft hand percussion, kalimba-like plucks, warm pads), night (crickets, low pad), dread (sub drone, glassy tones), science (clean pulses, light arpeggio), stop (silence). Crossfade ≈1 s; duck music −10 dB under voice.
SFX vocabulary: crickets, birds, cattle, wind, water lap, deep rumble, gas hiss (low filtered noise), whoosh, impact, tick, clock, pencil, paper, stamp, boat motor, bubble, fountain, heartbeat, glitch, ring.
SFX list per shot: [name, at seconds, duration]. Auto whoosh on transitions, impact on every card. Master −14 LUFS, true peak −1 dBTP.
Silence rule: the moment the gas reaches the village (Part 1) plays with NO music and only a fading cricket bed that stops.

6. ENGINE & RENDER PIPELINE
parts/partN.json: {part, title, voice, speed, shots:[{scene, chunks, lead, tail, hud, hud_at, card, source, params, sfx, music, trans, capY, dur, voice}]}.
voice.py → timeline.json + voice.wav + partN.srt. render/index.html loads the art kit + scenes; scenes[name](localTime, params, shot) → SVG string; an overlay layer draws captions, HUD, cards, source chips, labels and transitions.
Render with Playwright + Chromium at 1920×1080, stepping renderAt(t) per frame, streaming JPEG frames to ffmpeg stdin; support --workers N and --from/--to for partial renders. Mix voice + SFX + music (ducking, loudnorm), mux, H.264 CRF 18, yuv420p, +faststart, AAC 192 kbps.
QA: contact sheet per part; captions never cover faces; every statistic has a source chip; no markup spoken; −14 LUFS; no accidental black frames; facts.md fully ✅.

7. RULES FOR TONE
Respectful. This happened to real families. No gore, no bodies in close-up, no sensational music during deaths. Local beliefs are shown with dignity. The documentary payoff is understanding and prevention, ending on the degassing pipes and the people who returned.
The emotional line of the series, Part 1 end: "The lake hadn't made a sound. It didn't need to." It lands in silence.
Keep every clue fair: a viewer of Part 1 should be able to guess "gas, heavier than air" before Part 3.

8. SHOT LISTS
PART 1 — THE SILENT MORNING (full shot list; narration subject to the fact-check gate)
[cold_open] Dawn mist over a green valley. Absolute stillness. A bird lies in the grass in the foreground (silhouette, no detail).
VO: ONE MORNING IN AUGUST 1986, A WHOLE VALLEY WOKE UP SILENT.
HUD DATE 22 AUG 1986 · TIME 06:10 · music → stop · sfx wind
[cold_open2] Slow pan across a village: smoke-less cooking fires, open doorways, a bicycle on its side, cattle lying still on the hillside.
VO: NO BIRDS. NO INSECTS. NO CATTLE CALLING. AND IN HOUSE AFTER HOUSE, NO ONE GOT UP.
sfx wind · tail 1.0
[title] Title card. VO: (no narration) · HUD hidden/reset · sfx whoosh, impact · 3.0s · PART 1 · THE SILENT MORNING
[map_zoom] Map zoom: Africa → Cameroon → the north-west highlands → a small round crater lake.
VO: THIS IS LAKE NYOS, IN THE HIGHLANDS OF NORTH-WEST CAMEROON.
HUD LOCATION LAKE NYOS · music → village · sfx whoosh, tick
[lake_beauty] The lake from the crater rim: deep blue, steep green walls, clouds reflected.
VO: A DEEP, *BLUE* CRATER LAKE. FOR GENERATIONS, FAMILIES FARMED AND HERDED CATTLE IN THE VALLEYS BELOW.
sfx birds, water
[village_day] Market day in the valley village: huts, a cooking fire, children running, cattle.
VO: LIFE HERE FOLLOWED THE SEASONS. AUGUST MEANT RAIN.
sfx birds, cattle
[ama_intro] Composite herder Ama with her cattle at the valley edge; COMPOSITE label pops in.
VO: TO SHOW WHAT SURVIVORS LATER DESCRIBED, WE'LL FOLLOW ONE COMPOSITE FAMILY.
NAME TAG AMA · HERDER · COMPOSITE CHARACTER · sfx cattle
[ngum] Ngum herding a calf uphill, laughing; Ama calls him back down for supper.
VO: HER SON NGUM LIKED TO SLEEP UP ON THE HILLSIDE WITH THE HERD.
sfx birds
[evening] Evening 21 August: lamps lit, the family eating, rain clouds over the crater.
VO: ON THE EVENING OF AUGUST 21ST, NOTHING SEEMED DIFFERENT.
HUD DATE 21 AUG 1986 · TIME 19:40 · music → night · sfx crickets
[rumble] Night. Ama looks up: a distant low rumble from the direction of the crater.
VO: AROUND NINE THIRTY, SOME PEOPLE NEAR THE LAKE REPORTED A *RUMBLE*.
HUD TIME 21:30 · sfx rumble · card EVIDENCE #1 "A RUMBLE FROM THE LAKE"
[lake_night] The lake at night from the rim: the surface heaves; a pale mist rises from the water.
VO: AT THE LAKE ITSELF, SOMETHING ROSE FROM THE WATER. NO ONE WAS THERE TO SEE IT CLEARLY.
music → dread · sfx gas_hiss, water
[gas_flow] Wide valley shot: a translucent grey layer pours over the crater lip and flows downhill, hugging the ground; the colours it touches desaturate.
VO: AN INVISIBLE CLOUD STARTED MOVING. NOT UP. *DOWN*.
HUD CO₂ CLOUD MOVING · DISTANCE 2 KM (at 70%) · sfx gas_hiss
[uphill_downhill] Split screen: Ngum asleep with the herd on the hillside (colour intact) / the village lower in the valley (being greyed out).
VO: IT FILLED THE LOW GROUND FIRST. THE VALLEYS. THE VILLAGES.
sfx crickets
[silence] The village under the grey layer. The cricket bed fades out to nothing. Lamps keep burning. Nothing moves.
VO: (no narration)
music → stop · sfx crickets (fade out) · 4.0s
[distance] Map: the cloud's path spreading down several valleys; distance markers tick up.
VO: IT TRAVELLED FOR KILOMETRES. SOME VILLAGES WERE MORE THAN TEN KILOMETRES AWAY.
HUD DISTANCE 10+ KM (at 60%) · source "Source: [verify]" · sfx tick, tick
[dawn_ngum] Dawn on the hillside: Ngum wakes, cattle around him lying still. He calls out. No answer.
VO: NGUM WOKE UP ON THE HILL. THE CATTLE AROUND HIM DIDN'T.
HUD DATE 22 AUG 1986 · TIME 06:10 · sfx wind
[run_down] Ngum running down the path toward the village, the camera tracking alongside.
VO: HE RAN DOWN TO THE VILLAGE.
sfx run, heartbeat
[village_empty] The village at dawn: open doors, a pot on a dead fire, an oil lamp burned out, a dropped bowl. No bodies shown.
VO: SURVIVORS DESCRIBED THE SAME THINGS. NO FIRE. NO WOUNDS. NO SIGN OF A STRUGGLE.
card EVIDENCE #2 "NO WOUNDS. NO FIRE." · sfx impact
[ama_wakes] Ama waking on the floor of her house, dazed, lamp light, holding her head. (Composite; she survives.)
VO: SOME WHO SURVIVED HAD BEEN UNCONSCIOUS FOR HOURS. THEY WOKE UP CONFUSED, WEAK, NOT KNOWING WHY.
card EVIDENCE #3 "SURVIVORS WOKE HOURS LATER" · sfx heartbeat
[hill_vs_valley] Diagram of the valley: green dots high, grey dots low. Ngum's position marked on the hill.
VO: AND THE PATTERN WAS STRANGE. PEOPLE ON *HIGHER* GROUND OFTEN LIVED.
card EVIDENCE #4 "HIGH GROUND SURVIVED" · music → dread · sfx tick
[lake_red] The crater rim in daylight: the lake is now rusty red-brown, flattened vegetation along one shore.
VO: THEN SOMEONE CLIMBED TO THE LAKE. THE BLUE WATER HAD TURNED *RUST RED*.
card EVIDENCE #5 "THE LAKE TURNED RED" · sfx wind, impact
[toll] Black screen, a single line of white text with the verified toll and source chip.
VO: ABOUT [VERIFIED NUMBER] PEOPLE DIED THAT NIGHT. AND THOUSANDS OF ANIMALS.
HUD LIVES LOST [VERIFIED] (at 50%) · source "Source: [verify]" · music → stop · tail 1.5
[world_asks] Newspaper-style montage drawn in flat vector (no real logos): headlines with question marks.
VO: THE WORLD WANTED TO KNOW WHAT KILLED THEM. THE FIRST ANSWERS WERE ALL WRONG.
music → dread · sfx paper, whoosh
[evidence_board] Cork board with the 5 evidence tags pinned and connected with string.
VO: SILENCE. NO WOUNDS. HIGH GROUND SAFE. A RED LAKE. WHAT KIND OF KILLER LEAVES ONLY THAT?
sfx pencil, tick
[final_line] The lake at dusk, perfectly calm and still.
VO: THE LAKE HADN'T MADE A SOUND. IT DIDN'T NEED TO.
music → stop · tail 2.0
[endcard] End card · HUD hidden/reset · sfx whoosh · 4.5s · NEXT PART 2 · THE THEORIES · CTA "WHAT DO YOU THINK HAPPENED? COMMENT ONE WORD"

PART 2 — THE THEORIES (write the full shot list from this beat sheet, same format, 45–60 shots, after the fact-check gate)
Beats: recap (the 5 evidence tags) → title → helicopters and aid arriving, the scale of loss (respectful, no bodies) → THEORY #1 chemical weapon / bomb (why people suspected it; why it didn't fit: no crater, no blast damage) → THEORY #2 volcanic eruption (why it fit partly: volcanic region; why not: no lava, no heat, lake not boiling, verify) → THEORY #3 local beliefs about the lake (respectful, told as cultural context, never mocked) → investigators arrive: boat, sample bottles, measurements; a sample bottle from the deep water fizzes when brought up (the "soda" clue) → Lake Monoun 1984 flashback: a smaller similar event two years earlier → the evidence board re-sorted: each THEORY card struck through in red, the gas idea circled → cliffhanger: an investigator drops a bottle on a rope into the depths, it comes up and the cap pops → end card CTA "WHAT WAS IN THE BOTTLE?".

PART 3 — THE LAKE THAT BREATHES (write the full shot list from this beat sheet)
Beats: recap → title → SCIENCE #1 CO₂ from below seeps into the deep water → SCIENCE #2 layers: cold, dense deep water holds the gas under pressure (lake cross-section diagram) → SCIENCE #3 the soda bottle analogy (shake/open → fizz) → SCIENCE #4 the trigger (landslide, rain, wind or overturn; present the uncertainty honestly) → SCIENCE #5 why the gas flowed down (CO₂ heavier than air; animation of the cloud as a liquid) → CLUE REPLAY section: split cards WHAT THEY SAW → WHAT IT WAS for each Part 1 evidence tag (silence → animals asphyxiated; no wounds → CO₂; woke hours later → edge of the cloud; high ground → heavy gas; red lake → iron-rich deep water) → the solution: degassing pipes, the fountain, the lake slowly releasing its gas → Lake Kivu: a far bigger lake with gas, monitored and partly used for energy (verify) → people returning to the valleys over the years (verify) → closing line in silence: "For one night, a lake breathed out. Now, it breathes slowly." → end card CTA "SHARE THIS WITH SOMEONE WHO LOVES SCIENCE".

Original concept: "The Wall at Ashford" by @OnlySainted (CC BY 4.0). This adaptation: a documentary template about a real event; verify everything before publishing.
