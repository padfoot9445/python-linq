from python_linq.aggregate_enumerable import AggregateEnumerable
from python_linq.select_enumerable import SelectEnumerable

lazy from .collect_enumerable import CollectEnumerable
lazy from .take_enumerable import TakeEnumerable


class Enumerable[T](SelectEnumerable[T], CollectEnumerable[T], AggregateEnumerable[T]):
    pass
