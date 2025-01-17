import pygame as pg

from scripts.action_buffer import ActionBuffer
from scripts.tile import Tile
from scripts.tiles import Tiles


class Level:
    """
    stores and renders all tiles currently on the levels tilemap
    """

    def __init__(self, tilesize: int = 16) -> None:
        self.tilesize: int = tilesize
        self._tilemap: dict[str, Tile] = {}

        self._offgrid_tiles: list[Tile] = []
        self._tiles = Tiles(self.tilesize)

        self._action_buffer = ActionBuffer

        for i in range(10):
            self._tilemap[f"{3 + i};10"] = Tile("generic", 0, (3 + i, 10))
            self._tilemap[f"10;{3 + i}"] = Tile("generic", 1, (10, 3 + i))

    @property
    def tilemap(self) -> dict[str, Tile]:
        return self._tilemap

    @property
    def offgrid_tiles(self) -> list[Tile]:
        return self._offgrid_tiles

    def import_tiles(self, surface: pg.Surface) -> None:
        self._tiles.load_tiles(surface)

    def add_tile(self) -> None: ...

    def add_offgrid_tile(self) -> None: ...

    def replace_tile(self) -> None: ...

    def remove_tile(self) -> None: ...

    def remove_offgrid_tile(self) -> None: ...

    def render(
        self,
        surface: pg.Surface,
        offset: pg.Vector2 = pg.Vector2(0.0, 0.0),
    ) -> None:
        if len(self._tilemap) == 0:
            return

        for tile in self._offgrid_tiles:
            _ = surface.blit(
                self._tiles.loaded_tiles[tile.tile_type][tile.variant],
                (
                    tile.position[0] - offset.x,
                    tile.position[1] - offset.y,
                ),
            )

        for loc in self._tilemap:
            tile = self._tilemap[loc]
            _ = surface.blit(
                self._tiles.loaded_tiles[tile.tile_type][tile.variant],
                (
                    tile.position[0] * self._tiles.tile_size - offset.x,
                    tile.position[1] * self._tiles.tile_size - offset.y,
                ),
            )
