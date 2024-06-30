import pygame as pg

from scripts.tile import Tile
from scripts.tiles import Tiles


class Level:
    '''
    stores and renders all tiles currently on the levels tilemap
    '''

    def __init__(self) -> None:
        self._tilemap: dict[str, Tile] = {}

        self._offgrid_tiles: list[Tile] = []
        self._tiles = Tiles(16)

        for i in range(10):
            self._tilemap[f'{3 + i};10'] = Tile('generic', 0, (3 + i, 10))
            self._tilemap[f'10;{3 + i}'] = Tile('generic', 1, (10, 3 + i))

    @property
    def tilemap(self) -> dict[str, Tile]:
        return self._tilemap

    @property
    def offgrid_tiles(self) -> list[Tile]:
        return self._offgrid_tiles

    def add_tiles(self, surface: pg.Surface) -> None:
        self._tiles.load_tiles(surface)

    def render(self, surface: pg.Surface) -> None:
        if len(self._tilemap) == 0:
            return

        for loc in self._tilemap:
            tile = self._tilemap[loc]
            surface.blit(
                self._tiles.loaded_tiles[tile.tile_type][tile.variant],
                (
                    tile.position[0] * self._tiles.tile_size,
                    tile.position[1] * self._tiles.tile_size,
                ),
            )

        for tile in self._offgrid_tiles:
            surface.blit(
                self._tiles.loaded_tiles[tile.tile_type][tile.variant],
                tile.position,
            )
