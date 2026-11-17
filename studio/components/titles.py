"""Reusable title-card and lower-third graphics."""

from manim import DOWN, DL, FadeIn, FadeOut, LEFT, Line, Text, UP, VGroup

from studio.theme import ACCENT, MUTED_TEXT, TEXT, THEME


class TitleCard(VGroup):
    """Centered title and optional subtitle with animated entrance/exit."""

    def __init__(
        self,
        title: str,
        subtitle: str | None = None,
        *,
        title_color: str = TEXT,
        subtitle_color: str = MUTED_TEXT,
    ) -> None:
        self.title = Text(
            title,
            font=THEME.font,
            font_size=THEME.title_size,
            color=title_color,
            weight="BOLD",
        )
        self.subtitle = (
            Text(
                subtitle,
                font=THEME.font,
                font_size=THEME.subtitle_size,
                color=subtitle_color,
            )
            if subtitle
            else None
        )
        if self.subtitle is not None:
            self.subtitle.next_to(self.title, DOWN, buff=0.28)
            super().__init__(self.title, self.subtitle)
            self.arrange(DOWN, buff=0.28).move_to(0)
        else:
            self.title.move_to(0)
            super().__init__(self.title)

    def animate_in(self, scene, *, run_time: float = THEME.title_runtime) -> None:
        """Fade the complete title card in on the given scene."""
        scene.play(FadeIn(self, shift=DOWN * 0.15), run_time=run_time)

    def animate_out(self, scene, *, run_time: float = THEME.transition_runtime) -> None:
        """Fade the title card away."""
        scene.play(FadeOut(self, shift=UP * 0.15), run_time=run_time)


class LowerThird(VGroup):
    """A compact speaker/section label anchored to the lower-left corner."""

    def __init__(
        self,
        label: str,
        detail: str | None = None,
        *,
        color: str = ACCENT,
    ) -> None:
        self.label = Text(
            label,
            font=THEME.font,
            font_size=THEME.label_size,
            color=TEXT,
            weight="BOLD",
        )
        self.rule = Line(LEFT, -LEFT, color=color, stroke_width=THEME.thin_stroke_width)
        self.rule.set_width(max(self.label.width, 1.5))
        self.rule.next_to(self.label, UP, buff=0.12, aligned_edge=LEFT)
        elements = [self.rule, self.label]
        self.detail = None
        if detail:
            self.detail = Text(
                detail,
                font=THEME.font,
                font_size=THEME.label_size - 4,
                color=MUTED_TEXT,
            )
            self.detail.next_to(self.label, DOWN, buff=0.08, aligned_edge=LEFT)
            elements.append(self.detail)
        super().__init__(*elements)
        self.to_corner(DL, buff=0.45)

    def animate_in(self, scene, *, run_time: float = THEME.transition_runtime) -> None:
        """Slide the lower third into view."""
        scene.play(FadeIn(self, shift=UP * 0.15), run_time=run_time)

    def animate_out(self, scene, *, run_time: float = THEME.transition_runtime) -> None:
        """Fade the lower third away."""
        scene.play(FadeOut(self, shift=DOWN * 0.1), run_time=run_time)
