# Kokoro TTS
**GitHub:** https://github.com/hexgrad/kokoro
**Stage:** AI Voiceover / Narration Generation
**Model Type:** Open-weight, runs locally

## What It Does
Converts written scripts into natural-sounding voiceovers with multiple voice styles.

## Why Kokoro for Documentaries
- Free, unlimited generations (local)
- Multiple voices: authoritative male, warm female, neutral narrator
- Fast generation — full 10-min script in minutes

## Setup
`ash
git clone https://github.com/hexgrad/kokoro
pip install -r requirements.txt
python generate.py --text "Your script here" --voice en_us_male_1
`

## Voice Selection Guide
| Documentary Tone | Recommended Voice Style |
|-----------------|------------------------|
| Crime / Mystery | Deep, authoritative male |
| History / Culture | Warm, measured neutral |
| Science / Nature | Clear, curious tone |
| Conspiracy / Thriller | Slightly tense, dramatic |

## Workflow
1. Paste final script into Kokoro
2. Generate 2–3 voice variants
3. Select best match for your doc's tone
4. Export WAV/MP3 ? import to editing software

## Notes
- Compare quality to ElevenLabs periodically
- Store your best voice configs in this folder
