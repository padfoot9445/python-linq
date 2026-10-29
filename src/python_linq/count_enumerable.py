from collections.abc import Callable

lazy from .copy_enumerable import CopyEnumerable

lazy from .enumerable import Enumerable
lazy from ._sentinels import MISSING


class CountEnumerable[T](CopyEnumerable[T]):
    def count(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(1 for _ in self)
        return sum(1 for item in self if predicate(item))

    def enumerate(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(self))

    def is_empty(self) -> bool:
        return next(iter(self.shallow_copy()), MISSING) is MISSING
