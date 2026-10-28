lazy from enum import StrEnum
lazy from typing import Any

lazy from .filter_enumerable import FilterEnumerable, FilterPredicate

lazy from .count_enumerable import CountEnumerable


class TakeEnumerable[T](CountEnumerable[T], FilterEnumerable[T]):
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
