lazy from enum import StrEnum
import itertools
import builtins
lazy from typing import Any, Callable, cast
from collections.abc import Hashable, Iterable, Iterator
from statistics import fmean
from typing import overload

from rustshed import Null, Option, Some

lazy from .collect_enumerable import CollectEnumerable


lazy from .whole_sequence_operations_enumerable import WholeSequenceOperationsEnumerable

lazy from .copy_enumerable import CopyEnumerable

lazy from .control_flow import ControlFlowEnumerable, ControlFlow

lazy from .type_enumerable import TypeEnumerable


lazy from .filter_enumerable import FilterEnumerable, FilterPredicate

lazy from .count_enumerable import CountEnumerable
lazy from .enumerable import Enumerable
lazy from ._sentinels import MISSING


class TakeEnumerable[T](
    CountEnumerable[T],
    FilterEnumerable[T],
    TypeEnumerable[T],
    ControlFlowEnumerable[T],
    CopyEnumerable[T],
    WholeSequenceOperationsEnumerable[T],
    CollectEnumerable[T],
):
    @overload
    def first(self, predicate: FilterPredicate[T] | None = None) -> T: ...

    @overload
    def first[U](self, predicate: FilterPredicate[T] | None, default: U) -> T | U: ...

    @overload
    def first[U](self, *, default: U) -> T | U: ...

    def first(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    @overload
    def single(self, predicate: FilterPredicate[T] | None = None) -> T: ...

    @overload
    def single[U](self, predicate: FilterPredicate[T] | None, default: U) -> T | U: ...

    @overload
    def single[U](self, *, default: U) -> T | U: ...

    def single(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(1, default=default).first()

    @overload
    def last(self, predicate: FilterPredicate[T] | None = None) -> T: ...

    @overload
    def last[U](self, predicate: FilterPredicate[T] | None, default: U) -> T | U: ...

    @overload
    def last[U](self, *, default: U) -> T | U: ...

    def last(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    @overload
    def exact(self, n: int) -> "Enumerable[T]": ...

    @overload
    def exact[U](self, n: int, default: U) -> "Enumerable[T | U]": ...

    def exact(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    @overload
    def nth(self, n: int) -> T: ...

    @overload
    def nth[U](self, n: int, default: U) -> T | U: ...

    def nth(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    @overload
    def find(self, predicate: FilterPredicate[T]) -> T: ...

    @overload
    def find[U](self, predicate: FilterPredicate[T], default: U) -> T | U: ...

    def find(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(predicate, default=default)

    def take_last(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def chunk(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def group_by[K: Hashable](
        self, key_selector: Callable[[T], K]
    ) -> "Enumerable[tuple[K, list[T]]]":
        def inner() -> Iterator[tuple[K, list[T]]]:
            groups: dict[K, list[T]] = {}
            for item in self:
                key = key_selector(item)
                groups.setdefault(key, []).append(item)
            yield from groups.items()

        return Enumerable(inner())

    def order_by(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        return Enumerable(inner())

    @overload
    def default_if_empty(self) -> "Enumerable[T | None]": ...

    @overload
    def default_if_empty[U](self, default: U) -> "Enumerable[T | U]": ...

    def default_if_empty(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def sum(self) -> T:
        return cast(T, builtins.sum(cast(Iterable[Any], self)))

    def average(self) -> float:
        return fmean(self)  # type: ignore[arg-type]

    def min(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=key)

    def max(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=key)

    def islice(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, step)
        return Enumerable(slice)

    def skip(self, n: int = 1) -> "Enumerable[T]":
        return self.islice(n, None)

    def skip_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if predicate(x)
                else ControlFlow[T].yield_control_ok(x)
            )
        )

    def take(self, n: int = 1) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(None, n)

    def take_while_lossy(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if predicate(x) else ControlFlow.stop()
        )

    def take_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.take_while_lossy(predicate)

    def take_while_inclusive(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if predicate(x) else ControlFlow[T].stop_ok(x)
            )
        )

    def take_while_lossless(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            count = 0
            for item in lookahead:
                if not predicate(item):
                    break
                count += 1
            yield from itertools.islice(self, count)

        return Enumerable(inner())

    def peek_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.shallow_copy().take_while_lossy(predicate)

    def peek(self) -> T:
        return self.peek_n(1).single()

    def try_peek(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) == 1:
            return Some(val[0])
        else:
            return Null

    def peek_n(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] < n)
            .map(lambda x: x[1])
        )

    def skip_last(self, n: int = 1) -> "Enumerable[T]":
        return self.reverse().skip(n).reverse()

    def reverse(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from reversed(self.to_list())

        return Enumerable(inner())


class TakeEnumerableExceptionCase(StrEnum):
    NotEnoughItems = (
        "There were not enough items remaining in the enumerable for this operation!"
    )
    TooManyItems = (
        "There were too many items remaining in the enumerable for this operation!"
    )


class TakeEnumerableException(Exception):
    def __init__(self, case: TakeEnumerableExceptionCase, *args: Any, **kwargs: Any):
        self.exception_case = case
        super().__init__(*args, **kwargs)

    @classmethod
    def not_enough_items(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def too_many_items(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )
