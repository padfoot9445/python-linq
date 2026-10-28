lazy from .base_enumerable import BaseEnumerable


class CollectEnumerable[T](BaseEnumerable[T]):
    def to_list(self) -> list[T]:
        return list(self)
