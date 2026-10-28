from typing import Callable, cast, overload


lazy from .take_enumerable import TakeEnumerable

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
        acc = seed
        if seed is sentinel:
            # assert isinstance(seed, T)
            acc = self.first()

        acc = cast(
            V, acc
        )  # safety: it is up to the caller (and type-checker, provided by the overloads above) to make sure that if T and V differ, seed is provided.

        for i in self:
            acc = aggregator(acc, i)
        return acc

    def join(
        self, sep: T, aggregator: Callable[[T, T], T] = (lambda x, y: x + y)
    ) -> T:  # pyright: ignore[reportUnknownLambdaType, reportOperatorIssue]
        return self.fold(lambda x, y: aggregator(x, aggregator(sep, y)))
