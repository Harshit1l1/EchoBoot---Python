from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json
@dataclass
class Event:
    kind: str
    detail: dict
    ts: str
    @staticmethod
    def now(kind: str, **detail) -> "Event":
        return Event(kind=kind, detail=detail, ts=datetime.now(timezone.utc).isoformat())
class Ledger:
    def __init__(self, path: Path):
        self.path = path
        self.events: list[Event] = []
    def add(self, ev: Event) -> None:
        self.events.append(ev)
    def write(self) -> None:
        data = [asdict(e) for e in self.events]
        self.path.write_text(json.dumps(data, indent=2))
    @staticmethod
    def sha256(path: Path, chunk_size: int = 1024 * 1024) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            while chunk := f.read(chunk_size):
                h.update(chunk)
        return h.hexdigest()
