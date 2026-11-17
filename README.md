# Manim Studio

A modular Manim Community Edition (ManimCE) starter for polished, repeatable
animation production.

## Project layout

```text
.
├── assets/
│   ├── audio/
│   ├── images/
│   └── svg/
├── media/                 # Rendered videos, images, TeX, and cache
├── scenes/
│   └── episode_01.py
├── studio/
│   ├── components/
│   │   ├── camera.py
│   │   ├── focus.py
│   │   └── titles.py
│   ├── base_scene.py
│   ├── config.py
│   └── theme.py
├── manim.cfg
└── render.py
```

## Setup

Use Python 3.10+ and install ManimCE and its system dependencies as described in
the [Manim installation guide](https://docs.manim.community/en/stable/installation.html):

```bash
python -m pip install -r requirements.txt
```

## Render

From the project root, render a fast preview or a production 1080p/60fps video:

```bash
python render.py scenes/episode_01.py StudioEpisode01 --mode preview
python render.py scenes/episode_01.py StudioEpisode01 --mode production
```

The preview uses Manim's `-ql`; production uses `-qh` with an explicit 1920x1080
resolution and 60 fps. For 4K, add `--4k` to the production command. Add
`--disable-caching` when you need to force a fresh render.

Manim can also be invoked directly, for example:

```bash
manim -qh --resolution 1920,1080 --fps 60 scenes/episode_01.py StudioEpisode01
```
