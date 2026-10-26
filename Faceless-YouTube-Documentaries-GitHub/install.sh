#!/usr/bin/env bash
# Faceless YouTube (Documentaries): macOS / Linux installer.
#
#   ./install.sh            core pipeline
#   ./install.sh --music    + ACE-Step 1.5 (NVIDIA GPU, ~10 GB)
#   ./install.sh --thumbs   + FLUX.2 thumbnails (torch + diffusers)
#   ./install.sh --full     + every reference tool in tools/tools.txt
# Re-running is safe: finished steps are skipped.
set -u

MUSIC=0; THUMBS=0; FULL=0
for a in "$@"; do
  case "$a" in
    --music) MUSIC=1 ;;
    --thumbs) THUMBS=1 ;;
    --full) FULL=1; MUSIC=1 ;;
    *) echo "unknown flag: $a"; exit 1 ;;
  esac
done

ROOT="$(cd "$(dirname "$0")" && pwd)"
TOOLS="$ROOT/tools"
VENV="$ROOT/.venv"
PY="$VENV/bin/python"

step() { printf '\n\033[36m==> %s\033[0m\n' "$1"; }
ok()   { printf '    \033[32mOK\033[0m  %s\n' "$1"; }
warn() { printf '    \033[33m!!\033[0m  %s\n' "$1"; }

step "Checking prerequisites (git, node, python3, ffmpeg)"
missing=""
for c in git node npm python3 ffmpeg curl; do command -v "$c" >/dev/null 2>&1 || missing="$missing $c"; done
if [ -n "$missing" ]; then
  warn "Missing:$missing"
  echo "    macOS:  brew install git node python@3.12 ffmpeg"
  echo "    Ubuntu: sudo apt install git nodejs npm python3 python3-venv ffmpeg curl"
  exit 1
fi
ok "$(git --version)"; ok "node $(node --version)"; ok "$(python3 --version)"; ok "$(ffmpeg -version | head -1)"

step "Cloning tools (pinned commits from tools/tools.txt)"
groups="core"; [ $MUSIC = 1 ] && groups="$groups music"; [ $FULL = 1 ] && groups="$groups full"
grep -v '^#' "$TOOLS/tools.txt" | while IFS='|' read -r name url sha group; do
  [ -z "$name" ] && continue
  case " $groups " in *" $group "*) ;; *) continue ;; esac
  dir="$TOOLS/$name"
  if [ -d "$dir/.git" ]; then ok "$name already cloned"; continue; fi
  echo "    cloning $name..."
  git clone --quiet --filter=blob:none --no-checkout "$url" "$dir"
  git -C "$dir" checkout --quiet "$sha" 2>/dev/null || { warn "$name: pinned commit not found, using default branch"; git -C "$dir" checkout --quiet HEAD; }
  ok "$name"
done

step "Downloading Kokoro TTS models (~350 MB)"
mkdir -p "$TOOLS/kokoro-models"
base="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  out="$TOOLS/kokoro-models/$f"
  if [ -s "$out" ] && [ "$(wc -c <"$out")" -gt 1000000 ]; then ok "$f already present"; continue; fi
  curl -L --fail --progress-bar -o "$out" "$base/$f" && ok "$f" || warn "download failed: $base/$f"
done

step "Python virtual environment (.venv) + packages"
[ -x "$PY" ] || python3 -m venv "$VENV"
"$PY" -m pip install --quiet --upgrade pip
"$PY" -m pip install --quiet -r "$ROOT/requirements.txt" && ok "kokoro-onnx, numpy, soundfile, scipy, yt-dlp" || warn "pip install failed"

if [ $THUMBS = 1 ]; then
  step "FLUX.2 thumbnail stack (torch + diffusers)"
  "$PY" -m pip install --quiet torch && "$PY" -m pip install --quiet -U diffusers transformers accelerate sentencepiece \
    && ok "torch + diffusers" || warn "torch/diffusers install failed"
fi

step "Node packages + Playwright Chromium for every production"
for d in "$ROOT"/Productions/*/; do
  [ -f "$d/package.json" ] || continue
  (cd "$d" && npm install --silent && npx playwright install chromium) && ok "$(basename "$d")"
done

if [ $MUSIC = 1 ]; then
  step "ACE-Step 1.5 (own uv venv, Python 3.12)"
  "$PY" -m pip install --quiet uv
  (cd "$TOOLS/ACE-Step-1.5" && "$VENV/bin/uv" sync --python 3.12) && ok "ACE-Step 1.5 ready" || warn "uv sync failed, see tools/ACE-Step-1.5/README.md"
fi

step "Done"
cat <<'EOF'
    Activate Python before running the pipeline:
      source .venv/bin/activate
    Then follow "SOP - EPISODE PRODUCTION.md" (commands run from Productions/<series>/).
    Quick test:
      cd "Productions/S01 Kestrel Lake"
      python voice.py --part 1
      node render.js --part 1 --still 5,30
    Note: gen_music.py uses the Windows venv path in its docstring; on macOS/Linux run it with
      ../../tools/ACE-Step-1.5/.venv/bin/python gen_music.py
EOF
