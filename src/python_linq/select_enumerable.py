lazy from typing import Any, Callable, Collection, Iterable

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable


class SelectEnumerable[T](BaseEnumerable[T]):
    def select[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, self))

    def map[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return self.select(callback)

    def flat_map[V](self, callback: Callable[[T], Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for result_bundle in self.map(callback):
                yield from result_bundle

        return Enumerable(inner())

    def tee(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(lambda x: x[1])
