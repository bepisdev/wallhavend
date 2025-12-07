"""
Wallhavend - A CLI tool for downloading wallpapers from wallhaven.cc

This package provides a command-line interface for searching and downloading
wallpapers from the Wallhaven.cc API.
"""

from .cli import run
from .api import WallhavenClient, ImageInfo
from .core import (
    WallpaperDownloader,
    load_config,
    save_config,
    get_config_path
)

__version__ = "0.3.0"

__all__ = [
    "run",
    "WallhavenClient",
    "ImageInfo",
    "WallpaperDownloader",
    "load_config",
    "save_config",
    "get_config_path"
]
