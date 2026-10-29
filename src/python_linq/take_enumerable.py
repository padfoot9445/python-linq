lazy from enum import StrEnum
import itertools
lazy from typing import Any, Callable, cast

from rustshed import Null, Option, Some

lazy from .whole_sequence_operations_enumerable import WholeSequenceOperationsEnumerable

lazy from .copy_enumerable import CopyEnumerable

lazy from .control_flow import ControlFlowEnumerable, ControlFlow

lazy from .type_enumerable import TypeEnumerable


lazy from .filter_enumerable import FilterEnumerable, FilterPredicate

lazy from .count_enumerable import CountEnumerable
lazy from .enumerable import Enumerable

sentinel = object()


class TakeEnumerable[T](
    CountEnumerable[T],
    FilterEnumerable[T],
    TypeEnumerable[T],
    ControlFlowEnumerable[T],
    CopyEnumerable[T],
    WholeSequenceOperationsEnumerable[T],
):
    def first(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: T | object = sentinel,
    ) -> T:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not sentinel:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def single(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: T | object = sentinel,
    ) -> T:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        first = self.first(default=default)
        first = self.first(default=default)
        count = self.count()
        if count != 0:
            raise TakeEnumerableException.too_many_items(1, count + 1)
        return first

    def last(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: T | object = sentinel,
    ) -> T:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last = default
        for i in self:
            last = i
        if last is sentinel:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return cast(
                T, last
            )  # safety: last can only be object where object !: T when last is sentinel

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
        return self.islice(None, n)

    def take_while_lossy(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if predicate(x) else ControlFlow.stop()
        )

    def take_while_inclusive(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if predicate(x) else ControlFlow[T].stop_ok(x)
            )
        )

    def take_while_lossless(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        last_index = (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: predicate(x[1]))
            .map(lambda x: x[0])
            .last(default=-1)
        )
        return self.take(last_index + 1)

    def peek_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.shallow_copy().take_while_lossy(predicate)
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
    def not_enough_items(cls, at_least: int | None = None, actual: int | None = None):
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def too_many_items(cls, at_most: int | None = None, actual: int | None = None):
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )
