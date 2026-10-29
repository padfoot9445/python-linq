lazy from typing import Any, Callable, Iterable, overload

lazy from .enumerable import Enumerable
lazy from ._sentinels import DROP, FilterMapDrop

lazy from .base_enumerable import BaseEnumerable


class SelectEnumerable[T](BaseEnumerable[T]):
    def select[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, self))

    def map[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return self.select(callback)

    def select_indexed[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(item, index)

        return Enumerable(inner())

    @overload
    def select_many[V](
        self, collection_selector: Callable[[T], Iterable[V]]
    ) -> "Enumerable[V]": ...

    @overload
    def select_many[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U],
    ) -> "Enumerable[U]": ...

    def select_many[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def flat_map[V](self, callback: Callable[[T], Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for result_bundle in self.map(callback):
                yield from result_bundle

        return Enumerable(inner())

    def filter_map[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(item)
                if result is not DROP:
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
