from typing import Any


class Stack:
    def __init__(self):
        self._size = 0
        self._elements = [-1, -1]

    def is_empty(self):
        return self._size == 0

    def push(self, item: Any):
        self._elements[self._size] = item
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise self.UnderflowException
        self._size -= 1
        return self._elements[self._size]

    class UnderflowException(Exception):
        pass
