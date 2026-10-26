# Asset Library Workflow (No-Stock Policy)
*We don't use stock footage. The equivalent of a stock library for this channel is our **own reusable asset library**: scenes, characters, props, music stems and SFX that every new series can pull from. Building it once makes each new series faster.*

## Library layout (proposed shared folder)
```
Visual Storytelling/Asset Library/
  scenes/        # S.<scene> functions copied from render/index.html, one file per scene, with a preview PNG
  characters/    # character specs: head, eyes, hoodie colour, poses (Noah, June, Biscuit, Tall Ones…)
  props/         # SVG props: generator, CO detector, rule card, note, flashlight
  hud/           # HUD layouts per series
  music/         # ACE-Step stems by mood (cabin, tension, rules, dread, drone) + prompt used
  sfx/           # rendered SFX wavs (wind, hum, knock…) for quick reuse
  thumbs/        # winning thumbnail art + text layouts
```

## Workflow when starting a new series
1. **Inventory:** list the scenes the new series needs. Mark which already exist (`window_pov, title, ext_cabin, int_cabin, shed, note, rule_card, alarm, woodpile, door, black, end_card`).
2. **Reskin, don't rebuild:** a new location is mostly a palette + background swap of an existing scene (cabin → basement).
3. **Build only the gaps:** new scenes go into the production's `render/index.html` as `S.<name>`, then get copied into the library when they've shipped.
4. **Music:** reuse mood stems if the tone matches; otherwise run `gen_music.py` with the PROMPT LIBRARY template and a new niche tone.
5. **Register** new assets in the library README table below.

## Library index
| Asset | Type | Created for | Reusable as | Preview |
|---|---|---|---|---|
| `window_pov` | scene | S01P1 | any "looking outside" shot | `scenes/window_pov.png` |
| `rule_card` | scene | S01P1 | every series | `scenes/rule_card.png` |
| Noah | character | S01 | narrator template | `characters/noah.md` |
| cabin / tension / rules / dread / drone | music | S01 | winter series | `assets/music/*.wav` |

## Quality rules
- Every library asset must follow the visual identity (CHANNEL BIBLE tokens, flat vector, film grain 7%).
- Keep a preview PNG for every scene (render with `node render.js --part N --still T`).
- Version scenes: `door_v2` instead of overwriting a scene a published Part depends on.

## Why this beats stock footage
Consistent style (brand recognition), no licence risk, no reused-content issues, and production time drops with each series.
