Master prompt adapted from "The Wall at Ashford" by @OnlySainted (CC BY 4.0). Paste this whole file into a coding agent (Claude Code, or any agent that can run code, Node/Python, Playwright and ffmpeg). It builds and renders a complete single-episode rule-horror video, "If The Sea Ever Leaves The Beach… FOLLOW THE BELL" (The Rules of Kalani Bay), with no stock assets. Everything is drawn in code, voiced with a free local TTS, and scored with synthesized or CC0 sound.

0. WHAT YOU ARE BUILDING
One horizontal (16:9) animated rule-horror video for YouTube:
Format: 1920×1080, 30 fps, H.264 MP4 with AAC audio, one file (video.mp4). Runtime ≈ 7–8 minutes.
Genre: "If You See [ordinary thing]… [COMMAND]" survival-guide horror with a protector twist. The feared figure is the one trying to save everyone; the real danger is a natural hazard (a tsunami). Every early detail must work on a second viewing.
Look: flat-vector 2D (SVG drawn in code), tropical beach palette that goes sickly and overcast as the rules break, cinematic gradients, heat haze, vignette, grain.
Every frame is a pure function of time renderAt(t). No Date.now(), no unseeded Math.random().
Deliver: video.mp4, a contact sheet (one still per shot), an SRT, a 1280×720 thumbnail, and the source code.

1. THE STORY BIBLE
Setup: Kalani Bay, a small fictional island beach town. Maya (14) and her little brother Kai (9) are spending the summer with their Aunt Lei. On the first day, older cousins hand them a laminated card, "THE RULES OF KALANI BAY", a local legend every kid "has to follow". Everyone in town jokes about the Bell Man: an old fisherman, Teo, who walks the beach ringing a brass bell and shouting at tourists. The rules turn him into a monster.
The rules (shown as 3D cards):
1. NEVER FOLLOW THE BELL MAN.
2. IF THE GROUND SHAKES, STAY INSIDE AND WAIT.
3. IF THE SEA STEPS BACK, PICK UP WHAT IT LEAVES. (the "gifts")
4. NEVER LISTEN TO THE ROAR.
5. STAY OFF THE HILL ROAD. (red)
MAYA'S RULE #6: FOLLOW THE BELL. (finale)
Seen → truth (the replay section uses WHAT WE SAW → WHAT IT WAS):
| Shown early | Truth |
|---|---|
| Teo's bell, shouting "UP! UP!" | He's warning people to go to high ground |
| Teo always points at the hill road | The evacuation route |
| "Gifts" left by the sea: fish flapping on bare sand | The sea drawing back before a tsunami |
| The ground shaking at breakfast "is normal here" | An offshore earthquake |
| Birds leaving the beach, dogs pulling inland | Animals reacting to the quake / sea |
| The "roar" from the horizon | The sound of the approaching wave |
| Faded blue signs with a wave and an arrow | Tsunami evacuation route signs |
| Teo's family photo in the bait shop, dated years ago | He lost family to a wave and has warned people ever since |
Characters (keep identical):
| Name | Role | Look |
|---|---|---|
| Maya (narrator, 14) | Cautious, rule-follower | Round head #8d5a3b skin, black curly bun, teal tank top #2a9d8f, white shorts, red sandals |
| Kai (9) | Curious, notices things | Yellow T-shirt #f4c542, blue shorts, oversized sunhat |
| Aunt Lei | Runs a beach café, busy, distracted | Floral dress #e76f51, apron, glasses on head |
| Cousins Nalu and Pika (16) | Hand out the rules as a prank-tradition | Board shorts, sunglasses |
| Teo, "the Bell Man" | Old fisherman | Very tall in Maya's imagination (shot low, long shadow), grey beard, yellow raincoat #e9c46a, brass bell; truth mode = a kind, tired old man |
Figures: round heads with dark outline, dot eyes, brows, simple mouths, stroke limbs, round hands, soft shadow; procedural walk/run cycles, breathing, blinking. No gore at any time; the wave is shown as a wall of water and spray, people are never shown hurt.

