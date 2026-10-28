lazy from .base_enumerable import BaseEnumerable


class CountEnumerable[T](BaseEnumerable[T]):
    def count(self) -> int:
        return sum(1 for _ in self)
