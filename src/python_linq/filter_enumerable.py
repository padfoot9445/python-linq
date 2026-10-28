lazy from typing import Callable

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable

type FilterPredicate[T] = Callable[[T], bool]


class FilterEnumerable[T](BaseEnumerable[T]):
    def where(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(callback, self.value))

    def filter(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return self.where(callback)
