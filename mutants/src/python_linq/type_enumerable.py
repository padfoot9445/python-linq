from typing import Type, cast

lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTypeEnumerableǁcast__mutmut: MutantDict = {}  # type: ignore


class TypeEnumerable[T](BaseEnumerable[T]):
    @_mutmut_mutated(mutants_xǁTypeEnumerableǁcast__mutmut)
    def cast[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("Enumerable[V]", self)
    def xǁTypeEnumerableǁcast__mutmut_orig[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("Enumerable[V]", self)
    def xǁTypeEnumerableǁcast__mutmut_1[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast(None, self)
    def xǁTypeEnumerableǁcast__mutmut_2[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("Enumerable[V]", None)
    def xǁTypeEnumerableǁcast__mutmut_3[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast(self)
    def xǁTypeEnumerableǁcast__mutmut_4[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("Enumerable[V]", )
    def xǁTypeEnumerableǁcast__mutmut_5[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("XXEnumerable[V]XX", self)
    def xǁTypeEnumerableǁcast__mutmut_6[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("enumerable[v]", self)
    def xǁTypeEnumerableǁcast__mutmut_7[V](self, t: Type[V] | None = None) -> "Enumerable[V]":
        return cast("ENUMERABLE[V]", self)

mutants_xǁTypeEnumerableǁcast__mutmut['_mutmut_orig'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_1'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_2'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_3'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_4'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_5'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_6'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTypeEnumerableǁcast__mutmut['xǁTypeEnumerableǁcast__mutmut_7'] = TypeEnumerable.xǁTypeEnumerableǁcast__mutmut_7 # type: ignore # mutmut generated
