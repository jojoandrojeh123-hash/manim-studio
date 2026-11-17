"""Project paths and render profiles shared by the CLI and studio code."""

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "assets"
MEDIA_DIR = PROJECT_ROOT / "media"


@dataclass(frozen=True)
class RenderProfile:
    """Output settings for a named render target."""

    quality_flag: str
    width: int | None = None
    height: int | None = None
    fps: int | None = None


PREVIEW_PROFILE = RenderProfile(quality_flag="-ql")
PRODUCTION_PROFILE = RenderProfile(
    quality_flag="-qh",
    width=1920,
    height=1080,
    fps=60,
)
FOUR_K_PROFILE = RenderProfile(
    quality_flag="-qh",
    width=3840,
    height=2160,
    fps=60,
)

__all__ = [
    "ASSETS_DIR",
    "FOUR_K_PROFILE",
    "MEDIA_DIR",
    "PREVIEW_PROFILE",
    "PROJECT_ROOT",
    "PRODUCTION_PROFILE",
    "RenderProfile",
]
