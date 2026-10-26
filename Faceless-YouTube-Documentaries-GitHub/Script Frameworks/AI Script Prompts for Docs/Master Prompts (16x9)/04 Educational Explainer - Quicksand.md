Master prompt adapted from "The Wall at Ashford" by @OnlySainted (CC BY 4.0). Paste this whole file into a coding agent (Claude Code, or any agent that can run code, Node/Python, Playwright and ffmpeg). It researches, fact-checks, builds and renders a myth-busting science explainer, "Quicksand Won't Swallow You (But It Can Still Kill You)", with no stock assets. Everything is drawn in code, voiced with a free local TTS, and scored with synthesized or CC0 sound.

0. WHAT YOU ARE BUILDING
One horizontal (16:9) animated science explainer for YouTube:
Format: 1920×1080, 30 fps, H.264 MP4 with AAC audio, one file (video.mp4). Runtime ≈ 6–8 minutes.
Genre: myth → clues → truth. It opens like a movie scene that sells the myth, then investigates it like a mystery with 5 clues, and reveals the real (less obvious) danger plus what to actually do. The "twist" is the true science; every early detail must be consistent with it.
Look: flat-vector 2D (SVG drawn in code), retro adventure-movie palette for the myth, clean lab/diagram style for the science; cinematic gradients, vignette, grain.
Every frame is a pure function of time renderAt(t). No Date.now(), no unseeded Math.random().
Deliver: video.mp4, a contact sheet, an SRT, a 1280×720 thumbnail, sources.md and the source code.

0.5 MANDATORY FACT-CHECK GATE (before recording any VO)
1. Extract every factual claim from sections 1 and 8 into facts.md.
2. Verify each against primary sources (the 2005 Nature paper "Liquefaction of quicksand under stress" by Khaldoun, Eiser, Wegdam and Bonn; university press releases about it; geological survey material; reputable science outlets citing the paper). Use web search.
3. Fix numbers in the VO; soften or remove anything unverifiable; never claim certainty the source doesn't.
4. Write sources.md and put "Source:" chips on every number on screen.
5. Safety lines must stay general and correct; no claims that a method "always" works.

