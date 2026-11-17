#!/usr/bin/env python3
"""Render a project scene using the preview, production, or 4K profile."""

import argparse
import subprocess
import sys
from pathlib import Path

from studio.config import (
    FOUR_K_PROFILE,
    MEDIA_DIR,
    PREVIEW_PROFILE,
    PROJECT_ROOT,
    PRODUCTION_PROFILE,
    RenderProfile,
)


def build_command(
    scene_file: Path,
    scene_name: str,
    profile: RenderProfile,
    *,
    disable_caching: bool = False,
) -> list[str]:
    """Build the equivalent Manim CLI invocation for the selected profile."""
    command = [
        sys.executable,
        "-m",
        "manim",
        profile.quality_flag,
        "--media_dir",
        str(MEDIA_DIR),
    ]
    if profile.width is not None and profile.height is not None:
        command.extend(
            ["--resolution", f"{profile.width},{profile.height}"]
        )
    if profile.fps is not None:
        command.extend(["--fps", str(profile.fps)])
    if disable_caching:
        command.append("--disable_caching")
    command.extend([str(scene_file), scene_name])
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene", type=Path, help="Path to the Python scene file")
    parser.add_argument("scene_name", help="Name of the Scene subclass to render")
    parser.add_argument(
        "--mode",
        choices=("preview", "production"),
        default="preview",
        help="Preview uses -ql; production uses -qh at 1080p/60fps",
    )
    parser.add_argument(
        "--4k",
        dest="four_k",
        action="store_true",
        help="Render production quality at 3840x2160 instead of 1920x1080",
    )
    parser.add_argument(
        "--disable-caching",
        action="store_true",
        help="Force recomputation instead of using Manim's partial-movie cache",
    )
    args = parser.parse_args()
    if args.four_k and args.mode != "production":
        parser.error("--4k can only be used with --mode production")
    return args


def main() -> int:
    args = parse_args()
    scene_file = args.scene.resolve()
    if not scene_file.is_file():
        raise FileNotFoundError(f"Scene file does not exist: {scene_file}")

    if args.mode == "preview":
        profile = PREVIEW_PROFILE
    elif args.four_k:
        profile = FOUR_K_PROFILE
    else:
        profile = PRODUCTION_PROFILE

    command = build_command(
        scene_file,
        args.scene_name,
        profile,
        disable_caching=args.disable_caching,
    )
    return subprocess.run(command, cwd=PROJECT_ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
