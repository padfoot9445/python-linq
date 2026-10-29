from typing import Callable, cast, overload


lazy from .take_enumerable import TakeEnumerable
lazy from .enumerable import Enumerable

sentinel = object()


class AggregateEnumerable[T](TakeEnumerable[T]):

    @overload
    def fold[V](self, aggregator: Callable[[V, T], V], seed: V) -> V: ...
    @overload
    def fold(self, aggregator: Callable[[T, T], T]) -> T: ...
    @overload
    def fold(self, aggregator: Callable[[T, T], T], seed: T) -> T: ...
    def fold[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, seed).reverse().take(1).single()

    def join(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = (
            lambda x, y: x + y  # pyright: ignore[reportUnknownLambdaType, reportOperatorIssue]
        ), 
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(sep, y)))

    @overload
    def scan[V](self, aggregator: Callable[[V, T], V], seed: V) -> "Enumerable[V]": ...
    @overload
    def scan(self, aggregator: Callable[[T, T], T]) -> "Enumerable[T]": ...
    @overload
    def scan(self, aggregator: Callable[[T, T], T], seed: T) -> "Enumerable[T]": ...
    def scan[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(aggregator, seed)

    def _scan[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner():
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())
