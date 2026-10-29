from collections.abc import Iterable, Iterator
from typing import cast

lazy from .take_enumerable import TakeEnumerable

lazy from .enumerable import Enumerable

sentinel = object()


class PartitionEnumerable[T](TakeEnumerable[T]):

    def split(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(T, sep)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def split_multiple(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        sep = list(cast(Iterable[T], sep))

        if len(sep) == 0:
            return self._split_no_separator()
        else:
            return self._split(
                cast(Iterable[T], sep)
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def _split_no_separator(self) -> "Enumerable[Enumerable[T]]":
        return self.map(lambda x: Enumerable([x]))

    def _split(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())
