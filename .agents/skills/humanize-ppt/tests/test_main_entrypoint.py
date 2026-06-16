import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_stable_main_entrypoint_exposes_help():
    entrypoint = ROOT / "scripts" / "humanize_ppt.py"

    result = subprocess.run(
        [sys.executable, str(entrypoint), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert "--source" in result.stdout
    assert "--out" in result.stdout
    assert "--presenter-adapter" in result.stdout
