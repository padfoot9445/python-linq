lazy from python_linq.aggregate_enumerable import AggregateEnumerable
lazy from python_linq.control_flow import ControlFlowEnumerable
from python_linq.select_enumerable import SelectEnumerable

lazy from .collect_enumerable import CollectEnumerable
lazy from .take_enumerable import TakeEnumerable


class Enumerable[T](
    CollectEnumerable[T], AggregateEnumerable[T], ControlFlowEnumerable[T]
):
    pass
