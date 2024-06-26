from typing import Any
from typing_extensions import TypeAlias


class TileMap:
    '''
    TileMap class

    tile format: {'coordinate': 'type'} e.g. {'10;20': 'grass'}
    '''

    def __init__(self, tile_size: int = 16) -> None:
        TileType: TypeAlias = dict[str, Any]
        self._tile_size: int = tile_size
        self._tilemap: dict[str, TileType] = {}
        self._offgrid_tiles: list[str] = []

        for i in range(10):
            new_tile: TileType = {
                'type': 'grass',
                'variant': 1,
                'pos': (3 + i, 10),
            }
            self._tilemap[f'{str(i + 3)};10'] = new_tile

            new_tile = {
                'type': 'stone',
                'variant': 1,
                'pos': (3 + i, 10),
            }
            self._tilemap[f'10;{str(i + 5)}'] = new_tile
