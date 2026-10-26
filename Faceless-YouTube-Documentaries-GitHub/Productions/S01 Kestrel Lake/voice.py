"""Voice + timeline + audio mix pipeline (Wall at Ashford engine, Kestrel Lake adaptation).

python voice.py --part 1
  -> build/part1/timeline.json   (shot timing, captions, talk intervals, HUD)  consumed by render/index.html
  -> build/part1/mix.wav         (VO + SFX + ducked music, loudnorm -14 LUFS / -1.5 dBTP)
  -> output/part1.srt            (closed captions for YouTube upload)
"""
import argparse, json, os, re, subprocess
import numpy as np
import soundfile as sf
from scipy import signal
from scipy.ndimage import uniform_filter1d

ROOT = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.join(ROOT, "..", "..", "tools", "kokoro-models")
SR = 48000
rng = np.random.default_rng(7)

EXTRA_VOICES = {"voice": {"voice": "bm_george", "speed": 0.88, "muffle": True}}


# ---------------------------------------------------------------- helpers
def db(x):
    return 10 ** (x / 20)


def env(n, a=0.005, r=0.05):
    """Attack/release envelope over n samples."""
    e = np.ones(n)
    na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e


def noise(n, color="white"):
    w = rng.standard_normal(n)
    if color == "pink":
        b, a = [0.049922035, -0.095993537, 0.050612699, -0.004408786], [1, -2.494956002, 2.017265875, -0.522189400]
        w = signal.lfilter(b, a, w) * 8
    elif color == "brown":
        w = np.cumsum(w); w = signal.lfilter([1, -1], [1, -0.995], w) / 30
    return w


def band(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, hi], btype="band", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def lp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, fs=SR, output="sos"), x)


def hp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, btype="high", fs=SR, output="sos"), x)


def norm(x, peak=0.9):
    m = np.max(np.abs(x)) or 1
    return x / m * peak


def x_rms(x, target_db):
    """Scale to a target RMS level so moods sit evenly under the voice (stems differ by ~7 dB)."""
    r = np.sqrt((x ** 2).mean()) or 1
    return x * db(target_db) / r


def t_(n):
    return np.arange(n) / SR


