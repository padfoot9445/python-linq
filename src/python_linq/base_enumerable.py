lazy from typing import Iterable


class BaseEnumerable[T]:
    def __init__(self, val: Iterable[T]):
        self.value = iter(val)

    def __iter__(self):
        return self.value
