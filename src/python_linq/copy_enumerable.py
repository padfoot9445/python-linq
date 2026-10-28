import itertools

lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable


class CopyEnumerable[T](BaseEnumerable[T]):
    def shallow_copy(self) -> "Enumerable[T]":
        i1, i2 = itertools.tee(self.value)
        self.value = i1
        return Enumerable(i2)
