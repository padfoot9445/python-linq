from typing import Type

lazy from python_linq.aggregate_enumerable import AggregateEnumerable
lazy from .whole_sequence_operations_enumerable import WholeSequenceOperationsEnumerable


lazy from .partition_enumerable import PartitionEnumerable


class Enumerable[T](
    AggregateEnumerable[T],
    PartitionEnumerable[T],
    WholeSequenceOperationsEnumerable[T],
):
    def __getitem__(self, _: Type[T]):
        return Enumerable
