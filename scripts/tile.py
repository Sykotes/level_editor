from typing import Any


class Tile:
    def __init__(
        self,
        tile_type: str,
        variant: int,
        pos: tuple[int, int],
    ) -> None:
        self._type: str = tile_type
        self._variant: int = variant
        self._position: tuple[int, int] = pos

    @property
    def tile_type(self) -> str:
        return self._type

    @property
    def variant(self) -> int:
        return self._variant

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    # def _pos_convert(self) -> str:
    #     '''
    #     converts (x, y) position to string variant 'x;y'
    #     this is done to work with JSON format
    #     '''
    #     return f'{self._position[0]};{self._position[1]}'

    @property
    def dict(self) -> dict[str, Any]:
        return {
            'type': self._type,
            'variant': self._variant,
            'position': self._position,
        }
