lazy from enum import StrEnum
import itertools
import builtins
lazy from typing import Any, Callable, cast
from collections.abc import Iterable, Iterator
from statistics import fmean
from typing import overload

from rustshed import Null, Option, Some

lazy from .collect_enumerable import CollectEnumerable


lazy from .whole_sequence_operations_enumerable import WholeSequenceOperationsEnumerable

lazy from .copy_enumerable import CopyEnumerable

lazy from .control_flow import ControlFlowEnumerable, ControlFlow

lazy from .type_enumerable import TypeEnumerable


lazy from .filter_enumerable import FilterEnumerable, FilterPredicate

lazy from .count_enumerable import CountEnumerable
lazy from .enumerable import Enumerable
lazy from ._sentinels import MISSING
lazy from .parity_enumerable import IteratorParityEnumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTakeEnumerableǁfirst__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁsingle__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁlast__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁexact__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁnth__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁfind__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake_last__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁchunk__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁgroup_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁorder_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁsum__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁaverage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁmin__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁmax__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁislice__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁskip__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁskip_while__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake_while__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁpeek_while__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁpeek__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁtry_peek__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁpeek_n__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁskip_last__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableǁreverse__mutmut: MutantDict = {}  # type: ignore


class TakeEnumerable[T](
    CountEnumerable[T],
    FilterEnumerable[T],
    TypeEnumerable[T],
    ControlFlowEnumerable[T],
    CopyEnumerable[T],
    WholeSequenceOperationsEnumerable[T],
    CollectEnumerable[T],
    IteratorParityEnumerable[T],
):
    @overload
    def first(self, predicate: FilterPredicate[T] | None = None) -> T: ...

    @overload
    def first[U](self, predicate: FilterPredicate[T] | None, default: U) -> T | U: ...

    @overload
    def first[U](self, *, default: U) -> T | U: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁfirst__mutmut)
    def first(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_orig(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_1(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_2(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=None)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_3(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(None).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_4(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(None)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_5(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_6(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(None, default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_7(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, None)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_8(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(default)
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_9(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, )
            raise TakeEnumerableException.not_enough_items(
                1, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_10(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                None, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_11(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, None
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_12(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_13(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_14(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                2, 0
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    def xǁTakeEnumerableǁfirst__mutmut_15(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).first(default=default)
        try:
            return next(self.value)
        except StopIteration as e:
            if default is not MISSING:
                return cast(T, default)
            raise TakeEnumerableException.not_enough_items(
                1, 1
            ) from e  # we know there must be 0 as if next fails the iterator must be empty

    @overload
    def single(self, predicate: FilterPredicate[T] | None = None) -> T: ...

    @overload
    def single[U](self, predicate: FilterPredicate[T] | None, default: U) -> T | U: ...

    @overload
    def single[U](self, *, default: U) -> T | U: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁsingle__mutmut)
    def single(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(1, default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_orig(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(1, default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_1(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is None:
            return self.filter(predicate).single(default=default)

        return self.exact(1, default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_2(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=None)

        return self.exact(1, default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_3(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(None).single(default=default)

        return self.exact(1, default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_4(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(None, default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_5(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(1, default=None).first()

    def xǁTakeEnumerableǁsingle__mutmut_6(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(default=default).first()

    def xǁTakeEnumerableǁsingle__mutmut_7(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(1, ).first()

    def xǁTakeEnumerableǁsingle__mutmut_8(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:

        if predicate is not None:
            return self.filter(predicate).single(default=default)

        return self.exact(2, default=default).first()

    @overload
    def last(self, predicate: FilterPredicate[T] | None = None) -> T: ...

    @overload
    def last[U](self, predicate: FilterPredicate[T] | None, default: U) -> T | U: ...

    @overload
    def last[U](self, *, default: U) -> T | U: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁlast__mutmut)
    def last(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_orig(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_1(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_2(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=None)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_3(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(None).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_4(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = None
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_5(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = None
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_6(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is not MISSING:
            raise TakeEnumerableException.not_enough_items(1, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_7(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(None, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_8(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, None)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_9(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_10(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, )
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_11(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(2, 0)
        else:
            return last

    def xǁTakeEnumerableǁlast__mutmut_12(
        self,
        predicate: FilterPredicate[T] | None = None,
        default: object = MISSING,
    ) -> object:
        if predicate is not None:
            return self.filter(predicate).last(default=default)
        last: T | object = default
        for i in self:
            last = i
        if last is MISSING:
            raise TakeEnumerableException.not_enough_items(1, 1)
        else:
            return last

    @overload
    def exact(self, n: int) -> "Enumerable[T]": ...

    @overload
    def exact[U](self, n: int, default: U) -> "Enumerable[T | U]": ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁexact__mutmut)
    def exact(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_orig(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_1(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n <= 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_2(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 1:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_3(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError(None)

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_4(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("XXn must be non-negativeXX")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_5(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("N MUST BE NON-NEGATIVE")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_6(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = None
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_7(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(None)
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_8(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(None, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_9(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, None))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_10(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_11(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, ))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_12(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n - 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_13(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 2))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_14(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) >= n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_15(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(None, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_16(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_17(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, )
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_18(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) <= n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_19(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is not MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_20(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(None, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_21(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, None)
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_22(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_23(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, )
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_24(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend(None)
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_25(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] / (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_26(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(None, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_27(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, None)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_28(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(default)] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_29(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, )] * (n - len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_30(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n + len(cache)))
            yield from cache

        return Enumerable(inner())

    def xǁTakeEnumerableǁexact__mutmut_31(self, n: int, default: object = MISSING) -> "Enumerable[Any]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            cache = list(itertools.islice(self, n + 1))
            if len(cache) > n:
                raise TakeEnumerableException.too_many_items(n, None)
            if len(cache) < n:
                if default is MISSING:
                    raise TakeEnumerableException.not_enough_items(n, len(cache))
                cache.extend([cast(T, default)] * (n - len(cache)))
            yield from cache

        return Enumerable(None)

    @overload
    def nth(self, n: int) -> T: ...

    @overload
    def nth[U](self, n: int, default: U) -> T | U: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁnth__mutmut)
    def nth(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_orig(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_1(self, n: int, default: object = MISSING) -> object:
        if n <= 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_2(self, n: int, default: object = MISSING) -> object:
        if n < 1:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_3(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError(None)
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_4(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("XXn must be non-negativeXX")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_5(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("N MUST BE NON-NEGATIVE")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_6(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(None):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_7(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index != n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_8(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_9(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(None, default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_10(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, None)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_11(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(default)
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_12(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, )
        raise TakeEnumerableException.not_enough_items(n + 1, None)

    def xǁTakeEnumerableǁnth__mutmut_13(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(None, None)

    def xǁTakeEnumerableǁnth__mutmut_14(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(None)

    def xǁTakeEnumerableǁnth__mutmut_15(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 1, )

    def xǁTakeEnumerableǁnth__mutmut_16(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n - 1, None)

    def xǁTakeEnumerableǁnth__mutmut_17(self, n: int, default: object = MISSING) -> object:
        if n < 0:
            raise ValueError("n must be non-negative")
        for index, item in enumerate(self):
            if index == n:
                return item
        if default is not MISSING:
            return cast(T, default)
        raise TakeEnumerableException.not_enough_items(n + 2, None)

    @overload
    def find(self, predicate: FilterPredicate[T]) -> T: ...

    @overload
    def find[U](self, predicate: FilterPredicate[T], default: U) -> T | U: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁfind__mutmut)
    def find(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(predicate, default=default)

    def xǁTakeEnumerableǁfind__mutmut_orig(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(predicate, default=default)

    def xǁTakeEnumerableǁfind__mutmut_1(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(None, default=default)

    def xǁTakeEnumerableǁfind__mutmut_2(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(predicate, default=None)

    def xǁTakeEnumerableǁfind__mutmut_3(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(default=default)

    def xǁTakeEnumerableǁfind__mutmut_4(self, predicate: FilterPredicate[T], default: object = MISSING) -> object:
        return self.first(predicate, )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake_last__mutmut)
    def take_last(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_orig(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_1(self, n: int = 2) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_2(self, n: int = 1) -> "Enumerable[T]":
        if n <= 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_3(self, n: int = 1) -> "Enumerable[T]":
        if n < 1:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_4(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError(None)

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_5(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("XXn must be non-negativeXX")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_6(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("N MUST BE NON-NEGATIVE")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_7(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n != 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_8(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 1:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_9(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = None
            yield from items[-n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_10(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[+n:]

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_last__mutmut_11(self, n: int = 1) -> "Enumerable[T]":
        if n < 0:
            raise ValueError("n must be non-negative")

        def inner() -> Iterator[T]:
            if n == 0:
                return
            items = self.to_list()
            yield from items[-n:]

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁchunk__mutmut)
    def chunk(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_orig(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_1(self, size: int) -> "Enumerable[list[T]]":
        if size < 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_2(self, size: int) -> "Enumerable[list[T]]":
        if size <= 1:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_3(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError(None)

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_4(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("XXsize must be greater than zeroXX")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_5(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("SIZE MUST BE GREATER THAN ZERO")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_6(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = None
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_7(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(None)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_8(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) != size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_9(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = None
            if chunk_items:
                yield chunk_items

        return Enumerable(inner())

    def xǁTakeEnumerableǁchunk__mutmut_10(self, size: int) -> "Enumerable[list[T]]":
        if size <= 0:
            raise ValueError("size must be greater than zero")

        def inner() -> Iterator[list[T]]:
            chunk_items: list[T] = []
            for item in self:
                chunk_items.append(item)
                if len(chunk_items) == size:
                    yield chunk_items
                    chunk_items = []
            if chunk_items:
                yield chunk_items

        return Enumerable(None)

    @overload
    def group_by[K](
        self, key_selector: Callable[[T], K]
    ) -> "Enumerable[tuple[K, list[T]]]": ...

    @overload
    def group_by[K](
        self,
        key_selector: Callable[[T], K],
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, list[T]]]": ...

    @overload
    def group_by[K, R](
        self,
        key_selector: Callable[[T], K],
        *,
        result_selector: Callable[[K, list[T]], R],
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[R]": ...

    @overload
    def group_by[K, V](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V],
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[tuple[K, list[V]]]": ...

    @overload
    def group_by[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V],
        result_selector: Callable[[K, list[V]], R],
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[R]": ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁgroup_by__mutmut)
    def group_by[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_orig[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_1[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = None
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_2[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = None
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_3[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(None)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_4[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = None
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_5[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if (element_selector is not None) and False
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_6[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if (element_selector is not None) or True
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_7[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(None)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_8[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_9[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(None, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_10[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, None)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_11[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_12[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, )
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_13[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = None
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_14[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if (comparer is not None) and False
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_15[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if (comparer is not None) or True
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_16[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(None, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_17[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, None)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_18[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_19[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, )
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_20[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_21[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key != existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_22[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(None)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_23[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        return
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_24[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append(None)
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_25[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is not None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_26[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(None, elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_27[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, None)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_28[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(elements)

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_29[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, )

        return Enumerable(inner())

    def xǁTakeEnumerableǁgroup_by__mutmut_30[K, V, R](
        self,
        key_selector: Callable[[T], K],
        element_selector: Callable[[T], V] | None = None,
        result_selector: Callable[[K, list[V]], R] | None = None,
        *,
        comparer: Callable[[K, K], bool] | None = None,
    ) -> "Enumerable[Any]":
        def inner() -> Iterator[Any]:
            groups: list[tuple[K, list[V]]] = []
            for item in self:
                key = key_selector(item)
                element = (
                    element_selector(item)
                    if element_selector is not None
                    else cast(V, item)
                )
                for existing_key, elements in groups:
                    same = (
                        comparer(key, existing_key)
                        if comparer is not None
                        else key == existing_key
                    )
                    if same:
                        elements.append(element)
                        break
                else:
                    groups.append((key, [element]))
            for key, elements in groups:
                if result_selector is None:
                    yield key, elements
                else:
                    yield result_selector(key, elements)

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁorder_by__mutmut)
    def order_by(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_orig(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_1(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = True,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_2(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is not None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_3(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = None
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_4(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(None, reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_5(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=None)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_6(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_7(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), )
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_8(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(None, self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_9(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], None), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_10(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_11(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], ), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_12(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(None, ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_13(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], None)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_14(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_15(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], )
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_16(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(None, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_17(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=None, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_18(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=None)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_19(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_20(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_21(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, )

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_22(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = None
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_23(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(None)
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_24(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(None, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_25(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, None, self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_26(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", None)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_27(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr("_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_28(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_29(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", )
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_30(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "XX_ordered_sourceXX", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_31(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ORDERED_SOURCE", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_32(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = None
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_33(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if (key is not None) and False else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_34(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if (key is not None) or True else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_35(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is None else lambda item: item
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_36(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: None
        setattr(result, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_37(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(None, "_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_38(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, None, ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_39(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", None)
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_40(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr("_ordering_keys", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_41(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_42(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ordering_keys", )
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_43(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "XX_ordering_keysXX", ((ordered_key, reverse),))
        return result

    def xǁTakeEnumerableǁorder_by__mutmut_44(
        self,
        key: Callable[[T], Any] | None = None,
        *,
        reverse: bool = False,
    ) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            if key is None:
                ordered = builtins.sorted(cast(Iterable[Any], self), reverse=reverse)
                yield from cast(list[T], ordered)
            else:
                yield from builtins.sorted(self, key=key, reverse=reverse)

        result = Enumerable(inner())
        setattr(result, "_ordered_source", self)
        ordered_key: Callable[[T], Any] = key if key is not None else lambda item: item
        setattr(result, "_ORDERING_KEYS", ((ordered_key, reverse),))
        return result

    @overload
    def default_if_empty(self) -> "Enumerable[T | None]": ...

    @overload
    def default_if_empty[U](self, default: U) -> "Enumerable[T | U]": ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut)
    def default_if_empty(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_orig(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_1(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = None
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_2(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = True
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_3(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = None
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_4(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = False
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_5(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if found:
                yield None if default is MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_6(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if (default is MISSING) and False else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_7(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if (default is MISSING) or True else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_8(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is not MISSING else default

        return Enumerable(inner())

    def xǁTakeEnumerableǁdefault_if_empty__mutmut_9(self, default: object = MISSING) -> "Enumerable[Any]":
        def inner() -> Iterator[object]:
            found = False
            for item in self:
                found = True
                yield item
            if not found:
                yield None if default is MISSING else default

        return Enumerable(None)

    @overload
    def sum(self) -> T: ...

    @overload
    def sum[V](self, selector: Callable[[T], V]) -> V: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁsum__mutmut)
    def sum(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_orig(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_1(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = None
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_2(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if (selector is None) and False else map(selector, self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_3(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if (selector is None) or True else map(selector, self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_4(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is not None else map(selector, self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_5(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(None, self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_6(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, None)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_7(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(self)
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_8(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, )
        return builtins.sum(cast(Iterable[Any], values))

    def xǁTakeEnumerableǁsum__mutmut_9(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(None)

    def xǁTakeEnumerableǁsum__mutmut_10(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(cast(None, values))

    def xǁTakeEnumerableǁsum__mutmut_11(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(cast(Iterable[Any], None))

    def xǁTakeEnumerableǁsum__mutmut_12(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(cast(values))

    def xǁTakeEnumerableǁsum__mutmut_13(self, selector: Callable[[T], Any] | None = None) -> Any:
        values = self if selector is None else map(selector, self)
        return builtins.sum(cast(Iterable[Any], ))

    @overload
    def average(self) -> float: ...

    @overload
    def average(self, selector: Callable[[T], Any]) -> float: ...

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁaverage__mutmut)
    def average(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(selector, self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_orig(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(selector, self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_1(self, selector: Callable[[T], Any] | None = None) -> float:
        values = None
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_2(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if (selector is None) and False else map(selector, self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_3(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if (selector is None) or True else map(selector, self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_4(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is not None else map(selector, self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_5(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(None, self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_6(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(selector, None)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_7(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(self)
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_8(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(selector, )
        return fmean(values)  # type: ignore[arg-type]

    def xǁTakeEnumerableǁaverage__mutmut_9(self, selector: Callable[[T], Any] | None = None) -> float:
        values = self if selector is None else map(selector, self)
        return fmean(None)  # type: ignore[arg-type]

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁmin__mutmut)
    def min(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_orig(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_1(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is not None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_2(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(None, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_3(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, None)
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_4(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_5(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, )
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_6(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(None))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_7(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(None, self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_8(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], None)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_9(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(self)))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_10(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], )))
        return builtins.min(self, key=key)

    def xǁTakeEnumerableǁmin__mutmut_11(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(None, key=key)

    def xǁTakeEnumerableǁmin__mutmut_12(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, key=None)

    def xǁTakeEnumerableǁmin__mutmut_13(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(key=key)

    def xǁTakeEnumerableǁmin__mutmut_14(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.min(cast(Iterable[Any], self)))
        return builtins.min(self, )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁmax__mutmut)
    def max(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_orig(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_1(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is not None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_2(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(None, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_3(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, None)
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_4(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_5(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, )
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_6(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(None))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_7(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(None, self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_8(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], None)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_9(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(self)))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_10(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], )))
        return builtins.max(self, key=key)

    def xǁTakeEnumerableǁmax__mutmut_11(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(None, key=key)

    def xǁTakeEnumerableǁmax__mutmut_12(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, key=None)

    def xǁTakeEnumerableǁmax__mutmut_13(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(key=key)

    def xǁTakeEnumerableǁmax__mutmut_14(self, *, key: Callable[[T], Any] | None = None) -> T:
        if key is None:
            return cast(T, builtins.max(cast(Iterable[Any], self)))
        return builtins.max(self, )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁislice__mutmut)
    def islice(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_orig(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_1(
        self, start: int | None, stop: int | None, step: int | None = 2
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_2(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = None
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_3(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(None, start, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_4(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, None, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_5(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, None, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_6(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, None)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_7(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(start, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_8(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, stop, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_9(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, step)
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_10(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, )
        return Enumerable(slice)

    def xǁTakeEnumerableǁislice__mutmut_11(
        self, start: int | None, stop: int | None, step: int | None = 1
    ) -> "Enumerable[T]":
        slice = itertools.islice(self, start, stop, step)
        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁskip__mutmut)
    def skip(self, n: int = 1) -> "Enumerable[T]":
        return self.islice(n, None)

    def xǁTakeEnumerableǁskip__mutmut_orig(self, n: int = 1) -> "Enumerable[T]":
        return self.islice(n, None)

    def xǁTakeEnumerableǁskip__mutmut_1(self, n: int = 2) -> "Enumerable[T]":
        return self.islice(n, None)

    def xǁTakeEnumerableǁskip__mutmut_2(self, n: int = 1) -> "Enumerable[T]":
        return self.islice(None, None)

    def xǁTakeEnumerableǁskip__mutmut_3(self, n: int = 1) -> "Enumerable[T]":
        return self.islice(None)

    def xǁTakeEnumerableǁskip__mutmut_4(self, n: int = 1) -> "Enumerable[T]":
        return self.islice(n, )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁskip_while__mutmut)
    def skip_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if predicate(x)
                else ControlFlow[T].yield_control_ok(x)
            )
        )

    def xǁTakeEnumerableǁskip_while__mutmut_orig(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if predicate(x)
                else ControlFlow[T].yield_control_ok(x)
            )
        )

    def xǁTakeEnumerableǁskip_while__mutmut_1(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            None
        )

    def xǁTakeEnumerableǁskip_while__mutmut_2(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: None
        )

    def xǁTakeEnumerableǁskip_while__mutmut_3(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if (predicate(x)) and False
                else ControlFlow[T].yield_control_ok(x)
            )
        )

    def xǁTakeEnumerableǁskip_while__mutmut_4(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if (predicate(x)) or True
                else ControlFlow[T].yield_control_ok(x)
            )
        )

    def xǁTakeEnumerableǁskip_while__mutmut_5(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if predicate(None)
                else ControlFlow[T].yield_control_ok(x)
            )
        )

    def xǁTakeEnumerableǁskip_while__mutmut_6(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow.skip()
                if predicate(x)
                else ControlFlow[T].yield_control_ok(None)
            )
        )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut)
    def skip_while_indexed(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_orig(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_1(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(None)
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_2(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(None)
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_3(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: None)
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_4(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(None, indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_5(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], None))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_6(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_7(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], ))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_8(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[2], indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_9(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], indexed[1]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_10(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: None)
        )

    def xǁTakeEnumerableǁskip_while_indexed__mutmut_11(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .skip_while(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: indexed[2])
        )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake__mutmut)
    def take(self, n: int = 1) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(None, n)

    def xǁTakeEnumerableǁtake__mutmut_orig(self, n: int = 1) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(None, n)

    def xǁTakeEnumerableǁtake__mutmut_1(self, n: int = 2) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(None, n)

    def xǁTakeEnumerableǁtake__mutmut_2(self, n: int = 1) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(None, None)

    def xǁTakeEnumerableǁtake__mutmut_3(self, n: int = 1) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(n)

    def xǁTakeEnumerableǁtake__mutmut_4(self, n: int = 1) -> "Enumerable[T]":
        assert isinstance(n, int)
        return self.islice(None, )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut)
    def take_while_lossy(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if predicate(x) else ControlFlow.stop()
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_orig(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if predicate(x) else ControlFlow.stop()
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_1(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            None
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_2(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: None
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_3(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if (predicate(x)) and False else ControlFlow.stop()
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_4(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if (predicate(x)) or True else ControlFlow.stop()
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_5(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(None) if predicate(x) else ControlFlow.stop()
        )

    def xǁTakeEnumerableǁtake_while_lossy__mutmut_6(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: ControlFlow[T].ok(x) if predicate(None) else ControlFlow.stop()
        )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake_while__mutmut)
    def take_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.take_while_lossy(predicate)

    def xǁTakeEnumerableǁtake_while__mutmut_orig(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.take_while_lossy(predicate)

    def xǁTakeEnumerableǁtake_while__mutmut_1(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.take_while_lossy(None)

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut)
    def take_while_indexed(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_orig(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_1(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(None)
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_2(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(None)
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_3(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: None)
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_4(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(None, indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_5(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], None))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_6(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_7(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], ))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_8(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[2], indexed[0]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_9(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], indexed[1]))
            .map(lambda indexed: indexed[1])
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_10(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: None)
        )

    def xǁTakeEnumerableǁtake_while_indexed__mutmut_11(
        self, predicate: Callable[[T, int], bool]
    ) -> "Enumerable[T]":
        return (
            self.enumerate()
            .take_while_lossy(lambda indexed: predicate(indexed[1], indexed[0]))
            .map(lambda indexed: indexed[2])
        )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut)
    def take_while_inclusive(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if predicate(x) else ControlFlow[T].stop_ok(x)
            )
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_orig(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if predicate(x) else ControlFlow[T].stop_ok(x)
            )
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_1(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            None
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_2(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: None
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_3(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if (predicate(x)) and False else ControlFlow[T].stop_ok(x)
            )
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_4(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if (predicate(x)) or True else ControlFlow[T].stop_ok(x)
            )
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_5(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(None) if predicate(x) else ControlFlow[T].stop_ok(x)
            )
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_6(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if predicate(None) else ControlFlow[T].stop_ok(x)
            )
        )

    def xǁTakeEnumerableǁtake_while_inclusive__mutmut_7(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.control_flow(
            lambda x: (
                ControlFlow[T].ok(x) if predicate(x) else ControlFlow[T].stop_ok(None)
            )
        )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut)
    def take_while_lossless(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    break
                next(iter(self))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_orig(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    break
                next(iter(self))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_1(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = None

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    break
                next(iter(self))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_2(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if predicate(item):
                    break
                next(iter(self))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_3(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(None):
                    break
                next(iter(self))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_4(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    return
                next(iter(self))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_5(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    break
                next(None)
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_6(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    break
                next(iter(None))
                yield item

        return Enumerable(inner())

    def xǁTakeEnumerableǁtake_while_lossless__mutmut_7(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        lookahead = self.shallow_copy()

        def inner() -> Iterator[T]:
            for item in lookahead:
                if not predicate(item):
                    break
                next(iter(self))
                yield item

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁpeek_while__mutmut)
    def peek_while(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.shallow_copy().take_while_lossy(predicate)

    def xǁTakeEnumerableǁpeek_while__mutmut_orig(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.shallow_copy().take_while_lossy(predicate)

    def xǁTakeEnumerableǁpeek_while__mutmut_1(self, predicate: Callable[[T], bool]) -> "Enumerable[T]":
        return self.shallow_copy().take_while_lossy(None)

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁpeek__mutmut)
    def peek(self) -> T:
        return self.peek_n(1).single()

    def xǁTakeEnumerableǁpeek__mutmut_orig(self) -> T:
        return self.peek_n(1).single()

    def xǁTakeEnumerableǁpeek__mutmut_1(self) -> T:
        return self.peek_n(None).single()

    def xǁTakeEnumerableǁpeek__mutmut_2(self) -> T:
        return self.peek_n(2).single()

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁtry_peek__mutmut)
    def try_peek(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) == 1:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_orig(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) == 1:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_1(self) -> Option[T]:
        val = None
        if len(val) == 1:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_2(self) -> Option[T]:
        val = self.peek_n(None).to_list()
        if len(val) == 1:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_3(self) -> Option[T]:
        val = self.peek_n(2).to_list()
        if len(val) == 1:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_4(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) != 1:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_5(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) == 2:
            return Some(val[0])
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_6(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) == 1:
            return Some(None)
        else:
            return Null

    def xǁTakeEnumerableǁtry_peek__mutmut_7(self) -> Option[T]:
        val = self.peek_n(1).to_list()
        if len(val) == 1:
            return Some(val[1])
        else:
            return Null

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁpeek_n__mutmut)
    def peek_n(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] < n)
            .map(lambda x: x[1])
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_orig(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] < n)
            .map(lambda x: x[1])
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_1(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] < n)
            .map(None)
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_2(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(None)
            .map(lambda x: x[1])
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_3(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: None)
            .map(lambda x: x[1])
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_4(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[1] < n)
            .map(lambda x: x[1])
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_5(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] <= n)
            .map(lambda x: x[1])
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_6(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] < n)
            .map(lambda x: None)
        )

    def xǁTakeEnumerableǁpeek_n__mutmut_7(self, n: int) -> "Enumerable[T]":
        return (
            self.shallow_copy()
            .enumerate()
            .take_while_lossy(lambda x: x[0] < n)
            .map(lambda x: x[2])
        )

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁskip_last__mutmut)
    def skip_last(self, n: int = 1) -> "Enumerable[T]":
        return self.reverse().skip(n).reverse()

    def xǁTakeEnumerableǁskip_last__mutmut_orig(self, n: int = 1) -> "Enumerable[T]":
        return self.reverse().skip(n).reverse()

    def xǁTakeEnumerableǁskip_last__mutmut_1(self, n: int = 2) -> "Enumerable[T]":
        return self.reverse().skip(n).reverse()

    def xǁTakeEnumerableǁskip_last__mutmut_2(self, n: int = 1) -> "Enumerable[T]":
        return self.reverse().skip(None).reverse()

    @_mutmut_mutated(mutants_xǁTakeEnumerableǁreverse__mutmut)
    def reverse(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from reversed(self.to_list())

        return Enumerable(inner())

    def xǁTakeEnumerableǁreverse__mutmut_orig(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from reversed(self.to_list())

        return Enumerable(inner())

    def xǁTakeEnumerableǁreverse__mutmut_1(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from reversed(None)

        return Enumerable(inner())

    def xǁTakeEnumerableǁreverse__mutmut_2(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from reversed(self.to_list())

        return Enumerable(None)

mutants_xǁTakeEnumerableǁfirst__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfirst__mutmut['xǁTakeEnumerableǁfirst__mutmut_15'] = TakeEnumerable.xǁTakeEnumerableǁfirst__mutmut_15 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁsingle__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsingle__mutmut['xǁTakeEnumerableǁsingle__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁsingle__mutmut_8 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁlast__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁlast__mutmut['xǁTakeEnumerableǁlast__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁlast__mutmut_12 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁexact__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_15'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_16'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_17'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_18'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_19'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_20'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_21'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_22'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_23'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_24'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_25'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_26'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_27'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_28'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_29'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_30'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁexact__mutmut['xǁTakeEnumerableǁexact__mutmut_31'] = TakeEnumerable.xǁTakeEnumerableǁexact__mutmut_31 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁnth__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_15'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_16'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁnth__mutmut['xǁTakeEnumerableǁnth__mutmut_17'] = TakeEnumerable.xǁTakeEnumerableǁnth__mutmut_17 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁfind__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁfind__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfind__mutmut['xǁTakeEnumerableǁfind__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁfind__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfind__mutmut['xǁTakeEnumerableǁfind__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁfind__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfind__mutmut['xǁTakeEnumerableǁfind__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁfind__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁfind__mutmut['xǁTakeEnumerableǁfind__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁfind__mutmut_4 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake_last__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_last__mutmut['xǁTakeEnumerableǁtake_last__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁtake_last__mutmut_11 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁchunk__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁchunk__mutmut['xǁTakeEnumerableǁchunk__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁchunk__mutmut_10 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁgroup_by__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_15'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_16'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_17'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_18'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_19'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_20'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_21'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_22'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_23'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_24'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_25'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_26'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_27'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_28'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_29'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁgroup_by__mutmut['xǁTakeEnumerableǁgroup_by__mutmut_30'] = TakeEnumerable.xǁTakeEnumerableǁgroup_by__mutmut_30 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁorder_by__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_15'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_16'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_17'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_18'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_19'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_20'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_21'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_22'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_23'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_24'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_25'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_26'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_27'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_28'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_29'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_30'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_31'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_32'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_33'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_34'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_35'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_36'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_37'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_38'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_39'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_40'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_41'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_42'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_43'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁorder_by__mutmut['xǁTakeEnumerableǁorder_by__mutmut_44'] = TakeEnumerable.xǁTakeEnumerableǁorder_by__mutmut_44 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁdefault_if_empty__mutmut['xǁTakeEnumerableǁdefault_if_empty__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁdefault_if_empty__mutmut_9 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁsum__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁsum__mutmut['xǁTakeEnumerableǁsum__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁsum__mutmut_13 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁaverage__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁaverage__mutmut['xǁTakeEnumerableǁaverage__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁaverage__mutmut_9 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁmin__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmin__mutmut['xǁTakeEnumerableǁmin__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁmin__mutmut_14 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁmax__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_12'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_13'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁmax__mutmut['xǁTakeEnumerableǁmax__mutmut_14'] = TakeEnumerable.xǁTakeEnumerableǁmax__mutmut_14 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁislice__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁislice__mutmut['xǁTakeEnumerableǁislice__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁislice__mutmut_11 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁskip__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁskip__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip__mutmut['xǁTakeEnumerableǁskip__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁskip__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip__mutmut['xǁTakeEnumerableǁskip__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁskip__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip__mutmut['xǁTakeEnumerableǁskip__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁskip__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip__mutmut['xǁTakeEnumerableǁskip__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁskip__mutmut_4 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁskip_while__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while__mutmut['xǁTakeEnumerableǁskip_while__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while__mutmut['xǁTakeEnumerableǁskip_while__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while__mutmut['xǁTakeEnumerableǁskip_while__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while__mutmut['xǁTakeEnumerableǁskip_while__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while__mutmut['xǁTakeEnumerableǁskip_while__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while__mutmut['xǁTakeEnumerableǁskip_while__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁskip_while__mutmut_6 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_while_indexed__mutmut['xǁTakeEnumerableǁskip_while_indexed__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁskip_while_indexed__mutmut_11 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake__mutmut['xǁTakeEnumerableǁtake__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake__mutmut['xǁTakeEnumerableǁtake__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtake__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake__mutmut['xǁTakeEnumerableǁtake__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtake__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake__mutmut['xǁTakeEnumerableǁtake__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtake__mutmut_4 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['xǁTakeEnumerableǁtake_while_lossy__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['xǁTakeEnumerableǁtake_while_lossy__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['xǁTakeEnumerableǁtake_while_lossy__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['xǁTakeEnumerableǁtake_while_lossy__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['xǁTakeEnumerableǁtake_while_lossy__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossy__mutmut['xǁTakeEnumerableǁtake_while_lossy__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossy__mutmut_6 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake_while__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake_while__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while__mutmut['xǁTakeEnumerableǁtake_while__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake_while__mutmut_1 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_8'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_9'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_10'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_indexed__mutmut['xǁTakeEnumerableǁtake_while_indexed__mutmut_11'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_indexed__mutmut_11 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_inclusive__mutmut['xǁTakeEnumerableǁtake_while_inclusive__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_inclusive__mutmut_7 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtake_while_lossless__mutmut['xǁTakeEnumerableǁtake_while_lossless__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁtake_while_lossless__mutmut_7 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁpeek_while__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁpeek_while__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_while__mutmut['xǁTakeEnumerableǁpeek_while__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁpeek_while__mutmut_1 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁpeek__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁpeek__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek__mutmut['xǁTakeEnumerableǁpeek__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁpeek__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek__mutmut['xǁTakeEnumerableǁpeek__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁpeek__mutmut_2 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁtry_peek__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁtry_peek__mutmut['xǁTakeEnumerableǁtry_peek__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁtry_peek__mutmut_7 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁpeek_n__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_3'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_4'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_5'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_6'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁpeek_n__mutmut['xǁTakeEnumerableǁpeek_n__mutmut_7'] = TakeEnumerable.xǁTakeEnumerableǁpeek_n__mutmut_7 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁskip_last__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁskip_last__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_last__mutmut['xǁTakeEnumerableǁskip_last__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁskip_last__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁskip_last__mutmut['xǁTakeEnumerableǁskip_last__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁskip_last__mutmut_2 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableǁreverse__mutmut['_mutmut_orig'] = TakeEnumerable.xǁTakeEnumerableǁreverse__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁreverse__mutmut['xǁTakeEnumerableǁreverse__mutmut_1'] = TakeEnumerable.xǁTakeEnumerableǁreverse__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableǁreverse__mutmut['xǁTakeEnumerableǁreverse__mutmut_2'] = TakeEnumerable.xǁTakeEnumerableǁreverse__mutmut_2 # type: ignore # mutmut generated


class TakeEnumerableExceptionCase(StrEnum):
    NotEnoughItems = (
        "There were not enough items remaining in the enumerable for this operation!"
    )
    TooManyItems = (
        "There were too many items remaining in the enumerable for this operation!"
    )
mutants_xǁTakeEnumerableExceptionǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut: MutantDict = {}  # type: ignore


class TakeEnumerableException(Exception):
    @_mutmut_mutated(mutants_xǁTakeEnumerableExceptionǁ__init____mutmut)
    def __init__(self, case: TakeEnumerableExceptionCase, *args: Any, **kwargs: Any):
        self.exception_case = case
        super().__init__(*args, **kwargs)
    def xǁTakeEnumerableExceptionǁ__init____mutmut_orig(self, case: TakeEnumerableExceptionCase, *args: Any, **kwargs: Any):
        self.exception_case = case
        super().__init__(*args, **kwargs)
    def xǁTakeEnumerableExceptionǁ__init____mutmut_1(self, case: TakeEnumerableExceptionCase, *args: Any, **kwargs: Any):
        self.exception_case = None
        super().__init__(*args, **kwargs)
    def xǁTakeEnumerableExceptionǁ__init____mutmut_2(self, case: TakeEnumerableExceptionCase, *args: Any, **kwargs: Any):
        self.exception_case = case
        super().__init__(**kwargs)
    def xǁTakeEnumerableExceptionǁ__init____mutmut_3(self, case: TakeEnumerableExceptionCase, *args: Any, **kwargs: Any):
        self.exception_case = case
        super().__init__(*args, )

    @classmethod
    @_mutmut_mutated(mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut, is_classmethod = True)
    def not_enough_items(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_orig(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_1(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            None,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_2(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            None,
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_3(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_4(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_5(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if (at_least is not None) and False else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_6(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if (at_least is not None) or True else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_7(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is None else "unknown(not provided)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_8(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "XXunknown(not provided)XX"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_9(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "UNKNOWN(NOT PROVIDED)"} items but got only {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_10(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if (actual is not None) and False else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_11(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if (actual is not None) or True else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_12(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_13(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "XXunknown(not provided)XX"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_14(
        cls, at_least: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.NotEnoughItems,
            f"Expected at least {at_least if at_least is not None else "unknown(not provided)"} items but got only {actual if actual is not None else "UNKNOWN(NOT PROVIDED)"} items",
        )

    @classmethod
    @_mutmut_mutated(mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut, is_classmethod = True)
    def too_many_items(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_orig(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_1(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            None,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_2(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            None,
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_3(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_4(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_5(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if (at_most is not None) and False else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_6(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if (at_most is not None) or True else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_7(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is None else "unknown(not provided)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_8(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "XXunknown(not provided)XX"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_9(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "UNKNOWN(NOT PROVIDED)"} items but got at least {actual if actual is not None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_10(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if (actual is not None) and False else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_11(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if (actual is not None) or True else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_12(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is None else "unknown(not provided)"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_13(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "XXunknown(not provided)XX"} items",
        )

    @classmethod
    def xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_14(
        cls, at_most: int | None = None, actual: int | None = None
    ) -> "TakeEnumerableException":
        return cls(
            TakeEnumerableExceptionCase.TooManyItems,
            f"Expected at most {at_most if at_most is not None else "unknown(not provided)"} items but got at least {actual if actual is not None else "UNKNOWN(NOT PROVIDED)"} items",
        )

mutants_xǁTakeEnumerableExceptionǁ__init____mutmut['_mutmut_orig'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁ__init____mutmut['xǁTakeEnumerableExceptionǁ__init____mutmut_1'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁ__init____mutmut['xǁTakeEnumerableExceptionǁ__init____mutmut_2'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁ__init____mutmut['xǁTakeEnumerableExceptionǁ__init____mutmut_3'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['_mutmut_orig'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_1'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_2'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_3'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_4'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_5'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_6'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_7'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_8'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_9'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_10'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_11'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_12'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_13'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁnot_enough_items__mutmut['xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_14'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁnot_enough_items__mutmut_14 # type: ignore # mutmut generated

mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['_mutmut_orig'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_1'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_2'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_3'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_4'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_5'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_6'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_7'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_8'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_9'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_10'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_11'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_12'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_13'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTakeEnumerableExceptionǁtoo_many_items__mutmut['xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_14'] = TakeEnumerableException.xǁTakeEnumerableExceptionǁtoo_many_items__mutmut_14 # type: ignore # mutmut generated