2. ART DIRECTION
Canvas 1920×1080. Layers: sky gradient → far ocean horizon → mid sea with animated wave lines → beach sand → town (pastel wooden houses, café, bait shop, palm trees) → characters → foreground (palm leaves, beach umbrellas, slight blur) → weather (haze, spray, flying birds, dust) → vignette → grain 6%.
Palette: sky #8ecae6 → #fefae0, sea #219ebc / #126782, sand #f2d7a6, palm #2d6a4f, sunset #f4a261 → #e76f51, storm grey #6c757d, warning yellow #ffd166, alarm red #e63946.
Props as functions: brass bell, laminated rule card, blue evacuation sign (wave + arrow), bait shop, café tables, flip-flops, fish on sand, seashells, dog on a leash, hill road with switchbacks, bell tower.
Camera: slow push-ins, lateral beach tracking, low angles on Teo (to make him tall and scary in early shots), handheld shake during the quake, a dramatic pull-back reveal of the bare seabed.

3. TEXT ON SCREEN
Captions: Oswald 700, ALL CAPS, 1–3 words per chunk, lower third (y ≈ 900–990). Thick black stroke, spring pop. Markup *word* = yellow #ffd166, _word_ = teal #2ec4b6, ~word~ = red #ff4a3d. Strip markup before TTS.
HUD (top-left, monospace): TIME 10:42 · SEA LEVEL NORMAL · RULES BROKEN 0 · BELL HEARD 0. In the replay section the HUD rewrites: SEA LEVEL NORMAL → SEA LEVEL −80 M (DRAWBACK), RULES BROKEN → LIVES SAVED.
RULE CARD: a laminated beach-card look (glossy plastic, rounded corners, sun-faded edges, a black chip "RULE #N"), flips in with 3D perspective, spring, sheen sweep, impact SFX; red variant for rule 5; handwritten variant (marker on cardboard) for Maya's rule 6.
Name tags: callout line + "NAME · ROLE".
Title card: the beach at dusk, a bell silhouette swinging, text "THE RULES OF KALANI BAY".
End card: CTA line + bell silhouette swinging, no "follow @channel".

4. VOICE
Kokoro-82M (ONNX) + espeak-ng. Maya = af_bella at 1.03. Kai = af_sky at 1.08. Aunt Lei = af_heart. Nalu = am_puck. Teo = bm_george at 0.9 (gravelly; add light lowpass when heard from far away).
Normalise text before TTS: strip * _ ~, "10:42" → "ten forty-two", "Mr." → "mister", no abbreviation full stops.
Timing: synthesise each line, trim silence, place caption chunks by phoneme weight. Shot length = lead 0.2 s + speech + tail 0.45 s.

5. SOUND & MUSIC (original only)
Moods: summer (ukulele-like plucks, light shaker), uneasy (detuned pads, slow pulse), dread (sub drone, metallic swells), run (driving drums), stop (silence).
SFX: waves, gulls, wind, bell, crowd, rumble (quake), rattle (dishes), dog bark, birds flap, fish flop, roar (distant growing wave), whoosh, impact, tick, run, heartbeat, siren (distant), glitch, rewind.
Every SFX = [name, at seconds, duration]. Duck music −10 dB under voice. Master −14 LUFS, −1 dBTP.

6. ENGINE & RENDER PIPELINE
parts/video.json: {title, voice, speed, shots:[{scene, chunks, lead, tail, hud, hud_at, card, params, sfx, music, trans, capY, dur, voice}]}. voice.py → timeline.json + voice.wav + SRT. render/index.html → scenes[name](localTime, params, shot) → SVG; overlay for captions, HUD, cards, tags, transitions. Playwright + Chromium at 1920×1080 → JPEG frames → ffmpeg stdin; --workers, --from/--to. Mix + loudnorm, H.264 CRF 18, yuv420p, +faststart, AAC 192 kbps. QA: contact sheet, captions never over faces, no markup spoken, −14 LUFS, no accidental black frames.

