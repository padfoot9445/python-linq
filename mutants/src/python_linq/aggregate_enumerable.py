from operator import add
from typing import Any, Callable, cast, overload
from collections.abc import Iterator


lazy from .take_enumerable import TakeEnumerable
lazy from .enumerable import Enumerable

sentinel = object()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAggregateEnumerableǁaggregate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAggregateEnumerableǁfold__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAggregateEnumerableǁreduce__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAggregateEnumerableǁjoin__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAggregateEnumerableǁscan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAggregateEnumerableǁ_scan__mutmut: MutantDict = {}  # type: ignore


class AggregateEnumerable[T](TakeEnumerable[T]):

    @overload
    def aggregate(self, seed: Callable[[T, T], T]) -> T: ...

    @overload
    def aggregate[V](self, seed: V, aggregator: Callable[[V, T], V]) -> V: ...

    @overload
    def aggregate[V, R](
        self,
        seed: V,
        aggregator: Callable[[V, T], V],
        result_selector: Callable[[V], R],
    ) -> R: ...

    @_mutmut_mutated(mutants_xǁAggregateEnumerableǁaggregate__mutmut)
    def aggregate(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_orig(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_1(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is not None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_2(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(None)
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_3(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(None, seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_4(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], None))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_5(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_6(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], ))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_7(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = None
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_8(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(None, seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_9(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, None)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_10(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(seed)
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_11(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, )
        return result_selector(result) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_12(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if (result_selector is not None) and False else result

    def xǁAggregateEnumerableǁaggregate__mutmut_13(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if (result_selector is not None) or True else result

    def xǁAggregateEnumerableǁaggregate__mutmut_14(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(None) if result_selector is not None else result

    def xǁAggregateEnumerableǁaggregate__mutmut_15(
        self,
        seed: object,
        aggregator: Callable[[Any, T], Any] | None = None,
        result_selector: Callable[[Any], Any] | None = None,
    ) -> Any:
        if aggregator is None:
            return self.fold(cast(Callable[[T, T], T], seed))
        result = self.fold(aggregator, seed)
        return result_selector(result) if result_selector is None else result

    @overload
    def fold[V](self, aggregator: Callable[[V, T], V], seed: V) -> V: ...
    @overload
    def fold(self, aggregator: Callable[[T, T], T]) -> T: ...
    @overload
    def fold(self, aggregator: Callable[[T, T], T], seed: T) -> T: ...
    @_mutmut_mutated(mutants_xǁAggregateEnumerableǁfold__mutmut)
    def fold[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, seed).reverse().take(1).single()
    def xǁAggregateEnumerableǁfold__mutmut_orig[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, seed).reverse().take(1).single()
    def xǁAggregateEnumerableǁfold__mutmut_1[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, seed).reverse().take(None).single()
    def xǁAggregateEnumerableǁfold__mutmut_2[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(None, seed).reverse().take(1).single()
    def xǁAggregateEnumerableǁfold__mutmut_3[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, None).reverse().take(1).single()
    def xǁAggregateEnumerableǁfold__mutmut_4[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(seed).reverse().take(1).single()
    def xǁAggregateEnumerableǁfold__mutmut_5[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, ).reverse().take(1).single()
    def xǁAggregateEnumerableǁfold__mutmut_6[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> V:
        return self._scan(aggregator, seed).reverse().take(2).single()

    @_mutmut_mutated(mutants_xǁAggregateEnumerableǁreduce__mutmut)
    def reduce(self, aggregator: Callable[[T, T], T]) -> T:
        return self.fold(aggregator)

    def xǁAggregateEnumerableǁreduce__mutmut_orig(self, aggregator: Callable[[T, T], T]) -> T:
        return self.fold(aggregator)

    def xǁAggregateEnumerableǁreduce__mutmut_1(self, aggregator: Callable[[T, T], T]) -> T:
        return self.fold(None)

    @_mutmut_mutated(mutants_xǁAggregateEnumerableǁjoin__mutmut)
    def join(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(sep, y)))

    def xǁAggregateEnumerableǁjoin__mutmut_orig(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(sep, y)))

    def xǁAggregateEnumerableǁjoin__mutmut_1(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(None)

    def xǁAggregateEnumerableǁjoin__mutmut_2(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: None)

    def xǁAggregateEnumerableǁjoin__mutmut_3(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(None, aggregator(sep, y)))

    def xǁAggregateEnumerableǁjoin__mutmut_4(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, None))

    def xǁAggregateEnumerableǁjoin__mutmut_5(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(aggregator(sep, y)))

    def xǁAggregateEnumerableǁjoin__mutmut_6(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, ))

    def xǁAggregateEnumerableǁjoin__mutmut_7(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(None, y)))

    def xǁAggregateEnumerableǁjoin__mutmut_8(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(sep, None)))

    def xǁAggregateEnumerableǁjoin__mutmut_9(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(y)))

    def xǁAggregateEnumerableǁjoin__mutmut_10(
        self,
        sep: T,
        aggregator: Callable[[T, T], T] = cast(Callable[[T, T], T], add),
    ) -> T:
        return self.fold(lambda x, y: aggregator(x, aggregator(sep, )))

    @overload
    def scan[V](self, aggregator: Callable[[V, T], V], seed: V) -> "Enumerable[V]": ...
    @overload
    def scan(self, aggregator: Callable[[T, T], T]) -> "Enumerable[T]": ...
    @overload
    def scan(self, aggregator: Callable[[T, T], T], seed: T) -> "Enumerable[T]": ...
    @_mutmut_mutated(mutants_xǁAggregateEnumerableǁscan__mutmut)
    def scan[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(aggregator, seed)
    def xǁAggregateEnumerableǁscan__mutmut_orig[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(aggregator, seed)
    def xǁAggregateEnumerableǁscan__mutmut_1[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(None, seed)
    def xǁAggregateEnumerableǁscan__mutmut_2[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(aggregator, None)
    def xǁAggregateEnumerableǁscan__mutmut_3[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(seed)
    def xǁAggregateEnumerableǁscan__mutmut_4[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        return self._scan(aggregator, )

    @_mutmut_mutated(mutants_xǁAggregateEnumerableǁ_scan__mutmut)
    def _scan[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_orig[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_1[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = None
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_2[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is not sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_3[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = None
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_4[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(None, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_5[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, None)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_6[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_7[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, )
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_8[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(None, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_9[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, None)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_10[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_11[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, )

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_12[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = None
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_13[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(None, i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_14[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), None)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_15[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_16[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), )
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_17[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(None, acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_18[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, None), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_19[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(acc), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_20[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, ), i)
                yield acc

        return Enumerable(inner())

    def xǁAggregateEnumerableǁ_scan__mutmut_21[V](
        self, aggregator: Callable[[V, T], V], seed: V | object = sentinel
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            acc = seed
            if seed is sentinel:
                acc = self.first()
                yield cast(V, acc)
            else:
                yield cast(V, seed)

            for i in self:
                acc = aggregator(cast(V, acc), i)
                yield acc

        return Enumerable(None)

mutants_xǁAggregateEnumerableǁaggregate__mutmut['_mutmut_orig'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_1'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_2'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_3'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_4'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_5'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_6'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_7'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_8'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_9'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_10'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_11'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_12'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_13'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_14'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁaggregate__mutmut['xǁAggregateEnumerableǁaggregate__mutmut_15'] = AggregateEnumerable.xǁAggregateEnumerableǁaggregate__mutmut_15 # type: ignore # mutmut generated

mutants_xǁAggregateEnumerableǁfold__mutmut['_mutmut_orig'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁfold__mutmut['xǁAggregateEnumerableǁfold__mutmut_1'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁfold__mutmut['xǁAggregateEnumerableǁfold__mutmut_2'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁfold__mutmut['xǁAggregateEnumerableǁfold__mutmut_3'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁfold__mutmut['xǁAggregateEnumerableǁfold__mutmut_4'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁfold__mutmut['xǁAggregateEnumerableǁfold__mutmut_5'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁfold__mutmut['xǁAggregateEnumerableǁfold__mutmut_6'] = AggregateEnumerable.xǁAggregateEnumerableǁfold__mutmut_6 # type: ignore # mutmut generated

mutants_xǁAggregateEnumerableǁreduce__mutmut['_mutmut_orig'] = AggregateEnumerable.xǁAggregateEnumerableǁreduce__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁreduce__mutmut['xǁAggregateEnumerableǁreduce__mutmut_1'] = AggregateEnumerable.xǁAggregateEnumerableǁreduce__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAggregateEnumerableǁjoin__mutmut['_mutmut_orig'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_1'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_2'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_3'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_4'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_5'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_6'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_7'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_8'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_9'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁjoin__mutmut['xǁAggregateEnumerableǁjoin__mutmut_10'] = AggregateEnumerable.xǁAggregateEnumerableǁjoin__mutmut_10 # type: ignore # mutmut generated

mutants_xǁAggregateEnumerableǁscan__mutmut['_mutmut_orig'] = AggregateEnumerable.xǁAggregateEnumerableǁscan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁscan__mutmut['xǁAggregateEnumerableǁscan__mutmut_1'] = AggregateEnumerable.xǁAggregateEnumerableǁscan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁscan__mutmut['xǁAggregateEnumerableǁscan__mutmut_2'] = AggregateEnumerable.xǁAggregateEnumerableǁscan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁscan__mutmut['xǁAggregateEnumerableǁscan__mutmut_3'] = AggregateEnumerable.xǁAggregateEnumerableǁscan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁscan__mutmut['xǁAggregateEnumerableǁscan__mutmut_4'] = AggregateEnumerable.xǁAggregateEnumerableǁscan__mutmut_4 # type: ignore # mutmut generated

mutants_xǁAggregateEnumerableǁ_scan__mutmut['_mutmut_orig'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_1'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_2'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_3'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_4'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_5'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_6'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_7'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_8'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_9'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_10'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_11'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_12'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_13'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_14'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_15'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_16'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_17'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_18'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_19'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_20'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAggregateEnumerableǁ_scan__mutmut['xǁAggregateEnumerableǁ_scan__mutmut_21'] = AggregateEnumerable.xǁAggregateEnumerableǁ_scan__mutmut_21 # type: ignore # mutmut generated
