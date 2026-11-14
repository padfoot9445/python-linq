from collections.abc import Callable

lazy from .copy_enumerable import CopyEnumerable

lazy from .enumerable import Enumerable
lazy from ._sentinels import MISSING


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCountEnumerableǁcount__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCountEnumerableǁenumerate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCountEnumerableǁis_empty__mutmut: MutantDict = {}  # type: ignore


class CountEnumerable[T](CopyEnumerable[T]):
    @_mutmut_mutated(mutants_xǁCountEnumerableǁcount__mutmut)
    def count(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(1 for _ in self)
        return sum(1 for item in self if predicate(item))
    def xǁCountEnumerableǁcount__mutmut_orig(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(1 for _ in self)
        return sum(1 for item in self if predicate(item))
    def xǁCountEnumerableǁcount__mutmut_1(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is not None:
            return sum(1 for _ in self)
        return sum(1 for item in self if predicate(item))
    def xǁCountEnumerableǁcount__mutmut_2(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(None)
        return sum(1 for item in self if predicate(item))
    def xǁCountEnumerableǁcount__mutmut_3(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(2 for _ in self)
        return sum(1 for item in self if predicate(item))
    def xǁCountEnumerableǁcount__mutmut_4(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(1 for _ in self)
        return sum(None)
    def xǁCountEnumerableǁcount__mutmut_5(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(1 for _ in self)
        return sum(2 for item in self if predicate(item))
    def xǁCountEnumerableǁcount__mutmut_6(self, predicate: Callable[[T], bool] | None = None) -> int:
        if predicate is None:
            return sum(1 for _ in self)
        return sum(1 for item in self if predicate(None))

    @_mutmut_mutated(mutants_xǁCountEnumerableǁenumerate__mutmut)
    def enumerate(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(self))

    def xǁCountEnumerableǁenumerate__mutmut_orig(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(self))

    def xǁCountEnumerableǁenumerate__mutmut_1(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(None)

    def xǁCountEnumerableǁenumerate__mutmut_2(self) -> "Enumerable[tuple[int, T]]":
        return Enumerable(enumerate(None))

    @_mutmut_mutated(mutants_xǁCountEnumerableǁis_empty__mutmut)
    def is_empty(self) -> bool:
        return next(iter(self.shallow_copy()), MISSING) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_orig(self) -> bool:
        return next(iter(self.shallow_copy()), MISSING) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_1(self) -> bool:
        return next(None, MISSING) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_2(self) -> bool:
        return next(iter(self.shallow_copy()), None) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_3(self) -> bool:
        return next(MISSING) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_4(self) -> bool:
        return next(iter(self.shallow_copy()), ) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_5(self) -> bool:
        return next(iter(None), MISSING) is MISSING

    def xǁCountEnumerableǁis_empty__mutmut_6(self) -> bool:
        return next(iter(self.shallow_copy()), MISSING) is not MISSING

mutants_xǁCountEnumerableǁcount__mutmut['_mutmut_orig'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁcount__mutmut['xǁCountEnumerableǁcount__mutmut_1'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁcount__mutmut['xǁCountEnumerableǁcount__mutmut_2'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁcount__mutmut['xǁCountEnumerableǁcount__mutmut_3'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁcount__mutmut['xǁCountEnumerableǁcount__mutmut_4'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁcount__mutmut['xǁCountEnumerableǁcount__mutmut_5'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁcount__mutmut['xǁCountEnumerableǁcount__mutmut_6'] = CountEnumerable.xǁCountEnumerableǁcount__mutmut_6 # type: ignore # mutmut generated

mutants_xǁCountEnumerableǁenumerate__mutmut['_mutmut_orig'] = CountEnumerable.xǁCountEnumerableǁenumerate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁenumerate__mutmut['xǁCountEnumerableǁenumerate__mutmut_1'] = CountEnumerable.xǁCountEnumerableǁenumerate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁenumerate__mutmut['xǁCountEnumerableǁenumerate__mutmut_2'] = CountEnumerable.xǁCountEnumerableǁenumerate__mutmut_2 # type: ignore # mutmut generated

mutants_xǁCountEnumerableǁis_empty__mutmut['_mutmut_orig'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁis_empty__mutmut['xǁCountEnumerableǁis_empty__mutmut_1'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁis_empty__mutmut['xǁCountEnumerableǁis_empty__mutmut_2'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁis_empty__mutmut['xǁCountEnumerableǁis_empty__mutmut_3'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁis_empty__mutmut['xǁCountEnumerableǁis_empty__mutmut_4'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁis_empty__mutmut['xǁCountEnumerableǁis_empty__mutmut_5'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCountEnumerableǁis_empty__mutmut['xǁCountEnumerableǁis_empty__mutmut_6'] = CountEnumerable.xǁCountEnumerableǁis_empty__mutmut_6 # type: ignore # mutmut generated
