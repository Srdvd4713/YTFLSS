# ffmpeg-skill ??
**GitHub:** https://github.com/kajisho5/ffmpeg-skill
**Stage:** AI-Driven Video Editing — Claude watches + edits your video
**Status:** ? BEST FOUND FOR EDITING READY VIDEOS

---

## Why This One Hits Different

Most AI video tools generate footage. This one **edits it**.

Claude literally watches your video, understands what's in it, then runs FFmpeg commands to edit it — perfectly, fast, in absurd quality. No timeline scrubbing. No manual trim points. Just describe what you want.

---

## What It Does

- Claude **watches your video** and understands the content
- You describe edits in natural language
- Claude generates precise FFmpeg commands
- Output: edited video in full quality — no re-encoding artifacts
- Works on **ready-to-upload** documentary files

---

## Why FFmpeg Is the Right Engine

| Property | Value |
|----------|-------|
| Speed | Fastest video processor available |
| Quality | Lossless and near-lossless modes |
| Format Support | Every format (MP4, MOV, MKV, WebM, etc.) |
| Cost | Free, open source, runs 100% local |
| Reliability | Industry standard since 2000 |

---

## What Claude Can Do With Your Documentary

### ?? Editing
- "Cut the first 10 seconds and start at the hook"
- "Remove the 3-minute segment between 12:40 and 15:20"
- "Trim all silences over 1.5 seconds"
- "Keep only the sections where the narrator is speaking"

### ?? Audio
- "Normalize audio to -14 LUFS for YouTube"
- "Remove background hum from the voiceover track"
- "Lower the music by 8dB during dialogue sections"
- "Add 0.5s fade in and fade out to the audio"

### ?? Visual
- "Add a subtle vignette to the entire video"
- "Increase contrast by 15% and slightly desaturate"
- "Apply a warm color grade — push shadows to amber"
- "Add letterbox bars for cinematic 2.35:1 aspect ratio"

### ?? Subtitles & Text
- "Burn in the SRT subtitle file to the video"
- "Add a chapter title card at 0:00, 5:30, 12:00, 18:45"
- "Add a lower third at 2:15 — 'Dr. Jane Morris, Harvard University'"

### ?? Export
- "Export optimized for YouTube (H.264, 4K, AAC audio)"
- "Create a 720p web preview version"
- "Export audio-only MP3 for podcast upload"
- "Extract frames at every chapter marker as JPG"

---

## Workflow for Faceless Documentaries

```
RAW EDIT (rough cut in any editor)
        ¦
        ?
[ffmpeg-skill + Claude]
        ¦
        +-- Watch video ? understand content
        +-- Apply: color grade (lemo-opuscar style)
        +-- Normalize audio to YouTube standard (-14 LUFS)
        +-- Burn subtitles
        +-- Add Remotion-generated chapter cards
        +-- Trim pacing issues
        +-- Export: YouTube-ready MP4
        ¦
        ?
UPLOAD-READY FILE
```

---

## Integration With Your Stack

| Tool | How ffmpeg-skill Works With It |
|------|-------------------------------|
| **Kokoro TTS** | Mix AI voiceover onto video track at correct levels |
| **ACE-Step music** | Layer background score, duck under dialogue |
| **Remotion** | Composite rendered title cards into video |
| **lemo-opuscar** | Apply film style filter via FFmpeg pipeline |
| **AI Shorts Generator** | Re-export clips in vertical 9:16 format |
| **Podcastfy** | Extract clean audio ? feed to podcast pipeline |

---

## Power Commands Reference

### YouTube Export (Copy + Save These)
```
# 4K YouTube optimized
-c:v libx264 -crf 18 -preset slow -c:a aac -b:a 320k -movflags +faststart

# 1080p YouTube optimized
-c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k -movflags +faststart

# Audio normalize to YouTube standard
-af loudnorm=I=-14:TP=-1.5:LRA=11
```

### Subtitles
```
# Burn in SRT
-vf subtitles=subtitles.srt:force_style='FontName=Inter,FontSize=24,PrimaryColour=&Hffffff'

# Burn in with documentary style (white text, black outline)
-vf subtitles=subs.srt:force_style='FontSize=26,PrimaryColour=&Hffffff,OutlineColour=&H000000,Outline=2'
```

### Silence Removal (Pacing Fix)
```
# Remove silences over 1.5 seconds
-af silenceremove=stop_periods=-1:stop_duration=1.5:stop_threshold=-40dB
```

### Quick Cuts
```
# Trim: keep 0:30 to 12:00
-ss 00:00:30 -to 00:12:00 -c copy

# Remove section 5:00–7:30 (requires concat)
# Claude handles this automatically with the skill
```

---

## Prompt Templates to Use With Claude

### Full Documentary Final Export
> "Watch this documentary file. Normalize the audio to -14 LUFS YouTube standard, remove any silences longer than 2 seconds, apply a subtle cinematic vignette, burn in the attached SRT file, and export as H.264 1080p optimized for YouTube. Keep quality as high as possible."

### Quick Pacing Fix
> "Watch this video and identify any sections with dead air or slow pacing. Trim those sections and export a tighter cut. Show me the timestamps of what you removed."

### Music Ducking
> "I have a voiceover track and a background music track. Mix them together so music is at -20dB during speech and rises to -12dB during non-speech sections. Export as a single audio file."

### Chapter Cards Composite
> "I have a main video and 5 Remotion-rendered chapter card clips (chapter_1.mp4 through chapter_5.mp4). Insert them at timestamps: 0:00, 4:30, 9:15, 14:00, 18:45. Export as one seamless video."

---

## Notes
- This is the **final stage** tool in your pipeline — runs on finished content
- No quality loss on copy-stream operations (Claude knows when to use `-c copy`)
- Fast because FFmpeg is native — no cloud upload/download cycles
- Works entirely locally — your footage never leaves your machine

---

## Placement in Full Pipeline

```
Research ? Script ? Voice (Kokoro) ? Music (ACE-Step)
                                           ¦
                          Rough Edit + Remotion Assets
                                           ¦
                                   ? ffmpeg-skill ?
                                  (Final polish + export)
                                           ¦
                                    Upload-Ready MP4
```

---

*Discovered: October 2026 | Status: Gold Standard for Documentary Finishing*
