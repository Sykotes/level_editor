from tkinter import filedialog

import pygame as pg


class Tiles:
    def __init__(self, tile_size: int) -> None:
        self._loaded_tiles: dict[str, list[pg.Surface]] = {
            "generic": list[pg.Surface](),
        }
        self._tile_size: int = tile_size

    @property
    def loaded_tiles(self) -> dict[str, list[pg.Surface]]:
        """
        dict of all loaded tiles
        the keys are the tiles type e.g. 'generic'
        the values are lists of the tile surfaces
        """
        return self._loaded_tiles

    @property
    def tile_size(self) -> int:
        return self._tile_size

    @staticmethod
    def _get_images() -> list[str]:
        filetypes = [("Select Tiles", "*.jpg;*.jpeg;*.png;")]
        selected_files = filedialog.askopenfilenames(filetypes=filetypes)
        return list(selected_files)

    @staticmethod
    def _render_new_tiles_prompt(new_tile_count: int) -> list[str]:
        """
        returns a list of tile types
        this is done by having the user specify each
        """

        tile_types: list[str] = []

        # temp setting of values for testing
        for _ in range(new_tile_count):
            tile_types.append("generic")

        return tile_types

    def load_tiles(self, surface: pg.Surface) -> None:
        """
        adds all user selected tiles to the loaded_tiles dict
        """

        _ = surface

        tile_locations: list[str] = self._get_images()
        tile_types_list: list[str] = self._render_new_tiles_prompt(len(tile_locations))

        for i, tile_path in enumerate(tile_locations):
            tile_surf: pg.Surface = pg.image.load(tile_path).convert()

            self._loaded_tiles[tile_types_list[i]].append(tile_surf)
