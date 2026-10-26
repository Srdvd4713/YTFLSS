r"""ACE-Step 1.5 score stems -> assets/music/<mood>.wav (picked up automatically by voice.py).

Run with the ACE-Step venv:
  ..\..\tools\ACE-Step-1.5\.venv\Scripts\python.exe gen_music.py
"""
import os, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ACE = os.path.abspath(os.path.join(ROOT, "..", "..", "tools", "ACE-Step-1.5"))
sys.path.insert(0, ACE)
os.chdir(ACE)

from acestep.handler import AceStepHandler
from acestep.llm_inference import LLMHandler
from acestep.inference import GenerationParams, GenerationConfig, generate_music

# Prompt template from the folder: "[NICHE TONE] cinematic, [MOOD], no lyrics, documentary score"
MOODS = {
    "cabin":   "winter survival cinematic, quiet unease, sparse felt piano and soft strings, slow, minor key, no lyrics, documentary score",
    "tension": "winter survival cinematic, creeping tension, low string tremolo, ticking pulse, minor key, no lyrics, documentary score",
    "rules":   "winter survival cinematic, steady determined pulse, low drums and cello ostinato, dark, no lyrics, documentary score",
    "dread":   "winter horror cinematic, deep dread, dark ambient drone, sub bass, distant metallic textures, no melody, no lyrics, documentary score",
    "drone":   "dark ambient, subtle tension, drone bass, mysterious, cinematic, no melody, no lyrics",
}

dit = AceStepHandler()
# offload: without it the models leave <1 GB free on an 8 GB laptop GPU and the VRAM pre-flight refuses to generate
msg = dit.initialize_service(project_root=ACE, config_path="acestep-v15-turbo", device="cuda", offload_to_cpu=True)
print("DiT:", msg)
llm = LLMHandler()

out_dir = os.path.join(ROOT, "assets", "music"); os.makedirs(out_dir, exist_ok=True)
tmp = os.path.join(ROOT, "build", "ace_tmp")
only = sys.argv[1:] or list(MOODS)
for mood in only:
    params = GenerationParams(caption=MOODS[mood], lyrics="[Instrumental]", instrumental=True,
                              duration=90, bpm=70, thinking=False, seed=1234)
    res = generate_music(dit, llm, params, GenerationConfig(batch_size=1, audio_format="wav"), save_dir=tmp)
    if not res.success:
        print(mood, "FAILED:", res.error); continue
    shutil.copy(res.audios[0]["path"], os.path.join(out_dir, f"{mood}.wav"))
    print(mood, "->", os.path.join(out_dir, f"{mood}.wav"))
