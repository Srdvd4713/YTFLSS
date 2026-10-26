# Audio Mixing Standards
*The mix is produced automatically by `voice.py` (SOP step 4). This file documents the targets, the signal chain and how to fix common problems. Full ffmpeg reference: `Automation & Systems/Content Pipeline SOPs/ffmpeg-skill GOLD.md`.*

## Delivery targets
| Item | Target |
|---|---|
| Integrated loudness | **-14 LUFS** (YouTube reference) |
| True peak | **≤ -1.5 dBTP** |
| Loudness range | ~11 LU (`LRA=11`) |
| Music under VO | ducked **-10 dB** while voice plays (current S01 bed sits ~-24 dB under VO; needs a human listen) |
| Format | 48 kHz, stereo, AAC in the final MP4 |

## Signal chain (what voice.py does, in order)
1. **Kokoro TTS** per line (clean, no noise. No denoise needed).
2. Per-role processing: door voice = lowpass 900 Hz + 60 ms echo (`muffle`).
3. Lines placed on the timeline (`build/partN/timeline.json`).
4. SFX layer placed per shot.
5. Music stems per mood, crossfaded between shots, ducked under VO.
6. Two-pass `loudnorm=I=-14:TP=-1.5:LRA=11` on the full mix → `build/partN/mix.wav`.

## Checks
```
ffmpeg -i build/partN/mix.wav -af ebur128=peak=true -f null -     # expect I: -14.0 LUFS, peak <= -1.5
ffmpeg -i output/partN.mp4 -af ebur128=peak=true -f null -        # same after render. Do NOT re-normalize
```

## Fixes for common problems
| Problem | Fix |
|---|---|
| Music too quiet / mix feels empty | Raise the music bed gain in voice.py by 3 dB steps; re-check -14 LUFS |
| VO masked by music | Increase duck depth to -12 dB, or EQ-dip the music at 2–4 kHz |
| Harsh "s" sounds in TTS | De-ess: `deesser` filter, or lower speed slightly (0.95) |
| SFX jump scare clips | Keep true peak limit; lower that SFX by 3–6 dB rather than squashing the mix |
| Clicks between lines | 10 ms fades at clip edges (`afade=t=in:d=0.01`, `afade=t=out:st=…:d=0.01`) |
| Voice sounds robotic in long lines | Split into shorter sentences (narration rule: 1–2 sentences per shot) |

## Human listen-through (required before upload)
- Headphones **and** phone speaker. Most viewers watch on mobile.
- Listen for: VO intelligibility at every point, music too loud during whispers, SFX that pull focus from a clue, silence that feels like an error.
- Note fixes as timestamps; re-run `python voice.py --part N`.

## Translated channels
Re-run voice.py with the new language voices; the same loudness targets apply. Check that longer translated lines don't overrun the shot (see `Script-to-Voice Alignment/`).
