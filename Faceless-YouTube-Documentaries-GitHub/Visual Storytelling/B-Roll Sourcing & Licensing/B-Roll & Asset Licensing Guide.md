# B-Roll & Asset Licensing Guide
*Our "B-roll" is generated, not filmed: SVG scenes from the render engine, FLUX.2 art, ACE-Step music, Kokoro voices, synthesized SFX. This file tracks the licence of every tool and asset source so the channel stays monetizable.*

## Licence register (verify against each tool's LICENSE file before commercial use)
| Asset type | Source | Where | Licence to check | Commercial use notes |
|---|---|---|---|---|
| Scenes / characters | Own code (SVG engine) | `Productions/*/render/` | Ours | ✅ owned |
| Thumbnail art | FLUX.2 Klein 4B | `tools/flux` + HF weights | Model licence on its Hugging Face page | Check the exact variant's licence; some FLUX variants are non-commercial |
| Music | ACE-Step 1.5 | `tools/ACE-Step-1.5` | Repo LICENSE | Check output rights in README; keep the generation prompt/seed log |
| Voice | Kokoro-82M | `tools/kokoro`, `tools/kokoro-models` | Apache-2.0 (verify) | Synthetic voice; label "AI-generated narration" if required by YouTube's altered/synthetic content rules |
| SFX | Synthesized in `voice.py` | Production folder | Ours | ✅ owned |
| Fonts | Oswald, Caveat (Google Fonts) | — | SIL Open Font License | ✅ free for commercial use |
| 3D / props | MCP for Blender assets (Poly Haven, Sketchfab, Poly Pizza) | — | Per asset: Poly Haven CC0; Sketchfab per model | Log each asset |

## If you ever need external assets
- **CC0 / public domain** first (Poly Haven, Freesound CC0 filter, public-domain US gov).
- CC BY is fine with a credit line in the description.
- Avoid CC BY-NC (non-commercial) and CC BY-ND (no derivatives). A monetized channel is commercial.
- Paid libraries: keep the receipt/licence PDF in `Monetization/` records.

## YouTube rules to respect
- **Reused content policy:** monetization requires meaningful original content. Our engine-made animation + original script satisfies this; don't upload compilations of other creators' material.
- **Altered or synthetic content disclosure:** tick the Studio disclosure when realistic synthetic media could mislead. A cartoon with an AI voice is generally not realistic, but re-check the current policy when uploading.
- **Content ID:** generated music can occasionally match. If a claim appears, dispute with the generation log (prompt, seed, date).

## Generation log (keep per series)
`Productions/S0X/assets/LOG.md` with: tool, model/version, prompt, seed, date, output file. This is the proof of origin for disputes.
