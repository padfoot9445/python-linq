import itertools
from collections.abc import Callable, Hashable, Iterable, Iterator, Sequence
from dataclasses import dataclass
from enum import IntEnum
from random import shuffle
from typing import Any, Protocol, cast, overload

from rustshed import Null, Option, Some

lazy from ._sentinels import DROP, FilterMapDrop, MISSING
lazy from .base_enumerable import BaseEnumerable
lazy from .enumerable import Enumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class Ordering(IntEnum):
    Less = -1
    Equal = 0
    Greater = 1


@dataclass(frozen=True)
class AdvanceByResult:
    complete: bool
    remaining: int


@dataclass(frozen=True)
class NextChunkResult[T]:
    items: list[T]
    complete: bool


class Extendable[T](Protocol):
    def extend(self, values: Iterable[T], /) -> object: ...
mutants_x__ordering__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__ordering__mutmut)
def _ordering(value: int) -> Ordering:
    if value < 0:
        return Ordering.Less
    if value > 0:
        return Ordering.Greater
    return Ordering.Equal


def x__ordering__mutmut_orig(value: int) -> Ordering:
    if value < 0:
        return Ordering.Less
    if value > 0:
        return Ordering.Greater
    return Ordering.Equal


def x__ordering__mutmut_1(value: int) -> Ordering:
    if value <= 0:
        return Ordering.Less
    if value > 0:
        return Ordering.Greater
    return Ordering.Equal


def x__ordering__mutmut_2(value: int) -> Ordering:
    if value < 1:
        return Ordering.Less
    if value > 0:
        return Ordering.Greater
    return Ordering.Equal


def x__ordering__mutmut_3(value: int) -> Ordering:
    if value < 0:
        return Ordering.Less
    if value >= 0:
        return Ordering.Greater
    return Ordering.Equal


def x__ordering__mutmut_4(value: int) -> Ordering:
    if value < 0:
        return Ordering.Less
    if value > 1:
        return Ordering.Greater
    return Ordering.Equal

mutants_x__ordering__mutmut['_mutmut_orig'] = x__ordering__mutmut_orig # type: ignore # mutmut generated
mutants_x__ordering__mutmut['x__ordering__mutmut_1'] = x__ordering__mutmut_1 # type: ignore # mutmut generated
mutants_x__ordering__mutmut['x__ordering__mutmut_2'] = x__ordering__mutmut_2 # type: ignore # mutmut generated
mutants_x__ordering__mutmut['x__ordering__mutmut_3'] = x__ordering__mutmut_3 # type: ignore # mutmut generated
mutants_x__ordering__mutmut['x__ordering__mutmut_4'] = x__ordering__mutmut_4 # type: ignore # mutmut generated
mutants_x__compare__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compare__mutmut)
def _compare(left: Any, right: Any) -> Ordering:
    if left < right:
        return Ordering.Less
    if left > right:
        return Ordering.Greater
    return Ordering.Equal


def x__compare__mutmut_orig(left: Any, right: Any) -> Ordering:
    if left < right:
        return Ordering.Less
    if left > right:
        return Ordering.Greater
    return Ordering.Equal


def x__compare__mutmut_1(left: Any, right: Any) -> Ordering:
    if left <= right:
        return Ordering.Less
    if left > right:
        return Ordering.Greater
    return Ordering.Equal


def x__compare__mutmut_2(left: Any, right: Any) -> Ordering:
    if left < right:
        return Ordering.Less
    if left >= right:
        return Ordering.Greater
    return Ordering.Equal

mutants_x__compare__mutmut['_mutmut_orig'] = x__compare__mutmut_orig # type: ignore # mutmut generated
mutants_x__compare__mutmut['x__compare__mutmut_1'] = x__compare__mutmut_1 # type: ignore # mutmut generated
mutants_x__compare__mutmut['x__compare__mutmut_2'] = x__compare__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁmap_while__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁfind_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁinspect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁfuse__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁcycle__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁfor_each__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁcollect_into__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁunzip__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁpartition__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁposition__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁrposition__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁmin_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁmax_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁproduct__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁcmp__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁlt__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁle__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁgt__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁge__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁis_sorted__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁunion__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁexcept___mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁintersect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁorder__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁthen_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁshuffle__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁof_type__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁto_array__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁto_hashset__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁright_join__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut: MutantDict = {}  # type: ignore


