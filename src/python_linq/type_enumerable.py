from typing import Type, cast

lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable

class TypeEnumerable[T](BaseEnumerable[T]):
    def cast[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("Enumerable[V]", self)