7. RULES FOR TONE
Creepy, never gory. The wave is spectacle and sound, never bodies. The emotional core: Maya protecting Kai, and Teo's grief. The key line, "He wasn't chasing us. He was the only one running toward the sea to warn everyone.", lands in silence.
REAL-SCIENCE OUTRO (≈45 s, calm documentary register): natural tsunami warnings (strong or long earthquake near the coast, the sea suddenly drawing back, a loud roar from the ocean) mean go to high ground or inland immediately, without waiting for an official alert; follow evacuation signs; stay away until officials say it's safe. Verify these points against NOAA/tsunami.gov or your national agency before rendering, and show "Source:" chips. Optional: the widely reported 2004 story of a child who recognised the drawback from a school lesson and helped clear a beach (verify details before using).

8. THE COMPLETE SHOT LIST (narration verbatim, build every shot)
[hook] Bright beach morning. Far down the sand, a tall figure in a yellow raincoat rings a bell and points at Maya. Low angle, long shadow.
VO: IF YOU EVER HEAR A BELL ON KALANI BAY… DON'T FOLLOW IT.
music → uneasy · sfx bell, waves, gulls
[hook2] Quick cut: the laminated rules card slapped onto a café table.
VO: THAT'S WHAT THE RULES SAID. WE FOLLOWED THEM. ALMOST ALL OF THEM.
sfx impact
[title] Title card · VO: (no narration) · HUD hidden/reset · sfx whoosh, bell · 3.0s
[arrival] Ferry arriving at a pastel island town; Maya and Kai with backpacks; Aunt Lei waving from her café.
VO: SUMMER. MY BROTHER KAI AND I WERE SENT TO STAY WITH AUNT LEI.
NAME TAG MAYA · ME · NAME TAG KAI · MY BROTHER · 9 · NAME TAG AUNT LEI · CAFÉ OWNER · music → summer · sfx waves, gulls
[cousins] Cousins Nalu and Pika lounging on surfboards; Nalu hands Maya the laminated card with a grin.
VO: OUR COUSINS GAVE US A CARD. "EVERY KID HERE FOLLOWS THESE. NO EXCEPTIONS."
NAME TAG NALU & PIKA · COUSINS · voice am_puck for Nalu line · sfx paper
[rulecard] RULE #1: "NEVER FOLLOW THE BELL MAN." · VO: RULE ONE: NEVER FOLLOW THE BELL MAN. · sfx impact
[bellman_far] Down the beach, Teo ringing his bell at tourists who laugh and wave him off.
VO: THE BELL MAN WALKED THE BEACH EVERY DAY. RINGING. SHOUTING. POINTING AT THE HILL.
HUD TIME 10:42 · SEA LEVEL NORMAL · RULES BROKEN 0 · BELL HEARD 1 · sfx bell, crowd
[legend] Nalu's campfire story illustration: Teo drawn as a monster with glowing eyes leading kids into the sea.
VO: NALU SAID HE LEADS KIDS AWAY. AND THEY NEVER COME BACK.
music → dread · sfx wind
[signs] Kai points at a faded blue sign with a wave and an arrow pointing uphill. Maya shrugs.
VO: KAI ASKED WHAT THE BLUE SIGNS MEANT. NOBODY KNEW. OR NOBODY CARED.
music → summer · sfx gulls
[rulecard] RULE #2: "IF THE GROUND SHAKES, STAY INSIDE AND WAIT." · VO: RULE TWO: IF THE GROUND SHAKES, STAY INSIDE AND WAIT. · sfx impact
[rulecard] RULE #3: "IF THE SEA STEPS BACK, PICK UP WHAT IT LEAVES." · VO: RULE THREE: IF THE SEA STEPS BACK, PICK UP WHAT IT LEAVES. NALU CALLED THEM GIFTS. · sfx impact
[rulecard] RULE #4: "NEVER LISTEN TO THE ROAR." · VO: RULE FOUR: NEVER LISTEN TO THE ROAR. · music → uneasy · sfx impact
[rulecard] RULE #5 (red): "STAY OFF THE HILL ROAD." · VO: AND RULE FIVE: STAY OFF THE HILL ROAD. THAT'S WHERE HE LIVES. · sfx impact, hit
[days] Montage of happy days: snorkelling, café shifts, Teo always in the background ringing, pointing up the hill.
VO: FOR TWO WEEKS, NOTHING HAPPENED. EXCEPT THE BELL. EVERY DAY.
HUD BELL HEARD 14 (at 80%) · music → summer · sfx bell, waves
[bait_shop] Maya and Kai hide behind shelves in the bait shop as Teo walks in. On the wall: an old photo of Teo with a woman and a little girl, faded.
VO: ONCE WE HID FROM HIM IN THE BAIT SHOP. HE JUST BOUGHT ROPE. AND LOOKED AT AN OLD PHOTO FOR A LONG TIME.
music → stop · sfx tick
[breakfast_quake] Morning at the café: cups rattle, a lamp sways, the ground shakes for a long time. Aunt Lei laughs nervously.
VO: THEN ONE MORNING, THE GROUND SHOOK. LONGER THAN I'VE EVER FELT.
HUD TIME 09:12 · sfx rumble, rattle · handheld shake
[stay_inside] Maya pulls Kai under a table, clutching the card.
VO: RULE TWO. WE STAYED INSIDE. AND WE WAITED.
sfx heartbeat
[animals] Through the window: birds leave the beach in a cloud; a dog drags its owner inland.
VO: THE BIRDS LEFT FIRST. THEN THE DOGS STARTED PULLING AWAY FROM THE WATER.
music → uneasy · sfx birds_flap, dog_bark
[bell_far] Teo's bell, frantic, getting closer; his voice far away: "UP! UP! EVERYBODY UP!"
VO: AND THEN THE BELL. FASTER THAN EVER.
HUD BELL HEARD 15 · voice bm_george (far, lowpass) · sfx bell, bell, bell
[sea_steps_back] The beach from the café deck: the waterline pulls back fast, revealing wet sand, rocks, coral and flapping fish. Tourists walk out to look.
VO: THE SEA *STEPPED BACK*. FARTHER THAN THE LOWEST TIDE. LIKE SOMEONE PULLED A PLUG.
HUD SEA LEVEL FALLING (at 50%) · music → dread · sfx waves (receding), fish_flop
[gifts] Kai runs onto the bare seabed toward the flapping fish and shells; Nalu and Pika already out there laughing.
VO: KAI RAN OUT FOR THE GIFTS. RULE THREE. EVERYONE WAS DOING IT.
HUD RULES BROKEN 0 · sfx run, crowd
[teo_runs] Teo running onto the sand TOWARD the kids, ringing the bell, yellow coat flapping. Low angle: he looks huge.
VO: AND THE BELL MAN WAS RUNNING STRAIGHT AT MY BROTHER.
sfx bell, run, heartbeat
[rule1_card] RULE #1 slams back in: "NEVER FOLLOW THE BELL MAN." · VO: (no narration) · sfx impact · 1.6s
[teo_grabs] Teo scoops Kai up and runs up the beach toward the hill road. Maya screams and chases.
VO: HE GRABBED KAI. AND HE RAN. *UP*.
sfx run, run · music → run
[roar] A low roar grows from the horizon. Maya turns: a white line on the horizon, getting thicker.
VO: THEN I HEARD THE ROAR. RULE FOUR SAID DON'T LISTEN. I LISTENED.
HUD SEA LEVEL WAVE INCOMING · sfx roar
[hill_road] Maya on the hill road switchbacks, chasing Teo; blue evacuation arrows on every sign she passes.
VO: I BROKE RULE FIVE. I RAN UP THE HILL ROAD. EVERY BLUE SIGN WAS AN ARROW. POINTING *UP*.
HUD RULES BROKEN 3 (at 60%) · sfx run, roar, heartbeat
[bell_tower] Teo reaches a bell tower at the top, sets Kai down, and rings the big town bell, again and again. People start streaming up the road behind Maya.
VO: AT THE TOP HE PUT KAI DOWN. AND HE RANG THE BIG BELL. AGAIN. AND AGAIN.
sfx bell (big), crowd, roar
[wave] From the hilltop: the wave washes over the beach and the lower town in a wall of white water and spray (no people visible in the water). Shot is wide and distant.
VO: (no narration)
music → stop · sfx roar, whoosh · 4.0s
[silence] Close on Maya, Kai and Teo, breathing, watching. Long silence.
VO: HE WASN'T CHASING US. HE WAS THE ONLY ONE RUNNING TOWARD THE SEA TO WARN EVERYONE.
tail 2.0
[cousins_safe] Nalu and Pika stumbling up the road, soaked to the knees, staring at Teo.
VO: NALU AND PIKA MADE IT UP. BARELY.
sfx crowd
[hud_rewrite] HUD glitches: SEA LEVEL → DRAWBACK, RULES BROKEN → LIVES SAVED, BELL HEARD → WARNINGS IGNORED 15.
VO: (no narration) · sfx glitch, tick, glitch · 3.0s
[rewind] VHS rewind through earlier scenes.
VO: EVERYTHING ON THAT CARD WAS BACKWARDS.
music → uneasy · sfx rewind
[clue] Split card WHAT WE SAW: THE BELL MAN → WHAT IT WAS: THE WARNING · VO: THE BELL MAN WASN'T LEADING KIDS AWAY. HE WAS LEADING THEM UP. · sfx glitch
[clue] WHAT WE SAW: "STAY INSIDE" → WHAT IT WAS: A COASTAL EARTHQUAKE · VO: A LONG EARTHQUAKE BY THE SEA ISN'T A REASON TO WAIT. IT'S A REASON TO LEAVE. · sfx glitch
[clue] WHAT WE SAW: GIFTS → WHAT IT WAS: THE DRAWBACK · VO: WHEN THE SEA PULLS BACK LIKE THAT, IT'S COMING BACK. FAST. · sfx glitch
[clue] WHAT WE SAW: THE ROAR → WHAT IT WAS: THE WAVE · VO: THE ROAR WAS THE WAVE. · sfx glitch
[clue] WHAT WE SAW: THE HILL ROAD → WHAT IT WAS: THE EVACUATION ROUTE · VO: AND THE ROAD WE WERE TOLD TO AVOID WAS THE WAY OUT. · sfx glitch
[clue] WHAT WE SAW: AN OLD PHOTO → WHAT IT WAS: WHY HE RINGS · VO: TEO LOST HIS FAMILY TO A WAVE, YEARS AGO. HE'S RUNG THAT BELL EVERY DAY SINCE. · music → stop · sfx glitch
[teo_truth] Truth mode: Teo is a small, kind, tired old man sitting on the step; Kai hands him back his bell.
VO: UP CLOSE, HE WASN'T TALL AT ALL.
music → summer (soft)
[rulecard6] Handwritten card on cardboard: MAYA'S RULE #6 · "FOLLOW THE BELL." · VO: SO I WROTE ONE MORE RULE. FOLLOW THE BELL. · sfx marker, impact
[science] Calm documentary register: diagram of a quake under the sea, the drawback, the wave; three icons: SHAKING · SEA PULLS BACK · ROAR → arrow to HIGH GROUND. Source chips.
VO: IN REAL LIFE, THESE ARE NATURE'S WARNINGS: A STRONG OR LONG EARTHQUAKE NEAR THE COAST, THE SEA SUDDENLY PULLING BACK, OR A LOUD ROAR FROM THE OCEAN. IF YOU NOTICE ANY OF THEM, GO TO HIGH GROUND OR INLAND, RIGHT AWAY. DON'T WAIT FOR AN ALARM. AND FOLLOW THE BLUE SIGNS.
music → summer · sfx tick, tick, tick · source "Source: NOAA / tsunami.gov (verify)"
[endcard] End card · HUD hidden/reset · sfx bell, whoosh · 4.5s · CTA "WOULD YOU HAVE FOLLOWED HIM? YES / NO"

Original concept: "The Wall at Ashford" by @OnlySainted (CC BY 4.0). This adaptation: fictional one-shot; verify the science outro before publishing.
