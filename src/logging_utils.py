from __future__ import annotations

import logging
import sys
import os
from datetime import date
from pathlib import Path

LOG_DIR= Path("logs")
_FMT= "%(asctime)s | %(name)-18s | %(levelname)-7s | %(message)s"
_BAR= "=" * 64

def get_logger(name: str) -> logging.logger:
    """Return a logger with one dated file handler + one stream handler."""
    short = name.split(".")[-1]
    logger = logging.getLogger(short)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    logger.propagate= False
    LOG_DIR.mkdir(exist_ok=True)

    fmt= logging.Formatter(_FMT)
    file_handler=logging.FileHandler(LOG_DIR / f"{short}_{date.today().isoformat()}.log")
    file_handler.setFormatter(fmt)
    steam_handler= logging.StreamHandler(sys.stdout)
    steam_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(steam_handler)
    return logger

def log_section(logger: logging.Logger, title:str, emoji: str= "🔹") -> None:
    """Print a seperator-line banner with an emoji marker."""
    logger.info(_BAR)
    logger.info("%s %s", emoji, title)
    logger.info(_BAR)