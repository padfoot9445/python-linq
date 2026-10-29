lazy from typing import Callable
from collections.abc import Iterator

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable

type FilterPredicate[T] = Callable[[T], bool]


class FilterEnumerable[T](BaseEnumerable[T]):
    def where(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(callback, self.value))

    def filter(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return self.where(callback)

    def distinct[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def contains(
        self, value: T, comparer: Callable[[T, T], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(item, value) for item in self)
