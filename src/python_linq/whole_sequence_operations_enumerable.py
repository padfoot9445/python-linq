import itertools
from typing import Callable, Iterable, cast

lazy from .select_enumerable import SelectEnumerable
lazy from .enumerable import Enumerable


class WholeSequenceOperationsEnumerable[T](SelectEnumerable[T]):
    def zip[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, strict=strict))

    def all(self, predicate: Callable[[T], bool]) -> bool:
        return all(self.map(predicate))

    def any(self, predicate: Callable[[T], bool]) -> bool:
        return any(self.map(predicate))

    def eq[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def neq[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(other, comparer=comparer)
