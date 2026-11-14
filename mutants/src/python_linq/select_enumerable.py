lazy from typing import Any, Callable, Iterable, overload

lazy from .enumerable import Enumerable
lazy from ._sentinels import DROP, FilterMapDrop

lazy from .base_enumerable import BaseEnumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSelectEnumerableǁselect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁmap__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁselect_indexed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁselect_many__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁflat_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁfilter_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁflatten__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁconcat__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁchain__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁappend__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁprepend__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSelectEnumerableǁtee__mutmut: MutantDict = {}  # type: ignore


class SelectEnumerable[T](BaseEnumerable[T]):
    @_mutmut_mutated(mutants_xǁSelectEnumerableǁselect__mutmut)
    def select[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, self))
    def xǁSelectEnumerableǁselect__mutmut_orig[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, self))
    def xǁSelectEnumerableǁselect__mutmut_1[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(None)
    def xǁSelectEnumerableǁselect__mutmut_2[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(None, self))
    def xǁSelectEnumerableǁselect__mutmut_3[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, None))
    def xǁSelectEnumerableǁselect__mutmut_4[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(self))
    def xǁSelectEnumerableǁselect__mutmut_5[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return Enumerable(map(callback, ))

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁmap__mutmut)
    def map[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return self.select(callback)

    def xǁSelectEnumerableǁmap__mutmut_orig[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return self.select(callback)

    def xǁSelectEnumerableǁmap__mutmut_1[V](self, callback: Callable[[T], V]) -> "Enumerable[V]":
        return self.select(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁselect_indexed__mutmut)
    def select_indexed[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(item, index)

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_orig[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(item, index)

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_1[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(None):
                yield callback(item, index)

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_2[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(None, index)

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_3[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(item, None)

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_4[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(index)

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_5[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(item, )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_indexed__mutmut_6[V](self, callback: Callable[[T, int], V]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for index, item in enumerate(self):
                yield callback(item, index)

        return Enumerable(None)

    @overload
    def select_many[V](
        self, collection_selector: Callable[[T], Iterable[V]]
    ) -> "Enumerable[V]": ...

    @overload
    def select_many[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U],
    ) -> "Enumerable[U]": ...

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁselect_many__mutmut)
    def select_many[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_orig[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_1[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(None):
                    yield (
                        result_selector(item, selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_2[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if (result_selector is not None) and False
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_3[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if (result_selector is not None) or True
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_4[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(None, selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_5[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, None)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_6[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_7[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, )
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_8[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if result_selector is None
                        else selected
                    )

        return Enumerable(inner())

    def xǁSelectEnumerableǁselect_many__mutmut_9[V, U](
        self,
        collection_selector: Callable[[T], Iterable[V]],
        result_selector: Callable[[T, V], U] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterable[Any]:
            for item in self:
                for selected in collection_selector(item):
                    yield (
                        result_selector(item, selected)
                        if result_selector is not None
                        else selected
                    )

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁflat_map__mutmut)
    def flat_map[V](self, callback: Callable[[T], Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for result_bundle in self.map(callback):
                yield from result_bundle

        return Enumerable(inner())

    def xǁSelectEnumerableǁflat_map__mutmut_orig[V](self, callback: Callable[[T], Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for result_bundle in self.map(callback):
                yield from result_bundle

        return Enumerable(inner())

    def xǁSelectEnumerableǁflat_map__mutmut_1[V](self, callback: Callable[[T], Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for result_bundle in self.map(None):
                yield from result_bundle

        return Enumerable(inner())

    def xǁSelectEnumerableǁflat_map__mutmut_2[V](self, callback: Callable[[T], Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for result_bundle in self.map(callback):
                yield from result_bundle

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁfilter_map__mutmut)
    def filter_map[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(item)
                if result is not DROP:
                    yield result

        return Enumerable(inner())

    def xǁSelectEnumerableǁfilter_map__mutmut_orig[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(item)
                if result is not DROP:
                    yield result

        return Enumerable(inner())

    def xǁSelectEnumerableǁfilter_map__mutmut_1[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = None
                if result is not DROP:
                    yield result

        return Enumerable(inner())

    def xǁSelectEnumerableǁfilter_map__mutmut_2[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(None)
                if result is not DROP:
                    yield result

        return Enumerable(inner())

    def xǁSelectEnumerableǁfilter_map__mutmut_3[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(item)
                if result is DROP:
                    yield result

        return Enumerable(inner())

    def xǁSelectEnumerableǁfilter_map__mutmut_4[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for item in self:
                result = callback(item)
                if result is not DROP:
                    yield result

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁflatten__mutmut)
    def flatten[V](self: Iterable[Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for items in self:
                yield from items

        return Enumerable(inner())

    def xǁSelectEnumerableǁflatten__mutmut_orig[V](self: Iterable[Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for items in self:
                yield from items

        return Enumerable(inner())

    def xǁSelectEnumerableǁflatten__mutmut_1[V](self: Iterable[Iterable[V]]) -> "Enumerable[V]":
        def inner() -> Iterable[V]:
            for items in self:
                yield from items

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁconcat__mutmut)
    def concat(self, other: Iterable[T]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield from other

        return Enumerable(inner())

    def xǁSelectEnumerableǁconcat__mutmut_orig(self, other: Iterable[T]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield from other

        return Enumerable(inner())

    def xǁSelectEnumerableǁconcat__mutmut_1(self, other: Iterable[T]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield from other

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁchain__mutmut)
    def chain(self, other: Iterable[T]) -> "Enumerable[T]":
        return self.concat(other)

    def xǁSelectEnumerableǁchain__mutmut_orig(self, other: Iterable[T]) -> "Enumerable[T]":
        return self.concat(other)

    def xǁSelectEnumerableǁchain__mutmut_1(self, other: Iterable[T]) -> "Enumerable[T]":
        return self.concat(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁappend__mutmut)
    def append(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield item

        return Enumerable(inner())

    def xǁSelectEnumerableǁappend__mutmut_orig(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield item

        return Enumerable(inner())

    def xǁSelectEnumerableǁappend__mutmut_1(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield from self
            yield item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁprepend__mutmut)
    def prepend(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield item
            yield from self

        return Enumerable(inner())

    def xǁSelectEnumerableǁprepend__mutmut_orig(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield item
            yield from self

        return Enumerable(inner())

    def xǁSelectEnumerableǁprepend__mutmut_1(self, item: T) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            yield item
            yield from self

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁSelectEnumerableǁtee__mutmut)
    def tee(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(lambda x: x[1])

    def xǁSelectEnumerableǁtee__mutmut_orig(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(lambda x: x[1])

    def xǁSelectEnumerableǁtee__mutmut_1(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(None)

    def xǁSelectEnumerableǁtee__mutmut_2(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(None).select(lambda x: x[1])

    def xǁSelectEnumerableǁtee__mutmut_3(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: None).select(lambda x: x[1])

    def xǁSelectEnumerableǁtee__mutmut_4(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(None), x)).select(lambda x: x[1])

    def xǁSelectEnumerableǁtee__mutmut_5(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(lambda x: None)

    def xǁSelectEnumerableǁtee__mutmut_6(self, callback: Callable[[T], Any]) -> "Enumerable[T]":
        return self.select(lambda x: (callback(x), x)).select(lambda x: x[2])

mutants_xǁSelectEnumerableǁselect__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁselect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect__mutmut['xǁSelectEnumerableǁselect__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁselect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect__mutmut['xǁSelectEnumerableǁselect__mutmut_2'] = SelectEnumerable.xǁSelectEnumerableǁselect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect__mutmut['xǁSelectEnumerableǁselect__mutmut_3'] = SelectEnumerable.xǁSelectEnumerableǁselect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect__mutmut['xǁSelectEnumerableǁselect__mutmut_4'] = SelectEnumerable.xǁSelectEnumerableǁselect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect__mutmut['xǁSelectEnumerableǁselect__mutmut_5'] = SelectEnumerable.xǁSelectEnumerableǁselect__mutmut_5 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁmap__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁmap__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁmap__mutmut['xǁSelectEnumerableǁmap__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁmap__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁselect_indexed__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_indexed__mutmut['xǁSelectEnumerableǁselect_indexed__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_indexed__mutmut['xǁSelectEnumerableǁselect_indexed__mutmut_2'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_indexed__mutmut['xǁSelectEnumerableǁselect_indexed__mutmut_3'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_indexed__mutmut['xǁSelectEnumerableǁselect_indexed__mutmut_4'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_indexed__mutmut['xǁSelectEnumerableǁselect_indexed__mutmut_5'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_indexed__mutmut['xǁSelectEnumerableǁselect_indexed__mutmut_6'] = SelectEnumerable.xǁSelectEnumerableǁselect_indexed__mutmut_6 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁselect_many__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_2'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_3'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_4'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_5'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_6'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_7'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_8'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁselect_many__mutmut['xǁSelectEnumerableǁselect_many__mutmut_9'] = SelectEnumerable.xǁSelectEnumerableǁselect_many__mutmut_9 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁflat_map__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁflat_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁflat_map__mutmut['xǁSelectEnumerableǁflat_map__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁflat_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁflat_map__mutmut['xǁSelectEnumerableǁflat_map__mutmut_2'] = SelectEnumerable.xǁSelectEnumerableǁflat_map__mutmut_2 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁfilter_map__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁfilter_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁfilter_map__mutmut['xǁSelectEnumerableǁfilter_map__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁfilter_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁfilter_map__mutmut['xǁSelectEnumerableǁfilter_map__mutmut_2'] = SelectEnumerable.xǁSelectEnumerableǁfilter_map__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁfilter_map__mutmut['xǁSelectEnumerableǁfilter_map__mutmut_3'] = SelectEnumerable.xǁSelectEnumerableǁfilter_map__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁfilter_map__mutmut['xǁSelectEnumerableǁfilter_map__mutmut_4'] = SelectEnumerable.xǁSelectEnumerableǁfilter_map__mutmut_4 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁflatten__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁflatten__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁflatten__mutmut['xǁSelectEnumerableǁflatten__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁflatten__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁconcat__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁconcat__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁconcat__mutmut['xǁSelectEnumerableǁconcat__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁconcat__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁchain__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁchain__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁchain__mutmut['xǁSelectEnumerableǁchain__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁchain__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁappend__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁappend__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁappend__mutmut['xǁSelectEnumerableǁappend__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁappend__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁprepend__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁprepend__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁprepend__mutmut['xǁSelectEnumerableǁprepend__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁprepend__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSelectEnumerableǁtee__mutmut['_mutmut_orig'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁtee__mutmut['xǁSelectEnumerableǁtee__mutmut_1'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁtee__mutmut['xǁSelectEnumerableǁtee__mutmut_2'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁtee__mutmut['xǁSelectEnumerableǁtee__mutmut_3'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁtee__mutmut['xǁSelectEnumerableǁtee__mutmut_4'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁtee__mutmut['xǁSelectEnumerableǁtee__mutmut_5'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSelectEnumerableǁtee__mutmut['xǁSelectEnumerableǁtee__mutmut_6'] = SelectEnumerable.xǁSelectEnumerableǁtee__mutmut_6 # type: ignore # mutmut generated
