lazy from .copy_enumerable import CopyEnumerable

lazy from .enumerable import Enumerable
lazy from ._sentinels import MISSING


class CountEnumerable[T](CopyEnumerable[T]):
    def count(self) -> int:
        return sum(1 for _ in self)

    def enumerate(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(self))

    def is_empty(self) -> bool:
        return next(iter(self.shallow_copy()), MISSING) is MISSING
