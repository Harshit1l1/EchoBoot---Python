from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
@dataclass
class Config:
    workdir: Path = Path.home() / ".echoboot"
    iso_catalog: Path = Path.home() / ".echoboot" / "isos.yaml"
cfg = Config()
cfg.workdir.mkdir(parents=True, exist_ok=True)