1. THE CONTENT BIBLE (brief, to be verified)
The myth: in old adventure movies, quicksand swallows people whole: they sink, struggle, disappear.
The truth: quicksand is a mix of sand, clay/salt and water that liquefies when disturbed. A human body is less dense than quicksand, so you can't sink completely: experiments suggest you'd sink to around the waist and then float. The real problems: (1) once you sink, the sand settles and packs around your legs, and pulling a leg out quickly takes enormous force, so you get stuck; (2) the real killers are what happens while stuck: rising tides on beaches and estuaries, exposure, exhaustion.
What to do (general guidance): don't panic or thrash; lean back to spread your weight and float; move legs slowly in small circles to let water flow back in around them; work out slowly toward firm ground; call for help; avoid known quicksand/tidal mud areas, especially with an incoming tide.
5 clues (CLUE #N cards):
| # | Clue | What it shows |
|---|---|---|
| 1 | Density | You float in water; quicksand is denser than water, so you float even more |
| 2 | The experiment | Researchers made lab quicksand and dropped beads with the density of a human: they didn't sink to the bottom |
| 3 | Shake it, it flows | Disturbance liquefies it; still, it thickens again: why you get stuck, not swallowed |
| 4 | The force | Pulling a stuck foot out fast needs a huge force (check the paper's figure, often compared to lifting a car) |
| 5 | The tide | Real deaths in "quicksand" situations are usually from tides or exposure while trapped |
Myth vs fact device for the reveal section: MYTH: IT SWALLOWS YOU → FACT: YOU FLOAT AT ABOUT WAIST DEPTH; MYTH: STRUGGLE HARDER → FACT: STRUGGLING DIGS YOU IN; MYTH: GRAB A VINE AND PULL → FACT: PULLING FAST IS ALMOST IMPOSSIBLE; MYTH: THE SAND KILLS YOU → FACT: THE TIDE AND TIME DO.
Characters:
| Name | Role | Look |
|---|---|---|
| Narrator / Host "Dr. Sandy" (cartoon host) | Curious, witty science host, appears in the corner during explainers | Round head #f1c27d, safari hat, lab coat over khaki, round glasses |
| The Explorer | Myth-movie hero (1950s adventure parody) | Pith helmet, moustache, khaki shirt #c2a878 |
| Test Dummy "Dusty" | Crash-test-style dummy used in experiments | Yellow #ffd60a with black/yellow target circles |
| Hiker Noor | Real-world scenario character on a tidal flat | Rain jacket #4361ee, backpack |

2. ART DIRECTION
Canvas 1920×1080. Myth scenes: sepia-tinted jungle, vines, drum-roll lighting, letterbox bars, film scratches. Science scenes: clean light-grey lab #eef1f4 with blue-grid backgrounds, beakers, cross-section diagrams. Real-world scenes: grey estuary at low tide, mudflats, a distant incoming tide line.
Palette: sand #d9b67a / #b8925a, water #4cc9f0, lab grey #eef1f4, ink #16181d, science blue #3a86ff, warning amber #ffbe0b, danger red #ef233c, jungle #2d6a4f, sepia overlay #704214 at 20%.
Props: vines, jungle pool of quicksand, beaker with layered sand/clay/water, density scale (balance), beads, force gauge, tide chart, clock, rope, mud boots, warning sign.
Camera: slow push-ins, cross-section cutaways (camera "dives" under the sand surface), split screens myth vs fact, time-lapse of the tide.

3. TEXT ON SCREEN
Captions: Oswald 700, ALL CAPS, 1–3 words per chunk, lower third (y ≈ 900–990). Markup *word* = amber #ffbe0b, _word_ = blue #3a86ff, ~word~ = red #ef233c. Strip markup before TTS.
HUD (top-left, monospace): MYTH METER 100% · CLUES 0/5 · DEPTH 0 CM · TIDE LOW. MYTH METER drops with each clue (100 → 80 → 60 → 40 → 20 → 0%), CLUES increments, DEPTH animates when the dummy sinks, TIDE changes in the estuary scenes.
CLUE CARD: a lab-clipboard card (metal clip, graph paper, "CLUE #N" stamp in science blue) that flips in with 3D perspective, spring physics and a sheen sweep, with an impact SFX.
MYTH / FACT CARD: split card, left half sepia "MYTH" with red stamp, right half clean "FACT" with blue check.
Source chip: bottom-left, Consolas 22 px, every number.
Title card: a sepia movie-poster parody "THE SANDS OF DOOM", then a "MYTH?" stamp slams onto it. Video title: "QUICKSAND WON'T SWALLOW YOU".
End card: CTA line + Dusty the dummy floating happily in quicksand. No "follow @channel".

4. VOICE
Kokoro-82M (ONNX) + espeak-ng. Narrator Dr. Sandy = af_heart at 1.02 (warm, witty). Movie announcer (myth scenes) = am_adam at 0.92 with old-radio FX (band-pass 300–3400 Hz, light crackle). The Explorer = bm_george with exaggerated drama.
Normalise text: "g/mL" → "grams per millilitre", "2005" → "two thousand five", strip * _ ~, no abbreviation full stops.
Timing: synthesise each line, trim silence, place caption chunks by phoneme weight. Shot = lead 0.2 s + speech + tail 0.45 s.

5. SOUND & MUSIC (original only)
Moods: myth (dramatic 1950s orchestral parody: timpani, brass stabs), curious (pizzicato, marimba), lab (light electronic pulse), tension (low strings, ticking), resolve (warm pads), stop.
SFX: jungle birds, drum roll, splash, squelch, suck (mud), bubble, beaker clink, tick, ding, stamp, whoosh, impact, film projector, crackle, waves (tide), wind, heartbeat.
SFX per shot [name, at, dur]. Duck music −10 dB under voice. Master −14 LUFS, −1 dBTP.

6. ENGINE & RENDER PIPELINE
parts/video.json: {title, voice, speed, shots:[{scene, chunks, lead, tail, hud, hud_at, card, source, params, sfx, music, trans, capY, dur, voice, radio}]}. voice.py → timeline.json + voice.wav + SRT. render/index.html → scenes[name](localTime, params, shot) → SVG + overlay (captions, HUD, cards, source chips). Playwright + Chromium 1920×1080 → JPEG → ffmpeg stdin, --workers, --from/--to. Film-scratch and sepia filters only on myth shots. Mix + loudnorm, H.264 CRF 18, yuv420p, +faststart, AAC 192 kbps. QA: contact sheet, every number has a source chip, no markup spoken, −14 LUFS, facts.md fully ✅.

7. RULES FOR TONE
Playful about the movies, serious about the safety. Don't mock real victims. Safety guidance is general, sourced, and never promises a method "always works". The key line, "The sand doesn't kill you. Time does.", lands in silence before the safety section.

8. THE COMPLETE SHOT LIST (narration verbatim; subject to the fact-check gate)
[hook_movie] Sepia jungle, letterbox bars, film scratches: the Explorer steps into a pool and sinks dramatically to his chin, reaching for a vine.
VO: (announcer, radio FX) IN THE SANDS OF DOOM, ONE WRONG STEP… AND THE EARTH ITSELF WILL SWALLOW YOU WHOLE!
voice am_adam (radio) · music → myth · sfx drum_roll, squelch, projector
[hook_gone] Only his pith helmet floats on the surface. Brass stab.
VO: (no narration) · sfx bubble, impact · 1.5s
[hook_host] Freeze-frame; colour floods back; Dr. Sandy walks into frame and taps the frozen helmet.
VO: GROWING UP, I WAS SURE QUICKSAND WOULD BE A BIG PROBLEM IN MY LIFE. IT WASN'T. AND IT DOESN'T WORK LIKE THIS.
music → curious · sfx record_scratch, ding
[hook_twist] Dr. Sandy, close: "But it CAN still kill you. Just not the way you think."
VO: BUT IT CAN STILL KILL YOU. JUST ~NOT~ THE WAY YOU THINK.
music → stop · tail 0.8
[title] Title card (poster + "MYTH?" stamp) · VO: (no narration) · HUD hidden/reset · sfx stamp, whoosh · 3.0s
[what_is] Lab: a beaker with layers: sand, a little clay/salt, water; diagram labels.
VO: FIRST, WHAT IS QUICKSAND? IT'S SAND MIXED WITH WATER, AND OFTEN CLAY OR SALT, THAT TURNS RUNNY WHEN YOU DISTURB IT.
HUD MYTH METER 100% · CLUES 0/5 · DEPTH 0 CM · TIDE LOW · music → lab · sfx beaker_clink
[where] Map icons: riverbanks, beaches, estuaries, marshes, springs.
VO: IT FORMS WHERE WATER SOAKS INTO SAND: RIVERBANKS, BEACHES, MARSHES, TIDAL FLATS.
sfx pop, pop, pop
[clue1] CLUE #1 card: DENSITY · sfx impact
[density] Balance scale: a person icon vs water: the person floats; then vs quicksand: floats higher.
VO: YOU FLOAT IN WATER BECAUSE YOUR BODY IS ABOUT AS DENSE AS WATER. QUICKSAND IS *DENSER* THAN WATER. SO IN QUICKSAND, YOU FLOAT EVEN MORE.
HUD MYTH METER 80% · CLUES 1/5 (at 80%) · source "Source: [verify]" · sfx tick, ding
[clue2] CLUE #2 card: THE EXPERIMENT · sfx impact
[lab_paper] A stylised journal page with "2005" and a lab bench; Dr. Sandy points at it.
VO: IN TWO THOUSAND FIVE, RESEARCHERS MADE QUICKSAND IN A LAB AND TESTED IT.
source "Source: Khaldoun et al., Nature, 2005 (verify)" · sfx page_flip
[beads] Cross-section: beads with the density of a human body dropped into lab quicksand stop partway down.
VO: THEY DROPPED IN BEADS AS DENSE AS A HUMAN BODY. THEY SANK PARTWAY… AND STOPPED.
sfx bubble, tick
[dummy_sink] Dusty the dummy steps into quicksand; DEPTH counter climbs and stops at waist height.
VO: SCALE THAT UP TO A PERSON, AND YOU'D SINK TO ABOUT YOUR *WAIST*. THEN YOU'D FLOAT.
NAME TAG DUSTY · TEST DUMMY · HUD DEPTH ~100 CM (at 70%) · HUD MYTH METER 60% · CLUES 2/5 · sfx squelch, ding
[myth_card1] MYTH/FACT card: IT SWALLOWS YOU WHOLE → YOU STOP AROUND WAIST DEPTH · sfx stamp
[clue3] CLUE #3 card: SHAKE IT, IT FLOWS · music → curious · sfx impact
[liquefy] Cross-section animation: sand grains locked together; a foot steps in, the structure collapses, water rushes between grains (runny); then grains settle and pack tight around the leg.
VO: WHEN YOU STEP IN, THE SAND'S STRUCTURE COLLAPSES AND IT FLOWS. BUT THEN THE SAND SETTLES AND PACKS AROUND YOUR LEGS. THICKER THAN BEFORE.
HUD MYTH METER 40% · CLUES 3/5 · sfx squelch, suck
[struggle] The Explorer (sepia) thrashing; cross-section shows him packing himself in tighter.
VO: AND THE MORE YOU THRASH AROUND, THE MORE YOU SHAKE IT UP, AND THE MORE STUCK YOU GET.
sfx splash, suck, suck
[myth_card2] MYTH/FACT: STRUGGLE HARDER → STRUGGLING DIGS YOU IN · sfx stamp
[clue4] CLUE #4 card: THE FORCE · music → tension · sfx impact
[force] A force gauge attached to Dusty's foot; the needle spins into the red; a car silhouette appears on the other side of a balance.
VO: HOW HARD IS IT TO PULL A STUCK FOOT OUT QUICKLY? THE RESEARCHERS ESTIMATED A FORCE COMPARABLE TO *LIFTING A CAR*.
HUD MYTH METER 20% · CLUES 4/5 · source "Source: Khaldoun et al., 2005 (verify figure)" · sfx tick, tick, impact
[vine] The Explorer pulled by a vine, stretching comically, not budging.
VO: SO THE CLASSIC MOVIE RESCUE, GRABBING A VINE AND YANKING? THAT'S THE ONE THING THAT WON'T WORK.
sfx stretch, squelch · tail 0.8
[myth_card3] MYTH/FACT: GRAB A VINE AND PULL → PULLING FAST IS ALMOST IMPOSSIBLE · sfx stamp
[clue5] CLUE #5 card: THE TIDE · sfx impact
[estuary] Grey estuary at low tide: Hiker Noor crossing a mudflat, the sea far away.
VO: NOW LET'S LEAVE THE MOVIES. THIS IS A TIDAL FLAT. AT LOW TIDE, IT LOOKS LIKE A SHORTCUT.
NAME TAG NOOR · HIKER · HUD TIDE LOW · music → tension · sfx wind, gulls
[stuck] Noor steps into soft mud and sinks to the knees; she can't pull free.
VO: ONE SOFT PATCH, AND YOU'RE STUCK TO THE KNEES. YOU WON'T SINK ANY FURTHER.
HUD DEPTH 50 CM · sfx squelch, suck
[tide_coming] Time-lapse: the tide line advancing across the flat toward her; a clock spins.
VO: BUT THE TIDE DOESN'T CARE THAT YOU'RE FLOATING. IT KEEPS COMING IN.
HUD TIDE RISING (at 40%) · HUD MYTH METER 0% · CLUES 5/5 · sfx waves, clock
[real_danger] Montage of the real risks as icons: rising water, cold, exhaustion, being far from help.
VO: IN REAL CASES, THE DANGER IS USUALLY WHAT HAPPENS WHILE YOU'RE STUCK: THE TIDE, THE COLD, EXHAUSTION.
source "Source: [verify with coastguard / geological survey material]" · sfx tick
[key_line] Close on the waterline creeping toward the camera. Silence.
VO: THE SAND DOESN'T KILL YOU. TIME DOES.
music → stop · tail 1.5
[myth_card4] MYTH/FACT: THE SAND KILLS YOU → THE TIDE AND TIME DO · sfx stamp
[escape_title] Clean card "IF YOU EVER GET STUCK" · music → resolve · sfx ding
[escape1] Dusty demonstrates: stops moving, calm breathing icon.
VO: ONE: DON'T PANIC AND DON'T THRASH.
sfx tick
[escape2] Dusty leans back, arms out, floating on the surface to spread his weight.
VO: TWO: LEAN BACK AND SPREAD YOUR WEIGHT. LET YOURSELF FLOAT.
sfx tick
[escape3] Cross-section: Dusty's leg moving in small slow circles; water flows back around it; the leg slowly frees.
VO: THREE: MOVE YOUR LEGS SLOWLY, IN SMALL CIRCLES, SO WATER CAN FLOW BACK IN AROUND THEM.
sfx tick, squelch
[escape4] Dusty slowly working toward firm ground; phone icon "CALL FOR HELP".
VO: FOUR: WORK YOUR WAY SLOWLY TO FIRM GROUND, AND CALL FOR HELP EARLY.
sfx tick
[escape5] A warning sign on a tidal flat; a tide chart icon.
VO: AND BEST OF ALL: KNOW THE TIDE TIMES, AND STAY OFF MUDFLATS AND SANDBARS WHEN THE TIDE IS COMING IN.
source "Source: [verify]" · sfx ding
[recap] Quick recap of the 5 clue cards spinning into a stack; the MYTH METER at 0%.
VO: SO, NO. QUICKSAND WON'T SWALLOW YOU. BUT IT WILL HOLD YOU STILL. AND THAT CAN BE ENOUGH.
music → resolve · sfx whoosh
[movie_fix] Back to the sepia movie: the Explorer, now calm, leans back and floats, giving a thumbs-up. Helmet still on.
VO: (announcer) IN THE SANDS OF DOOM… HE FLOATED. AND WAS SLIGHTLY INCONVENIENCED.
voice am_adam (radio) · sfx projector, drum_roll (short)
[endcard] End card: Dusty floating happily. HUD hidden/reset · sfx whoosh · 4.5s · CTA "WHICH MOVIE MYTH SHOULD WE BUST NEXT?"

Original concept: "The Wall at Ashford" by @OnlySainted (CC BY 4.0). This adaptation: an educational explainer template; verify every fact before publishing.
