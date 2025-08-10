from __future__ import annotations
import logging
from rich.logging import RichHandler
_DEF_FMT = "%(message)s"
def setup(level: int = logging.INFO) -> None:
    logging.basicConfig(level=level, format=_DEF_FMT, datefmt="%H:%M:%S", handlers=[RichHandler(rich_tracebacks=True, markup=True)])
