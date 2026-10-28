lazy from enum import StrEnum
lazy from typing import Any, Callable

lazy from .copy_enumerable import CopyEnumerable

lazy from .control_flow import ControlFlowEnumerable, ControlFlow

lazy from .type_enumerable import TypeEnumerable

lazy from .select_enumerable import SelectEnumerable

lazy from .filter_enumerable import FilterEnumerable, FilterPredicate

lazy from .count_enumerable import CountEnumerable
lazy from .enumerable import Enumerable


class TakeEnumerable[T](
    SelectEnumerable[T],
    CountEnumerable[T],
    FilterEnumerable[T],
    TypeEnumerable[T],
    ControlFlowEnumerable[T],
    CopyEnumerable[T]
):
    def first(self, predicate: FilterPredicate[T] | None = None) -> T:
        if predicate is not None:
            return self.filter(predicate).first()
        try:
            return next(self.value)
        except StopIteration as e:
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def single(self, predicate: FilterPredicate[T] | None = None) -> T:

        if predicate is not None:
            return self.filter(predicate).single()

        first = self.first()
        count = self.count()
        if count != 0:
            raise TakeEnumerableException.too_many_items(1, count)
        return first

    def skip(self, n: int = 1) -> "Enumerable[T]":
        return self.enumerate().skip_while(lambda x: x[0] < n).map(lambda x: x[1])

    def skip_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow.skip() if predicate(x) else ControlFlow[T].ok(x)
        )

    def take(self, n: int = 1) -> "Enumerable[T]":
        return self.enumerate().take_while(lambda x: x[0] < n).map(lambda x: x[1])

    def take_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if predicate(x) else ControlFlow.stop()
        )

    def peek_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.shallow_copy().take_while(predicate)

    def peek(self) -> T:
        return self.peek_n(1).single()
    
    def peek_n(self, n: int) -> "Enumerable[T]":
        return self.shallow_copy().enumerate().take_while(lambda x: x[0] < n).map(lambda x: x[1])



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
        super().__init__(*args, *kwargs)

    @classmethod
    def not_enough_items(cls, at_least: int | None = None, actual: int | None = None):
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def too_many_items(cls, at_most: int | None = None, actual: int | None = None):
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )
