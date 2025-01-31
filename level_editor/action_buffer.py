from level_editor.action import Action


class ActionBuffer:
    """
    A circular buffer for storing editor actions like tile places
    If the buffer is full, a new insert will replace oldest value
    Actions are poped in using a Last In First Out system like a stack
    """

    def __init__(self, size: int = 10) -> None:
        self._size: int = size
        self._buffer: list[Action | None] = [None] * self._size
        self._head: int = 0

    def insert(self, action: Action) -> None:
        self._buffer[self._head] = action
        self._head = (self._head + 1) % self._size

    def pop(self) -> Action | None:
        self._head = (self._head - 1) % self._size
        action: Action | None = self._buffer[self._head]
        self._buffer[self._head] = None
        return action
