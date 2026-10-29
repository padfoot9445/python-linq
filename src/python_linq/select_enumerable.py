lazy from typing import Any, Callable, Iterable

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

    def filter_map[V](self, callback: Callable[[T], V | None]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(item)
                if result is not None:
                    yield result

        return Enumerable(inner())

    def flatten[V](self: Iterable[Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for items in self:
                yield from items

        return Enumerable(inner())

    def concat(self, other: Iterable[T]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield from other

        return Enumerable(inner())

    def chain(self, other: Iterable[T]) -> "Enumerable[T]":
        return self.concat(other)

    def append(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield item

        return Enumerable(inner())

    def prepend(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield item
            yield from self

        return Enumerable(inner())

    def tee(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(lambda x: x[1])
