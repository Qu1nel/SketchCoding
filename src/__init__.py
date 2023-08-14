"""Cardioid - visualization of an interesting version of this curve in animation."""
import sys
from pathlib import Path

import pygame as pg  # type: ignore

from src.main import App


def resource_path(relative_path: Path) -> Path:
    """Function for working paths inside an exe for python."""
    base_path = Path(getattr(sys, "_MEIPASS", ".")).absolute()
    return base_path.joinpath(relative_path)


pg.init()

icon_name = "icon.png"
icon_folder_name = "icons"
icon_path = Path(icon_folder_name) / Path(icon_name)

icon = pg.image.load(resource_path(icon_path))

pg.display.set_icon(icon)
pg.display.set_caption("Cardioid")


def main() -> None:
    """Entry point to the game."""
    game = App()
    game.run()
