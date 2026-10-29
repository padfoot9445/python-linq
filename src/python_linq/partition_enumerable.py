from typing import Iterable, Iterator, cast

lazy from .take_enumerable import TakeEnumerable

lazy from .enumerable import Enumerable
sentinel = object()
class PartitionEnumerable[T](TakeEnumerable[T]):

    def split(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple([cast(T, sep)]) # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take
    
    def split_multiple(self, sep: Iterable[T] | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self._split(cast(Iterable[T], sep)) # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take
    
    def _split_no_separator(self) -> "Enumerable[Enumerable[T]]":
        return self.map(lambda x: Enumerable([x]))
    
    def _split(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)
        def inner():
            while True:
                segment = self.take_while_lossless(lambda _: self.peek_n(len(sep)).neq(Enumerable(sep)))
                if segment.is_empty():
                    # No more non-separator elements - check if we should yield an empty segment after separator
                    has_separator = self.peek_n(len(sep)).eq(Enumerable(sep))
                    if has_separator:
                        self.skip(len(sep))  # consume the separator
                        continue  # will yield empty segment in next iteration
                    else:
                        break  # EOF or no more separators - we're done
                yield segment

        return Enumerable(inner())

