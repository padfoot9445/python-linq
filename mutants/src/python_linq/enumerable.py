import itertools
from typing import Any

lazy from python_linq.aggregate_enumerable import AggregateEnumerable
lazy from .whole_sequence_operations_enumerable import WholeSequenceOperationsEnumerable


lazy from .partition_enumerable import PartitionEnumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEnumerableǁempty__mutmut: MutantDict = {}  # type: ignore
mutants_xǁEnumerableǁrange__mutmut: MutantDict = {}  # type: ignore
mutants_xǁEnumerableǁrepeat__mutmut: MutantDict = {}  # type: ignore
mutants_xǁEnumerableǁsequence__mutmut: MutantDict = {}  # type: ignore
mutants_xǁEnumerableǁinfinite_sequence__mutmut: MutantDict = {}  # type: ignore


class Enumerable[T](
    AggregateEnumerable[T],
    PartitionEnumerable[T],
    WholeSequenceOperationsEnumerable[T],
):
    @classmethod
    @_mutmut_mutated(mutants_xǁEnumerableǁempty__mutmut, is_classmethod = True)
    def empty(cls) -> "Enumerable[T]":
        return cls(())
    @classmethod
    def xǁEnumerableǁempty__mutmut_orig(cls) -> "Enumerable[T]":
        return cls(())
    @classmethod
    def xǁEnumerableǁempty__mutmut_1(cls) -> "Enumerable[T]":
        return cls(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁEnumerableǁrange__mutmut, is_classmethod = True)
    def range(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_orig(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_1(cls, start: int, count: int) -> "Enumerable[int]":
        if count <= 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_2(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 1:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_3(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError(None)
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_4(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("XXcount must be non-negativeXX")
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_5(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("COUNT MUST BE NON-NEGATIVE")
        return Enumerable(range(start, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_6(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(None)

    @classmethod
    def xǁEnumerableǁrange__mutmut_7(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(None, start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_8(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, None))

    @classmethod
    def xǁEnumerableǁrange__mutmut_9(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start + count))

    @classmethod
    def xǁEnumerableǁrange__mutmut_10(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, ))

    @classmethod
    def xǁEnumerableǁrange__mutmut_11(cls, start: int, count: int) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(range(start, start - count))

    @classmethod
    @_mutmut_mutated(mutants_xǁEnumerableǁrepeat__mutmut, is_classmethod = True)
    def repeat(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_orig(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_1(cls, value: T, count: int) -> "Enumerable[T]":
        if count <= 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_2(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 1:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_3(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError(None)
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_4(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("XXcount must be non-negativeXX")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_5(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("COUNT MUST BE NON-NEGATIVE")
        return Enumerable(itertools.repeat(value, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_6(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(None)

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_7(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(None, count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_8(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, None))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_9(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(count))

    @classmethod
    def xǁEnumerableǁrepeat__mutmut_10(cls, value: T, count: int) -> "Enumerable[T]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(itertools.repeat(value, ))

    @classmethod
    @_mutmut_mutated(mutants_xǁEnumerableǁsequence__mutmut, is_classmethod = True)
    def sequence(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_orig(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_1(cls, start: int, count: int, step: int = 2) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_2(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count <= 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_3(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 1:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_4(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError(None)
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_5(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("XXcount must be non-negativeXX")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_6(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("COUNT MUST BE NON-NEGATIVE")
        return Enumerable(start + step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_7(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(None)

    @classmethod
    def xǁEnumerableǁsequence__mutmut_8(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start - step * index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_9(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step / index for index in range(count))

    @classmethod
    def xǁEnumerableǁsequence__mutmut_10(cls, start: int, count: int, step: int = 1) -> "Enumerable[int]":
        if count < 0:
            raise ValueError("count must be non-negative")
        return Enumerable(start + step * index for index in range(None))

    @classmethod
    @_mutmut_mutated(mutants_xǁEnumerableǁinfinite_sequence__mutmut, is_classmethod = True)
    def infinite_sequence(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, step))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_orig(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, step))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_1(cls, start: int = 1, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, step))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_2(cls, start: int = 0, step: int = 2) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, step))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_3(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(None)

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_4(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(None, step))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_5(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, None))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_6(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(step))

    @classmethod
    def xǁEnumerableǁinfinite_sequence__mutmut_7(cls, start: int = 0, step: int = 1) -> "Enumerable[int]":
        return Enumerable(itertools.count(start, ))

    def __getitem__(self, _: type[T]) -> type["Enumerable[Any]"]:
        return Enumerable

mutants_xǁEnumerableǁempty__mutmut['_mutmut_orig'] = Enumerable.xǁEnumerableǁempty__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEnumerableǁempty__mutmut['xǁEnumerableǁempty__mutmut_1'] = Enumerable.xǁEnumerableǁempty__mutmut_1 # type: ignore # mutmut generated

mutants_xǁEnumerableǁrange__mutmut['_mutmut_orig'] = Enumerable.xǁEnumerableǁrange__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_1'] = Enumerable.xǁEnumerableǁrange__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_2'] = Enumerable.xǁEnumerableǁrange__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_3'] = Enumerable.xǁEnumerableǁrange__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_4'] = Enumerable.xǁEnumerableǁrange__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_5'] = Enumerable.xǁEnumerableǁrange__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_6'] = Enumerable.xǁEnumerableǁrange__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_7'] = Enumerable.xǁEnumerableǁrange__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_8'] = Enumerable.xǁEnumerableǁrange__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_9'] = Enumerable.xǁEnumerableǁrange__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_10'] = Enumerable.xǁEnumerableǁrange__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrange__mutmut['xǁEnumerableǁrange__mutmut_11'] = Enumerable.xǁEnumerableǁrange__mutmut_11 # type: ignore # mutmut generated

mutants_xǁEnumerableǁrepeat__mutmut['_mutmut_orig'] = Enumerable.xǁEnumerableǁrepeat__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_1'] = Enumerable.xǁEnumerableǁrepeat__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_2'] = Enumerable.xǁEnumerableǁrepeat__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_3'] = Enumerable.xǁEnumerableǁrepeat__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_4'] = Enumerable.xǁEnumerableǁrepeat__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_5'] = Enumerable.xǁEnumerableǁrepeat__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_6'] = Enumerable.xǁEnumerableǁrepeat__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_7'] = Enumerable.xǁEnumerableǁrepeat__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_8'] = Enumerable.xǁEnumerableǁrepeat__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_9'] = Enumerable.xǁEnumerableǁrepeat__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEnumerableǁrepeat__mutmut['xǁEnumerableǁrepeat__mutmut_10'] = Enumerable.xǁEnumerableǁrepeat__mutmut_10 # type: ignore # mutmut generated

mutants_xǁEnumerableǁsequence__mutmut['_mutmut_orig'] = Enumerable.xǁEnumerableǁsequence__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_1'] = Enumerable.xǁEnumerableǁsequence__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_2'] = Enumerable.xǁEnumerableǁsequence__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_3'] = Enumerable.xǁEnumerableǁsequence__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_4'] = Enumerable.xǁEnumerableǁsequence__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_5'] = Enumerable.xǁEnumerableǁsequence__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_6'] = Enumerable.xǁEnumerableǁsequence__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_7'] = Enumerable.xǁEnumerableǁsequence__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_8'] = Enumerable.xǁEnumerableǁsequence__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_9'] = Enumerable.xǁEnumerableǁsequence__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEnumerableǁsequence__mutmut['xǁEnumerableǁsequence__mutmut_10'] = Enumerable.xǁEnumerableǁsequence__mutmut_10 # type: ignore # mutmut generated

mutants_xǁEnumerableǁinfinite_sequence__mutmut['_mutmut_orig'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_1'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_2'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_3'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_4'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_5'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_6'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEnumerableǁinfinite_sequence__mutmut['xǁEnumerableǁinfinite_sequence__mutmut_7'] = Enumerable.xǁEnumerableǁinfinite_sequence__mutmut_7 # type: ignore # mutmut generated
