Master prompt adapted from "The Wall at Ashford" by @OnlySainted (CC BY 4.0). Paste this whole file into a coding agent (Claude Code, or any agent that can run code, Node/Python, Playwright and ffmpeg). It builds and renders a complete "What If" stickman video, "What If You Never Needed To Sleep Again?", with no stock assets. Everything is drawn in code, voiced with a free local TTS, and scored with synthesized or CC0 sound.

0. WHAT YOU ARE BUILDING
One horizontal (16:9) animated "What If" video for YouTube:
Format: 1920×1080, 30 fps, H.264 MP4 with AAC audio, one file (video.mp4). Runtime ≈ 8–10 minutes.
Genre: second-person ("you") speculative story with deadpan humour. Formula: a mundane superpower → "Sounds amazing. It's also kind of awful." → escalating consequences, each one logical → a final turn that reframes what the power cost you. Not horror: wonder, comedy, then a quiet, emotional ending.
Look: flat-vector 2D stickman style (SVG drawn in code): the protagonist has a solid black round head with two big white oval eyes and a coloured hoodie; dark navy night palette with warm lamp light, clean bold shapes.
Every frame is a pure function of time renderAt(t). No Date.now(), no unseeded Math.random().
Deliver: video.mp4, a contact sheet, an SRT, a 1280×720 thumbnail, and the source code.

1. THE STORY BIBLE
Premise: one morning you wake up and you never need to sleep again. No tiredness, no health cost: your body is fine. Everyone else still sleeps 8 hours. The consequences come from the WORLD and from what sleep secretly did for you, not from illness.
Arc in 5 chapters (chapter card at each):
1. THE GIFT: 8 free hours a day. You learn guitar, finish every game, read 40 books, get top grades.
2. THE NIGHT SHIFT: the world is closed at 3 am. Friends are asleep. You become the person who's always online. You get weird.
3. THE MATH: 8 hours × 365 days = 2,920 extra hours a year. Over a lifetime, decades more awake time. You become the most skilled person you know, and the loneliest.
4. THE THING YOU MISSED: no dreams. You realise you haven't dreamed in months. Real-science interlude: sleep is when the brain does important work on memory and emotion (keep it simple, cite sources, no medical claims). Your "power" skips the dreams. Your memories of the year feel flat, like a list.
5. THE TRADE: your little sister has a nightmare and asks you to tell her what you dreamed. You can't. Final turn: you'd trade all the free hours for one dream. You lie down, close your eyes… and the screen holds black. Final line in silence.
The "what you thought → what it really was" device (used in chapter 5 replay, one line each):
| What you thought | What it really was |
|---|---|
| Free time | Time alone |
| Being always available | Nobody to talk to |
| Remembering everything you studied | Forgetting how things felt |
| Never tired | Never rested |
| More life | Fewer dreams |
Characters (keep identical):
| Name | Role | Look |
|---|---|---|
| You | Protagonist | Black round head, white oval eyes, hoodie #3a86ff, grey joggers |
| Lily (8) | Your little sister | Smaller, black round head, pink pyjamas #ff8fab, plush rabbit |
| Sam | Best friend | Black head, green hoodie #2a9d8f, headphones |
| Mum | Parent | Black head, cardigan #e9c46a, mug |
| The Clock | Recurring visual gag | A wall clock with a tired face that ticks |
Figures: Ifverse-style stickmen: black round heads (no skin, no hair, no nose), white oval eyes with small pupils, brows drawn as short strokes, coloured hoodies, stroke limbs, round hands, soft shadow; procedural walk, idle sway, blink.

