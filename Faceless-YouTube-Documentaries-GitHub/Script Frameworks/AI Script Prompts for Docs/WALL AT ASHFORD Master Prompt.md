Open-source master prompt by @OnlySainted (on X). Paste this whole file into a coding agent (Claude Code, or any agent that can run code, Node/Python, Playwright and ffmpeg). It builds and renders the complete 6-part vertical series "The Wall at Ashford" from scratch, with no stock assets. Everything is drawn in code, voiced with a free local TTS, and scored with synthesized or CC0 sound. Licence suggestion: story and prompt CC BY 4.0. Credit "@OnlySainted" if you publish a derivative.

0. WHAT YOU ARE BUILDING
Build a 6-part vertical (9:16) animated story series for YouTube Shorts, TikTok and Reels:
Format: 1080×1920, 30 fps, H.264 MP4 with AAC audio, one file per part (part1.mp4 … part6.mp4). Each part runs ≈ 60–100 seconds.
Genre: apocalyptic survival mystery, narrated in the first person by Jess, 16. The big twist arrives in Part 5: the "monsters" were CDC medics all along, and the town was infected. Every earlier detail must work on a second viewing.
Look: flat-vector 2D illustration (SVG drawn in code), muted rural palette, cinematic lighting with gradients, vignettes, fog, rain and fire. Big bold captions with colour-highlighted keywords, a "survival HUD" tracker, and glossy 3D "RULE" cards.
Every frame is a pure function of time renderAt(t). There is no Date.now() and no unseeded Math.random(), so renders are identical and can be split across workers.
Deliver: the 6 MP4s, a contact sheet per part (one still per shot), and the source code.
1. THE STORY BIBLE (read this before you draw anything)
Setup. Ashford, Montana, population 1,140. A fungus gets into the town water (the water comes out gray). Infected people get nosebleeds, then their vision changes. They see healthy people in hazmat suits as tall black monsters with glass faces. They see the CDC's air filters as a rasping sound, dart rifles as sticks, and food crates as bait. To the infected, each other still look normal. The CDC evacuates 928 people. The 212 who hid behind a wall of buses, grain trucks and shipping containers become the "survivors". They are the infected.
The rules (Dad's, shown as 3D rule cards):
NEVER LET THEM TOUCH YOU.
BURN WHAT THEY LEAVE.
BITTEN GO OVER THE WALL.
NO ONE GOES OUT ALONE.
ANYONE WHO DEFENDS THEM IS TURNING. (red)
JESS'S RULE #6: LOOK TWICE. (finale)
What each clue really was (Part 5 replays every one as WHAT I SAW → WHAT IT WAS):
Shown early
Truth
Gray tap water (Day 1)
Fungal spores
Glass faces + rasping sound
Visors + air filters
They always come in pairs
CDC rule: never enter alone
The sticks they never swing
Dart rifles (treatment)
Mrs. Kowalski "taken"
Carried to an ambulance
1,140 → 212
928 evacuated; the 212 hid
The crates (smelled like bread)
Bread, water and ASH-7
The bitten "turn"
They were recovering
Scout's bandage
The CDC vet tent
The 9 PM voice, 47 seconds
A loudspeaker counting the days of treatment left
Toby's "nightmare" drawings
Exactly what he saw
Toby crying on Day 22
He had injected himself, could see, and was looking at gray Jess

Characters (keep them identical across all 6 parts):
Name
Role
Look (flat vector)
Jess Calloway (narrator, 16)
Brave, keeps secrets
Auburn ponytail #8a3b22, grey jacket #6f7a86, red scarf #9c2f2f, navy jeans #2f3e57
Toby (10)
Little brother, sees the truth first
Messy brown hair #6b4428, orange jacket #c8742f, blue jeans, short
Wade "Dad" Calloway
Volunteer fire chief who runs the town
Navy cap #2e3a4f, tan jacket #b88d4e with a reflective stripe, beard #6b4a30
Doc Harlan
Town doctor for 41 years
White hair, round glasses, white coat, blue shirt
Dale Pruitt
Hardware store owner, first "bitten"
Bald, grey beard, blue shirt #3d5a7a
Scout
The family dog
Shaggy golden dog. He never barks at them
Mrs. Kowalski
Neighbour
White hair, purple cardigan
Pvt. Rosa Alvarez
CDC field medic
Yellow hazmat suit, clear visor, kind face
Dr. Dana Ruiz
CDC investigator (the epilogue tent)
Lab coat, calm
The "monsters"
CDC teams seen through infected eyes
Huge black hooded silhouettes, dark glossy glass visor with a highlight, a long black "stick" on the back, sometimes a head lamp. Truth mode = a yellow suit with a "CDC" chest band, a clear visor showing a human face, a respirator and a grey dart rifle
Infected (truth mode)
How the townspeople really look
Gray skin #9fa59b, thin purple fungal crack lines, red-dark eyes. No gore

People are simple vector figures: round head with a dark outline, dot eyes, brows (worried or angry), mouths (flat, smile, frown, o, teeth), stroke-limbs with round hands, and a soft ground shadow. They're animated procedurally with walk and run cycles, breathing, blinking, idle sway and head tilt.
2. ART DIRECTION
Canvas 1080×1920 SVG, recomposed every frame. Layers: sky gradient → far hills or mountains → pine forest silhouettes → mid-ground set → characters → foreground silhouettes (grass, fence, wall edge) with slight blur for depth → weather (rain streaks, drifting dust, fog bands) → vignette → film grain.
Palette (keep it tight): skin #f1d9b0, ink #16181d, grass #5f7a43 / #7a9653, dirt #b99d6b, day sky #b9cfd6 → #e7e3d2, dusk #4b4f6b → #c98f6d, night #07090e → #1b2230, fog #c9cbc2, barn red #a8352a, school bus #e3a72a, pines #3f5b3c.
Signature props, drawn as reusable functions: houses, barn, water tower, school bus (also rusted), shipping containers, grain truck, chain-link fence, the wall ring (buses and containers in a circle, seen from the air), white crates with a red cross, burn barrel, flames, flashlight and floodlight cones, a rifle scope POV (circular mask and crosshair), chalk or explainer boards, a cork board with string.
Lighting: night scenes use cones of light and rim light; fire scenes get flickering orange light on faces; dawn and dusk scenes get long soft shadows. Add a light bloom pass on bright pixels only, so the text stays crisp.
Camera in 2D: slow push-ins, drifts, parallax between layers, handheld shake on tense beats, whip pans and zoom-blur transitions.
3. TEXT ON SCREEN
Captions: Oswald 700, ALL CAPS, 1–3 words per chunk, centred low (y ≈ 1560–1760; some shots raise them to y ≈ 640–760 so they don't cover faces). Thick black stroke and soft shadow. Each word pops in with spring easing on its own timing. Highlight markup in the script: *word* = lime #c8f53c, _word_ = orange #ffa63d, ~word~ = red #ff4a3d. Strip all markup before TTS (never let the voice read "tilde").
Survival HUD (top-left, monospace): stacked KEY VALUE rows that persist between shots: DAY 39, SURVIVORS 212, FOOD 41 DAYS, THREAT HIGH, CRATES BURNED 19, SECRETS 1, TREATMENT WINDOW 05:12:00, PATIENTS 211, FOLLOWING 209 / 211. A value that changes flashes and pops, numbers roll, and the countdowns tick in real time. hud_at = the fraction of the shot where the change lands. HUD null hides and resets it. In Part 5 the HUD glitches and rewrites itself (SURVIVORS → PATIENTS, THREAT → TREATMENT WINDOW).
3D RULE CARD: a lime metal sign (radial gradient #efff7a → #6fa806), hazard stripes top and bottom, rivets, scratches, grime, a black chip "RULE #N" and the text in Oswald 700 black. It flips in with 3D perspective and spring physics, with a light sheen sweep and an impact SFX. A red variant for the dark rules. A variant labelled "CDC NOTICE #N" for the loudspeaker messages.
Name tags: a small callout line from the character to a label "NAME" + "ROLE".
Title card (each part): an illustrated navy night with guard towers and blinking red lamps, razor wire, sweeping floodlights, a glowing green ☣. Text: "THE WALL AT ASHFORD" (stencil), a "PART N" chip and the subtitle, with spray-paint drips.
End card: "NEXT: PART N+1 · SUBTITLE" + the call-to-action line + a monster silhouette with a blinking visor lamp. Do not add "FOLLOW @channel" to end cards.
4. VOICE
Free local TTS: Kokoro-82M (ONNX) + espeak-ng. Narrator Jess = af_bella at speed 1.04 (Parts 1–4) and 1.02 (Parts 5–6). Other voices: Alvarez af_nicole, the CDC loudspeaker am_michael at 0.95 with radio FX (band-pass 450–3200 Hz, saturation, slap echo, reverb), Dad am_adam, Doc bm_george, Toby af_sky at 1.08, Dr. Ruiz af_sarah.
Normalise text before TTS: Mr. → mister, Mrs. → missus, Dr. → doctor, "1,140" → 1140, "3 A.M." → "3 eh em", strip * _ ~. Abbreviations with full stops cause unwanted pauses, so remove them.
Timing: synthesise each shot's line, trim the silence, then place each caption chunk by phoneme weight snapped to real silences in the audio. The shot length = lead (≈0.2 s) + speech + tail (≈0.45 s, longer where the script says tail).
5. SOUND & MUSIC (original only)
Music moods switched by the script: calm (soft pads, sparse piano-like plucks, guitar harmonics), dark (haunted hum, low drone, glassy tones, choir swells), build (pulsing bass hits that rise, a ratcheting arpeggio, a reverse-boom riser), stop (silence). Crossfade about 1 s. Duck the music under the voice (about −10 dB while speaking).
SFX vocabulary (synthesize or use CC0 samples): wind, rain, crickets, birds, crows, the monster rasp (a filtered breath with valve flutter: secretly the air filter), a groan (the 9 PM voice) plus slowed-down versions, fire, whoomp (ignition), impact, hit (sub boom), sting, whoosh, swoosh, tick, clock, chain, creak, run (footsteps), thump (heartbeat pairs), pencil and marker, weld, engine, murmur (crowd), bell, dart (pfft), snap, glitch, rewind, ring (tinnitus), boom, radio.
Every SFX in the shot list is [name, at seconds, duration], relative to the shot start. Add automatic whoosh SFX for whip and zoom transitions, and an impact for every card.
Master: −14 LUFS, true peak −1 dBTP, a gentle limiter.
6. ENGINE & RENDER PIPELINE
parts/partN.json holds the shot list exactly as in section 8: {part, title, voice, speed, shots:[{scene, chunks, lead, tail, hud, hud_at, card, params, tags, sfx, music, trans, capY, dur, voice, radio}]}.
voice.py turns the part JSON into timeline.json (each shot's start, duration and caption chunk times) and voice.wav.
render/index.html loads the art kit + scene functions. scenes[name](localTime, params, shot) → SVG string. The overlay layer draws the captions, HUD, cards, tags and transitions.
Render with Playwright and Chromium at 1080×1920, stepping renderAt(t) for every frame and streaming JPEG frames into ffmpeg through stdin. Motion blur: on shots flagged fast and during transitions, average 3 sub-frames with a 180° shutter. Bloom: blur the bright, saturated pixels of a caption-free frame and screen it back on.
Mix the audio (voice + SFX + music, ducking, then loudnorm), mux, and encode H.264 (CRF 17–18, +faststart), AAC 192 kbps.
QA before delivery: a contact sheet of every shot. Check that captions never cover faces, the HUD values are correct, no markup is spoken, the audio is −14 LUFS, and no shot is ever blank or black by mistake.
7. RULES FOR TONE
Scary but not gory: violence happens off-screen or in silhouette, and the infected look gray and cracked, not bloody (nosebleeds only as small red drops).
The emotional core is siblings and trust. The finale's line, "He didn't see what I saw. He just chose to trust me.", must land in silence.
Keep every clue fair. A viewer who rewatches should be able to spot all twelve.
8. THE COMPLETE SHOT LISTS (narration is verbatim; build every shot)
PART 1 — THE RULES (narrator speed 1.04)
[hook_food] Dawn, low fog. Close on the town gate (rusted bus + container wall). Two tall black hazmat silhouettes set a white crate with a red cross in the dirt, then step back. Crows lift off a fence.
VO: EVERY MORNING, THE MONSTERS LEAVE FOOD AT YOUR GATE.
sfx wind, haunt, rasp, impact, thump, crows
[hook_burn] Whip to the same crate inside the gate: Dad pours fuel, a match drops, it erupts in flame. Orange light on faces behind him.
VO: AND EVERY MORNING, YOU BURN IT.
transition whip · sfx swoosh, whoomp, hit, fire
[gate_night] Night, heavy rain. Toby (small, orange jacket) at the chained gate, pulling the chain off. Floodlit silhouettes waiting beyond. Slow push-in, lightning flicker.
VO: ON DAY 39, MY LITTLE BROTHER OPENED THE GATE.
HUD DAY 39 · transition zoom · sfx rain, chain, rasp, drone_low
[title] Illustrated animated title card: dark navy sky, guard towers with blinking red lamps, razor wire, a glowing toxic-green biohazard symbol. "THE WALL AT ASHFORD" in heavy stencil + "PART N" chip + the part subtitle, spray-paint drips, flood-light cones sweeping.
VO: (no narration)
HUD hidden/reset · sfx whoosh, hit · 2.6s · PART 1 · THE RULES
[aerial_town] High aerial: a small Montana town in a valley: grid of houses, a water tower, red barn, church, pine forest on every side, mountains behind, birds crossing. Slow drone drift.
VO: ASHFORD, MONTANA. POPULATION 1,140.
music → calm · sfx wind, birds
[kitchen] Morning kitchen. Jess at the sink; the tap runs GRAY water into a glass. Toby at the table with cereal; Dad in the doorway in his fire-chief jacket. Name tags pop in.
VO: IT STARTED ON A TUESDAY. THE WATER CAME OUT GRAY.
NAME TAG JESS · ME · NAME TAG TOBY · MY BROTHER · 10 · NAME TAG WADE · MY DAD · sfx faucet
[clinic] Small-town clinic waiting room: people holding tissues to bleeding noses, a line out the door. Doc Harlan (white hair, round glasses, white coat) with a clipboard.
VO: BY THURSDAY, HALF THE TOWN HAD NOSEBLEEDS.
NAME TAG DOC HARLAN · TOWN DOCTOR · 41 YRS · sfx murmur
[treeline_night] Night. The edge of the pine forest behind a yard. Between the trunks, several tall black figures with glassy faces stand perfectly still. Crickets stop.
VO: THEN ON FRIDAY, THEY CAME OUT OF THE TREES.
music → dark · sfx drone_dark, rasp, crickets
[monster_closeup] Extreme close-up of a "monster": a hooded black shape with a dark glass faceplate reflecting a streetlight; breath fogs. (Secretly: a CDC hazmat suit seen through infected eyes.)
VO: TALL. FACES LIKE GLASS. AND THAT SOUND.
sfx rasp, rasp
[yard_chase] Wide backyard at night: neighbours run, an old woman (Mrs. Kowalski, purple cardigan) is lifted and carried off by two tall figures toward the trees.
VO: NO ONE KNEW WHERE THEY CAME FROM. BUT WE KNEW WHAT THEY WANTED. US.
sfx run, sting, hit
[firehouse_map] Firehouse interior: Dad marks a town map pinned to a board with a red marker, volunteers around him. Name tag WADE CALLOWAY · FIRE CHIEF.
VO: MY DAD RAN THE VOLUNTEER FIRE DEPARTMENT. BY SUNDAY, HE RAN THE TOWN.
NAME TAG WADE CALLOWAY · FIRE CHIEF · music → build · sfx marker
[wall_build] Time-lapse montage: school buses, grain trucks and shipping containers pushed into a ring with sparks from welders, people hauling sheet metal, a forklift.
VO: IN 48 HOURS, WE BUILT A WALL. BUSES. GRAIN TRUCKS. SHIPPING CONTAINERS.
sfx weld, engine
[aerial_wall] Aerial zoom-out: the finished WALL ring around the town centre, tiny figures on top, empty houses outside it. HUD appears: DAY 3 · SURVIVORS 212 · FOOD 41 DAYS · THREAT HIGH.
VO: 1,140 PEOPLE LIVED IN ASHFORD. 212 MADE IT INSIDE.
HUD DAY 3 · SURVIVORS 212 · FOOD 41 DAYS · THREAT HIGH (at 75% of shot) · transition zoom · sfx wind, hit
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: DAD MADE RULES. RULE ONE: NEVER LET THEM TOUCH YOU.
CARD RULE #1: "NEVER LET THEM TOUCH YOU."
[explainer_move] Explainer board: chalky diagram of a monster silhouette with arrows: "DON'T RUN" (walking pace icon), "CAN'T CLIMB" (crossed-out ladder). Hand-drawn pencil lines animate on.
VO: HERE'S WHAT WE LEARNED. THEY DON'T RUN. THEY CAN'T CLIMB.
sfx pencil, tick, tick
[treeline_pair] Two tall figures always side by side at the treeline, mirrored poses.
VO: THEY ALWAYS COME IN PAIRS.
sfx rasp, rasp
[stick_closeup] Close-up of the long black "stick" one carries over its shoulder (secretly a dart rifle). It is never swung.
VO: THEY CARRY THESE. BUT THEY NEVER SWING THEM.
[explainer_clock] Explainer: a clock face with only DAWN and DUSK wedges lit, sun and moon icons sliding.
VO: AND THEY ONLY COME AT DAWN AND DUSK.
sfx clock
[crate_gate] Dawn: another white crate with a red cross left at the gate. Rule card #2 "BURN WHAT THEY LEAVE." slaps on screen.
VO: RULE TWO: BURN WHAT THEY LEAVE. BECAUSE SOMETIMES, THEY LEAVE THINGS.
CARD RULE #2: "BURN WHAT THEY LEAVE." · music → calm · sfx crows
[crate_fire] The crate burning in a steel barrel; Dad watching with arms crossed. HUD: CRATES BURNED 1.
VO: DAD SAID THE RED CROSS WAS A TRICK. BAIT.
HUD CRATES BURNED 1 · sfx whoomp, fire
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: RULE THREE: BITTEN GO OVER THE WALL. BECAUSE THE BITTEN... TURN.
CARD RULE #3: "BITTEN GO OVER THE WALL." · music → dark · sfx hit
[exile_wall] Grey morning on top of the wall: a bandaged man is lowered over the side on a rope while the town watches; he is strangely calm.
VO: WE LOST THREE PEOPLE THAT WAY THE FIRST WEEK. THE WORST PART WASN'T THE SCREAMING. IT WAS HOW CALM THEY GOT BEFORE.
HUD DAY 6 · sfx creak, creak, wind
[night_watch] Jess on the wall at night with a flashlight and Scout (shaggy golden dog). Stars, treeline far off. Name tag SCOUT · OUR DOG.
VO: I TOOK THE NIGHT WATCH. ME AND SCOUT.
HUD DAY 8 · NAME TAG SCOUT · OUR DOG · music → calm · sfx crickets
[scout_wag] Scout's tail thumping happily while he stares at the dark treeline where figures stand.
VO: SCOUT NEVER BARKED AT THEM. DAD SAID HE WAS TOO DUMB TO BE SCARED.
sfx thump, thump, thump, crickets
[canteen] School-gym canteen: tins and water jugs on tables, a hand-written RULES sheet taped to the wall. HUD FOOD 38 DAYS.
VO: WE HAD FOOD. WE HAD WATER. WE HAD RULES.
HUD FOOD 38 DAYS (at 20% of shot) · sfx tick
[ashes] Morning: Toby crouched in the burn pit ashes, pulling out a scorched metal case. Music cuts.
VO: THEN ON DAY 9, TOBY FOUND SOMETHING IN THE ASHES.
HUD DAY 9 · music → stop · sfx drone_dark, hit
[endcard] End card: dark illustrated background, "NEXT: PART N+1 · SUBTITLE", the call-to-action line, a monster silhouette with a blinking visor lamp.
VO: (no narration)
HUD hidden/reset · sfx rasp, whoosh · 4.2s · NEXT PART 2 · THE CRATES · CTA "DON'T LET THEM TOUCH YOU"
PART 2 — THE CRATES (narrator speed 1.04)
[recap] Fast recap collage: the wall, the three rule cards, the crowd of 212.
VO: 212 PEOPLE. ONE WALL. THREE RULES.
HUD DAY 9 · SURVIVORS 212 · FOOD 38 DAYS · sfx whoosh, hit, drone_low
[title] Illustrated animated title card: dark navy sky, guard towers with blinking red lamps, razor wire, a glowing toxic-green biohazard symbol. "THE WALL AT ASHFORD" in heavy stencil + "PART N" chip + the part subtitle, spray-paint drips, flood-light cones sweeping.
VO: (no narration)
sfx whoosh, hit · 2.4s · PART 2 · THE CRATES
[case_open] Close-up: the scorched case opens: rows of syringes with burned labels.
VO: THE CASE WAS FULL OF NEEDLES.
sfx creak
[doc_pen] Doc turning a syringe in the light, frowning at the burned label.
VO: DOC SAID THE LABEL WAS TOO BURNED TO READ. AND ANYTHING THEY WANT IN OUR VEINS... IS POISON.
music → dark · sfx hit
[burn_barrel] Dad tips the case into the burn barrel; in the foreground Toby slips ONE syringe into his sleeve.
VO: DAD BURNED IT. TOBY KEPT ONE.
HUD CRATES BURNED 4 · sfx fire, sting
[ex_food_title] Explainer title card "PROBLEM ONE: FOOD" with a bread icon.
VO: PROBLEM ONE: FOOD.
music → build · sfx tick, hit
[ex_food_math] Explainer: 212 little people icons × 2,000 kcal = 424,000 kcal per day, the numbers count up.
VO: 212 PEOPLE × 2,000 CALORIES A DAY = 424,000 CALORIES. EVERY DAY.
sfx tick, tick, tick
[ex_food_stock] Explainer: grocery store bar = 9 days, pantries bar = 32 days, total 41.
VO: THE GROCERY STORE: 9 DAYS. EVERY PANTRY IN TOWN: 32 DAYS. TOTAL: 41.
sfx tick, tick, tick
[hud_food_drop] HUD close-up: DAY rolls 3 → 12, FOOD drops 41 → 29 DAYS with a red flash.
VO: BUT THAT WAS DAY 3. IT'S DAY 12. AND THE FIRST WEEK, WE ATE LIKE PEOPLE WHO THOUGHT HELP WAS COMING.
HUD DAY 12 · FOOD 29 DAYS (at 25% of shot) · sfx tick, hit
[gym] The gym: people in a line receiving half portions from Dad.
VO: SO DAD CUT EVERYONE TO 1,200 CALORIES.
sfx murmur
[ex_ration] Explainer: the 29-day bar stretches to 48 at 1,200 kcal; then a water drop icon appears.
VO: RATIONING TURNED 29 DAYS INTO 48. SOLVED. UNTIL THE WATER.
HUD FOOD 48 DAYS (at 40% of shot) · sfx tick, hit
[ex_water] Explainer: the water tower (150,000 gal) with a pump and a power cable.
VO: PROBLEM TWO: THE TOWER HOLDS 150,000 GALLONS. BUT THE PUMP NEEDS POWER.
sfx tick
[grid_dies] Night town from the wall: windows go dark block by block; the water tower light dies last.
VO: THE GRID DIED ON DAY 11.
music → dark · sfx hit, drone_dark
[doc_dust] Doc at the wall brushing gray dust off a container, dust drifting in the wind.
VO: DOC SAID IT DIDN'T MATTER. HE THOUGHT THE GRAY DUST FROM THE WALL WAS GETTING INTO EVERYTHING.
sfx wind
[ex_nosebleeds] Explainer: 212 icons, every one gets a red drop under the nose.
VO: EVERY SINGLE PERSON INSIDE THE WALL HAD NOSEBLEEDS.
sfx tick, tick
[aerial_river] Aerial: the wall ring and the river 400 yards outside it, a dotted path between them.
VO: THE NEAREST WATER WAS THE RIVER. 400 YARDS OUTSIDE THE WALL.
sfx wind
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: SO DAD MADE RULE FOUR: NO ONE GOES OUT ALONE.
CARD RULE #4: "NO ONE GOES OUT ALONE."
[crate_montage] Montage: crate after crate at dawn, fire after fire; HUD CRATES BURNED climbs to 19.
VO: AND THE CRATES KEPT COMING. EVERY DAWN. LIKE THEY WANTED US TO NEED THEM.
HUD CRATES BURNED 19 (at 50% of shot) · music → calm · sfx fire, whoomp, whoomp
[smell_smoke] Jess on the wall, eyes closed, smelling smoke drifting up from the burn pit.
VO: SOMETIMES YOU COULD SMELL WHAT WAS BURNING. IT SMELLED LIKE BREAD.
sfx wind
[scout_escape] Day 15: the gate opens a crack for a cart; Scout bolts through and runs toward the figures in the trees.
VO: ON DAY 15, SCOUT SLIPPED THROUGH THE GATE. TOWARD THEM.
HUD DAY 15 · music → dark · sfx run, chain, sting
[toby_bed] Night bedroom: Toby crying under the blanket, Jess sitting on the edge of the bed.
VO: TOBY CRIED ALL NIGHT. I THOUGHT IT WAS ABOUT SCOUT.
music → calm · sfx crickets
[river_run] Rainy river bank: Jess and Mr. Pruitt (bald, beard, blue shirt) filling jugs. Name tag DALE PRUITT · HARDWARE STORE.
VO: DAY 20. WATER RUN. ME AND MR. PRUITT.
HUD DAY 20 · NAME TAG DALE PRUITT · HARDWARE STORE · music → stop · sfx wind, rain
[dart_hit] Something small hits Pruitt's neck; he flinches but doesn't scream; a figure in the reeds lowers its stick.
VO: SOMETHING HIT HIM. HE DIDN'T SCREAM.
music → dark · sfx rasp, thump, hit
[run_back] Jess and Pruitt running back through the gate, jugs sloshing, the chain slammed.
VO: WE RAN. AND WE DIDN'T TELL ANYONE.
sfx run, chain, hit
[mirror] Bathroom mirror at night: Pruitt shows Jess a small puncture wound on his neck, finger to his lips.
VO: THAT NIGHT, I SAW THE WOUND ON HIS NECK. HE ASKED ME NOT TO TELL.
sfx drone_dark, thump, thump
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: RULE THREE: BITTEN GO OVER THE WALL.
CARD RULE #3: "BITTEN GO OVER THE WALL." (red) · sfx hit
[toby_inject] Night: a silhouette of Toby alone in the dark, the syringe, a tiny sound. Music stops.
VO: DAY 22. I DIDN'T FIND OUT WHAT TOBY DID THAT NIGHT UNTIL IT WAS ALMOST TOO LATE.
HUD DAY 22 · music → stop · sfx crickets, snap, hit
[endcard_choice] End card with a choice: two big buttons "TELL" / "HIDE" and the prompt COMMENT ONE WORD.
VO: (no narration)
HUD hidden/reset · sfx whoosh, rasp · 4.6s · NEXT PART 3 · THE BITTEN · CTA "COMMENT ONE WORD" · choice TELL / HIDE
PART 3 — THE BITTEN (narrator speed 1.04)
[breakfast_flinch] Breakfast table: Toby flinches away from Dad's hand on his shoulder; he won't look at anyone.
VO: THE NEXT MORNING, TOBY WOULDN'T LOOK AT ANY OF US. HE FLINCHED WHEN DAD TOUCHED HIM.
HUD DAY 23 · SURVIVORS 212 · FOOD 31 DAYS · sfx drone_low, sting
[title] Illustrated animated title card: dark navy sky, guard towers with blinking red lamps, razor wire, a glowing toxic-green biohazard symbol. "THE WALL AT ASHFORD" in heavy stencil + "PART N" chip + the part subtitle, spray-paint drips, flood-light cones sweeping.
VO: (no narration)
sfx whoosh, hit · 2.4s · PART 3 · THE BITTEN
[jess_think] Close on Jess, thinking; HUD gains a new line: SECRETS 1.
VO: I THOUGHT HE MISSED SCOUT. AND I HAD A SECRET.
HUD SECRETS 1 (at 60% of shot) · music → calm · sfx tick
[hardware] Pruitt behind his hardware-store counter: healthy colour, no nosebleed, smiling while everyone else looks sick.
VO: MR. PRUITT'S NOSEBLEEDS STOPPED. HIS FEVER BROKE. HE LOOKED BETTER THAN ANY OF US.
sfx tick, tick
[jess_scared] Close on Jess, scared, lit from below.
VO: THAT'S WHAT SCARED ME.
music → dark · sfx hit
[pruitt_watch] Night: Pruitt alone on the wall staring at the figures in the trees.
VO: HE STARTED WATCHING THEM. EVERY NIGHT.
sfx rasp, crickets
[pruitt_whisper] Pruitt hands Jess a rifle scope and whispers in her ear.
VO: HE TOLD ME TO LOOK AT THEIR HANDS. REALLY LOOK.
sfx crickets
[scope_claws] Scope POV (circular vignette, crosshair): a figure's hands: black claws.
VO: ALL I SAW WERE CLAWS.
sfx rasp, hit
[dinner] Long dinner table in the gym, everyone eating in silence.
VO: THEN AT DINNER, TOBY SAID SOMETHING NOBODY WAS ALLOWED TO SAY.
HUD DAY 26 · music → stop · sfx murmur
[dinner_toby] Toby stands up and says it out loud; the room freezes; forks stop.
VO: "THEY'RE NOT MONSTERS. THEY'RE WEARING SUITS. LIKE BEEKEEPERS."
sfx drone_dark
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: DAD MADE A NEW RULE THAT NIGHT. ANYONE WHO DEFENDS THEM IS TURNING.
CARD RULE #5: "ANYONE WHO DEFENDS THEM IS TURNING." (red) · sfx thump, hit
[toby_quiet] Toby sitting alone on the stairs, small.
VO: TOBY NEVER SAID IT AGAIN.
music → calm
[dad_arm] 3 AM: Jess sees Dad at a sink scrubbing his forearm, an ugly wound.
VO: THEN, AT 3 A.M., I SAW DAD'S ARM.
HUD SECRETS 2 (at 80% of shot) · music → dark · sfx faucet, sting, tick
[dad_hide] Dad pulls his sleeve down when he sees her; tense heartbeat close-ups.
VO: HE'D BEEN HIDING IT FOR DAYS. AND FOR THE FIRST TIME, I WONDERED WHO ELSE WAS HIDING SOMETHING.
sfx thump, thump, thump, thump
[who_bitten] Suspect grid: portraits of Dad, Toby, Pruitt, Doc with question marks; one by one a red tick lands; ends on "WHO IS BITTEN?".
VO: (no narration)
sfx tick, tick, tick, tick, hit · 3.4s
[bite_check] Weekly bite check: a queue in the clinic, Doc inspecting necks and arms. Tag BITE CHECK · WEEKLY.
VO: DAY 28. EVERY WEEK, DOC CHECKED EVERYONE FOR BITES.
HUD DAY 28 · NAME TAG BITE CHECK · WEEKLY · sfx murmur
[bite_found] Doc freezes at Pruitt's neck: the puncture.
VO: THIS WEEK, HE FOUND ONE.
sfx hit, sting
[pruitt_plead] Pruitt calm, palms open, speaking to Dad.
VO: MR. PRUITT JUST SAID: "I'M NOT SICK, WADE. I'M THE ONLY ONE HERE WHO ISN'T."
music → stop · sfx drone_dark
[dad_look] Dad turns to Jess: "Did you know?" Jess says nothing; heartbeat.
VO: DAD LOOKED AT ME. "DID YOU KNOW?" I SAID NOTHING.
sfx thump, thump, thump, thump
[exile_pruitt] Pruitt lowered over the wall. HUD SURVIVORS 212 → 211.
VO: RULE THREE.
HUD SURVIVORS 211 (at 50% of shot) · sfx creak, tick, wind · 3.0s
[pruitt_walk] Pruitt walks calmly across the field toward the figures, not running.
VO: HE DIDN'T RUN FROM THEM. HE WALKED TOWARD THEM.
music → dark · sfx wind, rasp
[scope_carry] Scope POV: two figures lay him on a stretcher and carry him into the trees.
VO: THEY LAID HIM ON SOMETHING FLAT. AND CARRIED HIM INTO THE TREES.
sfx rasp, rasp
[dad_feed] Dad on the wall, stone-faced, explaining it away.
VO: DAD SAID THEY WERE TAKING HIM SOMEWHERE TO FEED.
sfx hit
[dad_alone] Night: Dad alone on the wall staring at the trees, exactly where Pruitt used to stand.
VO: DAY 30. THAT NIGHT, DAD STOOD ON THE WALL ALONE. STARING AT THE TREES. THE SAME WAY MR. PRUITT USED TO.
HUD DAY 30 · sfx wind, drone_dark, hit
[endcard] End card: dark illustrated background, "NEXT: PART N+1 · SUBTITLE", the call-to-action line, a monster silhouette with a blinking visor lamp.
VO: (no narration)
HUD hidden/reset · sfx whoosh, rasp · 4.4s · NEXT PART 4 · THE VOICE · CTA "COMMENT WHO YOU THINK IS BITTEN"
PART 4 — THE VOICE (narrator speed 1.04)
[confront_dad] Jess confronts Dad on the wall; he shows the arm: a burn scar, not a bite.
VO: DAY 31. SO I ASKED HIM. IT WASN'T A BITE. IT WAS A BURN.
HUD DAY 31 · SURVIVORS 211 · FOOD 22 DAYS · SECRETS 2 · sfx wind, hit
[title] Illustrated animated title card: dark navy sky, guard towers with blinking red lamps, razor wire, a glowing toxic-green biohazard symbol. "THE WALL AT ASHFORD" in heavy stencil + "PART N" chip + the part subtitle, spray-paint drips, flood-light cones sweeping.
VO: (no narration)
sfx whoosh, hit · 2.4s · PART 4 · THE VOICE
[burn_flashback] Sepia flashback: the first crate fire flaring up onto Dad's arm.
VO: FROM THE FIRST CRATE. HE HID IT BECAUSE IF THE TOWN SAW HIM HURT, THEY'D STOP LISTENING.
sfx whoomp, fire
[hug_wall] Jess hugging Dad on the wall at dusk. HUD SECRETS 2 → 1.
VO: MY DAD WASN'T TURNING. HE WAS JUST TIRED.
HUD SECRETS 1 (at 30% of shot) · music → calm · sfx tick
[voice_night] Night town, silence, then a long inhuman groan rolls in from the trees; everyone looks up.
VO: THEN THERE WAS THE VOICE.
music → stop · sfx groan, drone_dark
[voice_nights] Montage of 3 nights, a clock at 9:00 PM, a stopwatch reading 47 seconds.
VO: EVERY NIGHT. 9 P.M. SAME LENGTH. 47 SECONDS.
sfx groan_short, groan_short, groan_short
[doc_record] Doc with an old reel-to-reel / cassette recorder on the wall.
VO: DOC STARTED RECORDING IT.
sfx snap
[ex_slowdown] Explainer: a waveform; playback speed 1x → 0.5x → 0.25x; at quarter speed the groan almost forms a word.
VO: AT HALF SPEED, IT WAS STILL A GROAN. AT QUARTER SPEED...
music → dark · sfx groan_slow
[doc_chalk] Doc's chalkboard: a column of numbers, each lower than the last.
VO: DOC SWORE HE HEARD A NUMBER. AND EVERY NIGHT, IT GOT LOWER.
sfx marker, marker
[countdown_reveal] The numbers resolve into a countdown; a clock ticks.
VO: IT WASN'T HUNGER. IT WAS A COUNTDOWN.
sfx clock, hit
[starving_burning] Thin, tired townspeople watching a crate burn. HUD FOOD 14 DAYS · CRATES BURNED 31.
VO: WE WERE STARVING. AND STILL BURNING EVERYTHING THEY LEFT.
HUD FOOD 14 DAYS · CRATES BURNED 31 (at 20% of shot) · sfx fire, tick
[scout_home] Day 33: Scout trots back to the gate, fat and happy.
VO: ON DAY 33, SCOUT CAME HOME. FATTER THAN WHEN HE LEFT.
HUD DAY 33 · music → calm · sfx chain, thump, thump
[scout_bandage] Close-up: a clean white bandage on Scout's paw.
VO: WITH A BANDAGE ON HIS PAW. SOMEONE OUT THERE HAD FIXED HIM.
music → stop · sfx hit
[scout_gate] Scout scratching at the gate, whining to go back out.
VO: AND ALL HE WANTED WAS TO GO BACK.
sfx thump, thump, thump
[doc_tells] Doc in the firehouse telling Dad everything, Dad's jaw tight.
VO: DOC TOLD DAD EVERYTHING. "THEY'RE TREATING THINGS, WADE. THEY'RE COUNTING DOWN TO SOMETHING."
music → dark · sfx murmur
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: RULE FIVE.
CARD RULE #5: "ANYONE WHO DEFENDS THEM IS TURNING." (red) · sfx hit · 2.2s
[doc_cell] Dad locks Doc in the sheriff's cell. Tag SHERIFF'S OFFICE · CELL 1.
VO: SO DAD LOCKED HIM IN THE SHERIFF'S CELL.
NAME TAG SHERIFF'S OFFICE · CELL 1 · sfx hit, chain
[clinic_board] Jess sneaks into Doc's clinic at night: a cork board of notes, photos and string.
VO: I SNUCK INTO DOC'S CLINIC. HE'D BEEN PUTTING IT TOGETHER.
sfx pencil
[board_day40] One note circled in red: "DAY 40?".
VO: AND ONE NOTE WAS CIRCLED IN RED.
sfx marker, hit
[drawings] Toby's crayon drawings spread on the floor (yellow suits with faces, people holding needles).
VO: DAY 37. I FOUND TOBY'S DRAWINGS. I THOUGHT HE WAS DRAWING NIGHTMARES.
HUD DAY 37 · music → calm · sfx pencil
[toby_door] Jess puts them back and stands outside Toby's door, not knocking.
VO: I PUT THEM BACK. I SHOULD HAVE ASKED HIM.
[doc_scream] Doc gripping the cell bars, screaming "TOMORROW!".
VO: ON DAY 38, DOC'S COUNT HIT ONE. HE SCREAMED FROM HIS CELL: "TOMORROW! IT'S TOMORROW!"
HUD DAY 38 · music → dark · sfx groan_short, clock, hit
[gate_night] Night, heavy rain. Toby (small, orange jacket) at the chained gate, pulling the chain off. Floodlit silhouettes waiting beyond. Slow push-in, lightning flicker.
VO: AND ON DAY 39, MY LITTLE BROTHER OPENED THE GATE.
HUD DAY 39 · music → stop · sfx rain, chain, rasp, hit
[endcard] End card: dark illustrated background, "NEXT: PART N+1 · SUBTITLE", the call-to-action line, a monster silhouette with a blinking visor lamp.
VO: (no narration)
HUD hidden/reset · sfx whoosh, rasp · 4.4s · NEXT PART 5 · DAY 40 · CTA "WATCH ALL 4 PARTS AGAIN BEFORE TOMORROW"
PART 5 — DAY 40 (narrator speed 1.02)
[breach] Rain, the gate open: figures pour in, this time with bright helmet lights.
VO: THEY CAME IN. AND THIS TIME, THEY HAD LIGHTS.
HUD DAY 39 · SURVIVORS 211 · THREAT CRITICAL · sfx rain, rasp, rasp, drone_dark
[title] Illustrated animated title card: dark navy sky, guard towers with blinking red lamps, razor wire, a glowing toxic-green biohazard symbol. "THE WALL AT ASHFORD" in heavy stencil + "PART N" chip + the part subtitle, spray-paint drips, flood-light cones sweeping.
VO: (no narration)
sfx whoosh, hit · 2.6s · PART 5 · DAY 40
[bell_mob] The town bell ringing; 211 people with bats and pipes charge twelve figures.
VO: 211 OF US. TWELVE OF THEM. IT SHOULD HAVE BEEN EASY.
music → build · sfx bell, run
[kneel] The figures kneel in the mud, hands raised, not fighting.
VO: BUT THEY DIDN'T FIGHT BACK. THEY JUST... KNELT.
music → stop · sfx drone_dark, hit
[mob_beat] The mob closes in; heavy thumps (off-screen violence, no gore).
VO: AND WE... WE DIDN'T STOP.
sfx thump, thump, thump, thump
[grab_wrist] A gloved hand grabs Jess's wrist. Rule card #1 "NEVER LET THEM TOUCH YOU." slams in.
VO: (no narration)
CARD RULE #1: "NEVER LET THEM TOUCH YOU." · sfx rasp, hit · 1.8s
[toby_jab] Toby, crying, says sorry and jabs the syringe into Jess's leg.
VO: TOBY SAID HE WAS SORRY. THEN HE STABBED SOMETHING INTO MY LEG.
sfx snap, hit
[blackout] Frame goes black; heartbeat; a glitch.
VO: AND THEN...
sfx thump, thump, thump, thump, glitch
[rerender] THE TWIST: the image re-renders like a glitch. The "monster" holding her wrist is a woman in a YELLOW CDC hazmat suit with a clear visor and a kind face.
VO: THE THING HOLDING MY WRIST... HAD A FACE.
sfx glitch, breath_mask
[alvarez] Pvt. Rosa Alvarez in yellow CDC suit, visor fogged, comforting Jess. Tag PVT. ROSA ALVAREZ · CDC FIELD MEDIC.
VO: "EASY. EASY. YOU'RE OKAY, HONEY."
NAME TAG PVT. ROSA ALVAREZ · CDC FIELD MEDIC · voice af_nicole · sfx breath_mask
[reveal_gear] Truth views: the "sticks" are dart rifles, the crates are medical kits with bread and water.
VO: THE STICKS WERE DART RIFLES. THE BOXES WERE MEDICINE.
music → dark
[loudspeaker] A CDC truck with a roof loudspeaker; notice card #1 INFECTED · FUNGUS IN THE WATER.
VO: "RESIDENTS OF ASHFORD. THIS IS THE CDC. YOU ARE INFECTED WITH A FUNGUS FROM YOUR WATER.
CARD CDC NOTICE #1: "INFECTED · FUNGUS IN THE WATER" · voice am_michael (radio FX) · sfx radio
[loudspeaker2] Notice card #2 WE ARE NOT MONSTERS.
VO: IT CHANGES WHAT YOU SEE. WE ARE NOT MONSTERS. WE ARE HERE TO HELP.
CARD CDC NOTICE #2: "WE ARE NOT MONSTERS." · voice am_michael (radio FX) · sfx radio
[loudspeaker3] Notice card #3 ASH-7 · SIGHT RETURNS IN 30 SECONDS.
VO: TREATMENT IS ONE INJECTION. A S H 7. YOUR SIGHT RETURNS IN 30 SECONDS.
CARD CDC NOTICE #3: "ASH-7 · SIGHT RETURNS IN 30 SECONDS" · voice am_michael (radio FX) · sfx radio
[loudspeaker4] Notice card #4 (red) AFTER 0600 THIS ZONE BURNS.
VO: TREATMENT ONLY WORKS UNTIL 6 A.M. AFTER THAT, THIS ZONE WILL BE BURNED."
CARD CDC NOTICE #4: "AFTER 0600 THIS ZONE BURNS." (red) · voice am_michael (radio FX) · sfx radio, hit
[turn_around] Jess turns around slowly.
VO: THEN I TURNED AROUND.
music → stop
[see_us] She sees the townspeople as they really are: gray skin, cracked fungal veins, red eyes (the infected). No gore.
VO: AND I SAW US.
sfx ring, hit
[window_me] In the hardware-store window, her own reflection: gray and cracked.
VO: AND IN THE WINDOW OF MR. PRUITT'S STORE, I SAW ME.
sfx hit
[hud_rewrite] The HUD glitches and rewrites itself: SURVIVORS → PATIENTS, THREAT → TREATMENT WINDOW, MONSTERS → CDC.
VO: (no narration)
HUD hidden/reset · sfx tick, glitch, tick, glitch, tick, tick, glitch · 4.2s
[rewind] VHS rewind effect through earlier scenes.
VO: THE MONSTERS WERE NEVER OUTSIDE THE WALL.
music → dark · sfx rewind, thump, thump
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: THE GRAY WATER. THE GRAY DUST. IT WAS THE FUNGUS.
sfx thump, thump, glitch · WHAT I SAW: GRAY WATER → WHAT IT WAS: FUNGAL SPORES · DAY 1
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: THE GLASS FACES WERE VISORS. THAT SOUND WAS THEIR AIR FILTERS.
sfx thump, thump, glitch · WHAT I SAW: GLASS FACES → WHAT IT WAS: VISORS + AIR FILTERS · DAY 5
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: THEY CAME IN PAIRS BECAUSE THAT'S THEIR RULE.
sfx thump, thump, glitch · WHAT I SAW: ALWAYS IN PAIRS → WHAT IT WAS: CDC RULE: NEVER ENTER ALONE · DAY 7
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: THE STICKS WERE DART RIFLES.
sfx thump, thump, glitch · WHAT I SAW: STICKS → WHAT IT WAS: DART RIFLES · TREATMENT · DAY 7
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: MRS. KOWALSKI WASN'T TAKEN. SHE WAS CARRIED TO AN AMBULANCE.
sfx thump, thump, glitch · WHAT I SAW: TAKEN → WHAT IT WAS: CARRIED TO AN AMBULANCE · DAY 4
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: 928 PEOPLE WERE EVACUATED. WE WERE THE ONES WHO HID.
sfx thump, thump, glitch, engine · WHAT I SAW: 1,140 → 212 → WHAT IT WAS: 928 EVACUATED · DAY 4
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: AND THE CRATES? IT REALLY WAS BREAD.
sfx thump, thump, glitch · WHAT I SAW: BAIT → WHAT IT WAS: BREAD · WATER · ASH-7 · EVERY DAWN
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: THE BITTEN NEVER TURNED. THEY WERE GETTING BETTER.
sfx thump, thump, glitch · WHAT I SAW: TURNING → WHAT IT WAS: RECOVERING · DAY 28
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: SCOUT'S BANDAGE CAME FROM THEIR VET TENT.
sfx thump, thump, glitch · WHAT I SAW: FIXED BY SOMEONE → WHAT IT WAS: CDC ANIMAL CARE · DAY 33
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: THE VOICE EVERY NIGHT WAS COUNTING DOWN THE DAYS WE HAD LEFT.
sfx thump, thump, glitch · WHAT I SAW: THE VOICE → WHAT IT WAS: DAYS OF TREATMENT LEFT · 9:00 PM
[clue] CLUE REPLAY: split card. Top: the original shot from an earlier part (e.g. the gray water) labelled "WHAT I SAW"; bottom: the same moment redrawn as the truth labelled "WHAT IT WAS". A day stamp in the corner.
VO: TOBY'S DRAWINGS WEREN'T NIGHTMARES. THEY WERE PERFECT.
sfx thump, thump, glitch · WHAT I SAW: NIGHTMARES → WHAT IT WAS: EXACTLY WHAT HE SAW · DAY 37
[clue_toby] Replay of Toby crying in bed (Day 22): now we see he was looking at Jess, who is gray.
VO: AND ON DAY 22, WHEN TOBY CRIED ALL NIGHT... IT WASN'T ABOUT SCOUT. HE WAS LOOKING AT ME.
music → calm · sfx glitch, thump, thump
[clue_hug] Replay: Toby hugging gray, cracked Jess goodnight.
VO: FOR 17 DAYS, MY LITTLE BROTHER LIVED WITH MONSTERS. AND HE STILL HUGGED ME GOODNIGHT.
music → stop · sfx ring
[alvarez_plea] Alvarez in the rain: "They'll follow you."
VO: "TO THEM, YOU STILL LOOK LIKE YOU. YOU'RE COVERED IN THE SAME DUST. THEY WON'T FOLLOW US. THEY'LL FOLLOW YOU."
music → dark · transition zoom · voice af_nicole · sfx rain, breath_mask
[dad_axe] Dad on the wall with a fire axe, staring at the CDC lights. HUD TREATMENT WINDOW 05:12:00 counting down.
VO: 5 HOURS. 211 PEOPLE WHO THINK I'M ONE OF THEM. AND MY DAD.
HUD TREATMENT WINDOW 05:12:00 · sfx clock, hit
[endcard] End card: dark illustrated background, "NEXT: PART N+1 · SUBTITLE", the call-to-action line, a monster silhouette with a blinking visor lamp.
VO: (no narration)
HUD hidden/reset · sfx whoosh, thump, thump · 4.8s · NEXT PART 6 · SUNRISE · CTA "THE FINALE · GO BACK AND COUNT THE CLUES"
PART 6 — SUNRISE (narrator speed 1.02)
[grab_axe] Dad lunges, yelling "JESS! GET AWAY FROM IT!".
VO: "JESS! GET AWAY FROM IT!"
HUD TREATMENT WINDOW 05:12:00 · PATIENTS 211 · voice am_adam · sfx rain, hit
[grab_axe2] Close on Dad's eyes: to him Jess still looks normal.
VO: TO DAD, I STILL LOOKED LIKE ME.
sfx rain
[title] Illustrated animated title card: dark navy sky, guard towers with blinking red lamps, razor wire, a glowing toxic-green biohazard symbol. "THE WALL AT ASHFORD" in heavy stencil + "PART N" chip + the part subtitle, spray-paint drips, flood-light cones sweeping.
VO: (no narration)
sfx whoosh, hit · 2.6s · PART 6 · SUNRISE
[rulecard] 3D RULE CARD (signature graphic): a lime-green metal sign with hazard stripes, rivets, scratches, grime, a black chip reading "RULE #N", the rule in heavy black condensed caps, flips in with spring physics and a sheen sweep; red variant for the dark rules.
VO: IF I TOLD THEM THE TRUTH, THEY'D THROW ME OVER THE WALL.
CARD RULE #5: "ANYONE WHO DEFENDS THEM IS TURNING." (red)
[firehouse_steps] Jess on the firehouse steps addressing the crowd.
VO: SO I USED HIS RULES.
music → build · sfx murmur
[speech] Jess mid-speech, fist raised; crowd roaring.
VO: "THEY'RE WEAK AT DAWN. THEIR NEST IS ACROSS THE RIVER. WE END THIS TONIGHT."
sfx murmur, hit
[plan_map] Jess marking the map: an arrow across the river to "THE NEST".
VO: SO I LIED. I TOLD THEM WE COULD END IT. AT THEIR NEST.
sfx pencil, tick
[doc_cell_free] Jess unlocks Doc's cell; he looks at her face and knows.
VO: DOC KNEW THE MOMENT HE SAW MY FACE.
music → calm · sfx chain, creak
[doc_front] Doc with a lantern: "Then I walk at the front."
VO: "YOU SEE THEM NOW, DON'T YOU? THEN I WALK AT THE FRONT."
voice bm_george
[ex_treatment] Explainer: the CDC line in the dark: dart teams, 30-second treatment icon, a 6:00 AM deadline.
VO: THE CDC SET UP A LINE. DART TEAMS IN THE DARK. 30 SECONDS TO WORK. BUT ONLY BEFORE SIX.
HUD TREATMENT WINDOW 03:40:00 · sfx radio, tick
[march] 4 AM: 209 people walk out of the gate with torches. HUD FOLLOWING 209 / 211.
VO: AT 4 A.M., 209 PEOPLE WALKED OUT OF THE GATE THEY BUILT.
HUD TREATMENT WINDOW 02:00:00 · FOLLOWING 209 / 211 · music → build · sfx run, fire
[holdouts] Two figures stay behind on the wall.
VO: TWO PEOPLE WOULDN'T COME.
music → stop · sfx crickets
[floodlights] Floodlights slam on across the field.
VO: (no narration)
HUD THREAT CRITICAL · sfx boom, murmur · 1.8s
[darts] Darts hit one person after another; each stops screaming. HUD PATIENTS TREATED 207.
VO: ONE BY ONE, THEY STOPPED SCREAMING...
HUD PATIENTS TREATED 207 (at 90% of shot) · music → dark · sfx dart, dart, dart, dart, dart, dart
[crying] People kneeling, crying, seeing clearly for the first time.
VO: ...AND STARTED CRYING.
music → calm
[dad_rifle] Dad, the last one, has taken a rifle and aims at Alvarez. HUD TREATMENT WINDOW 00:01:30.
VO: DAD WAS THE LAST ONE.
HUD TREATMENT WINDOW 00:01:30 · music → stop · sfx snap, clock
[dad_rifle_talk] Dad shouting "RULE ONE!".
VO: "JESS. IT'S TOUCHING YOU. RULE ONE. RULE ONE!"
voice am_adam · sfx clock
[jess_step] Jess steps between them, calm.
VO: "YOU MADE THE RULES TO KEEP US SAFE. LOOK AT ME. DO I LOOK SCARED?"
sfx thump, thump, thump, thump
[toby_plea] Toby beside Jess: "They're nice."
VO: "DAD. I'VE SEEN THEM FOR 17 DAYS. THEY'RE NICE."
voice af_sky
[dad_choose] Dad lowers the rifle; a dart hits. HUD 00:00:47.
VO: HE DIDN'T SEE WHAT I SAW. HE JUST CHOSE TO TRUST ME.
HUD TREATMENT WINDOW 00:00:47 · sfx clock, snap
[dad_treated] Glitch-to-clear: Dad's vision re-renders. HUD TREATED.
VO: WITH 12 SECONDS LEFT.
HUD TREATMENT WINDOW TREATED (at 50% of shot) · music → calm · sfx glitch, whoosh
[dad_kneel] Dad on his knees seeing his real kids (gray, healing) and crying.
VO: AND FOR THE FIRST TIME IN 40 DAYS, MY DAD SAW HIS KIDS.
[recovered_board] A CDC board of recovered patients: Dale Pruitt photo, RECOVERED · DAY 31, Mrs. Kowalski, the exiled.
VO: EVERY PERSON DAD EVER THREW OVER THE WALL... HAD BEEN SAVED.
NAME TAG DALE PRUITT · RECOVERED · DAY 31
[doc_note] An empty camp cot with Doc's note.
VO: DOC WASN'T IN THE CAMP. "TWO STAYED. SOMEONE HAS TO WALK THEM OUT."
music → dark · sfx wind
[burn] 6 AM: CDC flamethrower trucks; the wall burns first, then the town. HUD TREATED 208 · LOST 3.
VO: AT 6 A.M., THEY BURNED ASHFORD. THE WALL BURNED FIRST. DOC NEVER CAME BACK.
HUD TREATED 208 · LOST 3 (at 70% of shot) · sfx engine, whoomp, fire, hit
[tent] A quiet CDC tent: Jess (healed) talking to Dr. Dana Ruiz. Tag DR. DANA RUIZ · CDC INVESTIGATOR.
VO: I'D BEEN TELLING THIS STORY TO A DOCTOR. FOR THREE HOURS.
HUD hidden/reset · NAME TAG DR. DANA RUIZ · CDC INVESTIGATOR · music → calm · sfx snap
[tent_dream] Close on Dr. Ruiz asking.
VO: "DO YOU STILL HAVE THE DREAMS?"
voice af_sarah
[tent_answer] Jess answers; a dream flash of gray figures in the trees.
VO: EVERY NIGHT. THEY COME OUT OF THE TREES. EXCEPT NOW... THEY'RE GRAY.
music → stop
[rulecard6] Final rule card in Jess's own handwriting style: JESS'S RULE #6 · "LOOK TWICE."
VO: SO I MADE ONE MORE RULE. LOOK TWICE.
CARD RULE #6: "LOOK TWICE."
[map_sting] A map of Montana with 4 red zones blinking. HUD ACTIVE ZONES 4.
VO: ASHFORD WASN'T THE ONLY TOWN WITH A WALL.
HUD ACTIVE ZONES 4 (at 50% of shot) · music → dark · sfx tick, hit
[elkhorn] SEQUEL STING: a different town, Elkhorn, Day 12: monsters leave food at THEIR gate.
VO: ELKHORN, DAY 12. EVERY MORNING, THE MONSTERS LEAVE FOOD AT THEIR GATE.
HUD ELKHORN DAY 12 · sfx wind, rasp, impact
[elkhorn_burn] And they burn it. Whip to black.
VO: AND EVERY MORNING... THEY BURN IT.
transition whip · sfx swoosh, whoomp, boom, fire
[endcard] End card: dark illustrated background, "NEXT: PART N+1 · SUBTITLE", the call-to-action line, a monster silhouette with a blinking visor lamp.
VO: (no narration)
HUD hidden/reset · sfx whoosh, rasp · 5.2s · NEXT THE END · SEASON 2? · CTA "COMMENT "ELKHORN""

The Wall at Ashford is an original story by @OnlySainted. This prompt is shared freely, so make something great with it.