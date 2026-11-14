lazy from .base_enumerable import BaseEnumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCollectEnumerableǁto_list__mutmut: MutantDict = {}  # type: ignore


class CollectEnumerable[T](BaseEnumerable[T]):
    @_mutmut_mutated(mutants_xǁCollectEnumerableǁto_list__mutmut)
    def to_list(self) -> list[T]:
        return list(self)
    def xǁCollectEnumerableǁto_list__mutmut_orig(self) -> list[T]:
        return list(self)
    def xǁCollectEnumerableǁto_list__mutmut_1(self) -> list[T]:
        return list(None)

mutants_xǁCollectEnumerableǁto_list__mutmut['_mutmut_orig'] = CollectEnumerable.xǁCollectEnumerableǁto_list__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCollectEnumerableǁto_list__mutmut['xǁCollectEnumerableǁto_list__mutmut_1'] = CollectEnumerable.xǁCollectEnumerableǁto_list__mutmut_1 # type: ignore # mutmut generated