2. ART DIRECTION
Canvas 1920×1080. Layers: background gradient (day: #cde7f0 → #f6f1e7; night: #0b1426 → #1c2c4f) → room or city set → characters → foreground props with slight blur → light (lamp cones, monitor glow) → vignette → grain 5%.
Palette: navy #0b1426, lamp amber #ffc23d, hoodie blue #3a86ff, snow #eef3fa, alarm red #e5383b, mint #5fd38d.
Props as functions: bed, desk, monitor glow, phone with notification bubbles, guitar, stack of books, wall clock with a face, city skyline with lit/unlit windows, 24-hour shop, calendar pages flying, graph boards, brain icon (simple, friendly), dream bubble.
Camera: slow push-ins, time-lapse sweeps (sun and moon arcs), split screens (you awake vs everyone asleep), whip pans between gags.

3. TEXT ON SCREEN
Captions: Oswald 700, ALL CAPS, 1–3 words per chunk, lower third (y ≈ 900–990), spring pop. Markup *word* = amber #ffc23d, _word_ = mint #5fd38d, ~word~ = red #e5383b. Strip markup before TTS.
HUD (top-left, monospace): HOURS AWAKE 0 · FREE HOURS GAINED 0 · BOOKS READ 0 · FRIENDS ONLINE 4 · DREAMS 0. Numbers roll and pop on change. In chapter 5 DREAMS is shown in red, and in the final shot the HUD fades out.
CHAPTER CARD: a big glossy navy card with an amber chip "CHAPTER N" and the title, flipping in with 3D perspective, spring physics, sheen sweep and impact SFX.
STAT CARD: white card with a big number (e.g. "2,920 HOURS / YEAR") that counts up.
Title card: your stickman lying in bed with eyes wide open, a ticking clock. Text "WHAT IF YOU NEVER NEEDED TO SLEEP AGAIN?".
End card: CTA line + your stickman yawning for the first time. No "follow @channel".

4. VOICE
Kokoro-82M (ONNX) + espeak-ng. Narrator = am_michael at 1.0 (calm deadpan, second person). Lily = af_sky at 1.1. Sam = am_puck. Mum = af_heart.
Normalise text: "2,920" → "two thousand nine hundred and twenty", "3 AM" → "three a m", strip * _ ~, no abbreviation full stops.
Timing: synthesise each line, trim silence, place caption chunks by phoneme weight. Shot = lead 0.2 s + speech + tail 0.4 s (comic beats tail 0.8 s).

5. SOUND & MUSIC (original only)
Moods: curious (pizzicato, light marimba), upbeat (bouncy synth bass, claps), lonely (soft piano, airy pad), wonder (warm strings swell), stop (silence).
SFX: tick, clock, alarm, notification, keyboard, guitar strum, page flip, whoosh, pop, ding, crickets, city hum, fridge hum, snore, yawn, heartbeat, record scratch.
SFX per shot [name, at, dur]. Duck music −10 dB under voice. Master −14 LUFS, −1 dBTP.

6. ENGINE & RENDER PIPELINE
parts/video.json: {title, voice, speed, shots:[{scene, chunks, lead, tail, hud, hud_at, card, params, sfx, music, trans, capY, dur, voice}]}. voice.py → timeline.json + voice.wav + SRT. render/index.html → scenes[name](localTime, params, shot) → SVG + overlay. Playwright + Chromium 1920×1080 → JPEG → ffmpeg stdin, --workers, --from/--to. Mix + loudnorm, H.264 CRF 18, yuv420p, +faststart, AAC 192 kbps. QA: contact sheet, captions never cover eyes, HUD values correct, no markup spoken, −14 LUFS.
Mid-roll safe break: a 1 s black + silence beat after chapter 3 (videos ≥ 8 min).

7. RULES FOR TONE
Deadpan and funny first, then sincere. Never mean. No medical advice: the science interlude is general and sourced (verify with sleep research from reputable sources such as NIH/NHLBI or university sleep labs; add "Source:" chips). The final line, "For the first time in a year, I couldn't wait to fall asleep.", lands in silence.

8. THE COMPLETE SHOT LIST (narration verbatim, build every shot)
[hook] Your stickman in bed at 3 AM, eyes wide open, perfectly awake; the clock face on the wall looks exhausted.
VO: IMAGINE YOU WAKE UP ONE MORNING, AND YOU NEVER NEED TO SLEEP AGAIN.
music → curious · sfx tick
[hook2] Quick montage of the good part: guitar, books, games, top grade.
VO: EIGHT EXTRA HOURS. EVERY DAY. FOREVER. *SOUNDS AMAZING*.
sfx whoosh, ding, guitar
[hook3] Record scratch; you freeze mid-celebration, looking at the camera.
VO: IT'S ALSO ~KIND OF AWFUL~.
music → stop · sfx record_scratch · tail 0.8
[title] Title card · VO: (no narration) · HUD hidden/reset · sfx whoosh, tick · 3.0s
[ch1] CHAPTER 1 card: "THE GIFT" · sfx impact
[night1] First night: you lie down, close your eyes, open them. Nothing. You sit up, confused.
VO: THE FIRST NIGHT, YOU LIE DOWN OUT OF HABIT. YOU WAIT. NOTHING HAPPENS.
HUD HOURS AWAKE 0 · FREE HOURS GAINED 0 · BOOKS READ 0 · FRIENDS ONLINE 4 · DREAMS 0 · music → curious · sfx crickets
[morning1] Morning: you're fresh as ever; Mum yawns into her mug.
VO: IN THE MORNING, YOU FEEL… FINE. BETTER THAN FINE.
NAME TAG MUM · sfx yawn, ding
[guitar] Time-lapse: you practising guitar every night, fingers a blur, the moon arcing past the window.
VO: SO YOU USE THE NIGHTS. YOU LEARN GUITAR IN A MONTH.
HUD FREE HOURS GAINED 240 (at 80%) · music → upbeat · sfx guitar, whoosh
[books] A tower of books growing next to the bed.
VO: YOU READ FORTY BOOKS.
HUD BOOKS READ 40 (at 70%) · sfx page_flip, page_flip, pop
[grades] Test paper slapped down: A+. Sam's jaw drops.
VO: YOUR GRADES GO UP. YOUR FRIEND SAM ASKS IF YOU'RE CHEATING.
NAME TAG SAM · BEST FRIEND · voice am_puck "ARE YOU CHEATING?" · sfx ding
[games] You finishing every game on your shelf; a trophy shelf fills.
VO: YOU FINISH EVERY GAME YOU OWN. TWICE.
sfx keyboard, pop
[ch2] CHAPTER 2 card: "THE NIGHT SHIFT" · music → curious · sfx impact
[3am_city] City skyline at 3 AM: windows go dark one by one; only yours stays lit.
VO: BUT AT THREE A M, THE WORLD IS CLOSED.
sfx city_hum
[phone] Your phone: you send messages; FRIENDS ONLINE drops to 0; grey ticks.
VO: YOUR FRIENDS ARE ASLEEP. EVERY. SINGLE. NIGHT.
HUD FRIENDS ONLINE 0 (at 60%) · sfx notification, tick
[shop] You at a 24-hour shop at 4 AM, the bored cashier staring; you buy one banana.
VO: YOU START GOING TO THE TWENTY-FOUR HOUR SHOP JUST TO SEE SOMEONE.
sfx fridge_hum, ding · tail 0.8
[fridge] You talking to the fridge. The fridge hums back.
VO: YOU START TALKING TO THE FRIDGE. THE FRIDGE IS A GOOD LISTENER.
sfx fridge_hum · tail 0.8
[always_online] Split screen: you sending long messages at 4 AM / Sam waking up to 63 unread messages, horrified.
VO: YOU BECOME THE PERSON WHO'S ALWAYS ONLINE. PEOPLE START MUTING YOU.
voice am_puck "SIXTY-THREE MESSAGES?" · sfx notification x6
[ch3] CHAPTER 3 card: "THE MATH" · music → curious · sfx impact
[math1] Stat card counting: 8 HOURS × 365 DAYS = 2,920 HOURS / YEAR.
VO: LET'S DO THE MATH. EIGHT HOURS, TIMES THREE SIXTY-FIVE. TWO THOUSAND NINE HUNDRED AND TWENTY EXTRA HOURS. EVERY YEAR.
sfx tick, tick, ding
[math2] Life bar: a normal life with a third shaded "SLEEP", then yours with it all lit up.
VO: MOST PEOPLE SPEND ABOUT A THIRD OF THEIR LIFE ASLEEP. YOU GET ALL OF IT BACK.
source "Source: general sleep guidance, e.g. NHLBI (verify)" · sfx whoosh
[skills] Montage of you mastering things: chess, three languages, drawing, cooking, coding.
VO: YOU BECOME THE MOST SKILLED PERSON YOU KNOW.
music → upbeat · sfx pop, pop, pop
[lonely] Pull back: you alone in a lit room in a dark city, still practising.
VO: AND THE MOST ALONE.
music → lonely · sfx crickets · tail 1.0
[break] Black + silence (mid-roll safe) · 1.0s
[ch4] CHAPTER 4 card: "THE THING YOU MISSED" · sfx impact
[sam_dream] Daytime: Sam telling a wild dream (a dream bubble: flying shark, school in space). Everyone laughs.
VO: ONE DAY, SAM TELLS EVERYONE ABOUT HIS DREAM. FLYING SHARKS. SCHOOL IN SPACE.
sfx crowd, pop
[realise] Close on you: the laughter fades. HUD DREAMS 0 flashes red.
VO: AND YOU REALISE: YOU HAVEN'T DREAMED IN MONTHS.
HUD DREAMS 0 (red) · music → stop · sfx heartbeat
[science] Calm interlude: a friendly brain icon; sleep as "the night shift" for the brain: sorting the day, saving important memories, processing emotions. Source chips.
VO: HERE'S THE REAL PART. SCIENTISTS THINK SLEEP IS WHEN YOUR BRAIN DOES SOME OF ITS MOST IMPORTANT WORK. SORTING THE DAY. SAVING WHAT MATTERS. HELPING YOU DEAL WITH HOW THINGS FELT.
music → wonder · source "Source: NIH / sleep research (verify)" · sfx tick
[flat_memories] Your memories of the year as a flat grey list on a board, vs Sam's memories as colourful bubbles.
VO: YOUR POWER SKIPS ALL OF THAT. YOU REMEMBER EVERYTHING YOU STUDIED. BUT THE YEAR FEELS LIKE A *LIST*.
sfx page_flip
[ch5] CHAPTER 5 card: "THE TRADE" · music → lonely · sfx impact
[lily_nightmare] Night: Lily appears in your doorway with her plush rabbit, scared.
VO: ONE NIGHT, YOUR LITTLE SISTER LILY WAKES UP FROM A NIGHTMARE.
NAME TAG LILY · MY SISTER · 8 · sfx crickets
[lily_ask] Lily on your bed: "What did YOU dream about? Tell me a good one."
VO: SHE ASKS YOU TO TELL HER YOUR DREAM. A GOOD ONE. SO SHE CAN HAVE IT TOO.
voice af_sky "TELL ME A GOOD ONE." · sfx heartbeat
[cant] Close on you: silence. You have nothing.
VO: YOU DON'T HAVE ONE.
music → stop · tail 1.2
[replay] Rapid split cards WHAT YOU THOUGHT → WHAT IT WAS: FREE TIME → TIME ALONE · ALWAYS AVAILABLE → NOBODY TO TALK TO · REMEMBERING EVERYTHING → FORGETTING HOW IT FELT · NEVER TIRED → NEVER RESTED · MORE LIFE → FEWER DREAMS.
VO: YOU THOUGHT YOU HAD MORE TIME. YOU JUST HAD MORE *NIGHT*.
sfx whoosh x5
[made_up] You make up a dream for Lily: the screen fills with a hand-drawn dream bubble (a whale carrying a lit house across the stars). Lily falls asleep smiling.
VO: SO YOU MAKE ONE UP. A WHALE CARRYING A HOUSE ACROSS THE STARS. SHE FALLS ASLEEP BEFORE THE END.
music → wonder · sfx snore (soft)
[trade] You alone, looking at the bed. HUD fades out line by line.
VO: AND FOR THE FIRST TIME, YOU'D TRADE EVERY FREE HOUR YOU EVER HAD. FOR ONE DREAM.
sfx tick
[lie_down] You lie down and close your eyes. Hold. The clock's face finally smiles.
VO: FOR THE FIRST TIME IN A YEAR, I COULDN'T WAIT TO FALL ASLEEP.
music → stop · tail 2.5
[black] Black screen, silence · 1.5s
[endcard] End card: your stickman yawning. HUD hidden/reset · sfx yawn, whoosh · 4.5s · CTA "WOULD YOU TAKE THE POWER? YES / NO"

Original concept: "The Wall at Ashford" by @OnlySainted (CC BY 4.0). This adaptation: a "What If" format template.