class IteratorParityEnumerable[T](BaseEnumerable[T]):
    def by_ref(self) -> "IteratorParityEnumerable[T]":
        return self

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁnext__mutmut)
    def next(self) -> Option[T]:
        try:
            return Some(next(self.value))
        except StopIteration:
            return Null

    def xǁIteratorParityEnumerableǁnext__mutmut_orig(self) -> Option[T]:
        try:
            return Some(next(self.value))
        except StopIteration:
            return Null

    def xǁIteratorParityEnumerableǁnext__mutmut_1(self) -> Option[T]:
        try:
            return Some(None)
        except StopIteration:
            return Null

    def xǁIteratorParityEnumerableǁnext__mutmut_2(self) -> Option[T]:
        try:
            return Some(next(None))
        except StopIteration:
            return Null

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut)
    def next_chunk(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_orig(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_1(self, size: int) -> NextChunkResult[T]:
        if size < 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_2(self, size: int) -> NextChunkResult[T]:
        if size <= 1:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_3(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError(None)
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_4(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("XXsize must be greater than zeroXX")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_5(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("SIZE MUST BE GREATER THAN ZERO")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_6(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = None
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_7(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(None)
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_8(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(None, size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_9(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, None))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_10(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(size))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_11(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, ))
        return NextChunkResult(items, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_12(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(None, len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_13(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, None)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_14(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(len(items) == size)

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_15(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, )

    def xǁIteratorParityEnumerableǁnext_chunk__mutmut_16(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) != size)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut)
    def advance_by(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_orig(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_1(self, count: int) -> AdvanceByResult:
        if count <= 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_2(self, count: int) -> AdvanceByResult:
        if count < 1:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_3(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError(None)
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_4(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("XXcount must be non-negativeXX")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_5(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("COUNT MUST BE NON-NEGATIVE")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_6(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = None
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_7(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(None)
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_8(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(2 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_9(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(None, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_10(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, None))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_11(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(count))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_12(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, ))
        return AdvanceByResult(advanced == count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_13(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(None, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_14(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, None)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_15(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_16(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, )

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_17(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced != count, count - advanced)

    def xǁIteratorParityEnumerableǁadvance_by__mutmut_18(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count + advanced)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁstep_by__mutmut)
    def step_by(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_orig(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_1(self, step: int) -> "Enumerable[T]":
        if step < 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_2(self, step: int) -> "Enumerable[T]":
        if step <= 1:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_3(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError(None)
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_4(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("XXstep must be greater than zeroXX")
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_5(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("STEP MUST BE GREATER THAN ZERO")
        return Enumerable(itertools.islice(self, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_6(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(None)

    def xǁIteratorParityEnumerableǁstep_by__mutmut_7(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(None, 0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_8(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, None, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_9(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, None))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_10(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(0, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_11(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, None, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_12(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, step))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_13(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, ))

    def xǁIteratorParityEnumerableǁstep_by__mutmut_14(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 1, None, step))

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁintersperse__mutmut)
    def intersperse(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_orig(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_1(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = None
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_2(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(None)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_3(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = None
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_4(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(None, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_5(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, None)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_6(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_7(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, )
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_8(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is not MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_9(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(None, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_10(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, None)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_11(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_12(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, )
            for item in iterator:
                yield separator
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse__mutmut_13(self, separator: T) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator
                yield item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut)
    def intersperse_with(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_orig(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_1(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = None
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_2(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(None)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_3(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = None
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_4(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(None, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_5(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, None)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_6(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_7(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, )
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_8(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is not MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_9(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(None, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_10(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, None)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_11(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_12(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, )
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁintersperse_with__mutmut_13(self, separator: Callable[[], T]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            iterator = iter(self)
            first = next(iterator, MISSING)
            if first is MISSING:
                return
            yield cast(T, first)
            for item in iterator:
                yield separator()
                yield item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁmap_while__mutmut)
    def map_while[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            for item in self:
                result = callback(item)
                if result is DROP:
                    return
                yield result

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_while__mutmut_orig[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            for item in self:
                result = callback(item)
                if result is DROP:
                    return
                yield result

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_while__mutmut_1[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            for item in self:
                result = None
                if result is DROP:
                    return
                yield result

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_while__mutmut_2[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            for item in self:
                result = callback(None)
                if result is DROP:
                    return
                yield result

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_while__mutmut_3[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            for item in self:
                result = callback(item)
                if result is not DROP:
                    return
                yield result

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_while__mutmut_4[V](
        self, callback: Callable[[T], V | FilterMapDrop]
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            for item in self:
                result = callback(item)
                if result is DROP:
                    return
                yield result

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁfind_map__mutmut)
    def find_map[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = callback(item)
            if result is not DROP:
                return Some(result)
        return Null

    def xǁIteratorParityEnumerableǁfind_map__mutmut_orig[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = callback(item)
            if result is not DROP:
                return Some(result)
        return Null

    def xǁIteratorParityEnumerableǁfind_map__mutmut_1[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = None
            if result is not DROP:
                return Some(result)
        return Null

    def xǁIteratorParityEnumerableǁfind_map__mutmut_2[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = callback(None)
            if result is not DROP:
                return Some(result)
        return Null

    def xǁIteratorParityEnumerableǁfind_map__mutmut_3[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = callback(item)
            if result is DROP:
                return Some(result)
        return Null

    def xǁIteratorParityEnumerableǁfind_map__mutmut_4[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = callback(item)
            if result is not DROP:
                return Some(None)
        return Null

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁinspect__mutmut)
    def inspect(self, callback: Callable[[T], object]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            for item in self:
                callback(item)
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁinspect__mutmut_orig(self, callback: Callable[[T], object]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            for item in self:
                callback(item)
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁinspect__mutmut_1(self, callback: Callable[[T], object]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            for item in self:
                callback(None)
                yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁinspect__mutmut_2(self, callback: Callable[[T], object]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            for item in self:
                callback(item)
                yield item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁfuse__mutmut)
    def fuse(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from self

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfuse__mutmut_orig(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from self

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfuse__mutmut_1(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from self

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁcycle__mutmut)
    def cycle(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            cache: list[T] = []
            for item in self:
                cache.append(item)
                yield item
            while cache:
                yield from cache

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcycle__mutmut_orig(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            cache: list[T] = []
            for item in self:
                cache.append(item)
                yield item
            while cache:
                yield from cache

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcycle__mutmut_1(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            cache: list[T] = None
            for item in self:
                cache.append(item)
                yield item
            while cache:
                yield from cache

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcycle__mutmut_2(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            cache: list[T] = []
            for item in self:
                cache.append(None)
                yield item
            while cache:
                yield from cache

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcycle__mutmut_3(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            cache: list[T] = []
            for item in self:
                cache.append(item)
                yield item
            while cache:
                yield from cache

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut)
    def array_chunks(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_orig(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_1(self, size: int) -> "Enumerable[list[T]]":
        if size < 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_2(self, size: int) -> "Enumerable[list[T]]":
        if size <= 1:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_3(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError(None)

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_4(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("XXsize must be greater than zeroXX")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_5(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("SIZE MUST BE GREATER THAN ZERO")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_6(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = None
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_7(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(None)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_8(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) != size:
                    yield chunk
                    chunk = []

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_9(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = None

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁarray_chunks__mutmut_10(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk: list[T] = []
            for item in self:
                chunk.append(item)
                if len(chunk) == size:
                    yield chunk
                    chunk = []

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut)
    def map_windows[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_orig[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_1[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size < 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_2[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 1:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_3[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError(None)

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_4[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("XXsize must be greater than zeroXX")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_5[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("SIZE MUST BE GREATER THAN ZERO")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_6[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = None
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_7[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(None)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_8[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) >= size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_9[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[1]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_10[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) != size:
                    yield callback(tuple(window))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_11[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(None)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_12[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(None))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁmap_windows__mutmut_13[V](
        self, size: int, callback: Callable[[Sequence[T]], V]
    ) -> "Enumerable[V]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[V]:
            window: list[T] = []
            for item in self:
                window.append(item)
                if len(window) > size:
                    del window[0]
                if len(window) == size:
                    yield callback(tuple(window))

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁfor_each__mutmut)
    def for_each(self, callback: Callable[[T], object]) -> None:
        for item in self:
            callback(item)

    def xǁIteratorParityEnumerableǁfor_each__mutmut_orig(self, callback: Callable[[T], object]) -> None:
        for item in self:
            callback(item)

    def xǁIteratorParityEnumerableǁfor_each__mutmut_1(self, callback: Callable[[T], object]) -> None:
        for item in self:
            callback(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁcollect_into__mutmut)
    def collect_into(self, collection: Extendable[T]) -> Extendable[T]:
        collection.extend(self)
        return collection

    def xǁIteratorParityEnumerableǁcollect_into__mutmut_orig(self, collection: Extendable[T]) -> Extendable[T]:
        collection.extend(self)
        return collection

    def xǁIteratorParityEnumerableǁcollect_into__mutmut_1(self, collection: Extendable[T]) -> Extendable[T]:
        collection.extend(None)
        return collection

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁunzip__mutmut)
    def unzip[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = []
        right: list[B] = []
        for first, second in self:
            left.append(first)
            right.append(second)
        return left, right

    def xǁIteratorParityEnumerableǁunzip__mutmut_orig[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = []
        right: list[B] = []
        for first, second in self:
            left.append(first)
            right.append(second)
        return left, right

    def xǁIteratorParityEnumerableǁunzip__mutmut_1[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = None
        right: list[B] = []
        for first, second in self:
            left.append(first)
            right.append(second)
        return left, right

    def xǁIteratorParityEnumerableǁunzip__mutmut_2[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = []
        right: list[B] = None
        for first, second in self:
            left.append(first)
            right.append(second)
        return left, right

    def xǁIteratorParityEnumerableǁunzip__mutmut_3[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = []
        right: list[B] = []
        for first, second in self:
            left.append(None)
            right.append(second)
        return left, right

    def xǁIteratorParityEnumerableǁunzip__mutmut_4[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = []
        right: list[B] = []
        for first, second in self:
            left.append(first)
            right.append(None)
        return left, right

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁpartition__mutmut)
    def partition(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if predicate(item) else not_matching).append(item)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_orig(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if predicate(item) else not_matching).append(item)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_1(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = None
        not_matching: list[T] = []
        for item in self:
            (matching if predicate(item) else not_matching).append(item)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_2(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = None
        for item in self:
            (matching if predicate(item) else not_matching).append(item)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_3(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if predicate(item) else not_matching).append(None)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_4(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if (predicate(item)) and False else not_matching).append(item)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_5(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if (predicate(item)) or True else not_matching).append(item)
        return matching, not_matching

    def xǁIteratorParityEnumerableǁpartition__mutmut_6(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if predicate(None) else not_matching).append(item)
        return matching, not_matching

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut)
    def is_partitioned(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_orig(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_1(self, predicate: Callable[[T], bool]) -> bool:
        found_false = None
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_2(self, predicate: Callable[[T], bool]) -> bool:
        found_false = True
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_3(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = None
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_4(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(None)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_5(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches or found_false:
                return False
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_6(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return True
            if not matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_7(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if matches:
                found_false = True
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_8(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = None
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_9(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = False
        return True

    def xǁIteratorParityEnumerableǁis_partitioned__mutmut_10(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return False

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁposition__mutmut)
    def position(self, predicate: Callable[[T], bool]) -> Option[int]:
        for index, item in enumerate(self):
            if predicate(item):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁposition__mutmut_orig(self, predicate: Callable[[T], bool]) -> Option[int]:
        for index, item in enumerate(self):
            if predicate(item):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁposition__mutmut_1(self, predicate: Callable[[T], bool]) -> Option[int]:
        for index, item in enumerate(None):
            if predicate(item):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁposition__mutmut_2(self, predicate: Callable[[T], bool]) -> Option[int]:
        for index, item in enumerate(self):
            if predicate(None):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁposition__mutmut_3(self, predicate: Callable[[T], bool]) -> Option[int]:
        for index, item in enumerate(self):
            if predicate(item):
                return Some(None)
        return Null

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁrposition__mutmut)
    def rposition(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_orig(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_1(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = None
        for index in range(len(items) - 1, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_2(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(None)
        for index in range(len(items) - 1, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_3(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(None, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_4(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, None, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_5(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, None):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_6(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(-1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_7(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_8(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, ):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_9(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) + 1, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_10(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 2, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_11(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, +1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_12(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -2, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_13(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, +1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_14(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, -2):
            if predicate(items[index]):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_15(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, -1):
            if predicate(None):
                return Some(index)
        return Null

    def xǁIteratorParityEnumerableǁrposition__mutmut_16(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, -1):
            if predicate(items[index]):
                return Some(None)
        return Null

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut)
    def min_by_key[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=False)

    def xǁIteratorParityEnumerableǁmin_by_key__mutmut_orig[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=False)

    def xǁIteratorParityEnumerableǁmin_by_key__mutmut_1[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(None, reverse=False)

    def xǁIteratorParityEnumerableǁmin_by_key__mutmut_2[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=None)

    def xǁIteratorParityEnumerableǁmin_by_key__mutmut_3[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(reverse=False)

    def xǁIteratorParityEnumerableǁmin_by_key__mutmut_4[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, )

    def xǁIteratorParityEnumerableǁmin_by_key__mutmut_5[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=True)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut)
    def max_by_key[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=True)

    def xǁIteratorParityEnumerableǁmax_by_key__mutmut_orig[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=True)

    def xǁIteratorParityEnumerableǁmax_by_key__mutmut_1[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(None, reverse=True)

    def xǁIteratorParityEnumerableǁmax_by_key__mutmut_2[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=None)

    def xǁIteratorParityEnumerableǁmax_by_key__mutmut_3[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(reverse=True)

    def xǁIteratorParityEnumerableǁmax_by_key__mutmut_4[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, )

    def xǁIteratorParityEnumerableǁmax_by_key__mutmut_5[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=False)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut)
    def _extreme_by_key(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_orig(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_1(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = None
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_2(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(None)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_3(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = None
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_4(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(None, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_5(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, None)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_6(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_7(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, )
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_8(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is not MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_9(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = None
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_10(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(None, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_11(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, None)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_12(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_13(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, )
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_14(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = None
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_15(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(None)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_16(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = None
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_17(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(None)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_18(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = None
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_19(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if (reverse) and False else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_20(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if (reverse) or True else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_21(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key >= best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_22(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key <= best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_23(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = None
                best_key = item_key
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_24(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = None
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_25(self, key: Callable[[T], Any], *, reverse: bool) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        best_key = key(best_item)
        for item in iterator:
            item_key = key(item)
            better = item_key > best_key if reverse else item_key < best_key
            if better:
                best_item = item
                best_key = item_key
        return Some(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁmin_by__mutmut)
    def min_by(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=False)

    def xǁIteratorParityEnumerableǁmin_by__mutmut_orig(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=False)

    def xǁIteratorParityEnumerableǁmin_by__mutmut_1(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(None, reverse=False)

    def xǁIteratorParityEnumerableǁmin_by__mutmut_2(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=None)

    def xǁIteratorParityEnumerableǁmin_by__mutmut_3(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(reverse=False)

    def xǁIteratorParityEnumerableǁmin_by__mutmut_4(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, )

    def xǁIteratorParityEnumerableǁmin_by__mutmut_5(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=True)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁmax_by__mutmut)
    def max_by(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=True)

    def xǁIteratorParityEnumerableǁmax_by__mutmut_orig(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=True)

    def xǁIteratorParityEnumerableǁmax_by__mutmut_1(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(None, reverse=True)

    def xǁIteratorParityEnumerableǁmax_by__mutmut_2(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=None)

    def xǁIteratorParityEnumerableǁmax_by__mutmut_3(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(reverse=True)

    def xǁIteratorParityEnumerableǁmax_by__mutmut_4(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, )

    def xǁIteratorParityEnumerableǁmax_by__mutmut_5(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=False)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut)
    def _extreme_by(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_orig(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_1(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = None
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_2(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(None)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_3(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = None
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_4(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(None, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_5(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, None)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_6(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_7(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, )
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_8(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is not MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_9(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = None
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_10(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(None, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_11(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, None)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_12(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_13(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, )
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_14(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = None
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_15(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(None, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_16(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, None)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_17(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_18(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, )
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_19(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if (reverse) and False else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_20(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if (reverse) or True else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_21(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result >= 0) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_22(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 1) if reverse else (result < 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_23(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result <= 0):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_24(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 1):
                best_item = item
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_25(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = None
        return Some(best_item)

    def xǁIteratorParityEnumerableǁ_extreme_by__mutmut_26(
        self, compare: Callable[[T, T], int], *, reverse: bool
    ) -> Option[T]:
        iterator = iter(self)
        best = next(iterator, MISSING)
        if best is MISSING:
            return Null
        best_item = cast(T, best)
        for item in iterator:
            result = compare(item, best_item)
            if (result > 0) if reverse else (result < 0):
                best_item = item
        return Some(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁproduct__mutmut)
    def product(self) -> Any:
        result: Any = 1
        for item in self:
            result *= item
        return result

    def xǁIteratorParityEnumerableǁproduct__mutmut_orig(self) -> Any:
        result: Any = 1
        for item in self:
            result *= item
        return result

    def xǁIteratorParityEnumerableǁproduct__mutmut_1(self) -> Any:
        result: Any = None
        for item in self:
            result *= item
        return result

    def xǁIteratorParityEnumerableǁproduct__mutmut_2(self) -> Any:
        result: Any = 2
        for item in self:
            result *= item
        return result

    def xǁIteratorParityEnumerableǁproduct__mutmut_3(self) -> Any:
        result: Any = 1
        for item in self:
            result = item
        return result

    def xǁIteratorParityEnumerableǁproduct__mutmut_4(self) -> Any:
        result: Any = 1
        for item in self:
            result /= item
        return result

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁcmp__mutmut)
    def cmp(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_orig(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_1(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(None, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_2(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(other, None)

    def xǁIteratorParityEnumerableǁcmp__mutmut_3(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(_compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_4(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(other, )

    def xǁIteratorParityEnumerableǁcmp__mutmut_5(self, other: Iterable[T]) -> Ordering:
        return cast(None, self).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_6(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", None).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_7(self, other: Iterable[T]) -> Ordering:
        return cast(self).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_8(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", ).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_9(self, other: Iterable[T]) -> Ordering:
        return cast("XXEnumerable[T]XX", self).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_10(self, other: Iterable[T]) -> Ordering:
        return cast("enumerable[t]", self).cmp_by(other, _compare)

    def xǁIteratorParityEnumerableǁcmp__mutmut_11(self, other: Iterable[T]) -> Ordering:
        return cast("ENUMERABLE[T]", self).cmp_by(other, _compare)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut)
    def cmp_by[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_orig[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_1[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(None, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_2[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, None, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_3[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=None):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_4[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_5[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_6[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, ):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_7[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is not MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_8[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is not MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_9[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = None
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_10[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(None)
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_11[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(None, cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_12[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), None))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_13[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_14[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), ))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_15[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(None, left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_16[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, None), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_17[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(left), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_18[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, ), cast(U, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_19[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(None, right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_20[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, None)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_21[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(right)))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_22[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, )))
            if ordering is not Ordering.Equal:
                return ordering
        return Ordering.Equal

    def xǁIteratorParityEnumerableǁcmp_by__mutmut_23[U](self, other: Iterable[U], compare: Callable[[T, U], int]) -> Ordering:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Ordering.Less
            if right is MISSING:
                return Ordering.Greater
            ordering = _ordering(compare(cast(T, left), cast(U, right)))
            if ordering is Ordering.Equal:
                return ordering
        return Ordering.Equal

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut)
    def partial_cmp[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_orig[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_1[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(None)
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_2[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(None, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_3[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, None))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_4[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_5[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, ))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_6[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(None, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_7[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, None)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_8[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_9[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, )

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_10[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast(None, self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_11[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", None).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_12[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast(self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_13[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", ).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_14[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("XXEnumerable[T]XX", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_15[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("enumerable[t]", self).partial_cmp_by(other, compare)

    def xǁIteratorParityEnumerableǁpartial_cmp__mutmut_16[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("ENUMERABLE[T]", self).partial_cmp_by(other, compare)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut)
    def partial_cmp_by[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_orig[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_1[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(None, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_2[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, None, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_3[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=None):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_4[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_5[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_6[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, ):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_7[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is not MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_8[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(None)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_9[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is not MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_10[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(None)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_11[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = None
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_12[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(None, cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_13[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), None)
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_14[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_15[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), )
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_16[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(None, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_17[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, None), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_18[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_19[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, ), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_20[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(None, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_21[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, None))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_22[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_23[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, ))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_24[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is not None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_25[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = None
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_26[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(None)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_27[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is Ordering.Equal:
                return Some(ordering)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_28[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(None)
        return Some(Ordering.Equal)

    def xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_29[U](
        self, other: Iterable[U], compare: Callable[[T, U], int | None]
    ) -> Option[Ordering]:
        for left, right in itertools.zip_longest(self, other, fillvalue=MISSING):
            if left is MISSING:
                return Some(Ordering.Less)
            if right is MISSING:
                return Some(Ordering.Greater)
            result = compare(cast(T, left), cast(U, right))
            if result is None:
                return Null
            ordering = _ordering(result)
            if ordering is not Ordering.Equal:
                return Some(ordering)
        return Some(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁeq_by__mutmut)
    def eq_by[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_orig[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_1[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(None, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_2[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(other, comparer=None)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_3[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_4[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(other, )

    def xǁIteratorParityEnumerableǁeq_by__mutmut_5[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast(None, self).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_6[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", None).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_7[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast(self).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_8[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", ).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_9[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("XXEnumerable[T]XX", self).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_10[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("enumerable[t]", self).eq(other, comparer=comparer)

    def xǁIteratorParityEnumerableǁeq_by__mutmut_11[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("ENUMERABLE[T]", self).eq(other, comparer=comparer)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁlt__mutmut)
    def lt(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Less

    def xǁIteratorParityEnumerableǁlt__mutmut_orig(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Less

    def xǁIteratorParityEnumerableǁlt__mutmut_1(self, other: Iterable[T]) -> bool:
        return self.cmp(None) is Ordering.Less

    def xǁIteratorParityEnumerableǁlt__mutmut_2(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Less

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁle__mutmut)
    def le(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Greater

    def xǁIteratorParityEnumerableǁle__mutmut_orig(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Greater

    def xǁIteratorParityEnumerableǁle__mutmut_1(self, other: Iterable[T]) -> bool:
        return self.cmp(None) is not Ordering.Greater

    def xǁIteratorParityEnumerableǁle__mutmut_2(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Greater

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁgt__mutmut)
    def gt(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Greater

    def xǁIteratorParityEnumerableǁgt__mutmut_orig(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Greater

    def xǁIteratorParityEnumerableǁgt__mutmut_1(self, other: Iterable[T]) -> bool:
        return self.cmp(None) is Ordering.Greater

    def xǁIteratorParityEnumerableǁgt__mutmut_2(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Greater

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁge__mutmut)
    def ge(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Less

    def xǁIteratorParityEnumerableǁge__mutmut_orig(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Less

    def xǁIteratorParityEnumerableǁge__mutmut_1(self, other: Iterable[T]) -> bool:
        return self.cmp(None) is not Ordering.Less

    def xǁIteratorParityEnumerableǁge__mutmut_2(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Less

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁis_sorted__mutmut)
    def is_sorted(self) -> bool:
        return self.is_sorted_by_key(lambda item: item)

    def xǁIteratorParityEnumerableǁis_sorted__mutmut_orig(self) -> bool:
        return self.is_sorted_by_key(lambda item: item)

    def xǁIteratorParityEnumerableǁis_sorted__mutmut_1(self) -> bool:
        return self.is_sorted_by_key(None)

    def xǁIteratorParityEnumerableǁis_sorted__mutmut_2(self) -> bool:
        return self.is_sorted_by_key(lambda item: None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut)
    def is_sorted_by(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_orig(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_1(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = None
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_2(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(None)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_3(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = None
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_4(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(None, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_5(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, None)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_6(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_7(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, )
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_8(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is not MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_9(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return False
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_10(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = None
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_11(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(None, item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_12(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), None)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_13(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_14(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), )
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_15(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(None, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_16(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, None), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_17(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_18(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, ), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_19(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None and ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_20(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is not None or ordering > 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_21(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering >= 0:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_22(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 1:
                return False
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_23(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return True
            previous = item
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_24(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = None
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by__mutmut_25(self, compare: Callable[[T, T], int | None]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        for item in iterator:
            ordering = compare(cast(T, previous), item)
            if ordering is None or ordering > 0:
                return False
            previous = item
        return False

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut)
    def is_sorted_by_key(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_orig(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_1(self, key: Callable[[T], Any]) -> bool:
        iterator = None
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_2(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(None)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_3(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = None
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_4(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(None, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_5(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, None)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_6(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_7(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, )
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_8(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is not MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_9(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return False
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_10(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = None
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_11(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(None)
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_12(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(None, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_13(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, None))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_14(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_15(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, ))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_16(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = None
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_17(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(None)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_18(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key <= previous_key:
                return False
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_19(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return True
            previous_key = item_key
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_20(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = None
        return True

    def xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_21(self, key: Callable[[T], Any]) -> bool:
        iterator = iter(self)
        previous = next(iterator, MISSING)
        if previous is MISSING:
            return True
        previous_key = key(cast(T, previous))
        for item in iterator:
            item_key = key(item)
            if item_key < previous_key:
                return False
            previous_key = item_key
        return False

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut)
    def distinct_by[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_orig[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_1[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = None
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_2[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = None
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_3[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_4[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_5[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_6[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_7[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_8[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = None
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_9[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(None)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_10[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_11[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(None):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_12[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(None, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_13[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, None) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_14[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_15[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, ) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_16[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(None)
                    yield item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁdistinct_by__mutmut_17[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            seen: list[K] = []
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            for item in self:
                item_key = key(item)
                if not any(equal(item_key, old_key) for old_key in seen):
                    seen.append(item_key)
                    yield item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁunion__mutmut)
    def union(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_orig(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_1(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            None,
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_2(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode=None,
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_3(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_4(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_5(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=None,
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_6(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_7(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_8(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_9(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_10(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            )

    def xǁIteratorParityEnumerableǁunion__mutmut_11(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(None, other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_12(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], None),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_13(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_14(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], ),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_15(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="XXunionXX",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_16(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="UNION",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_17(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_18(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_19(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_20(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, None),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_21(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(comparer),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_22(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, ),
        )

    def xǁIteratorParityEnumerableǁunion__mutmut_23(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] & None, comparer),
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁexcept___mutmut)
    def except_(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_orig(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_1(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            None,
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_2(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode=None,
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_3(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_4(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_5(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=None,
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_6(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_7(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_8(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_9(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_10(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            )

    def xǁIteratorParityEnumerableǁexcept___mutmut_11(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(None, other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_12(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], None),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_13(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_14(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], ),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_15(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="XXexceptXX",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_16(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="EXCEPT",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_17(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_18(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_19(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_20(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, None),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_21(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(comparer),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_22(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, ),
        )

    def xǁIteratorParityEnumerableǁexcept___mutmut_23(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] & None, comparer),
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁintersect__mutmut)
    def intersect(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_orig(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_1(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            None,
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_2(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode=None,
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_3(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_4(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_5(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=None,
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_6(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_7(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_8(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_9(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_10(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            )

    def xǁIteratorParityEnumerableǁintersect__mutmut_11(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(None, other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_12(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], None),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_13(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_14(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], ),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_15(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="XXintersectXX",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_16(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="INTERSECT",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_17(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_18(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_19(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_20(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, None),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_21(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(comparer),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_22(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, ),
        )

    def xǁIteratorParityEnumerableǁintersect__mutmut_23(
        self,
        other: Iterable[T],
        comparer: Callable[[T, T], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect",
            left_key=lambda item: item,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] & None, comparer),
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁunion_by__mutmut)
    def union_by[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_orig[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_1[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            None,
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_2[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode=None,
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_3[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=None,
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_4[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_5[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=None,
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_6[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_7[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_8[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_9[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_10[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_11[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(None, other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_12[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], None),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_13[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_14[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], ),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_15[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="XXunionXX",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_16[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="UNION",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_17[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(None, key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_18[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], None),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_19[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_20[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], ),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_21[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(None, key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_22[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], None),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_23[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_24[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], ),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_25[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(None, comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_26[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, None),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_27[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(comparer),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_28[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] | None, ),
        )

    def xǁIteratorParityEnumerableǁunion_by__mutmut_29[K](
        self,
        other: Iterable[T],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="union",
            left_key=cast(Callable[[T], object], key),
            right_key=cast(Callable[[object], object], key),
            comparer=cast(Callable[[object, object], bool] & None, comparer),
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut)
    def except_by[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_orig[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_1[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            None,
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_2[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode=None,
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_3[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_4[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_5[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=None,
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_6[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_7[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_8[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_9[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_10[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_11[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(None, other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_12[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], None),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_13[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_14[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], ),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_15[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="XXexcept_byXX",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_16[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="EXCEPT_BY",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_17[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(None, key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_18[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], None),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_19[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_20[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], ),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_21[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_22[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(None, comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_23[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, None),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_24[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(comparer),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_25[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, ),
        )

    def xǁIteratorParityEnumerableǁexcept_by__mutmut_26[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="except_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] & None, comparer),
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut)
    def intersect_by[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_orig[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_1[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            None,
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_2[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode=None,
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_3[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=None,
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_4[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_5[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=None,
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_6[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_7[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_8[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_9[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_10[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_11[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(None, other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_12[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], None),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_13[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_14[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], ),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_15[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="XXintersect_byXX",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_16[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="INTERSECT_BY",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_17[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(None, key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_18[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], None),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_19[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_20[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], ),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_21[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: None,
            comparer=cast(Callable[[object, object], bool] | None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_22[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(None, comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_23[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, None),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_24[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(comparer),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_25[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] | None, ),
        )

    def xǁIteratorParityEnumerableǁintersect_by__mutmut_26[K](
        self,
        other: Iterable[K],
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[T]":
        return self._set_operation(
            cast(Iterable[object], other),
            mode="intersect_by",
            left_key=cast(Callable[[T], object], key),
            right_key=lambda item: item,
            comparer=cast(Callable[[object, object], bool] & None, comparer),
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut)
    def _set_operation(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_orig(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_1(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = None
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_2(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_3(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_4(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_5(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_6(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_7(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = None
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_8(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if (mode != "union") and False else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_9(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if (mode != "union") or True else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_10(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(None) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_11(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode == "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_12(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "XXunionXX" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_13(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "UNION" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_14(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = None
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_15(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(None) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_16(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = None

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_17(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = None
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_18(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(None)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_19(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(None, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_20(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, None) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_21(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_22(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, ) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_23(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = None
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_24(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    None
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_25(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(None, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_26(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, None) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_27(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_28(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, ) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_29(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(None)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_30(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other) and (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_31(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union" and (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_32(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode != "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_33(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "XXunionXX"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_34(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "UNION"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_35(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") or not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_36(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode not in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_37(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("XXexceptXX", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_38(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("EXCEPT", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_39(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "XXexcept_byXX") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_40(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "EXCEPT_BY") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_41(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_42(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") or present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_43(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode not in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_44(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("XXintersectXX", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_45(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("INTERSECT", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_46(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "XXintersect_byXX") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_47(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "INTERSECT_BY") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_48(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(None, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_49(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, None)
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_50(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_51(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, )
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_52(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(None))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_53(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode != "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_54(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "XXunionXX":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_55(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "UNION":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_56(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(None, right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_57(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), None)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_58(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_59(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), )

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_60(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(None, other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_61(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, None), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_62(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(other_item), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_63(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, ), right_key(other_item))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_64(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(None))

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁ_set_operation__mutmut_65(
        self,
        other: Iterable[object],
        *,
        mode: str,
        left_key: Callable[[T], object],
        right_key: Callable[[object], object],
        comparer: Callable[[object, object], bool] | None = None,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            equal: Callable[[object, object], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            other_values = list(other) if mode != "union" else []
            other_keys = [right_key(value) for value in other_values]
            seen: list[object] = []

            def emit(item: T, item_key: object) -> Iterator[T]:
                already_seen = any(equal(item_key, old_key) for old_key in seen)
                present_other = any(
                    equal(item_key, other_key) for other_key in other_keys
                )
                if already_seen:
                    return
                seen.append(item_key)
                if (
                    mode == "union"
                    or (mode in ("except", "except_by") and not present_other)
                    or (mode in ("intersect", "intersect_by") and present_other)
                ):
                    yield item

            for item in self:
                yield from emit(item, left_key(item))
            if mode == "union":
                for other_item in other:
                    yield from emit(cast(T, other_item), right_key(other_item))

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁcount_by__mutmut)
    def count_by[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_orig[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_1[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = None
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_2[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = None
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_3[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(None)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_4[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(None):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_5[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = None
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_6[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if (comparer is not None) and False
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_7[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if (comparer is not None) or True
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_8[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(None, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_9[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, None)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_10[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_11[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, )
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_12[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_13[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key != old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_14[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = None
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_15[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count - 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_16[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 2)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_17[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        return
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_18[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append(None)
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_19[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 2))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁcount_by__mutmut_20[K](
        self,
        key: Callable[[T], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, int]]":
        def inner() -> Iterator[tuple[K, int]]:
            groups: list[tuple[K, int]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, count) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, count + 1)
                        break
                else:
                    groups.append((item_key, 1))
            yield from groups

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut)
    def aggregate_by[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_orig[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_1[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = None
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_2[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = None
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_3[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(None)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_4[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(None):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_5[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = None
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_6[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if (comparer is not None) and False
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_7[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if (comparer is not None) or True
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_8[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(None, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_9[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, None)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_10[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_11[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, )
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_12[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_13[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key != old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_14[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = None
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_15[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(None, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_16[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, None))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_17[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_18[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, ))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_19[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        return
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_20[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append(None)
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_21[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(None, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_22[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, None)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_23[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_24[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, )))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by__mutmut_25[K, A](
        self,
        key: Callable[[T], K],
        seed: A,
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed, item)))
            yield from groups

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut)
    def aggregate_by_seed_selector[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_orig[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_1[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = None
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_2[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = None
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_3[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(None)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_4[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(None):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_5[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = None
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_6[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if (comparer is not None) and False
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_7[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if (comparer is not None) or True
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_8[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(None, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_9[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, None)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_10[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_11[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, )
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_12[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_13[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key != old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_14[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = None
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_15[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(None, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_16[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, None))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_17[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_18[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, ))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_19[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        return
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_20[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append(None)
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_21[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(None, item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_22[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), None)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_23[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_24[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), )))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_25[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(None), item)))
            yield from groups

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_26[K, A](
        self,
        key: Callable[[T], K],
        seed_selector: Callable[[K], A],
        aggregator: Callable[[A, T], A],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, A]]":
        def inner() -> Iterator[tuple[K, A]]:
            groups: list[tuple[K, A]] = []
            for item in self:
                item_key = key(item)
                for index, (old_key, acc) in enumerate(groups):
                    same = (
                        comparer(item_key, old_key)
                        if comparer is not None
                        else item_key == old_key
                    )
                    if same:
                        groups[index] = (old_key, aggregator(acc, item))
                        break
                else:
                    groups.append((item_key, aggregator(seed_selector(item_key), item)))
            yield from groups

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁorder__mutmut)
    def order(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_orig(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_1(self, *, reverse: bool = True) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_2(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=None)

    def xǁIteratorParityEnumerableǁorder__mutmut_3(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast(None, self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_4(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("Enumerable[T]", None).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_5(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast(self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_6(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("Enumerable[T]", ).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_7(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("XXEnumerable[T]XX", self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_8(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("enumerable[t]", self).order_by(reverse=reverse)

    def xǁIteratorParityEnumerableǁorder__mutmut_9(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("ENUMERABLE[T]", self).order_by(reverse=reverse)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut)
    def order_descending(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_orig(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_1(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=None)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_2(self) -> "Enumerable[T]":
        return cast(None, self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_3(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", None).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_4(self) -> "Enumerable[T]":
        return cast(self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_5(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", ).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_6(self) -> "Enumerable[T]":
        return cast("XXEnumerable[T]XX", self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_7(self) -> "Enumerable[T]":
        return cast("enumerable[t]", self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_8(self) -> "Enumerable[T]":
        return cast("ENUMERABLE[T]", self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_descending__mutmut_9(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=False)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut)
    def order_by_descending[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_orig[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_1[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=None, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_2[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=key, reverse=None)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_3[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_4[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=key, )

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_5[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast(None, self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_6[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", None).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_7[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast(self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_8[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", ).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_9[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("XXEnumerable[T]XX", self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_10[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("enumerable[t]", self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_11[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("ENUMERABLE[T]", self).order_by(key=key, reverse=True)

    def xǁIteratorParityEnumerableǁorder_by_descending__mutmut_12[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=key, reverse=False)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁthen_by__mutmut)
    def then_by[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=False)

    def xǁIteratorParityEnumerableǁthen_by__mutmut_orig[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=False)

    def xǁIteratorParityEnumerableǁthen_by__mutmut_1[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(None, reverse=False)

    def xǁIteratorParityEnumerableǁthen_by__mutmut_2[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=None)

    def xǁIteratorParityEnumerableǁthen_by__mutmut_3[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(reverse=False)

    def xǁIteratorParityEnumerableǁthen_by__mutmut_4[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, )

    def xǁIteratorParityEnumerableǁthen_by__mutmut_5[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=True)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut)
    def then_by_descending[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=True)

    def xǁIteratorParityEnumerableǁthen_by_descending__mutmut_orig[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=True)

    def xǁIteratorParityEnumerableǁthen_by_descending__mutmut_1[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(None, reverse=True)

    def xǁIteratorParityEnumerableǁthen_by_descending__mutmut_2[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=None)

    def xǁIteratorParityEnumerableǁthen_by_descending__mutmut_3[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(reverse=True)

    def xǁIteratorParityEnumerableǁthen_by_descending__mutmut_4[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, )

    def xǁIteratorParityEnumerableǁthen_by_descending__mutmut_5[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=False)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut)
    def _then_by(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_orig(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_1(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_2(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(None, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_3(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, None):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_4(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr("_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_5(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, ):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_6(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "XX_ordering_keysXX"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_7(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ORDERING_KEYS"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_8(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError(None)
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_9(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("XXthen_by requires a sequence produced by order_byXX")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_10(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("THEN_BY REQUIRES A SEQUENCE PRODUCED BY ORDER_BY")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_11(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = None
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_12(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(None, getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_13(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], None)
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_14(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_15(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], )
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_16(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(None, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_17(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, None))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_18(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr("_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_19(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, ))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_20(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "XX_ordered_sourceXX"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_21(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ORDERED_SOURCE"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_22(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = None
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_23(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            None,
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_24(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            None,
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_25(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_26(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_27(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(None, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_28(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, None),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_29(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr("_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_30(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, ),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_31(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "XX_ordering_keysXX"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_32(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ORDERING_KEYS"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_33(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = None

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_34(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys - ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_35(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = None
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_36(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(None)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_37(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(None):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_38(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=None, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_39(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=None)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_40(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_41(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, )
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_42(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = None
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_43(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(None)
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_44(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(None, "_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_45(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, None, source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_46(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", None)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_47(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr("_ordered_source", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_48(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_49(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", )
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_50(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "XX_ordered_sourceXX", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_51(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ORDERED_SOURCE", source)
        setattr(result, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_52(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(None, "_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_53(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, None, ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_54(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", None)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_55(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr("_ordering_keys", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_56(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_57(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ordering_keys", )
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_58(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "XX_ordering_keysXX", ordering_keys)
        return result

    def xǁIteratorParityEnumerableǁ_then_by__mutmut_59(self, key: Callable[[T], Any], *, reverse: bool) -> "Enumerable[T]":
        if not hasattr(self, "_ordering_keys"):
            raise TypeError("then_by requires a sequence produced by order_by")
        source = cast(Iterable[T], getattr(self, "_ordered_source"))
        existing_keys = cast(
            tuple[tuple[Callable[[T], Any], bool], ...],
            getattr(self, "_ordering_keys"),
        )
        ordering_keys = existing_keys + ((key, reverse),)

        def inner() -> Iterator[T]:
            items = list(source)
            for selector, descending in reversed(ordering_keys):
                items.sort(key=selector, reverse=descending)
            yield from items

        result = Enumerable(inner())
        setattr(result, "_ordered_source", source)
        setattr(result, "_ORDERING_KEYS", ordering_keys)
        return result

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁshuffle__mutmut)
    def shuffle(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = list(self)
            shuffle(items)
            yield from items

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁshuffle__mutmut_orig(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = list(self)
            shuffle(items)
            yield from items

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁshuffle__mutmut_1(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = None
            shuffle(items)
            yield from items

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁshuffle__mutmut_2(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = list(None)
            shuffle(items)
            yield from items

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁshuffle__mutmut_3(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = list(self)
            shuffle(None)
            yield from items

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁshuffle__mutmut_4(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = list(self)
            shuffle(items)
            yield from items

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁof_type__mutmut)
    def of_type[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_orig[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_1[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(None)
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_2[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(None)
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_3[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast(None, self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_4[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", None)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_5[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast(self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_6[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", )
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_7[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("XXEnumerable[T]XX", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_8[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("enumerable[t]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_9[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("ENUMERABLE[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_10[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: None)
            .map(lambda item: cast(U, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_11[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: None)
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_12[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(None, item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_13[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, None))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_14[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(item))
        )

    def xǁIteratorParityEnumerableǁof_type__mutmut_15[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, ))
        )

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁto_array__mutmut)
    def to_array(self) -> list[T]:
        return cast("Enumerable[T]", self).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_orig(self) -> list[T]:
        return cast("Enumerable[T]", self).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_1(self) -> list[T]:
        return cast(None, self).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_2(self) -> list[T]:
        return cast("Enumerable[T]", None).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_3(self) -> list[T]:
        return cast(self).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_4(self) -> list[T]:
        return cast("Enumerable[T]", ).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_5(self) -> list[T]:
        return cast("XXEnumerable[T]XX", self).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_6(self) -> list[T]:
        return cast("enumerable[t]", self).to_list()

    def xǁIteratorParityEnumerableǁto_array__mutmut_7(self) -> list[T]:
        return cast("ENUMERABLE[T]", self).to_list()

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁto_hashset__mutmut)
    def to_hashset(self) -> set[T]:
        return set(self)

    def xǁIteratorParityEnumerableǁto_hashset__mutmut_orig(self) -> set[T]:
        return set(self)

    def xǁIteratorParityEnumerableǁto_hashset__mutmut_1(self) -> set[T]:
        return set(None)

    @overload
    def to_dictionary[K: Hashable](
        self, key_selector: Callable[[T], K]
    ) -> dict[K, T]: ...

    @overload
    def to_dictionary[K: Hashable, V](
        self, key_selector: Callable[[T], K], element_selector: Callable[[T], V]
    ) -> dict[K, V]: ...

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut)
    def to_dictionary[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_orig[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_1[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = None
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_2[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = None
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_3[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(None)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_4[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key not in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_5[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(None)
            result[item_key] = (
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_6[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = None
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_7[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if (element_selector is not None) and False else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_8[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if (element_selector is not None) or True else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_9[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(None) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_dictionary__mutmut_10[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, Any]:
        result: dict[K, Any] = {}
        for item in self:
            item_key = key_selector(item)
            if item_key in result:
                raise ValueError(f"duplicate key: {item_key!r}")
            result[item_key] = (
                element_selector(item) if element_selector is None else item
            )
        return result

    @overload
    def to_lookup[K: Hashable](
        self, key_selector: Callable[[T], K]
    ) -> dict[K, list[T]]: ...

    @overload
    def to_lookup[K: Hashable, V](
        self, key_selector: Callable[[T], K], element_selector: Callable[[T], V]
    ) -> dict[K, list[V]]: ...

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut)
    def to_lookup[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_orig[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_1[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = None
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_2[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = None
            result.setdefault(item_key, []).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_3[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(None)
            result.setdefault(item_key, []).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_4[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                None
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_5[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(None, []).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_6[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, None).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_7[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault([]).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_8[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, ).append(
                element_selector(item) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_9[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(item) if (element_selector is not None) and False else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_10[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(item) if (element_selector is not None) or True else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_11[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(None) if element_selector is not None else item
            )
        return result

    def xǁIteratorParityEnumerableǁto_lookup__mutmut_12[K: Hashable, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
    ) -> dict[K, list[Any]]:
        result: dict[K, list[Any]] = {}
        for item in self:
            item_key = key_selector(item)
            result.setdefault(item_key, []).append(
                element_selector(item) if element_selector is None else item
            )
        return result

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut)
    def join_on[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_orig[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_1[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = None
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_2[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_3[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_4[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_5[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_6[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_7[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = None
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_8[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(None)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_9[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = None
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_10[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(None)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_11[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(None, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_12[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, None):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_13[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_14[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, ):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_15[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(None)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_16[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(None, inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_17[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, None)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_18[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_19[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, )

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁjoin_on__mutmut_20[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, U], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                outer_value = outer_key(outer_item)
                for inner_item in inner_values:
                    if equal(outer_value, inner_key(inner_item)):
                        yield result_selector(outer_item, inner_item)

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut)
    def group_join[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_orig[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_1[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = None
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_2[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_3[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_4[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_5[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_6[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_7[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = None
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_8[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(None)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_9[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = None
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_10[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(None)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_11[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = None
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_12[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(None, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_13[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, None)
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_14[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_15[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, )
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_16[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(None))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_17[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(None, matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_18[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, None)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_19[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(matches)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_20[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, )

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁgroup_join__mutmut_21[U, K, V](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        result_selector: Callable[[T, list[U]], V],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[V]":
        def inner() -> Iterator[V]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                yield result_selector(outer_item, matches)

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁleft_join__mutmut)
    def left_join[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_orig[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_1[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = None
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_2[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_3[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_4[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_5[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_6[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_7[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = None
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_8[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(None)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_9[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = None
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_10[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(None)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_11[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = None
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_12[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(None, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_13[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, None)
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_14[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_15[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, )
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_16[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(None))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_17[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(None)
                else:
                    yield outer_item, Null

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁleft_join__mutmut_18[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[T, Option[U]]]":
        def inner() -> Iterator[tuple[T, Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            for outer_item in self:
                selected_key = outer_key(outer_item)
                matches = [
                    item
                    for item in inner_values
                    if equal(selected_key, inner_key(item))
                ]
                if matches:
                    for item in matches:
                        yield outer_item, Some(item)
                else:
                    yield outer_item, Null

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁright_join__mutmut)
    def right_join[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_orig[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_1[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = None
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_2[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_3[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_4[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_5[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_6[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_7[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = None
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_8[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(None)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_9[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = None
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_10[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(None)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_11[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = None
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_12[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(None, selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_13[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), None)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_14[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_15[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), )
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_16[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(None), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_17[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(None), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁright_join__mutmut_18[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], U]]":
        def inner() -> Iterator[tuple[Option[T], U]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            outer_values = list(self)
            for inner_item in other:
                selected_key = inner_key(inner_item)
                matches = [
                    item
                    for item in outer_values
                    if equal(outer_key(item), selected_key)
                ]
                if matches:
                    for item in matches:
                        yield Some(item), inner_item
                else:
                    yield Null, inner_item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁfull_join__mutmut)
    def full_join[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_orig[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_1[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = None
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_2[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) and False else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_3[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if (comparer is not None) or True else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_4[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_5[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: None
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_6[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left != right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_7[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = None
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_8[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(None)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_9[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = None
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_10[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = None
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_11[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(None)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_12[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = None
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_13[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = True
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_14[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(None):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_15[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(None, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_16[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, None):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_17[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_18[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, ):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_19[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(None)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_20[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = None
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_21[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = False
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_22[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(None)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_23[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(None), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_24[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(None)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_25[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_26[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(None), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_27[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(None):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_28[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_29[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(None)

        return Enumerable(inner())

    def xǁIteratorParityEnumerableǁfull_join__mutmut_30[U, K](
        self,
        other: Iterable[U],
        outer_key: Callable[[T], K],
        inner_key: Callable[[U], K],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[Option[T], Option[U]]]":
        def inner() -> Iterator[tuple[Option[T], Option[U]]]:
            equal: Callable[[K, K], bool] = (
                comparer if comparer is not None else lambda left, right: left == right
            )
            inner_values = list(other)
            matched_inner: set[int] = set()
            for outer_item in self:
                selected_key = outer_key(outer_item)
                found = False
                for index, inner_item in enumerate(inner_values):
                    if equal(selected_key, inner_key(inner_item)):
                        found = True
                        matched_inner.add(index)
                        yield Some(outer_item), Some(inner_item)
                if not found:
                    yield Some(outer_item), Null
            for index, inner_item in enumerate(inner_values):
                if index not in matched_inner:
                    yield Null, Some(inner_item)

        return Enumerable(None)

    @overload
    def first_or_default(
        self, default: None = None, *, predicate: Callable[[T], bool] | None = None
    ) -> T | None: ...

    @overload
    def first_or_default[U](
        self, default: U, *, predicate: Callable[[T], bool] | None = None
    ) -> T | U: ...

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut)
    def first_or_default(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_orig(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_1(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(None, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_2(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(predicate, default=None)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_3(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_4(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(predicate, )

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_5(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast(None, self).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_6(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", None).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_7(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast(self).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_8(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", ).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_9(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("XXEnumerable[T]XX", self).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_10(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("enumerable[t]", self).first(predicate, default=default)

    def xǁIteratorParityEnumerableǁfirst_or_default__mutmut_11(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("ENUMERABLE[T]", self).first(predicate, default=default)

    @overload
    def last_or_default(
        self, default: None = None, *, predicate: Callable[[T], bool] | None = None
    ) -> T | None: ...

    @overload
    def last_or_default[U](
        self, default: U, *, predicate: Callable[[T], bool] | None = None
    ) -> T | U: ...

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut)
    def last_or_default(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_orig(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_1(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(None, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_2(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(predicate, default=None)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_3(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_4(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(predicate, )

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_5(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast(None, self).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_6(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", None).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_7(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast(self).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_8(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", ).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_9(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("XXEnumerable[T]XX", self).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_10(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("enumerable[t]", self).last(predicate, default=default)

    def xǁIteratorParityEnumerableǁlast_or_default__mutmut_11(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("ENUMERABLE[T]", self).last(predicate, default=default)

    @overload
    def single_or_default(
        self, default: None = None, *, predicate: Callable[[T], bool] | None = None
    ) -> T | None: ...

    @overload
    def single_or_default[U](
        self, default: U, *, predicate: Callable[[T], bool] | None = None
    ) -> T | U: ...

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut)
    def single_or_default(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_orig(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_1(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(None, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_2(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(predicate, default=None)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_3(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_4(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(predicate, )

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_5(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast(None, self).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_6(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", None).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_7(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast(self).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_8(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", ).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_9(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("XXEnumerable[T]XX", self).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_10(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("enumerable[t]", self).single(predicate, default=default)

    def xǁIteratorParityEnumerableǁsingle_or_default__mutmut_11(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("ENUMERABLE[T]", self).single(predicate, default=default)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁelement_at__mutmut)
    def element_at(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_orig(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_1(self, index: int) -> T:
        if index <= 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_2(self, index: int) -> T:
        if index < 1:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_3(self, index: int) -> T:
        if index < 0:
            items = None
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_4(self, index: int) -> T:
        if index < 0:
            items = cast(None, self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_5(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", None).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_6(self, index: int) -> T:
        if index < 0:
            items = cast(self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_7(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", ).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_8(self, index: int) -> T:
        if index < 0:
            items = cast("XXEnumerable[T]XX", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_9(self, index: int) -> T:
        if index < 0:
            items = cast("enumerable[t]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_10(self, index: int) -> T:
        if index < 0:
            items = cast("ENUMERABLE[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_11(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    None, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_12(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, None
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_13(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_14(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_15(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    +index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_16(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", self).nth(None)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_17(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast(None, self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_18(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", None).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_19(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast(self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_20(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("Enumerable[T]", ).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_21(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("XXEnumerable[T]XX", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_22(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("enumerable[t]", self).nth(index)

    def xǁIteratorParityEnumerableǁelement_at__mutmut_23(self, index: int) -> T:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            try:
                return items[index]
            except IndexError as error:
                from .take_enumerable import TakeEnumerableException

                raise TakeEnumerableException.not_enough_items(
                    -index, len(items)
                ) from error
        return cast("ENUMERABLE[T]", self).nth(index)

    @overload
    def element_at_or_default(self, index: int) -> T | None: ...

    @overload
    def element_at_or_default[U](self, index: int, default: U) -> T | U: ...

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut)
    def element_at_or_default(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_orig(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_1(self, index: int, default: object = None) -> object:
        if index <= 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_2(self, index: int, default: object = None) -> object:
        if index < 1:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_3(self, index: int, default: object = None) -> object:
        if index < 0:
            items = None
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_4(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast(None, self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_5(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", None).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_6(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast(self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_7(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", ).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_8(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("XXEnumerable[T]XX", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_9(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("enumerable[t]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_10(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("ENUMERABLE[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_11(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if (-index <= len(items)) and False else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_12(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if (-index <= len(items)) or True else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_13(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if +index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_14(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index < len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_15(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(None, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_16(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=None)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_17(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_18(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, )

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_19(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast(None, self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_20(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", None).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_21(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast(self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_22(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", ).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_23(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("XXEnumerable[T]XX", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_24(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("enumerable[t]", self).nth(index, default=default)

    def xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_25(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("ENUMERABLE[T]", self).nth(index, default=default)

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁlong_count__mutmut)
    def long_count(self) -> int:
        return cast("Enumerable[T]", self).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_orig(self) -> int:
        return cast("Enumerable[T]", self).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_1(self) -> int:
        return cast(None, self).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_2(self) -> int:
        return cast("Enumerable[T]", None).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_3(self) -> int:
        return cast(self).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_4(self) -> int:
        return cast("Enumerable[T]", ).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_5(self) -> int:
        return cast("XXEnumerable[T]XX", self).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_6(self) -> int:
        return cast("enumerable[t]", self).count()

    def xǁIteratorParityEnumerableǁlong_count__mutmut_7(self) -> int:
        return cast("ENUMERABLE[T]", self).count()

    @_mutmut_mutated(mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut)
    def try_get_non_enumerated_count(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(count) if count is not None else Null

    def xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_orig(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(count) if count is not None else Null

    def xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_1(self) -> Option[int]:
        count = None
        return Some(count) if count is not None else Null

    def xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_2(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(count) if (count is not None) and False else Null

    def xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_3(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(count) if (count is not None) or True else Null

    def xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_4(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(None) if count is not None else Null

    def xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_5(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(count) if count is None else Null

mutants_xǁIteratorParityEnumerableǁnext__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext__mutmut['xǁIteratorParityEnumerableǁnext__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext__mutmut['xǁIteratorParityEnumerableǁnext__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁnext_chunk__mutmut['xǁIteratorParityEnumerableǁnext_chunk__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁnext_chunk__mutmut_16 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁadvance_by__mutmut['xǁIteratorParityEnumerableǁadvance_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁadvance_by__mutmut_18 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁstep_by__mutmut['xǁIteratorParityEnumerableǁstep_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁstep_by__mutmut_14 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse__mutmut['xǁIteratorParityEnumerableǁintersperse__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse__mutmut_13 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersperse_with__mutmut['xǁIteratorParityEnumerableǁintersperse_with__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersperse_with__mutmut_13 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁmap_while__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_while__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_while__mutmut['xǁIteratorParityEnumerableǁmap_while__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_while__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_while__mutmut['xǁIteratorParityEnumerableǁmap_while__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_while__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_while__mutmut['xǁIteratorParityEnumerableǁmap_while__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_while__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_while__mutmut['xǁIteratorParityEnumerableǁmap_while__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_while__mutmut_4 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁfind_map__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfind_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfind_map__mutmut['xǁIteratorParityEnumerableǁfind_map__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfind_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfind_map__mutmut['xǁIteratorParityEnumerableǁfind_map__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfind_map__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfind_map__mutmut['xǁIteratorParityEnumerableǁfind_map__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfind_map__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfind_map__mutmut['xǁIteratorParityEnumerableǁfind_map__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfind_map__mutmut_4 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁinspect__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁinspect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁinspect__mutmut['xǁIteratorParityEnumerableǁinspect__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁinspect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁinspect__mutmut['xǁIteratorParityEnumerableǁinspect__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁinspect__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁfuse__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfuse__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfuse__mutmut['xǁIteratorParityEnumerableǁfuse__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfuse__mutmut_1 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁcycle__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcycle__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcycle__mutmut['xǁIteratorParityEnumerableǁcycle__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcycle__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcycle__mutmut['xǁIteratorParityEnumerableǁcycle__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcycle__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcycle__mutmut['xǁIteratorParityEnumerableǁcycle__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcycle__mutmut_3 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁarray_chunks__mutmut['xǁIteratorParityEnumerableǁarray_chunks__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁarray_chunks__mutmut_10 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmap_windows__mutmut['xǁIteratorParityEnumerableǁmap_windows__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmap_windows__mutmut_13 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁfor_each__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfor_each__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfor_each__mutmut['xǁIteratorParityEnumerableǁfor_each__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfor_each__mutmut_1 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁcollect_into__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcollect_into__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcollect_into__mutmut['xǁIteratorParityEnumerableǁcollect_into__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcollect_into__mutmut_1 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁunzip__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunzip__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunzip__mutmut['xǁIteratorParityEnumerableǁunzip__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunzip__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunzip__mutmut['xǁIteratorParityEnumerableǁunzip__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunzip__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunzip__mutmut['xǁIteratorParityEnumerableǁunzip__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunzip__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunzip__mutmut['xǁIteratorParityEnumerableǁunzip__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunzip__mutmut_4 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁpartition__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartition__mutmut['xǁIteratorParityEnumerableǁpartition__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartition__mutmut['xǁIteratorParityEnumerableǁpartition__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartition__mutmut['xǁIteratorParityEnumerableǁpartition__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartition__mutmut['xǁIteratorParityEnumerableǁpartition__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartition__mutmut['xǁIteratorParityEnumerableǁpartition__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartition__mutmut['xǁIteratorParityEnumerableǁpartition__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartition__mutmut_6 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_partitioned__mutmut['xǁIteratorParityEnumerableǁis_partitioned__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_partitioned__mutmut_10 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁposition__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁposition__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁposition__mutmut['xǁIteratorParityEnumerableǁposition__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁposition__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁposition__mutmut['xǁIteratorParityEnumerableǁposition__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁposition__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁposition__mutmut['xǁIteratorParityEnumerableǁposition__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁposition__mutmut_3 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁrposition__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁrposition__mutmut['xǁIteratorParityEnumerableǁrposition__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁrposition__mutmut_16 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut['xǁIteratorParityEnumerableǁmin_by_key__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut['xǁIteratorParityEnumerableǁmin_by_key__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut['xǁIteratorParityEnumerableǁmin_by_key__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut['xǁIteratorParityEnumerableǁmin_by_key__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by_key__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by_key__mutmut['xǁIteratorParityEnumerableǁmin_by_key__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by_key__mutmut_5 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut['xǁIteratorParityEnumerableǁmax_by_key__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut['xǁIteratorParityEnumerableǁmax_by_key__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut['xǁIteratorParityEnumerableǁmax_by_key__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut['xǁIteratorParityEnumerableǁmax_by_key__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by_key__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by_key__mutmut['xǁIteratorParityEnumerableǁmax_by_key__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by_key__mutmut_5 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut['xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by_key__mutmut_25 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁmin_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by__mutmut['xǁIteratorParityEnumerableǁmin_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by__mutmut['xǁIteratorParityEnumerableǁmin_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by__mutmut['xǁIteratorParityEnumerableǁmin_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by__mutmut['xǁIteratorParityEnumerableǁmin_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmin_by__mutmut['xǁIteratorParityEnumerableǁmin_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmin_by__mutmut_5 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁmax_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by__mutmut['xǁIteratorParityEnumerableǁmax_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by__mutmut['xǁIteratorParityEnumerableǁmax_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by__mutmut['xǁIteratorParityEnumerableǁmax_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by__mutmut['xǁIteratorParityEnumerableǁmax_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁmax_by__mutmut['xǁIteratorParityEnumerableǁmax_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁmax_by__mutmut_5 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_extreme_by__mutmut['xǁIteratorParityEnumerableǁ_extreme_by__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_extreme_by__mutmut_26 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁproduct__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁproduct__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁproduct__mutmut['xǁIteratorParityEnumerableǁproduct__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁproduct__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁproduct__mutmut['xǁIteratorParityEnumerableǁproduct__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁproduct__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁproduct__mutmut['xǁIteratorParityEnumerableǁproduct__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁproduct__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁproduct__mutmut['xǁIteratorParityEnumerableǁproduct__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁproduct__mutmut_4 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁcmp__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp__mutmut['xǁIteratorParityEnumerableǁcmp__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp__mutmut_11 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcmp_by__mutmut['xǁIteratorParityEnumerableǁcmp_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcmp_by__mutmut_23 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp__mutmut['xǁIteratorParityEnumerableǁpartial_cmp__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp__mutmut_16 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_26 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_27'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_27 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_28'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_28 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut['xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_29'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁpartial_cmp_by__mutmut_29 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁeq_by__mutmut['xǁIteratorParityEnumerableǁeq_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁeq_by__mutmut_11 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁlt__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlt__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlt__mutmut['xǁIteratorParityEnumerableǁlt__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlt__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlt__mutmut['xǁIteratorParityEnumerableǁlt__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlt__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁle__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁle__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁle__mutmut['xǁIteratorParityEnumerableǁle__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁle__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁle__mutmut['xǁIteratorParityEnumerableǁle__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁle__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁgt__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgt__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgt__mutmut['xǁIteratorParityEnumerableǁgt__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgt__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgt__mutmut['xǁIteratorParityEnumerableǁgt__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgt__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁge__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁge__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁge__mutmut['xǁIteratorParityEnumerableǁge__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁge__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁge__mutmut['xǁIteratorParityEnumerableǁge__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁge__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁis_sorted__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted__mutmut['xǁIteratorParityEnumerableǁis_sorted__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted__mutmut['xǁIteratorParityEnumerableǁis_sorted__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted__mutmut_2 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by__mutmut['xǁIteratorParityEnumerableǁis_sorted_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by__mutmut_25 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut['xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁis_sorted_by_key__mutmut_21 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁdistinct_by__mutmut['xǁIteratorParityEnumerableǁdistinct_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁdistinct_by__mutmut_17 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁunion__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion__mutmut['xǁIteratorParityEnumerableǁunion__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion__mutmut_23 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁexcept___mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept___mutmut['xǁIteratorParityEnumerableǁexcept___mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept___mutmut_23 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁintersect__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect__mutmut['xǁIteratorParityEnumerableǁintersect__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect__mutmut_23 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_26 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_27'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_27 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_28'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_28 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁunion_by__mutmut['xǁIteratorParityEnumerableǁunion_by__mutmut_29'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁunion_by__mutmut_29 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁexcept_by__mutmut['xǁIteratorParityEnumerableǁexcept_by__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁexcept_by__mutmut_26 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁintersect_by__mutmut['xǁIteratorParityEnumerableǁintersect_by__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁintersect_by__mutmut_26 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_26 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_27'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_27 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_28'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_28 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_29'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_29 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_30'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_30 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_31'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_31 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_32'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_32 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_33'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_33 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_34'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_34 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_35'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_35 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_36'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_36 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_37'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_37 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_38'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_38 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_39'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_39 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_40'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_40 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_41'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_41 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_42'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_42 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_43'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_43 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_44'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_44 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_45'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_45 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_46'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_46 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_47'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_47 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_48'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_48 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_49'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_49 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_50'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_50 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_51'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_51 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_52'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_52 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_53'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_53 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_54'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_54 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_55'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_55 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_56'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_56 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_57'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_57 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_58'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_58 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_59'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_59 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_60'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_60 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_61'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_61 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_62'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_62 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_63'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_63 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_64'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_64 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_set_operation__mutmut['xǁIteratorParityEnumerableǁ_set_operation__mutmut_65'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_set_operation__mutmut_65 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁcount_by__mutmut['xǁIteratorParityEnumerableǁcount_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁcount_by__mutmut_20 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by__mutmut['xǁIteratorParityEnumerableǁaggregate_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by__mutmut_25 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut['xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁaggregate_by_seed_selector__mutmut_26 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁorder__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder__mutmut['xǁIteratorParityEnumerableǁorder__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder__mutmut_9 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_descending__mutmut['xǁIteratorParityEnumerableǁorder_descending__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_descending__mutmut_9 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁorder_by_descending__mutmut['xǁIteratorParityEnumerableǁorder_by_descending__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁorder_by_descending__mutmut_12 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁthen_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by__mutmut['xǁIteratorParityEnumerableǁthen_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by__mutmut['xǁIteratorParityEnumerableǁthen_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by__mutmut['xǁIteratorParityEnumerableǁthen_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by__mutmut['xǁIteratorParityEnumerableǁthen_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by__mutmut['xǁIteratorParityEnumerableǁthen_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by__mutmut_5 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by_descending__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut['xǁIteratorParityEnumerableǁthen_by_descending__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by_descending__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut['xǁIteratorParityEnumerableǁthen_by_descending__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by_descending__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut['xǁIteratorParityEnumerableǁthen_by_descending__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by_descending__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut['xǁIteratorParityEnumerableǁthen_by_descending__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by_descending__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁthen_by_descending__mutmut['xǁIteratorParityEnumerableǁthen_by_descending__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁthen_by_descending__mutmut_5 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_26 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_27'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_27 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_28'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_28 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_29'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_29 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_30'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_30 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_31'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_31 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_32'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_32 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_33'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_33 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_34'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_34 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_35'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_35 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_36'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_36 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_37'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_37 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_38'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_38 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_39'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_39 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_40'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_40 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_41'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_41 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_42'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_42 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_43'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_43 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_44'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_44 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_45'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_45 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_46'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_46 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_47'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_47 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_48'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_48 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_49'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_49 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_50'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_50 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_51'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_51 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_52'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_52 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_53'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_53 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_54'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_54 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_55'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_55 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_56'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_56 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_57'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_57 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_58'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_58 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁ_then_by__mutmut['xǁIteratorParityEnumerableǁ_then_by__mutmut_59'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁ_then_by__mutmut_59 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁshuffle__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁshuffle__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁshuffle__mutmut['xǁIteratorParityEnumerableǁshuffle__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁshuffle__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁshuffle__mutmut['xǁIteratorParityEnumerableǁshuffle__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁshuffle__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁshuffle__mutmut['xǁIteratorParityEnumerableǁshuffle__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁshuffle__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁshuffle__mutmut['xǁIteratorParityEnumerableǁshuffle__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁshuffle__mutmut_4 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁof_type__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁof_type__mutmut['xǁIteratorParityEnumerableǁof_type__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁof_type__mutmut_15 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁto_array__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_array__mutmut['xǁIteratorParityEnumerableǁto_array__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_array__mutmut_7 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁto_hashset__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_hashset__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_hashset__mutmut['xǁIteratorParityEnumerableǁto_hashset__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_hashset__mutmut_1 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_dictionary__mutmut['xǁIteratorParityEnumerableǁto_dictionary__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_dictionary__mutmut_10 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁto_lookup__mutmut['xǁIteratorParityEnumerableǁto_lookup__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁto_lookup__mutmut_12 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁjoin_on__mutmut['xǁIteratorParityEnumerableǁjoin_on__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁjoin_on__mutmut_20 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁgroup_join__mutmut['xǁIteratorParityEnumerableǁgroup_join__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁgroup_join__mutmut_21 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁleft_join__mutmut['xǁIteratorParityEnumerableǁleft_join__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁleft_join__mutmut_18 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁright_join__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁright_join__mutmut['xǁIteratorParityEnumerableǁright_join__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁright_join__mutmut_18 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_26'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_26 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_27'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_27 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_28'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_28 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_29'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_29 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfull_join__mutmut['xǁIteratorParityEnumerableǁfull_join__mutmut_30'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfull_join__mutmut_30 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁfirst_or_default__mutmut['xǁIteratorParityEnumerableǁfirst_or_default__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁfirst_or_default__mutmut_11 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlast_or_default__mutmut['xǁIteratorParityEnumerableǁlast_or_default__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlast_or_default__mutmut_11 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁsingle_or_default__mutmut['xǁIteratorParityEnumerableǁsingle_or_default__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁsingle_or_default__mutmut_11 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at__mutmut['xǁIteratorParityEnumerableǁelement_at__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at__mutmut_23 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_8'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_9'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_10'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_11'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_12'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_13'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_14'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_15'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_16'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_17'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_18'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_19'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_20'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_21'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_22'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_23'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_24'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁelement_at_or_default__mutmut['xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_25'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁelement_at_or_default__mutmut_25 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_6'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁlong_count__mutmut['xǁIteratorParityEnumerableǁlong_count__mutmut_7'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁlong_count__mutmut_7 # type: ignore # mutmut generated

mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut['_mutmut_orig'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut['xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_1'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut['xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_2'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut['xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_3'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut['xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_4'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut['xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_5'] = IteratorParityEnumerable.xǁIteratorParityEnumerableǁtry_get_non_enumerated_count__mutmut_5 # type: ignore # mutmut generated
