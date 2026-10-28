lazy from typing import Callable

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable


class SelectEnumerable[T](BaseEnumerable[T]):
    def select[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, self))

    def map[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return self.select(callback)
