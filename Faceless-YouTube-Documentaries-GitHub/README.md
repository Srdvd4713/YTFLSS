# Faceless YouTube (Documentaries) — sistema de producción

Sistema completo para crear un canal de YouTube *faceless* de **series animadas de supervivencia con giro de ciencia real**: investigación, guion, voz con TTS local, música generada, animación dibujada en código (SVG + Playwright), miniaturas, Shorts y monetización. Todo funciona en local y con herramientas gratuitas.

## Qué hay dentro
| Carpeta / archivo | Para qué sirve |
|---|---|
| `CHANNEL BIBLE.md` | Identidad del canal: nicho, audiencia, voz, colores, calendario |
| `SOP - EPISODE PRODUCTION.md` | Paso a paso para producir un episodio (comandos incluidos) |
| `EPISODE TRACKER.md` | Estado de cada episodio |
| `PROMPT LIBRARY.md` | Prompts que ya funcionaron, por fase |
| `CLAUDE MASTER BOOTSTRAP PROMPT.md` | Prompt para que Claude Code arranque y estudie todo el sistema |
| `Script Frameworks/` | Hooks, retención, tensión, frameworks de serie y **prompts maestros** (Ashford + 4 adaptaciones 16:9) |
| `Research System/` | Investigación, prompts de research y fact-checking |
| `Niche & Topic Selection/` | Análisis de competencia, psicología de audiencia, backlog de series |
| `Thumbnails & Titles/` | Fórmulas de títulos, miniaturas y A/B testing |
| `Visual Storytelling/`, `Voiceover & Narration/`, `Editing & Packaging/` | Guías de cada parte de la producción |
| `Growth Engine/`, `Monetization/`, `Automation & Systems/` | Crecimiento, monetización, escalado y outsourcing |
| `Productions/S01 Kestrel Lake/` | El motor real: `voice.py`, `render.js`, `render/index.html`, `make_shorts.py`, `gen_music.py`, `gen_thumbs.py`, `thumbs.js` |
| `tools/tools.txt` | Herramientas externas (repos de GitHub) con el commit exacto usado |

## Requisitos
- **Windows 10/11** (probado), macOS o Linux
- Git, Node.js 20+ (probado con 24), Python 3.11+ y ffmpeg. En Windows el instalador los instala con `-Prereqs`
- ~2 GB de disco para el núcleo; +10 GB para la música (ACE-Step) y +10 GB para las miniaturas (FLUX)
- GPU NVIDIA (8 GB o más) solo para música y miniaturas. La voz y la animación funcionan sin GPU

## Instalación
```powershell
git clone <URL-DE-ESTE-REPO>
cd <carpeta>
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Prereqs          # núcleo (+ instala git/node/python/ffmpeg si faltan)
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Music -Thumbs    # opcional: música + miniaturas (GPU)
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Full             # opcional: todas las herramientas de referencia
```
macOS / Linux:
```bash
chmod +x install.sh && ./install.sh            # añade --music --thumbs --full según necesites
```

El instalador:
1. Comprueba (y opcionalmente instala) git, node, python y ffmpeg
2. Clona las herramientas de `tools/tools.txt` en los commits fijados
3. Descarga los modelos de voz Kokoro (`tools/kokoro-models/`)
4. Crea `.venv` con los paquetes de Python (`requirements.txt`)
5. Instala Playwright + Chromium en cada producción
6. Opcional: ACE-Step 1.5 (música), torch + diffusers (FLUX.2), registro del MCP de REA en Claude Code (`-Rea`)

## Primer uso
```powershell
.\.venv\Scripts\Activate.ps1
cd "Productions\S01 Kestrel Lake"
python voice.py --part 1                   # voz + mezcla a -14 LUFS
node render.js --part 1 --still 5,30,60    # fotogramas de prueba en build\part1\stills
node render.js --part 1 --workers 6        # render completo -> output\part1.mp4
```
Con Claude Code: abre la carpeta y pega el contenido de `CLAUDE MASTER BOOTSTRAP PROMPT.md`, o usa `Automation & Systems/Prompt Libraries/Agent Task Prompts.md`.

## Qué NO está en el repo (se regenera)
Repos clonados en `tools/`, modelos, `.venv`, `node_modules`, renders (`build/`, `*.mp4`) y la música generada (`assets/music/*.wav`, se regenera con `gen_music.py`).

## Créditos y licencias
- El formato de serie deriva de *The Wall at Ashford*, un prompt maestro de @OnlySainted (CC BY 4.0).
- Cada herramienta de `tools/` mantiene su propia licencia. Antes de monetizar, revisa la de los pesos del modelo FLUX y la de ACE-Step (ver `Visual Storytelling/B-Roll Sourcing & Licensing/`).
- Fuentes Oswald y Caveat: SIL Open Font License.
