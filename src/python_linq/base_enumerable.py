lazy from collections.abc import Iterable, Iterator


class BaseEnumerable[T]:
    def __init__(self, val: Iterable[T] = ()):
        self.value = iter(val)

    def __iter__(self) -> Iterator[T]:
        return self.value
