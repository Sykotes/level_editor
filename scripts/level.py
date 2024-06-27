import pygame as pg

from scripts.tile import Tile
from scripts.tiles import loaded_tiles
from scripts.tiles import tile_size


class Level:
    '''
    stores and renders all tiles currently on the levels tilemap
    '''

    def __init__(self) -> None:
        self._tilemap: dict[str, Tile] = {}
        self._offgrid_tiles: list[Tile] = []

        for i in range(10):
            self._tilemap[f'{3 + i};10'] = Tile('grass', 1, (3 + i, 10))
            self._tilemap[f'10;{3 + i}'] = Tile('stone', 1, (10, 3 + i))

    @property
    def tilemap(self) -> dict[str, Tile]:
        return self._tilemap

    @property
    def offgrid_tiles(self) -> list[Tile]:
        return self._offgrid_tiles

    def render(self, surface: pg.Surface) -> None:
        for loc in self._tilemap:
            tile = self._tilemap[loc]
            surface.blit(
                loaded_tiles[tile.tile_type][tile.variant],
                (tile.position[0] * tile_size, tile.position[1] * tile_size),
            )
