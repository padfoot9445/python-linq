import itertools
from typing import Any, Callable, Self

lazy from python_linq.aggregate_enumerable import AggregateEnumerable
lazy from .whole_sequence_operations_enumerable import WholeSequenceOperationsEnumerable


lazy from .partition_enumerable import PartitionEnumerable


class Enumerable[T](
    AggregateEnumerable[T],
    PartitionEnumerable[T],
    WholeSequenceOperationsEnumerable[T],
):
    @classmethod
    def empty(cls) -> "Enumerable[T]":
        return cls(())

    @classmethod
    def range(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, start + count))

    @classmethod
    def repeat(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def sequence(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def infinite_sequence(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, step))

    def __getitem__(self, _: type[T]) -> type["Enumerable[Any]"]:
        return Enumerable
    def then[TOut](self, fn: Callable[[Self], TOut]) -> TOut:
        return fn(self)
