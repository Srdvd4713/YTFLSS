# tools/

This folder is filled by the installer (`install.ps1` on Windows, `install.sh` on macOS/Linux). The repos are not committed; `tools.txt` lists each one with the exact commit the pipeline was built against.

After install you'll have:
- `tools/<repo>/`: the cloned repos (core group, plus music/full if requested)
- `tools/kokoro-models/`: `kokoro-v1.0.onnx` + `voices-v1.0.bin` (~350 MB, used by `voice.py`)
