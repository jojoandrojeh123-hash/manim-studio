"""Shared visual design tokens for Studio scenes and components."""

from dataclasses import dataclass

@dataclass(frozen=True)
class StudioTheme:
    """Colors, typography, and timing defaults used across the project."""

    background: str = "#0B1020"
    primary: str = "#72A7FF"
    secondary: str = "#A78BFA"
    accent: str = "#FFC857"
    text: str = "#F4F6FC"
    muted_text: str = "#AAB3C5"
    grid: str = "#7F8AA3"
    font: str = "DejaVu Sans"
    title_size: int = 48
    subtitle_size: int = 28
    body_size: int = 30
    label_size: int = 22
    stroke_width: float = 3.0
    thin_stroke_width: float = 1.5
    title_runtime: float = 0.8
    transition_runtime: float = 0.45
    emphasis_runtime: float = 0.5


THEME = StudioTheme()

# Conventional aliases make the palette easy to use from scene code.
BACKGROUND = THEME.background
PRIMARY = THEME.primary
SECONDARY = THEME.secondary
ACCENT = THEME.accent
TEXT = THEME.text
MUTED_TEXT = THEME.muted_text
GRID = THEME.grid

__all__ = [
    "ACCENT",
    "BACKGROUND",
    "GRID",
    "MUTED_TEXT",
    "PRIMARY",
    "SECONDARY",
    "TEXT",
    "THEME",
    "StudioTheme",
]
