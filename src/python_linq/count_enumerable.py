lazy from .copy_enumerable import CopyEnumerable

lazy from .enumerable import Enumerable


class CountEnumerable[T](CopyEnumerable[T]):
    def count(self) -> int:
        return sum(1 for _ in self)

    def enumerate(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(self))

    def is_empty(self) -> bool:
        sentinel = object()
        return self.shallow_copy().first(default=sentinel) is sentinel