# ---------------------------------------------------------------- SFX library (synthesized, no stock)
def sfx(name, dur=None):
    if name == "wind":
        n = int((dur or 6) * SR); x = band(noise(n, "pink"), 150, 900)
        lfo = 0.55 + 0.45 * np.sin(2 * np.pi * 0.13 * t_(n) + 1) * np.sin(2 * np.pi * 0.07 * t_(n))
        return norm(x * lfo, 0.8)
    if name == "hum":  # gas generator through a wall
        n = int((dur or 6) * SR); tt = t_(n); f = 58 + 0.6 * np.sin(2 * np.pi * 0.3 * tt)
        ph = 2 * np.pi * np.cumsum(f) / SR
        x = sum(np.sin(k * ph) / k ** 0.8 for k in range(1, 9))
        x *= 0.8 + 0.2 * np.sin(ph / 2)  # 2-stroke lope
        x += 0.15 * lp(noise(n), 400)
        return norm(lp(x, 500), 0.8)
    if name == "heartbeat":
        out = np.zeros(int(4.2 * SR))
        for i in range(4):
            for off, g in ((0, 1), (0.22, 0.7)):
                s = int((i * 0.95 + off) * SR); n = int(0.18 * SR); tt = t_(n)
                out[s:s + n] += g * np.sin(2 * np.pi * (55 - 20 * tt / 0.18) * tt) * np.exp(-tt * 22)
        return norm(out)
    if name == "boom":
        n = int(3.5 * SR); tt = t_(n)
        x = np.sin(2 * np.pi * np.cumsum(80 * np.exp(-tt * 1.4) + 32) / SR) * np.exp(-tt * 1.3)
        x += 0.5 * lp(noise(n), 300) * np.exp(-tt * 6)
        return norm(x)
    if name == "snore":
        n = int(3.0 * SR); tt = t_(n)
        x = band(noise(n), 80, 500) * np.clip(np.sin(np.pi * tt / 1.6), 0, 1) ** 2
        return norm(x, 0.6)
    if name == "static":
        n = int(2.6 * SR); x = band(noise(n), 900, 6000) * (0.7 + 0.3 * (rng.random(n) > 0.997))
        return norm(x * env(n, 0.05, 0.4), 0.7)
    if name == "paper":
        n = int(1.0 * SR); x = hp(noise(n), 2500) * (rng.random(n) ** 6)
        x = lp(x, 9000) * np.abs(np.sin(np.pi * t_(n) / 1.0))
        return norm(x, 0.7)
    if name == "pencil":
        n = int(1.6 * SR); tt = t_(n)
        x = band(noise(n), 2000, 7000) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 7 * tt)))
        return norm(x * env(n, 0.02, 0.2), 0.5)
    if name == "flip":  # whoosh + metal tick
        n = int(0.7 * SR); tt = t_(n)
        w = band(noise(n), 400, 3000) * np.sin(np.pi * np.clip(tt / 0.45, 0, 1)) ** 2
        k = np.zeros(n); s = int(0.42 * SR); m = int(0.25 * SR); tk = t_(m)
        k[s:s + m] = (np.sin(2 * np.pi * 2600 * tk) + 0.6 * np.sin(2 * np.pi * 3900 * tk)) * np.exp(-tk * 30)
        return norm(0.7 * w + k)
    if name == "ring":
        n = int(4.0 * SR); return 0.3 * np.sin(2 * np.pi * 6100 * t_(n)) * env(n, 1.0, 2.0)
    if name == "crunch":
        n = int(0.35 * SR); tt = t_(n)
        x = lp(noise(n), 3500) * (rng.random(n) ** 3) * np.exp(-tt * 9)
        return norm(x)
    if name == "door":
        n = int(1.2 * SR); tt = t_(n)
        thud = np.sin(2 * np.pi * 70 * tt) * np.exp(-tt * 12)
        creak = signal.sawtooth(2 * np.pi * np.cumsum(180 + 40 * np.sin(2 * np.pi * 3 * tt)) / SR) * env(n, 0.3, 0.5)
        return norm(thud + 0.12 * band(creak, 300, 2000))
    if name == "chirp":
        n = int(0.09 * SR); return 0.9 * np.sin(2 * np.pi * 3200 * t_(n)) * env(n, 0.002, 0.01)
    if name == "click":
        n = int(0.06 * SR); tt = t_(n)
        return norm(hp(noise(n), 1500) * np.exp(-tt * 120) + np.sin(2 * np.pi * 1800 * tt) * np.exp(-tt * 90))
    if name == "riser":
        n = int(3.0 * SR); tt = t_(n)
        x = np.sin(2 * np.pi * np.cumsum(120 + 500 * (tt / 3) ** 2) / SR) * (tt / 3) ** 2
        return norm(x + 0.5 * band(noise(n), 500, 5000) * (tt / 3) ** 3, 0.8)
    if name == "knock":  # heavy knuckle on a wooden door
        n = int(0.3 * SR); tt = t_(n)
        x = (np.sin(2 * np.pi * 110 * tt) + 0.6 * np.sin(2 * np.pi * 240 * tt) + 0.3 * np.sin(2 * np.pi * 530 * tt)) * np.exp(-tt * 28)
        x += 0.4 * lp(noise(n), 2500) * np.exp(-tt * 90)
        return norm(x)
    raise ValueError(name)


