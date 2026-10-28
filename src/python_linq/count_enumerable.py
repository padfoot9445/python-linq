lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable

class CountEnumerable[T](BaseEnumerable[T]):
    def count(self) -> int:
        return sum(1 for _ in self)
    def enumerate(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(self))
