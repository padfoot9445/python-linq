lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCopyEnumerableǁshallow_copy__mutmut: MutantDict = {}  # type: ignore


class CopyEnumerable[T](BaseEnumerable[T]):
    @_mutmut_mutated(mutants_xǁCopyEnumerableǁshallow_copy__mutmut)
    def shallow_copy(self) -> "Enumerable[T]":
        return Enumerable(self.value.fork())
    def xǁCopyEnumerableǁshallow_copy__mutmut_orig(self) -> "Enumerable[T]":
        return Enumerable(self.value.fork())
    def xǁCopyEnumerableǁshallow_copy__mutmut_1(self) -> "Enumerable[T]":
        return Enumerable(None)

mutants_xǁCopyEnumerableǁshallow_copy__mutmut['_mutmut_orig'] = CopyEnumerable.xǁCopyEnumerableǁshallow_copy__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCopyEnumerableǁshallow_copy__mutmut['xǁCopyEnumerableǁshallow_copy__mutmut_1'] = CopyEnumerable.xǁCopyEnumerableǁshallow_copy__mutmut_1 # type: ignore # mutmut generated
