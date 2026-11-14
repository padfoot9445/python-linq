import itertools
from typing import Callable, Iterable, cast, overload

lazy from .select_enumerable import SelectEnumerable
lazy from .enumerable import Enumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWholeSequenceOperationsEnumerableǁall__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut: MutantDict = {}  # type: ignore


class WholeSequenceOperationsEnumerable[T](SelectEnumerable[T]):
    @_mutmut_mutated(mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut)
    def zip[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_orig[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_1[TOther](
        self, other: Iterable[TOther], strict: bool = True
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_2[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(None)
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_3[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(None, other, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_4[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, None, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_5[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, strict=None))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_6[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(other, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_7[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, strict=strict))
    def xǁWholeSequenceOperationsEnumerableǁzip__mutmut_8[TOther](
        self, other: Iterable[TOther], strict: bool = False
    ) -> "Enumerable[tuple[T, TOther]]":
        return Enumerable(zip(self, other, ))

    @_mutmut_mutated(mutants_xǁWholeSequenceOperationsEnumerableǁall__mutmut)
    def all(self, predicate: Callable[[T], bool]) -> bool:
        return all(self.map(predicate))

    def xǁWholeSequenceOperationsEnumerableǁall__mutmut_orig(self, predicate: Callable[[T], bool]) -> bool:
        return all(self.map(predicate))

    def xǁWholeSequenceOperationsEnumerableǁall__mutmut_1(self, predicate: Callable[[T], bool]) -> bool:
        return all(None)

    def xǁWholeSequenceOperationsEnumerableǁall__mutmut_2(self, predicate: Callable[[T], bool]) -> bool:
        return all(self.map(None))

    @overload
    def any(self) -> bool: ...

    @overload
    def any(self, predicate: Callable[[T], bool]) -> bool: ...

    @_mutmut_mutated(mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut)
    def any(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return True
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_orig(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return True
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_1(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is not None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return True
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_2(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(None)
            except StopIteration:
                return False
            return True
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_3(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(None))
            except StopIteration:
                return False
            return True
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_4(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return True
            return True
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_5(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return False
        return any(predicate(item) for item in self)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_6(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return True
        return any(None)

    def xǁWholeSequenceOperationsEnumerableǁany__mutmut_7(self, predicate: Callable[[T], bool] | None = None) -> bool:
        if predicate is None:
            try:
                next(iter(self))
            except StopIteration:
                return False
            return True
        return any(predicate(None) for item in self)

    @_mutmut_mutated(mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut)
    def eq[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_orig[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_1[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = None
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_2[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(None, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_3[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, None, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_4[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=None):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_5[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_6[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_7[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, ):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_8[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing and b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_9[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is not missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_10[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is not missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_11[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return True  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_12[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if comparer(cast(T, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_13[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(None, cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_14[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), None):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_15[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_16[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), ):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_17[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(None, a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_18[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, None), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_19[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(a), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_20[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, ), cast(TOther, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_21[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(None, b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_22[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, None)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_23[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(b)):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_24[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, )):
                return False
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_25[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return True
        return True

    def xǁWholeSequenceOperationsEnumerableǁeq__mutmut_26[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        missing = object()
        for a, b in itertools.zip_longest(self, other, fillvalue=missing):
            if a is missing or b is missing:
                return False  # one side ran out first
            if not comparer(cast(T, a), cast(TOther, b)):
                return False
        return False

    @_mutmut_mutated(mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut)
    def neq[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(other, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁneq__mutmut_orig[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(other, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁneq__mutmut_1[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(other, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁneq__mutmut_2[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(None, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁneq__mutmut_3[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(other, comparer=None)

    def xǁWholeSequenceOperationsEnumerableǁneq__mutmut_4[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁneq__mutmut_5[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return not self.eq(other, )

    @_mutmut_mutated(mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut)
    def sequence_equal[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(other, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_orig[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(other, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_1[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(None, comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_2[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(other, comparer=None)

    def xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_3[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(comparer=comparer)

    def xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_4[TOther](
        self,
        other: Iterable[TOther],
        comparer: Callable[[T, TOther], bool] = (lambda x, y: x == y),
    ) -> bool:
        return self.eq(other, )

mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['_mutmut_orig'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_1'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_2'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_3'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_4'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_5'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_6'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_7'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁzip__mutmut['xǁWholeSequenceOperationsEnumerableǁzip__mutmut_8'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁzip__mutmut_8 # type: ignore # mutmut generated

mutants_xǁWholeSequenceOperationsEnumerableǁall__mutmut['_mutmut_orig'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁall__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁall__mutmut['xǁWholeSequenceOperationsEnumerableǁall__mutmut_1'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁall__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁall__mutmut['xǁWholeSequenceOperationsEnumerableǁall__mutmut_2'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁall__mutmut_2 # type: ignore # mutmut generated

mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['_mutmut_orig'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_1'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_2'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_3'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_4'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_5'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_6'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁany__mutmut['xǁWholeSequenceOperationsEnumerableǁany__mutmut_7'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁany__mutmut_7 # type: ignore # mutmut generated

mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['_mutmut_orig'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_1'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_2'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_3'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_4'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_5'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_6'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_7'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_8'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_9'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_10'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_11'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_12'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_13'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_14'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_15'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_16'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_17'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_18'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_19'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_20'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_21'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_22'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_23'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_24'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_25'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁeq__mutmut['xǁWholeSequenceOperationsEnumerableǁeq__mutmut_26'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁeq__mutmut_26 # type: ignore # mutmut generated

mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut['_mutmut_orig'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁneq__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut['xǁWholeSequenceOperationsEnumerableǁneq__mutmut_1'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁneq__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut['xǁWholeSequenceOperationsEnumerableǁneq__mutmut_2'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁneq__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut['xǁWholeSequenceOperationsEnumerableǁneq__mutmut_3'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁneq__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut['xǁWholeSequenceOperationsEnumerableǁneq__mutmut_4'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁneq__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁneq__mutmut['xǁWholeSequenceOperationsEnumerableǁneq__mutmut_5'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁneq__mutmut_5 # type: ignore # mutmut generated

mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut['_mutmut_orig'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut['xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_1'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut['xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_2'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut['xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_3'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut['xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_4'] = WholeSequenceOperationsEnumerable.xǁWholeSequenceOperationsEnumerableǁsequence_equal__mutmut_4 # type: ignore # mutmut generated
