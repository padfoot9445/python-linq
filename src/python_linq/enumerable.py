from typing import Type

lazy from python_linq.aggregate_enumerable import AggregateEnumerable
lazy from python_linq.control_flow import ControlFlowEnumerable
lazy from .copy_enumerable import CopyEnumerable
from python_linq.select_enumerable import SelectEnumerable

lazy from .collect_enumerable import CollectEnumerable
lazy from .take_enumerable import TakeEnumerable


class Enumerable[T](
    CollectEnumerable[T], AggregateEnumerable[T], ControlFlowEnumerable[T], CopyEnumerable[T]
):
    def __getitem__(self, _: Type[T]):
        return Enumerable
