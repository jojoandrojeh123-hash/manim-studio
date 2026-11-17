"""Highlighting, callout, and dimming helpers for scene focus."""

from manim import (
    AnimationGroup,
    Arrow,
    Mobject,
    Restore,
    SurroundingRectangle,
    Text,
    VGroup,
    RIGHT,
)

from studio.theme import ACCENT, TEXT, THEME


def highlight(
    mobject: Mobject,
    *,
    color: str = ACCENT,
    buff: float = 0.14,
) -> SurroundingRectangle:
    """Create a clean outline around a mobject."""
    return SurroundingRectangle(
        mobject,
        color=color,
        buff=buff,
        stroke_width=THEME.stroke_width,
    )


def callout(
    label: str,
    target: Mobject,
    *,
    direction=RIGHT,
    color: str = ACCENT,
) -> VGroup:
    """Create a text label and arrow pointing from the label to a target."""
    text = Text(
        label,
        font=THEME.font,
        font_size=THEME.label_size,
        color=TEXT,
    )
    text.next_to(target, direction, buff=0.45)
    arrow = Arrow(
        start=text.get_critical_point(-direction),
        end=target.get_boundary_point(direction),
        color=color,
        stroke_width=THEME.thin_stroke_width + 1,
        buff=0.08,
        max_tip_length_to_length_ratio=0.18,
    )
    return VGroup(arrow, text)


class FocusDimmer:
    """Animate non-focus objects dimmer, then restore their saved appearance."""

    def __init__(
        self,
        scene,
        focus: Mobject,
        *,
        opacity: float = 0.2,
    ) -> None:
        if not 0 <= opacity <= 1:
            raise ValueError("opacity must be between zero and one")
        self.scene = scene
        self.focus = focus
        self.dimmed = [
            mobject
            for mobject in scene.mobjects
            if not any(member is focus for member in mobject.get_family())
        ]
        for mobject in self.dimmed:
            mobject.save_state()
        self.opacity = opacity

    def dim(self, *, run_time: float = THEME.emphasis_runtime) -> None:
        """Fade all scene roots except the focus toward the requested opacity."""
        if not self.dimmed:
            return
        animations = AnimationGroup(
            *(mobject.animate.set_opacity(self.opacity) for mobject in self.dimmed)
        )
        self.scene.play(animations, run_time=run_time)
        self.scene.bring_to_front(self.focus)

    def restore(self, *, run_time: float = THEME.emphasis_runtime) -> None:
        """Restore the saved appearance of everything dimmed by this helper."""
        if not self.dimmed:
            return
        self.scene.play(
            *(Restore(mobject) for mobject in self.dimmed),
            run_time=run_time,
        )
