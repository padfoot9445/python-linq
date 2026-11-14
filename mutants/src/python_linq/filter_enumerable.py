lazy from typing import Callable, overload
from collections.abc import Iterator

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable

type FilterPredicate[T] = Callable[[T], bool]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁFilterEnumerableǁwhere__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFilterEnumerableǁfilter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFilterEnumerableǁdistinct__mutmut: MutantDict = {}  # type: ignore
mutants_xǁFilterEnumerableǁcontains__mutmut: MutantDict = {}  # type: ignore


class FilterEnumerable[T](BaseEnumerable[T]):
    @_mutmut_mutated(mutants_xǁFilterEnumerableǁwhere__mutmut)
    def where(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(callback, self.value))
    def xǁFilterEnumerableǁwhere__mutmut_orig(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(callback, self.value))
    def xǁFilterEnumerableǁwhere__mutmut_1(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(None)
    def xǁFilterEnumerableǁwhere__mutmut_2(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(None, self.value))
    def xǁFilterEnumerableǁwhere__mutmut_3(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(callback, None))
    def xǁFilterEnumerableǁwhere__mutmut_4(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(self.value))
    def xǁFilterEnumerableǁwhere__mutmut_5(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return Enumerable(filter(callback, ))

    @_mutmut_mutated(mutants_xǁFilterEnumerableǁfilter__mutmut)
    def filter(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return self.where(callback)

    def xǁFilterEnumerableǁfilter__mutmut_orig(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return self.where(callback)

    def xǁFilterEnumerableǁfilter__mutmut_1(self, callback: FilterPredicate[T]) -> "Enumerable[T]":
        return self.where(None)

    @_mutmut_mutated(mutants_xǁFilterEnumerableǁdistinct__mutmut)
    def distinct[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_orig[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_1[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = None
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_2[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = None
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_3[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if (key is not None) and False else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_4[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if (key is not None) or True else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_5[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(None) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_6[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_7[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_8[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(None):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_9[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key != existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_10[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(None)
                    yield item

        return Enumerable(inner())

    def xǁFilterEnumerableǁdistinct__mutmut_11[K](self, key: Callable[[T], K] | None = None) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[object] = []
            for item in self:
                item_key: object = key(item) if key is not None else item
                if not any(item_key == existing for existing in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(None)
    @overload
    def contains(self, value: T) -> bool: ...
    @overload
    def contains[V](self, value: V, comparer: Callable[[T, V], bool]) -> bool: ...
    @_mutmut_mutated(mutants_xǁFilterEnumerableǁcontains__mutmut)
    def contains[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(item, value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_orig[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(item, value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_1[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is not None:
            return any(item == value for item in self)
        return any(comparer(item, value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_2[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(None)
        return any(comparer(item, value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_3[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item != value for item in self)
        return any(comparer(item, value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_4[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(None)
    def xǁFilterEnumerableǁcontains__mutmut_5[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(None, value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_6[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(item, None) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_7[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(value) for item in self)
    def xǁFilterEnumerableǁcontains__mutmut_8[V](
        self, value: V, comparer: Callable[[T, V], bool] | None = None
    ) -> bool:
        if comparer is None:
            return any(item == value for item in self)
        return any(comparer(item, ) for item in self)

mutants_xǁFilterEnumerableǁwhere__mutmut['_mutmut_orig'] = FilterEnumerable.xǁFilterEnumerableǁwhere__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁwhere__mutmut['xǁFilterEnumerableǁwhere__mutmut_1'] = FilterEnumerable.xǁFilterEnumerableǁwhere__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁwhere__mutmut['xǁFilterEnumerableǁwhere__mutmut_2'] = FilterEnumerable.xǁFilterEnumerableǁwhere__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁwhere__mutmut['xǁFilterEnumerableǁwhere__mutmut_3'] = FilterEnumerable.xǁFilterEnumerableǁwhere__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁwhere__mutmut['xǁFilterEnumerableǁwhere__mutmut_4'] = FilterEnumerable.xǁFilterEnumerableǁwhere__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁwhere__mutmut['xǁFilterEnumerableǁwhere__mutmut_5'] = FilterEnumerable.xǁFilterEnumerableǁwhere__mutmut_5 # type: ignore # mutmut generated

mutants_xǁFilterEnumerableǁfilter__mutmut['_mutmut_orig'] = FilterEnumerable.xǁFilterEnumerableǁfilter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁfilter__mutmut['xǁFilterEnumerableǁfilter__mutmut_1'] = FilterEnumerable.xǁFilterEnumerableǁfilter__mutmut_1 # type: ignore # mutmut generated

mutants_xǁFilterEnumerableǁdistinct__mutmut['_mutmut_orig'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_1'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_2'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_3'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_4'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_5'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_6'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_7'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_8'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_8 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_9'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_9 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_10'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_10 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁdistinct__mutmut['xǁFilterEnumerableǁdistinct__mutmut_11'] = FilterEnumerable.xǁFilterEnumerableǁdistinct__mutmut_11 # type: ignore # mutmut generated

mutants_xǁFilterEnumerableǁcontains__mutmut['_mutmut_orig'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_orig # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_1'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_1 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_2'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_2 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_3'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_3 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_4'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_4 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_5'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_5 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_6'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_6 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_7'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_7 # type: ignore # mutmut generated
mutants_xǁFilterEnumerableǁcontains__mutmut['xǁFilterEnumerableǁcontains__mutmut_8'] = FilterEnumerable.xǁFilterEnumerableǁcontains__mutmut_8 # type: ignore # mutmut generated
