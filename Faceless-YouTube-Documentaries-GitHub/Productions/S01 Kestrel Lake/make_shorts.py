"""3 vertical Shorts per episode (standing instruction #8).

python make_shorts.py --part 1  ->  output/shorts/part1_short{1,2,3}.mp4  (1080x1920, -14 LUFS)
Each short = shot range from parts/partN.json "shorts", 16:9 frame centred over a blurred fill, hook text on top, CTA at the bottom.
"""
import argparse, json, os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    return s.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--part", type=int, required=True); a = ap.parse_args()
    spec = json.load(open(os.path.join(ROOT, "parts", f"part{a.part}.json"), encoding="utf8"))
    tl = json.load(open(os.path.join(ROOT, "build", f"part{a.part}", "timeline.json"), encoding="utf8"))
    shots = {s["id"]: s for s in tl["shots"]}
    src = os.path.join(ROOT, "output", f"part{a.part}.mp4")
    out_dir = os.path.join(ROOT, "output", "shorts"); os.makedirs(out_dir, exist_ok=True)
    # ffmpeg filter paths: run from the fonts dir so the fontfile path has no drive colon / spaces
    fonts = os.path.join(ROOT, "render", "fonts")
    for i, sh in enumerate(spec["shorts"], 1):
        t0, t1 = shots[sh["from"]]["start"], min(shots[sh["to"]]["end"], shots[sh["from"]]["start"] + 59)
        out = os.path.join(out_dir, f"part{a.part}_short{i}.mp4")
        vf = (
            "[0:v]split[a][b];"
            "[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=40,eq=brightness=-0.18[bg];"
            "[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2,"
            f"drawtext=fontfile=Oswald.ttf:text='{esc(sh['hook'])}':fontsize={78 if len(sh['hook']) <= 22 else 62}:fontcolor=0xffc23d:borderw=6:bordercolor=0x0b1426:"
            "x=(w-tw)/2:y=330,"
            f"drawtext=fontfile=Oswald.ttf:text='THE QUIET AT KESTREL LAKE · PART {a.part}':fontsize=40:fontcolor=0xeef3fa:x=(w-tw)/2:y=250,"
            "drawtext=fontfile=Oswald.ttf:text='FULL EPISODE ON THE CHANNEL':fontsize=52:fontcolor=0xeef3fa:borderw=5:bordercolor=0x0b1426:"
            "x=(w-tw)/2:y=1560[v]"
        )
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t0:.3f}", "-to", f"{t1:.3f}", "-i", src,
                        "-filter_complex", vf, "-map", "[v]", "-map", "0:a",
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st=%.2f:d=0.6" % (t1 - t0 - 0.6),
                        "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "30",
                        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True, cwd=fonts)
        print(f"short {i}: {t1 - t0:.1f}s -> {out}")


if __name__ == "__main__":
    main()
