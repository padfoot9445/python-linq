import itertools
from typing import Callable, Iterable, cast, overload

lazy from .select_enumerable import SelectEnumerable
lazy from .enumerable import Enumerable


class WholeSequenceOperationsEnumerable[T](SelectEnumerable[T]):
    def zip[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, strict=strict))

    def all(self, predicate: Callable[[T], bool]) -> bool:
        return all(self.map(predicate))

    @overload
    def any(self) -> bool: ...

    @overload
    def any(self, predicate: Callable[[T], bool]) -> bool: ...

    def any(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return True
        return any(predicate(item) for item in self)

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

    def sequence_equal[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(other, comparer=comparer)
