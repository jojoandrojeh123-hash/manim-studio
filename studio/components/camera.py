"""Convenience camera moves for MovingCameraScene-based productions."""

from manim import Mobject, MovingCameraScene

from studio.theme import THEME


class CameraRig:
    """Frame, pan, and zoom the moving camera around scene content."""

    def __init__(self, scene: MovingCameraScene) -> None:
        self.scene = scene

    def pan_to(
        self,
        mobject: Mobject,
        *,
        run_time: float = THEME.transition_runtime,
    ) -> None:
        """Move the camera center to a mobject without changing its zoom."""
        self.scene.play(
            self.scene.camera.frame.animate.move_to(mobject.get_center()),
            run_time=run_time,
        )

    def zoom_to(
        self,
        mobject: Mobject,
        *,
        factor: float = 1.5,
        run_time: float = THEME.transition_runtime,
    ) -> None:
        """Center on a mobject and zoom in by a positive scale factor."""
        if factor <= 0:
            raise ValueError("factor must be greater than zero")
        self.scene.play(
            self.scene.camera.frame.animate.move_to(mobject.get_center()).scale(
                1 / factor
            ),
            run_time=run_time,
        )

    def frame_mobject(
        self,
        mobject: Mobject,
        *,
        padding: float = 0.5,
        run_time: float = THEME.transition_runtime,
    ) -> None:
        """Fit a mobject in frame while preserving the camera's aspect ratio."""
        if padding < 0:
            raise ValueError("padding cannot be negative")
        frame = self.scene.camera.frame
        aspect_ratio = frame.width / frame.height
        desired_width = max(
            mobject.width + 2 * padding,
            (mobject.height + 2 * padding) * aspect_ratio,
            0.1,
        )
        self.scene.play(
            frame.animate.move_to(mobject.get_center()).scale(
                desired_width / frame.width
            ),
            run_time=run_time,
        )
