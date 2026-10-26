"""FLUX.2 Klein 4B (Apache-2.0) thumbnail art -> build/thumbs/art_<n>.png  (text is composited later by thumbs.js)."""
import os, sys, torch
from diffusers import Flux2KleinPipeline

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "build", "thumbs"); os.makedirs(OUT, exist_ok=True)

BASE = ("flat 2D vector illustration, YouTube thumbnail, 16:9. A cartoon boy whose head is a perfectly round solid pitch-black circle "
        "with no skin, no hair, no nose and no ears, only two big white oval eyes (silhouette stickman style), "
        "wearing a red hoodie, {pose}, inside a dark log cabin at night. Behind him a frosted window shows a snowy pine treeline where "
        "two very tall dark figures stand, each with a single glowing white light for an eye. Deep navy and warm amber palette, strong rim "
        "light, clean bold shapes, high contrast, empty space top-left for text, no text, no watermark.")
POSES = [
    "facing the viewer with wide frightened eyes, his back to the window",
    "pressed against the cabin door with both hands, eyes wide",
    "holding a flashlight pointed at the window, side view, tense",
    "close-up of his face in the left third, eyes wide, the window glowing behind his shoulder",
    "kneeling beside a little girl with the same pitch-black round head and white oval eyes, wearing a yellow hoodie and red beanie, shielding her, both staring at the window",
]

pipe = Flux2KleinPipeline.from_pretrained("black-forest-labs/FLUX.2-klein-4B", torch_dtype=torch.bfloat16)
pipe.enable_sequential_cpu_offload()  # 4B transformer is ~8 GB bf16 — stream layers on an 8 GB card
only = [int(a) for a in sys.argv[1:]] or range(len(POSES))
for i in only:
    img = pipe(prompt=BASE.format(pose=POSES[i]), width=1280, height=720, num_inference_steps=4, guidance_scale=1.0,
               generator=torch.Generator("cpu").manual_seed(100 + i)).images[0]
    p = os.path.join(OUT, f"art_{i + 1}.png"); img.save(p); print(p, flush=True)
