"""Console entry point for wallhavend.

This module serves as the main entry point for the wallhavend CLI application.
The actual implementation has been refactored into the cli module.
"""

from .cli import run

# For backwards compatibility
__all__ = ["run"]
