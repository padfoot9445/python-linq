lazy import itertools
from collections.abc import Iterable, Iterator, Sized


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁ_Cursorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁ_Cursorǁ__next____mutmut: MutantDict = {}  # type: ignore
mutants_xǁ_Cursorǁfork__mutmut: MutantDict = {}  # type: ignore


class _Cursor[T](Iterator[T]):
    @_mutmut_mutated(mutants_xǁ_Cursorǁ__init____mutmut)
    def __init__(self, iterator: Iterator[T]) -> None:
        self._iterator = iterator
    def xǁ_Cursorǁ__init____mutmut_orig(self, iterator: Iterator[T]) -> None:
        self._iterator = iterator
    def xǁ_Cursorǁ__init____mutmut_1(self, iterator: Iterator[T]) -> None:
        self._iterator = None

    def __iter__(self) -> "_Cursor[T]":
        return self

    @_mutmut_mutated(mutants_xǁ_Cursorǁ__next____mutmut)
    def __next__(self) -> T:
        return next(self._iterator)

    def xǁ_Cursorǁ__next____mutmut_orig(self) -> T:
        return next(self._iterator)

    def xǁ_Cursorǁ__next____mutmut_1(self) -> T:
        return next(None)

    def non_enumerated_count(self) -> int | None:
        if isinstance(self._iterator, Sized):
            return len(self._iterator)
        return None

    @_mutmut_mutated(mutants_xǁ_Cursorǁfork__mutmut)
    def fork(self) -> Iterator[T]:
        current, copy = itertools.tee(self._iterator)
        self._iterator = current
        return copy

    def xǁ_Cursorǁfork__mutmut_orig(self) -> Iterator[T]:
        current, copy = itertools.tee(self._iterator)
        self._iterator = current
        return copy

    def xǁ_Cursorǁfork__mutmut_1(self) -> Iterator[T]:
        current, copy = None
        self._iterator = current
        return copy

    def xǁ_Cursorǁfork__mutmut_2(self) -> Iterator[T]:
        current, copy = itertools.tee(None)
        self._iterator = current
        return copy

    def xǁ_Cursorǁfork__mutmut_3(self) -> Iterator[T]:
        current, copy = itertools.tee(self._iterator)
        self._iterator = None
        return copy

mutants_xǁ_Cursorǁ__init____mutmut['_mutmut_orig'] = _Cursor.xǁ_Cursorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_Cursorǁ__init____mutmut['xǁ_Cursorǁ__init____mutmut_1'] = _Cursor.xǁ_Cursorǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁ_Cursorǁ__next____mutmut['_mutmut_orig'] = _Cursor.xǁ_Cursorǁ__next____mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_Cursorǁ__next____mutmut['xǁ_Cursorǁ__next____mutmut_1'] = _Cursor.xǁ_Cursorǁ__next____mutmut_1 # type: ignore # mutmut generated

mutants_xǁ_Cursorǁfork__mutmut['_mutmut_orig'] = _Cursor.xǁ_Cursorǁfork__mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_Cursorǁfork__mutmut['xǁ_Cursorǁfork__mutmut_1'] = _Cursor.xǁ_Cursorǁfork__mutmut_1 # type: ignore # mutmut generated
mutants_xǁ_Cursorǁfork__mutmut['xǁ_Cursorǁfork__mutmut_2'] = _Cursor.xǁ_Cursorǁfork__mutmut_2 # type: ignore # mutmut generated
mutants_xǁ_Cursorǁfork__mutmut['xǁ_Cursorǁfork__mutmut_3'] = _Cursor.xǁ_Cursorǁfork__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBaseEnumerableǁ__init____mutmut: MutantDict = {}  # type: ignore


class BaseEnumerable[T]:
    @_mutmut_mutated(mutants_xǁBaseEnumerableǁ__init____mutmut)
    def __init__(self, val: Iterable[T] = ()):
        self.value = _Cursor(iter(val))
    def xǁBaseEnumerableǁ__init____mutmut_orig(self, val: Iterable[T] = ()):
        self.value = _Cursor(iter(val))
    def xǁBaseEnumerableǁ__init____mutmut_1(self, val: Iterable[T] = ()):
        self.value = None
    def xǁBaseEnumerableǁ__init____mutmut_2(self, val: Iterable[T] = ()):
        self.value = _Cursor(None)
    def xǁBaseEnumerableǁ__init____mutmut_3(self, val: Iterable[T] = ()):
        self.value = _Cursor(iter(None))

    def __iter__(self) -> Iterator[T]:
        return self.value

mutants_xǁBaseEnumerableǁ__init____mutmut['_mutmut_orig'] = BaseEnumerable.xǁBaseEnumerableǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBaseEnumerableǁ__init____mutmut['xǁBaseEnumerableǁ__init____mutmut_1'] = BaseEnumerable.xǁBaseEnumerableǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁBaseEnumerableǁ__init____mutmut['xǁBaseEnumerableǁ__init____mutmut_2'] = BaseEnumerable.xǁBaseEnumerableǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁBaseEnumerableǁ__init____mutmut['xǁBaseEnumerableǁ__init____mutmut_3'] = BaseEnumerable.xǁBaseEnumerableǁ__init____mutmut_3 # type: ignore # mutmut generated