# ---------------------------------------------------------------- music bed
def score_bed(mood, n, t0):
    """ACE-Step stem if present in assets/music/<mood>.wav, else synthesized fallback.  t0 = global offset (keeps phase continuous)."""
    path = os.path.join(ROOT, "assets", "music", f"{mood}.wav")
    if os.path.exists(path):
        x, sr = sf.read(path, always_2d=True); x = x.mean(1)
        if sr != SR: x = signal.resample_poly(x, SR, sr)
        start = int(t0 * SR) % len(x)
        reps = np.tile(x, (start + n) // len(x) + 2)
        return x_rms(reps[start:start + n], -22)
    tt = t_(n) + t0

    def pad(freqs, det=0.6, bright=900):
        x = sum(signal.sawtooth(2 * np.pi * f * tt) + signal.sawtooth(2 * np.pi * (f + det) * tt) for f in freqs)
        return lp(x, bright)

    if mood == "drone":
        x = pad([55, 82.4], 0.3, 300) + 0.3 * band(noise(n, "brown"), 40, 200)
    elif mood == "cabin":  # slow A-minor plucks over a soft pad
        x = 0.5 * pad([110, 164.8, 220], 0.4, 600)
        notes = [220, 261.6, 329.6, 293.7, 261.6, 196, 220, 164.8]
        step = 1.1
        for i in range(int(t0 / step), int((t0 + n / SR) / step) + 1):
            s = int((i * step - t0) * SR)
            m = int(2.5 * SR); tk = t_(m); f = notes[i % len(notes)]
            pl = (np.sin(2 * np.pi * f * tk) + 0.3 * np.sin(4 * np.pi * f * tk)) * np.exp(-tk * 2.2)
            a, b = max(s, 0), min(s + m, n)
            if b > a: x[a:b] += 1.8 * pl[a - s:b - s]
    elif mood == "tension":
        x = pad([110, 116.5], 0.7, 700) * (0.8 + 0.2 * np.sin(2 * np.pi * 6 * tt))
        x += pad([55], 0.2, 200)
    elif mood == "rules":
        x = pad([73.4, 110], 0.5, 500)
        beat = (tt % 0.75) < 0.06
        x += 3 * lp(noise(n), 200) * beat
    elif mood == "dread":
        x = pad([41.2, 43.65, 61.7], 0.2, 260) + 0.4 * band(noise(n, "brown"), 30, 120)
    elif mood == "sting":
        x = pad([55, 82.4, 110], 0.5, 1200) * np.exp(-((tt - t0) % 100) * 0.4)
    else:
        return np.zeros(n)
    return norm(x, 0.5)


# ---------------------------------------------------------------- TTS
def tts_engine():
    from kokoro_onnx import Kokoro
    return Kokoro(os.path.join(MODELS, "kokoro-v1.0.onnx"), os.path.join(MODELS, "voices-v1.0.bin"))


def speak(k, text, cfg):
    audio, sr = k.create(text, voice=cfg["voice"], speed=cfg.get("speed", 1.0), lang="en-us")
    audio = signal.resample_poly(audio, SR, sr)
    # trim leading/trailing silence so captions align with speech
    idx = np.where(np.abs(audio) > 0.01)[0]
    if len(idx): audio = audio[max(idx[0] - 240, 0): idx[-1] + 2400]
    if cfg.get("muffle"):  # through-the-door voice: lowpass + short room echo
        audio = lp(audio, 900, 4)
        d = int(0.06 * SR); audio = np.concatenate([audio, np.zeros(d)]); audio[d:] += 0.35 * audio[:-d]
    return audio.astype(np.float64)


def caption_chunks(text, start, dur, who):
    """Split a VO line into <=4-word chunks; time words by character weight."""
    words = []
    for w in text.split():
        hl = "*" in w
        words.append({"w": w.replace("*", ""), "hl": hl})
    weights = np.array([len(w["w"]) + 2 + (6 if re.search(r"[.,!?…]$", w["w"]) else 0) for w in words], float)
    cum = np.concatenate([[0], np.cumsum(weights)]) / weights.sum() * dur
    for i, w in enumerate(words):
        w["t"] = round(start + cum[i], 3)
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= 4 or re.search(r"[.!?…]$|\.\.\.$", w["w"]) or (re.search(r",$", w["w"]) and len(cur) >= 2):
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    out = []
    ends = [c[0]["t"] for c in chunks[1:]] + [start + dur]
    for c, e in zip(chunks, ends):
        out.append({"start": c[0]["t"], "end": round(e, 3), "who": who, "words": c})
    return out


def srt_time(s):
    h, r = divmod(s, 3600); m, r = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(r):02},{int((r % 1) * 1000):03}"


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, required=True)
    args = ap.parse_args()
    spec = json.load(open(os.path.join(ROOT, "parts", f"part{args.part}.json"), encoding="utf8"))
    voices = {**EXTRA_VOICES, **spec["voices"]}
    bdir = os.path.join(ROOT, "build", f"part{args.part}"); os.makedirs(bdir, exist_ok=True)
    k = tts_engine()

    timeline, vo_clips, t, hud = [], [], 0.0, {"visible": False}
    GAP = 0.32
    for shot in spec["shots"]:
        pre, post = shot.get("pad", [0.3, 0.5])
        cursor, caps, talk = t + pre, [], []
        for line in shot.get("vo", []):
            clean = line["text"].replace("*", "")
            a = speak(k, clean, voices[line["who"]])
            d = len(a) / SR
            vo_clips.append((cursor, a, line["who"]))
            caps += caption_chunks(line["text"], cursor, d, line["who"])
            talk.append({"who": line["who"], "start": round(cursor, 3), "end": round(cursor + d, 3)})
            cursor += d + GAP
        if shot.get("vo"): cursor -= GAP
        dur = max(cursor + post - t, shot.get("min", 0))
        hud = {**hud, **shot["hud"]} if "hud" in shot else hud
        timeline.append({**{k_: v for k_, v in shot.items() if k_ not in ("vo",)},
                         "start": round(t, 3), "end": round(t + dur, 3), "captions": caps, "talk": talk, "hud": hud})
        t += dur
    total = t
    print(f"part {args.part}: {len(timeline)} shots, {total:.1f}s")

    n = int(total * SR) + SR
    vo = np.zeros(n); fx = np.zeros(n); mus = np.zeros(n)
    for start, a, who in vo_clips:
        s = int(start * SR); vo[s:s + len(a)] += a * (0.8 if who != "voice" else 0.55)

    for sh in timeline:
        s0, s1 = int(sh["start"] * SR), int(sh["end"] * SR)
        for e in sh.get("sfx", []):
            dur = sh["end"] - sh["start"]
            if e.get("loop"):
                clip = sfx(e["name"], dur + 0.5)
                at = s0
            else:
                clip = sfx(e["name"])
                at = s0 + int((e["at"] if e["at"] >= 0 else dur + e["at"]) * SR)
            g = db(e.get("gain", -12))
            if e.get("loop"):  # fade loops at shot edges to avoid clicks
                clip = clip[: s1 - s0 + int(0.4 * SR)] * env(min(len(clip), s1 - s0 + int(0.4 * SR)), 0.3, 0.4)
            end = min(at + len(clip), n)
            fx[at:end] += clip[: end - at] * g

    # music: per-shot mood with 1.2s crossfades
    XF = int(1.2 * SR)
    for sh in timeline:
        mood = sh.get("music", "silence")
        s0, s1 = max(int(sh["start"] * SR) - XF // 2, 0), min(int(sh["end"] * SR) + XF // 2, n)
        seg = score_bed(mood, s1 - s0, s0 / SR) * env(s1 - s0, 0.6, 0.6)
        if mood == "sting": seg *= 1.6
        mus[s0:s1] += seg * db(-17)

    # duck music -10 dB under narration (smoothed sidechain)
    vo_env = uniform_filter1d(np.abs(vo), int(0.05 * SR))
    gate = uniform_filter1d((vo_env > 0.01).astype(float), int(0.4 * SR))
    mus *= 1 - (1 - db(-10)) * np.clip(gate, 0, 1)

    mix = vo + fx + mus
    mix = np.tanh(mix * 0.9) / 0.9  # gentle safety clip
    raw = os.path.join(bdir, "mix_raw.wav"); sf.write(raw, np.stack([mix, mix], 1).astype(np.float32), SR)

    # two-pass loudnorm to -14 LUFS (YouTube)
    out = os.path.join(bdir, "mix.wav")
    p1 = subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                        capture_output=True, text=True).stderr
    m = json.loads(p1[p1.rindex("{"):p1.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", af, "-ar", str(SR), out], check=True)

    json.dump({"part": args.part, "series": spec["series"], "title": spec["title"], "width": spec["width"],
               "height": spec["height"], "fps": spec["fps"], "duration": round(total, 3), "shots": timeline},
              open(os.path.join(bdir, "timeline.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)

    os.makedirs(os.path.join(ROOT, "output"), exist_ok=True)
    with open(os.path.join(ROOT, "output", f"part{args.part}.srt"), "w", encoding="utf8") as f:
        i = 1
        for sh in timeline:
            for c in sh["captions"]:
                f.write(f"{i}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{' '.join(w['w'] for w in c['words'])}\n\n"); i += 1
    print("wrote", out)


if __name__ == "__main__":
    main()
