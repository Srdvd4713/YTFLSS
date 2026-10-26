<#
  Faceless YouTube (Documentaries): Windows installer.

  Usage (from the repo root, in PowerShell):
    powershell -ExecutionPolicy Bypass -File .\install.ps1              # core pipeline
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Music       # + ACE-Step 1.5 (NVIDIA GPU, ~10 GB)
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Thumbs      # + FLUX.2 thumbnails (torch + diffusers, NVIDIA GPU)
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Full        # + every reference tool in tools\tools.txt
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Prereqs     # install missing git/node/python/ffmpeg with winget first
    powershell -ExecutionPolicy Bypass -File .\install.ps1 -Rea         # register the REA MCP server in Claude Code for this folder
  Flags can be combined. Re-running is safe: finished steps are skipped.
#>
param(
  [switch]$Music,
  [switch]$Thumbs,
  [switch]$Full,
  [switch]$Prereqs,
  [switch]$Rea
)

$ErrorActionPreference = 'Continue'
$Root  = Split-Path -Parent $MyInvocation.MyCommand.Path
$Tools = Join-Path $Root 'tools'
$Venv  = Join-Path $Root '.venv'
$VenvPy = Join-Path $Venv 'Scripts\python.exe'

function Step($msg) { Write-Host "`n==> $msg" -ForegroundColor Cyan }
function Ok($msg)   { Write-Host "    OK  $msg" -ForegroundColor Green }
function Warn($msg) { Write-Host "    !!  $msg" -ForegroundColor Yellow }
function Has($cmd)  { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Refresh-Path {
  $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
}

# ---------------------------------------------------------------- prerequisites
Step 'Checking prerequisites (git, node, python, ffmpeg)'
$winget = @{ git = 'Git.Git'; node = 'OpenJS.NodeJS.LTS'; python = 'Python.Python.3.12'; ffmpeg = 'Gyan.FFmpeg' }
$missing = @()
foreach ($c in 'git', 'node', 'python', 'ffmpeg') { if (-not (Has $c)) { $missing += $c } }

if ($missing.Count -gt 0 -and $Prereqs) {
  if (-not (Has 'winget')) { Warn 'winget not found. Install the missing tools manually (see README).'; exit 1 }
  foreach ($c in $missing) {
    Write-Host "    installing $c ($($winget[$c]))..."
    winget install --id $winget[$c] -e --accept-source-agreements --accept-package-agreements
  }
  Refresh-Path
  $missing = @()
  foreach ($c in 'git', 'node', 'python', 'ffmpeg') { if (-not (Has $c)) { $missing += $c } }
}
if ($missing.Count -gt 0) {
  Warn ("Missing: " + ($missing -join ', '))
  Write-Host '    Re-run with -Prereqs to install them with winget, or install manually:'
  foreach ($c in $missing) { Write-Host "      winget install --id $($winget[$c]) -e" }
  Write-Host '    Then open a NEW terminal and run this script again.'
  exit 1
}
Ok ("git " + (git --version)); Ok ("node " + (node --version)); Ok (python --version 2>&1); Ok ((ffmpeg -version | Select-Object -First 1))

# ---------------------------------------------------------------- tools
Step 'Cloning tools (pinned commits from tools\tools.txt)'
$groups = @('core')
if ($Music) { $groups += 'music' }
if ($Full)  { $groups += 'music', 'full' }
Get-Content (Join-Path $Tools 'tools.txt') | Where-Object { $_ -and -not $_.StartsWith('#') } | ForEach-Object {
  $name, $url, $sha, $group = $_.Split('|')
  if ($groups -notcontains $group) { return }
  $dir = Join-Path $Tools $name
  if (Test-Path (Join-Path $dir '.git')) { Ok "$name already cloned"; return }
  Write-Host "    cloning $name..."
  git clone --quiet --filter=blob:none --no-checkout $url $dir
  git -C $dir checkout --quiet $sha
  if ($LASTEXITCODE -ne 0) { Warn "${name}: pinned commit $sha not found, staying on the default branch"; git -C $dir checkout --quiet HEAD }
  Ok $name
}

# ---------------------------------------------------------------- kokoro models
Step 'Downloading Kokoro TTS models (~350 MB)'
$models = Join-Path $Tools 'kokoro-models'
New-Item -ItemType Directory -Force $models | Out-Null
$base = 'https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0'
foreach ($f in 'kokoro-v1.0.onnx', 'voices-v1.0.bin') {
  $out = Join-Path $models $f
  if ((Test-Path $out) -and (Get-Item $out).Length -gt 1MB) { Ok "$f already present"; continue }
  Write-Host "    downloading $f..."
  curl.exe -L --fail --progress-bar -o $out "$base/$f"
  if ($LASTEXITCODE -ne 0) { Warn "Download failed: $base/$f" } else { Ok $f }
}

# ---------------------------------------------------------------- python
Step 'Python virtual environment (.venv) + packages'
if (-not (Test-Path $VenvPy)) { python -m venv $Venv }
& $VenvPy -m pip install --quiet --upgrade pip
& $VenvPy -m pip install --quiet -r (Join-Path $Root 'requirements.txt')
if ($LASTEXITCODE -eq 0) { Ok 'kokoro-onnx, numpy, soundfile, scipy, yt-dlp' } else { Warn 'pip install failed (see errors above)' }

if ($Thumbs) {
  Step 'FLUX.2 thumbnail stack (torch CUDA + diffusers)'
  & $VenvPy -m pip install --quiet torch --index-url https://download.pytorch.org/whl/cu128
  & $VenvPy -m pip install --quiet -U diffusers transformers accelerate sentencepiece
  if ($LASTEXITCODE -eq 0) { Ok 'torch + diffusers (FLUX.2 Klein weights download on first run of gen_thumbs.py)' } else { Warn 'torch/diffusers install failed' }
}

# ---------------------------------------------------------------- node + playwright
Step 'Node packages + Playwright Chromium for every production'
Get-ChildItem (Join-Path $Root 'Productions') -Directory | ForEach-Object {
  if (Test-Path (Join-Path $_.FullName 'package.json')) {
    Push-Location $_.FullName
    npm install --silent
    npx playwright install chromium
    Pop-Location
    Ok $_.Name
  }
}

# ---------------------------------------------------------------- ACE-Step 1.5
if ($Music -or $Full) {
  Step 'ACE-Step 1.5 (own uv venv, Python 3.12)'
  $ace = Join-Path $Tools 'ACE-Step-1.5'
  & $VenvPy -m pip install --quiet uv
  Push-Location $ace
  & (Join-Path $Venv 'Scripts\uv.exe') sync --python 3.12
  Pop-Location
  if ($LASTEXITCODE -eq 0) { Ok 'ACE-Step 1.5 ready (checkpoints download on first run of gen_music.py, ~10 GB)' } else { Warn 'uv sync failed, see tools\ACE-Step-1.5\README.md' }
}

# ---------------------------------------------------------------- REA MCP
if ($Rea) {
  Step 'Registering REA MCP server in Claude Code (local scope, this folder only)'
  if (Has 'claude') {
    Push-Location $Root
    npx -y rea-agents@6.8.0 --version | Out-Null
    claude mcp add --scope local rea -- cmd.exe /d /c npx -y rea-agents@6.8.0 mcp
    Pop-Location
  } else { Warn 'Claude Code CLI not found; skipped.' }
}

# ---------------------------------------------------------------- done
Step 'Done'
Write-Host @"
    Activate Python before running the pipeline:
      .\.venv\Scripts\Activate.ps1
    Then follow SOP - EPISODE PRODUCTION.md (commands run from Productions\<series>\).
    Quick test:
      cd "Productions\S01 Kestrel Lake"
      python voice.py --part 1
      node render.js --part 1 --still 5,30
"@
