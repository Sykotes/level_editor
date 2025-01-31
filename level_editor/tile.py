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

    @property
    def dict(self) -> dict[str, Any]:
        return {
            "type": self._type,
            "variant": self._variant,
            "position": self._position,
        }
