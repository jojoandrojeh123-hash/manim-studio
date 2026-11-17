"""Sample Studio episode demonstrating titles, graph transforms, and callouts."""

from manim import (
    DOWN,
    FadeIn,
    MathTex,
    Axes,
    Create,
    Dot,
    Transform,
    UP,
    config,
)

from studio.base_scene import StudioScene
from studio.components.focus import callout, highlight
from studio.components.titles import TitleCard
from studio.theme import ACCENT, PRIMARY, SECONDARY, TEXT, THEME


class StudioEpisode01(StudioScene):
    """Translate a parabola and inspect its new vertex."""

    def construct(self) -> None:
        intro = TitleCard("A Shifted Parabola", "A short tour of transformations")
        intro.animate_in(self)
        self.wait(0.6)
        intro.animate_out(self)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 4, 1],
            x_length=8,
            y_length=4.5,
            tips=False,
            axis_config={"color": TEXT, "stroke_width": 2},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        )
        original_graph = axes.plot(
            lambda x: x**2,
            x_range=[-2, 2],
            color=PRIMARY,
            stroke_width=THEME.stroke_width,
        )
        equation = MathTex(r"f(x)=x^2", color=TEXT).scale(0.9)
        equation.to_corner(UP + LEFT, buff=0.5).shift(DOWN * 0.45)

        self.play(
            Create(axes),
            Create(original_graph),
            FadeIn(equation, shift=DOWN * 0.15),
            run_time=1.1,
        )
        self.wait(0.3)

        shifted_graph = axes.plot(
            lambda x: (x - 1) ** 2 + 1,
            x_range=[-1.0, 2.7],
            color=SECONDARY,
            stroke_width=THEME.stroke_width,
        )
        shifted_equation = MathTex(r"f(x)=(x-1)^2+1", color=TEXT).scale(0.9)
        shifted_equation.move_to(equation)
        self.play(
            Transform(original_graph, shifted_graph),
            Transform(equation, shifted_equation),
            run_time=1.2,
        )

        vertex = Dot(axes.c2p(1, 1), color=ACCENT, radius=0.09)
        self.play(FadeIn(vertex, scale=0.6), run_time=THEME.emphasis_runtime)
        self.camera_rig.frame_mobject(vertex, padding=1.8, run_time=0.9)

        vertex_callout = callout("Vertex: (1, 1)", vertex, color=ACCENT)
        marker = highlight(vertex, color=ACCENT, buff=0.18)
        self.play(Create(marker), FadeIn(vertex_callout, shift=UP * 0.12))
        self.wait(0.8)

        self.clear_stage()
        self.play(
            self.camera.frame.animate.move_to(0).scale(
                config.frame_width / self.camera.frame.width
            ),
            run_time=0.7,
        )
        outro = TitleCard("Thanks for watching", "More visual mathematics, next time")
        outro.animate_in(self)
        self.wait(0.8)
        outro.animate_out(self)
