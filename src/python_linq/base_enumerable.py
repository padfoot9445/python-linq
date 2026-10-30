lazy import itertools
from collections.abc import Iterable, Iterator, Sized


class _Cursor[T](Iterator[T]):
    def __init__(self, iterator: Iterator[T]) -> None:
        self._iterator = iterator

    def __iter__(self) -> "_Cursor[T]":
        return self

    def __next__(self) -> T:
        return next(self._iterator)

    def non_enumerated_count(self) -> int | None:
        if isinstance(self._iterator, Sized):
            return len(self._iterator)
        return None

    def fork(self) -> Iterator[T]:
        current, copy = itertools.tee(self._iterator)
        self._iterator = current
        return copy


class BaseEnumerable[T]:
    def __init__(self, val: Iterable[T] = ()):
        self.value = _Cursor(iter(val))

    def __iter__(self) -> Iterator[T]:
        return self.value
