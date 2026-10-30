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


def _ordering(value: int) -> Ordering:
    if value < 0:
        return Ordering.Less
    if value > 0:
        return Ordering.Greater
    return Ordering.Equal


def _compare(left: Any, right: Any) -> Ordering:
    if left < right:
        return Ordering.Less
    if left > right:
        return Ordering.Greater
    return Ordering.Equal


class IteratorParityEnumerable[T](BaseEnumerable[T]):
    def by_ref(self) -> "IteratorParityEnumerable[T]":
        return self

    def next(self) -> Option[T]:
        try:
            return Some(next(self.value))
        except StopIteration:
            return Null

    def next_chunk(self, size: int) -> NextChunkResult[T]:
        if size <= 0:
            raise ValueError("size must be greater than zero")
        items = list(itertools.islice(self, size))
        return NextChunkResult(items, len(items) == size)

    def advance_by(self, count: int) -> AdvanceByResult:
        if count < 0:
            raise ValueError("count must be non-negative")
        advanced = sum(1 for _ in itertools.islice(self, count))
        return AdvanceByResult(advanced == count, count - advanced)

    def step_by(self, step: int) -> "Enumerable[T]":
        if step <= 0:
            raise ValueError("step must be greater than zero")
        return Enumerable(itertools.islice(self, 0, None, step))

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

    def find_map[V](self, callback: Callable[[T], V | FilterMapDrop]) -> Option[V]:
        for item in self:
            result = callback(item)
            if result is not DROP:
                return Some(result)
        return Null

    def inspect(self, callback: Callable[[T], object]) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            for item in self:
                callback(item)
                yield item

        return Enumerable(inner())

    def fuse(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            yield from self

        return Enumerable(inner())

    def cycle(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            cache: list[T] = []
            for item in self:
                cache.append(item)
                yield item
            while cache:
                yield from cache

        return Enumerable(inner())

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

    def for_each(self, callback: Callable[[T], object]) -> None:
        for item in self:
            callback(item)

    def collect_into(self, collection: Extendable[T]) -> Extendable[T]:
        collection.extend(self)
        return collection

    def unzip[A, B](
        self: "IteratorParityEnumerable[tuple[A, B]]",
    ) -> tuple[list[A], list[B]]:
        left: list[A] = []
        right: list[B] = []
        for first, second in self:
            left.append(first)
            right.append(second)
        return left, right

    def partition(self, predicate: Callable[[T], bool]) -> tuple[list[T], list[T]]:
        matching: list[T] = []
        not_matching: list[T] = []
        for item in self:
            (matching if predicate(item) else not_matching).append(item)
        return matching, not_matching

    def is_partitioned(self, predicate: Callable[[T], bool]) -> bool:
        found_false = False
        for item in self:
            matches = predicate(item)
            if matches and found_false:
                return False
            if not matches:
                found_false = True
        return True

    def position(self, predicate: Callable[[T], bool]) -> Option[int]:
        for index, item in enumerate(self):
            if predicate(item):
                return Some(index)
        return Null

    def rposition(self, predicate: Callable[[T], bool]) -> Option[int]:
        items = list(self)
        for index in range(len(items) - 1, -1, -1):
            if predicate(items[index]):
                return Some(index)
        return Null

    def min_by_key[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=False)

    def max_by_key[K](self, key: Callable[[T], K]) -> Option[T]:
        return self._extreme_by_key(key, reverse=True)

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

    def min_by(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=False)

    def max_by(self, compare: Callable[[T, T], int]) -> Option[T]:
        return self._extreme_by(compare, reverse=True)

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

    def product(self) -> Any:
        result: Any = 1
        for item in self:
            result *= item
        return result

    def cmp(self, other: Iterable[T]) -> Ordering:
        return cast("Enumerable[T]", self).cmp_by(other, _compare)

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

    def partial_cmp[U](self, other: Iterable[U]) -> Option[Ordering]:
        def compare(left: T, right: U) -> int | None:
            try:
                return int(_compare(left, right))
            except TypeError:
                return None

        return cast("Enumerable[T]", self).partial_cmp_by(other, compare)

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

    def eq_by[U](self, other: Iterable[U], comparer: Callable[[T, U], bool]) -> bool:
        return cast("Enumerable[T]", self).eq(other, comparer=comparer)

    def lt(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Less

    def le(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Greater

    def gt(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is Ordering.Greater

    def ge(self, other: Iterable[T]) -> bool:
        return self.cmp(other) is not Ordering.Less

    def is_sorted(self) -> bool:
        return self.is_sorted_by_key(lambda item: item)

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

    def order(self, *, reverse: bool = False) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=reverse)

    def order_descending(self) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(reverse=True)

    def order_by_descending[K](
        self, key: Callable[[T], K] | None = None
    ) -> "Enumerable[T]":
        return cast("Enumerable[T]", self).order_by(key=key, reverse=True)

    def then_by[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=False)

    def then_by_descending[K](self, key: Callable[[T], K]) -> "Enumerable[T]":
        return self._then_by(key, reverse=True)

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

    def shuffle(self) -> "Enumerable[T]":
        def inner() -> Iterator[T]:
            items = list(self)
            shuffle(items)
            yield from items

        return Enumerable(inner())

    def of_type[U](self, target_type: type[U]) -> "Enumerable[U]":
        return (
            cast("Enumerable[T]", self)
            .where(lambda item: isinstance(item, target_type))
            .map(lambda item: cast(U, item))
        )

    def to_array(self) -> list[T]:
        return cast("Enumerable[T]", self).to_list()

    def to_hashset(self) -> set[T]:
        return set(self)

    @overload
    def to_dictionary[K: Hashable](
        self, key_selector: Callable[[T], K]
    ) -> dict[K, T]: ...

    @overload
    def to_dictionary[K: Hashable, V](
        self, key_selector: Callable[[T], K], element_selector: Callable[[T], V]
    ) -> dict[K, V]: ...

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

    @overload
    def to_lookup[K: Hashable](
        self, key_selector: Callable[[T], K]
    ) -> dict[K, list[T]]: ...

    @overload
    def to_lookup[K: Hashable, V](
        self, key_selector: Callable[[T], K], element_selector: Callable[[T], V]
    ) -> dict[K, list[V]]: ...

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

    @overload
    def first_or_default(
        self, default: None = None, *, predicate: Callable[[T], bool] | None = None
    ) -> T | None: ...

    @overload
    def first_or_default[U](
        self, default: U, *, predicate: Callable[[T], bool] | None = None
    ) -> T | U: ...

    def first_or_default(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).first(predicate, default=default)

    @overload
    def last_or_default(
        self, default: None = None, *, predicate: Callable[[T], bool] | None = None
    ) -> T | None: ...

    @overload
    def last_or_default[U](
        self, default: U, *, predicate: Callable[[T], bool] | None = None
    ) -> T | U: ...

    def last_or_default(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).last(predicate, default=default)

    @overload
    def single_or_default(
        self, default: None = None, *, predicate: Callable[[T], bool] | None = None
    ) -> T | None: ...

    @overload
    def single_or_default[U](
        self, default: U, *, predicate: Callable[[T], bool] | None = None
    ) -> T | U: ...

    def single_or_default(
        self, default: object = None, *, predicate: Callable[[T], bool] | None = None
    ) -> object:
        return cast("Enumerable[T]", self).single(predicate, default=default)

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

    @overload
    def element_at_or_default(self, index: int) -> T | None: ...

    @overload
    def element_at_or_default[U](self, index: int, default: U) -> T | U: ...

    def element_at_or_default(self, index: int, default: object = None) -> object:
        if index < 0:
            items = cast("Enumerable[T]", self).to_list()
            return items[index] if -index <= len(items) else default
        return cast("Enumerable[T]", self).nth(index, default=default)

    def long_count(self) -> int:
        return cast("Enumerable[T]", self).count()

    def try_get_non_enumerated_count(self) -> Option[int]:
        count = self.value.non_enumerated_count()
        return Some(count) if count is not None else Null
