lazy from .collect_enumerable import CollectEnumerable
lazy from .take_enumerable import TakeEnumerable
lazy from .select_enumerable import SelectEnumerable


class Enumerable[T](SelectEnumerable[T], TakeEnumerable[T], CollectEnumerable[T]):
    pass
