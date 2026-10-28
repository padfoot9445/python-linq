from typing import Callable, Iterable

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
        other: "Enumerable[TOther]",
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.neq(other, comparer=comparer)

    def neq[TOther](
        self,
        other: "Enumerable[TOther]",
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.zip(other).any(lambda x: not comparer(*x)) or other.count() > 0
