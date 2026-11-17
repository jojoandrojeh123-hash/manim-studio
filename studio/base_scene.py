"""Base scene that applies Studio defaults and common stage transitions."""

from manim import (
    DOWN,
    Line,
    MovingCameraScene,
    RIGHT,
    Text,
    UP,
    VGroup,
    config,
    FadeOut,
)

from studio.components.camera import CameraRig
from studio.components.titles import LowerThird
from studio.theme import BACKGROUND, GRID, MUTED_TEXT, THEME


class StudioScene(MovingCameraScene):
    """Moving-camera scene with a consistent background and camera utilities."""

    show_grid = True
    show_watermark = True
    grid_spacing = 0.5

    def setup(self) -> None:
        """Set the scene background and add the persistent studio backdrop."""
        super().setup()
        self.camera.background_color = BACKGROUND
        self.camera_rig = CameraRig(self)
        self._studio_background = self._make_background()
        self.add(self._studio_background)

    def _make_background(self) -> VGroup:
        backdrop = VGroup()
        if self.show_grid:
            half_width = config.frame_width / 2
            half_height = config.frame_height / 2
            vertical_count = int(half_width / self.grid_spacing)
            horizontal_count = int(half_height / self.grid_spacing)
            grid_lines = VGroup()
            for index in range(-vertical_count, vertical_count + 1):
                x = index * self.grid_spacing
                grid_lines.add(
                    Line(
                        [x, -half_height, 0],
                        [x, half_height, 0],
                        color=GRID,
                        stroke_width=0.6,
                        stroke_opacity=0.14,
                    )
                )
            for index in range(-horizontal_count, horizontal_count + 1):
                y = index * self.grid_spacing
                grid_lines.add(
                    Line(
                        [-half_width, y, 0],
                        [half_width, y, 0],
                        color=GRID,
                        stroke_width=0.6,
                        stroke_opacity=0.14,
                    )
                )
            backdrop.add(grid_lines)
        if self.show_watermark:
            watermark = Text(
                "MANIM STUDIO",
                font=THEME.font,
                font_size=14,
                color=MUTED_TEXT,
            )
            watermark.set_opacity(0.42)
            watermark.to_corner(UP + RIGHT, buff=0.28)
            backdrop.add(watermark)
        backdrop.set_z_index(-100)
        return backdrop

    def clear_stage(self, *, run_time: float = THEME.transition_runtime) -> None:
        """Fade every non-background mobject out, preserving the studio backdrop."""
        stage_objects = [
            mobject
            for mobject in self.mobjects
            if mobject is not self._studio_background
        ]
        if stage_objects:
            self.play(
                *(FadeOut(mobject, shift=DOWN * 0.08) for mobject in stage_objects),
                run_time=run_time,
            )

    def add_lower_third(self, label: str, detail: str | None = None) -> LowerThird:
        """Add and animate a reusable lower third."""
        lower_third = LowerThird(label, detail)
        lower_third.animate_in(self)
        return lower_third
