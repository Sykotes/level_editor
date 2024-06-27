import pygame as pg
from tkinter import filedialog

loaded_tiles: dict[str, list[pg.Surface]] = {}
tile_size: int = 16


def _get_images() -> list[str]:
    filetypes = [("Select Tiles", "*.jpg;*.jpeg;*.png;")]
    selected_files = filedialog.askopenfilenames(filetypes=filetypes)
    return list(selected_files)


def _render_new_tiles_prompt() -> list[str]:
    '''
    returns a list of tile types
    this is done by having the user specify each
    '''

    tile_types: list[str] = []
    return tile_types


def load_tiles(surface: pg.Surface) -> None:
    '''
    adds all user selected tiles to the loaded_tiles dict
    '''
    tile_locations: list[str] = _get_images()
    tile_types_list: list[str] = _render_new_tiles_prompt()
    for i, tile_path in enumerate(tile_locations):
        tile_surf: pg.Surface = pg.image.load(tile_path).convert()

        loaded_tiles[tile_types_list[i]].append(tile_surf)


def export(): ...
