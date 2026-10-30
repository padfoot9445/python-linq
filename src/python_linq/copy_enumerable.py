lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable


class CopyEnumerable[T](BaseEnumerable[T]):
    def shallow_copy(self) -> "Enumerable[T]":
        return Enumerable(self.value.fork())
