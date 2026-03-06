from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LoggingSettings:
    level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "logs/test.log")
    format: str = os.getenv(
        "LOG_FORMAT",
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    date_format: str = os.getenv("LOG_DATE_FORMAT", "%Y-%m-%d %H:%M:%S")


def setup_logging(settings: LoggingSettings | None = None) -> None:
    resolved = settings or LoggingSettings()

    handlers: list[logging.Handler] = [logging.StreamHandler()]

    if resolved.log_file:
        log_path = Path(resolved.log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_path, encoding="utf-8"))

    logging.basicConfig(
        level=resolved.level,
        format=resolved.format,
        datefmt=resolved.date_format,
        handlers=handlers,
        force=True,
    )
