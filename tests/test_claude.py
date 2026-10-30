"""Contract tests for python_linq, derived from the API reference and parity matrix.

Written from the documentation alone. Tests in ``TestUndocumentedChoices`` and
the ``xfail`` hazards pin down behavior the docs leave open: adjust them to
whatever you decide the contract should be.
"""

from __future__ import annotations

import pathlib
import random
import re
import statistics

import pytest
from rustshed import Null, Some

from python_linq import (
    DROP,
    AdvanceByResult,
    ControlFlow,
    Enumerable,
    NextChunkResult,
    Ordering,
    TakeEnumerableException,
)

E = Enumerable


class Spy:
    """Iterable that records how many times iter() was called."""

    def __init__(self, items):
        self.items = list(items)
        self.iter_calls = 0

    def __iter__(self):
        self.iter_calls += 1
        return iter(self.items)


# --------------------------------------------------------------------------
# Core model: single pass
# --------------------------------------------------------------------------
class TestCoreModel:
    def test_constructor_calls_iter_exactly_once_immediately(self):
        spy = Spy([1, 2])
        e = E(spy)
        assert spy.iter_calls == 1
        e.to_list()
        assert spy.iter_calls == 1

    def test_same_instance_resumes_cursor(self):
        e = E([1, 2, 3])
        assert e.take(2).to_list() == [1, 2]
        assert e.to_list() == [3]

    def test_derived_sequences_are_not_replayable(self):
        mapped = E([1, 2]).map(lambda x: x * 2)
        assert mapped.to_list() == [2, 4]
        assert mapped.to_list() == []

    def test_default_constructor_is_empty(self):
        assert E().to_list() == []

    def test_shallow_copy_branches_are_independent(self):
        e = E([None, 2, 3])
        c = e.shallow_copy()
        assert c.first() is None
        assert e.first() is None
        assert c.to_list() == [2, 3]
        assert e.to_list() == [2, 3]

    def test_by_ref_is_same_object_and_shares_cursor(self):
        e = E([1, 2, 3, 4])
        r = e.by_ref()
        assert r is e
        assert r.take(2).to_list() == [1, 2]
        assert e.to_list() == [3, 4]

    def test_generic_marker_does_not_validate(self):
        assert E[int](["not", "ints"]).to_list() == ["not", "ints"]

    def test_adaptor_created_before_is_empty_loses_nothing(self):
        e = E([1, 2, 3])
        mapped = e.map(lambda x: x)
        assert e.is_empty() is False
        assert mapped.to_list() == [1, 2, 3]

    def test_repeated_is_empty_does_not_blow_up(self):
        # HAZARD: each call tees; nested tee layers could degrade/recurse.
        e = E(range(10_000))
        for _ in range(3_000):
            assert e.is_empty() is False
        assert e.count() == 10_000


# --------------------------------------------------------------------------
# Creation
# --------------------------------------------------------------------------
class TestCreation:
    def test_range_uses_start_and_count(self):
        assert E.range(4, 3).to_list() == [4, 5, 6]
        assert E.range(0, 0).to_list() == []

    def test_negative_counts_raise(self):
        with pytest.raises(ValueError):
            E.range(0, -1).to_list()
        with pytest.raises(ValueError):
            E.repeat("x", -1).to_list()
        with pytest.raises(ValueError):
            E.sequence(0, -1).to_list()

    def test_repeat_keeps_none(self):
        assert E.repeat(None, 2).to_list() == [None, None]

    def test_sequence_and_infinite_sequence(self):
        assert E.sequence(2, 3, step=4).to_list() == [2, 6, 10]
        assert E.infinite_sequence(5, 2).take(4).to_list() == [5, 7, 9, 11]

    def test_empty(self):
        assert E.empty().to_list() == []


# --------------------------------------------------------------------------
# Projection and filtering
# --------------------------------------------------------------------------
class TestProjection:
    def test_where_and_filter_are_aliases(self):
        assert E([1, 2, 3, 4]).where(lambda n: n % 2 == 0).to_list() == [2, 4]
        assert E([1, 2, 3, 4]).filter(lambda n: n % 2 == 0).to_list() == [2, 4]

    def test_select_keeps_none_results(self):
        assert E([1, 2]).select(lambda n: None).to_list() == [None, None]

    def test_select_indexed_passes_item_then_index(self):
        assert E("ab").select_indexed(lambda item, i: (i, item)).to_list() == [
            (0, "a"),
            (1, "b"),
        ]

    def test_filter_map_only_drops_DROP(self):
        out = E([1, 2, 3]).filter_map(
            lambda n: None if n == 1 else n if n == 2 else DROP
        )
        assert out.to_list() == [None, 2]

    def test_map_while_stops_on_DROP_but_keeps_None(self):
        out = E([1, 2, 3, 4]).map_while(
            lambda n: DROP if n == 3 else None if n == 1 else n
        )
        assert out.to_list() == [None, 2]

    def test_flat_map_and_select_many(self):
        assert E([1, 2]).flat_map(lambda n: [n, n]).to_list() == [1, 1, 2, 2]
        assert E([1, 2]).select_many(
            lambda n: [n * 10, n * 100], lambda outer, inner: (outer, inner)
        ).to_list() == [(1, 10), (1, 100), (2, 20), (2, 200)]

    def test_flat_map_non_iterable_raises_type_error(self):
        with pytest.raises(TypeError):
            E([1]).flat_map(lambda n: None).to_list()
        with pytest.raises(TypeError):
            E([None]).flatten().to_list()

    def test_flatten_one_level_only(self):
        assert E([[1, [2]], [3]]).flatten().to_list() == [1, [2], 3]

    def test_flatten_splits_strings_into_chars(self):
        # Python-correct, but a footgun worth pinning.
        assert E(["ab", "c"]).flatten().to_list() == ["a", "b", "c"]

    def test_distinct_supports_unhashable_and_keeps_first_order(self):
        assert E([[1], [2], [1], [3]]).distinct().to_list() == [[1], [2], [3]]

    def test_distinct_by_with_comparer(self):
        rows = [{"id": 1}, {"id": 1}, {"id": 2}]
        assert E(rows).distinct_by(lambda r: r["id"]).to_list() == [
            {"id": 1},
            {"id": 2},
        ]
        out = E(["a", "A", "b"]).distinct_by(
            lambda s: s, comparer=lambda x, y: x.lower() == y.lower()
        )
        assert out.to_list() == ["a", "b"]

    def test_of_type_is_runtime_isinstance(self):
        assert E([None, "x", 3]).of_type(int).to_list() == [3]

    def test_of_type_int_matches_bool(self):
        assert E([True, 1, "a"]).of_type(int).to_list() == [True, 1]

    def test_inspect_and_tee_are_lazy_and_pass_through(self):
        seen: list[int] = []
        it = E([1, 2, 3]).inspect(seen.append)
        assert seen == []
        assert it.take(2).to_list() == [1, 2]
        assert seen == [1, 2]
        seen2: list[int] = []
        assert E([1, 2]).tee(seen2.append).to_list() == [1, 2]
        assert seen2 == [1, 2]

    def test_cast_does_not_validate_or_convert(self):
        assert E(["1"]).cast(int).to_list() == ["1"]


# --------------------------------------------------------------------------
# Composition
# --------------------------------------------------------------------------
class TestComposition:
    def test_append_prepend_concat(self):
        assert E([1, 2]).prepend(0).append(3).concat([4]).to_list() == [0, 1, 2, 3, 4]
        assert E([1]).chain([2]).to_list() == [1, 2]

    def test_concat_does_not_enter_other_until_exhausted(self):
        spy = Spy([9])
        out = E([1]).concat(spy).take(1).to_list()
        assert out == [1]
        assert spy.iter_calls == 0

    def test_zip(self):
        assert E([None, 2]).zip(["m", "two"]).to_list() == [(None, "m"), (2, "two")]
        assert E([1, 2, 3]).zip([1]).to_list() == [(1, 1)]

    def test_zip_strict_raises_on_length_mismatch(self):
        with pytest.raises(ValueError):
            E([1, 2]).zip([1], strict=True).to_list()

    def test_enumerate_is_lazy_index_first(self):
        assert E("ab").enumerate().to_list() == [(0, "a"), (1, "b")]

    def test_default_if_empty(self):
        assert E[int]([]).default_if_empty(7).to_list() == [7]
        assert E[int]([]).default_if_empty().to_list() == [None]
        assert E[int]([]).default_if_empty(None).to_list() == [None]
        assert E([None]).default_if_empty(7).to_list() == [None]


# --------------------------------------------------------------------------
# Lazy adaptors
# --------------------------------------------------------------------------
class TestAdaptors:
    def test_step_by(self):
        assert E(range(7)).step_by(3).to_list() == [0, 3, 6]

    @pytest.mark.parametrize("bad", [0, -1])
    def test_step_by_validates_at_call_time(self, bad):
        with pytest.raises(ValueError):
            E([1]).step_by(bad)

    def test_intersperse_between_only_and_preserves_none(self):
        assert E([None, 1, 2]).intersperse(None).to_list() == [None, None, 1, None, 2]
        assert E([]).intersperse(0).to_list() == []
        assert E([1]).intersperse(0).to_list() == [1]

    def test_intersperse_with_calls_only_between_items(self):
        calls = []
        out = E([1, 2, 3]).intersperse_with(lambda: calls.append(1) or 0).to_list()
        assert out == [1, 0, 2, 0, 3]
        assert len(calls) == 2
        calls.clear()
        E([1]).intersperse_with(lambda: calls.append(1) or 0).to_list()
        assert calls == []

    def test_cycle(self):
        assert E([1, 2]).cycle().take(5).to_list() == [1, 2, 1, 2, 1]
        assert E([]).cycle().take(3).to_list() == []

    def test_fuse_stops_permanently(self):
        class Flaky:
            def __init__(self):
                self.calls = 0

            def __iter__(self):
                return self

            def __next__(self):
                self.calls += 1
                if self.calls == 2:
                    raise StopIteration
                return self.calls

        fused = E(Flaky()).fuse()
        assert fused.to_list() == [1]
        assert fused.to_list() == []

    def test_array_chunks_drops_incomplete_tail(self):
        assert E([1, 2, 3, 4, 5]).array_chunks(2).to_list() == [[1, 2], [3, 4]]

    def test_map_windows(self):
        assert E([1, 2, 3, 4]).map_windows(3, sum).to_list() == [6, 9]
        assert E([1, 2]).map_windows(3, sum).to_list() == []

    @pytest.mark.parametrize("name", ["array_chunks", "chunk"])
    def test_non_positive_sizes_validated_at_call_time(self, name):
        with pytest.raises(ValueError):
            getattr(E([1]), name)(0)

    def test_chunk_includes_short_final_chunk(self):
        assert E([1, 2, 3]).chunk(2).to_list() == [[1, 2], [3]]


# --------------------------------------------------------------------------
# Slicing, peeking, splitting
# --------------------------------------------------------------------------
class TestSlicing:
    def test_take_skip(self):
        assert E([1, 2, 3]).take(2).to_list() == [1, 2]
        assert E([1, 2, 3]).skip(2).to_list() == [3]
        assert E([1, 2, 3]).take().to_list() == [1]  # default n=1

    def test_negative_take_skip_rejected(self):
        with pytest.raises(ValueError):
            E([1]).take(-1)
        with pytest.raises(ValueError):
            E([1]).skip(-1)

    def test_take_zero_does_not_consume(self):
        e = E([1, 2])
        assert e.take(0).to_list() == []
        assert e.to_list() == [1, 2]

    def test_islice_step_must_be_positive(self):
        assert E(range(10)).islice(1, 8, 3).to_list() == [1, 4, 7]
        with pytest.raises(ValueError):
            E(range(3)).islice(0, 3, 0)

    def test_take_last_skip_last(self):
        assert E([1, 2, 3]).take_last(2).to_list() == [2, 3]
        assert E([1, 2, 3]).skip_last(1).to_list() == [1, 2]
        with pytest.raises(ValueError):
            E([1]).take_last(-1).to_list()
        with pytest.raises(ValueError):
            E([1]).skip_last(-1).to_list()

    def test_take_last_zero_does_not_consume(self):
        e = E([1, 2])
        assert e.take_last(0).to_list() == []
        assert e.to_list() == [1, 2]

    def test_take_while_variants_on_remaining_cursor(self):
        lt3 = lambda n: n < 3  # noqa: E731
        e = E([1, 2, 3, 4])
        assert e.take_while(lt3).to_list() == [1, 2]
        assert e.to_list() == [4]
        e = E([1, 2, 3, 4])
        assert e.take_while_lossy(lt3).to_list() == [1, 2]
        assert e.to_list() == [4]
        e = E([1, 2, 3, 4])
        assert e.take_while_inclusive(lt3).to_list() == [1, 2, 3]
        assert e.to_list() == [4]
        e = E([1, 2, 3, 4])
        assert e.take_while_lossless(lt3).to_list() == [1, 2]
        assert e.to_list() == [3, 4]

    def test_take_while_lossless_abandoned_midway(self):
        e = E([1, 2, 3, 4])
        view = e.take_while_lossless(lambda n: n < 4)
        assert next(iter(view)) == 1
        assert e.to_list() == [2, 3, 4]

    def test_indexed_variants(self):
        assert E("abcd").take_while_indexed(lambda item, i: i < 2).to_list() == [
            "a",
            "b",
        ]
        assert E("abcd").skip_while_indexed(lambda item, i: i < 2).to_list() == [
            "c",
            "d",
        ]

    def test_skip_while(self):
        assert E([1, 2, 3, 1]).skip_while(lambda n: n < 3).to_list() == [3, 1]


class TestPeeking:
    def test_peek_does_not_consume(self):
        e = E([1, 2])
        assert e.peek() == 1
        assert e.to_list() == [1, 2]

    def test_peek_empty_raises(self):
        with pytest.raises(TakeEnumerableException):
            E([]).peek()

    def test_try_peek_distinguishes_present_none(self):
        assert E([None]).try_peek() == Some(None)
        assert E([]).try_peek() == Null
        assert Some(None) != Null

    def test_peek_n_and_peek_while_are_non_consuming(self):
        e = E([None, 4, 5])
        assert e.peek_n(2).to_list() == [None, 4]
        assert e.peek_n(0).to_list() == []
        assert e.peek_n(-3).to_list() == []
        assert e.peek_while(lambda x: x is None or x < 5).to_list() == [None, 4]
        assert e.to_list() == [None, 4, 5]

    def test_is_empty_does_not_advance(self):
        e = E([1])
        assert e.is_empty() is False
        assert e.to_list() == [1]
        assert e.is_empty() is True


class TestSplit:
    @staticmethod
    def parts(enum):
        return [p.to_list() for p in enum]

    def test_split_no_args_yields_singletons(self):
        assert self.parts(E([1, 2]).split()) == [[1], [2]]
        assert self.parts(E([]).split()) == []

    def test_split_on_separator_keeps_empty_segments(self):
        assert self.parts(E([1, 0, 0, 2, 0]).split(0)) == [[1], [], [2], []]
        assert self.parts(E([0, 1]).split(0)) == [[], [1]]

    def test_split_empty_input_with_separator_gives_one_empty_segment(self):
        assert self.parts(E([]).split(0)) == [[]]

    def test_split_none_is_a_real_separator_not_the_omitted_marker(self):
        assert self.parts(E([1, None, 2]).split(None)) == [[1], [2]]

    def test_split_multiple(self):
        assert self.parts(E([None, 1, None]).split_multiple([None])) == [[], [1], []]
        assert self.parts(E([1, 2]).split_multiple([])) == [[1], [2]]


# --------------------------------------------------------------------------
# Grouping, sets, ordering, joins
# --------------------------------------------------------------------------
class TestGroupingAndSets:
    def test_group_by_order_and_unhashable_keys(self):
        out = E(["ant", "ape", "bee"]).group_by(lambda w: w[0]).to_list()
        assert out == [("a", ["ant", "ape"]), ("b", ["bee"])]
        out = E([1, 2, 3, 4]).group_by(lambda n: [n % 2]).to_list()
        assert out == [([1], [1, 3]), ([0], [2, 4])]

    def test_group_by_none_key_is_a_group(self):
        assert E([None, 1, None]).group_by(lambda x: x).to_list() == [
            (None, [None, None]),
            (1, [1]),
        ]

    def test_group_by_element_selector_and_comparer(self):
        out = E(["a", "A", "b"]).group_by(
            lambda s: s,
            element_selector=lambda s: s.upper(),
            comparer=lambda x, y: x.lower() == y.lower(),
        )
        assert out.to_list() == [("a", ["A", "A"]), ("b", ["B"])]

    def test_count_by(self):
        assert E(["ant", "ape", "bee"]).count_by(lambda w: w[0]).to_list() == [
            ("a", 2),
            ("b", 1),
        ]

    def test_aggregate_by(self):
        out = E(["a", "bb", "c"]).aggregate_by(len, 0, lambda acc, _: acc + 1)
        assert out.to_list() == [(1, 2), (2, 1)]

    def test_aggregate_by_seed_selector_called_once_per_key(self):
        seeds = []

        def seed(key):
            seeds.append(key)
            return []

        out = E(["a", "bb", "c"]).aggregate_by_seed_selector(
            len, seed, lambda acc, x: acc + [x]
        )
        assert out.to_list() == [(1, ["a", "c"]), (2, ["bb"])]
        assert seeds == [1, 2]

    def test_union_streams_first_source_before_second(self):
        spy = Spy([3])
        assert E([1, 2]).union(spy).take(1).to_list() == [1]
        assert spy.iter_calls == 0

    def test_union_keeps_order_and_none(self):
        assert E([None, 1, None]).union([1, None, 2]).to_list() == [None, 1, 2]
        assert E([[1]]).union([[1], [2]]).to_list() == [[1], [2]]

    def test_union_by(self):
        assert E(["a", "b"]).union_by(["B", "c"], str.lower).to_list() == [
            "a",
            "b",
            "c",
        ]

    def test_except_and_intersect_preserve_first_source_order(self):
        assert E([3, 1, 2, 1]).except_([2]).to_list() == [3, 1]
        assert E([3, 1, 2, 1]).intersect([1, 3]).to_list() == [3, 1]
        assert E([[1], [2]]).except_([[1]]).to_list() == [[2]]
        assert E(["a", "bb"]).except_by([1], len).to_list() == ["bb"]
        assert E(["a", "bb"]).intersect_by([1], len).to_list() == ["a"]

    def test_except_buffers_second_only_when_iteration_starts(self):
        spy = Spy([2])
        out = E([1, 2, 3]).except_(spy)
        assert spy.iter_calls == 0
        assert out.take(1).to_list() == [1]
        assert spy.iter_calls == 1


class TestOrdering:
    def test_order_by_is_stable(self):
        rows = [("a", 2), ("b", 1), ("a", 1)]
        assert E(rows).order_by(key=lambda r: r[0]).to_list() == [
            ("a", 2),
            ("a", 1),
            ("b", 1),
        ]

    def test_order_by_descending_keeps_input_order_for_ties(self):
        rows = [("a", 1), ("b", 2), ("c", 1), ("d", 2)]
        out = E(rows).order_by_descending(key=lambda r: r[1]).to_list()
        assert out == [("b", 2), ("d", 2), ("a", 1), ("c", 1)]
        out2 = E(rows).order_by(key=lambda r: r[1], reverse=True).to_list()
        assert out2 == out

    def test_then_by_and_descending(self):
        rows = [("a", 2), ("b", 1), ("a", 1)]
        out = E(rows).order_by(key=lambda r: r[0]).then_by(lambda r: r[1]).to_list()
        assert out == [("a", 1), ("a", 2), ("b", 1)]
        out = (
            E(rows)
            .order_by(key=lambda r: r[0])
            .then_by_descending(lambda r: r[1])
            .to_list()
        )
        assert out == [("a", 2), ("a", 1), ("b", 1)]

    def test_then_by_requires_ordered_source(self):
        with pytest.raises(TypeError):
            E([1, 2]).then_by(lambda x: x)
        with pytest.raises(TypeError):
            E([1, 2]).map(lambda x: x).then_by(lambda x: x)

    def test_order_and_order_descending(self):
        assert E([2, 3, 1]).order().to_list() == [1, 2, 3]
        assert E([2, 3, 1]).order_descending().to_list() == [3, 2, 1]

    def test_none_without_key_raises_type_error(self):
        with pytest.raises(TypeError):
            E([None, 1]).order_by().to_list()

    def test_order_by_is_deferred(self):
        spy = Spy([2, 1])
        out = E(spy).order_by()
        assert out.to_list() == [1, 2]

    def test_reverse_and_shuffle(self):
        assert E([1, 2, 3]).reverse().to_list() == [3, 2, 1]
        random.seed(0)
        out = E(range(20)).shuffle().to_list()
        assert sorted(out) == list(range(20))


class TestJoins:
    outer = [("x", None), ("y", 2)]

    def test_join_on_inner(self):
        out = E([1, 2, 3]).join_on(
            [(2, "b"), (3, "c"), (3, "cc")],
            lambda o: o,
            lambda i: i[0],
            lambda o, i: (o, i[1]),
        )
        assert out.to_list() == [(2, "b"), (3, "c"), (3, "cc")]

    def test_group_join_gives_list_per_outer(self):
        out = E([1, 2]).group_join(
            [(1, "a"), (1, "b")], lambda o: o, lambda i: i[0], lambda o, g: (o, g)
        )
        assert out.to_list() == [(1, [(1, "a"), (1, "b")]), (2, [])]

    def test_left_join_uses_some_and_null(self):
        out = (
            E(self.outer)
            .left_join([("x", 10)], lambda r: r[0], lambda r: r[0])
            .to_list()
        )
        assert out == [(("x", None), Some(("x", 10))), (("y", 2), Null)]

    def test_right_join_uses_some_and_null(self):
        out = E([1]).right_join([1, 2], lambda o: o, lambda i: i).to_list()
        assert (Some(1), 1) in out
        assert (Null, 2) in out

    def test_full_join_includes_unmatched_on_both_sides(self):
        out = E([1, 2]).full_join([2, 3], lambda o: o, lambda i: i).to_list()
        assert len(out) == 3
        assert (Some(2), Some(2)) in out
        assert (Some(1), Null) in out
        assert (Null, Some(3)) in out

    def test_none_keys_match_each_other_documented(self):
        # Documented here, but DIFFERS from LINQ, which ignores null keys in joins.
        out = E([None]).join_on([None], lambda o: o, lambda i: i, lambda o, i: "hit")
        assert out.to_list() == ["hit"]

    def test_join_is_aggregate_fold_not_relational(self):
        assert E(["a", "b", "c"]).join(",") == "a,b,c"
        assert E(["a"]).join(",") == "a"
        with pytest.raises(Exception):
            E([]).join(",")


# --------------------------------------------------------------------------
# Terminals
# --------------------------------------------------------------------------
class TestSelection:
    def test_first(self):
        assert E([None, 3]).first() is None
        assert E([1, 2, 3]).first(lambda n: n > 1) == 2
        assert E([]).first(default=None) is None

    def test_first_missing_raises_not_enough_items(self):
        with pytest.raises(TakeEnumerableException) as ei:
            E([]).first()
        assert ei.value.exception_case.name == "NotEnoughItems"
        with pytest.raises(TakeEnumerableException):
            E([1]).first(lambda n: n > 5)

    def test_single(self):
        assert E([5]).single() == 5
        assert E([]).single(default=0) == 0
        with pytest.raises(TakeEnumerableException) as ei:
            E([1, 2]).single(default=0)
        assert ei.value.exception_case.name == "TooManyItems"

    def test_last_consumes_everything(self):
        e = E([1, 2, 3])
        assert e.last() == 3
        assert e.to_list() == []
        with pytest.raises(TakeEnumerableException):
            E([]).last()
        assert E([]).last(default=9) == 9

    def test_or_default_family(self):
        assert E([]).first_or_default() is None
        assert E([]).first_or_default(5) == 5
        assert E([1, 2]).first_or_default(predicate=lambda n: n > 1) == 2
        assert E([1, 2]).last_or_default(predicate=lambda n: n < 2) == 1
        assert E([]).single_or_default(7) == 7
        with pytest.raises(TakeEnumerableException):
            E([1, 2]).single_or_default()

    def test_first_or_default_positional_lambda_is_a_default_not_a_predicate(self):
        # FOOTGUN (LINQ habit): the lambda is silently used as `default`.
        assert E([1]).first_or_default(lambda n: n > 5) == 1
        assert callable(E([]).first_or_default(lambda n: n > 5))

    def test_nth_and_element_at(self):
        assert E([10, 20, 30]).nth(1) == 20
        with pytest.raises(ValueError):
            E([1]).nth(-1)
        with pytest.raises(TakeEnumerableException):
            E([1]).nth(3)
        assert E([1]).nth(3, default=0) == 0
        assert E([10, 20, 30]).element_at(-1) == 30
        with pytest.raises(TakeEnumerableException):
            E([1]).element_at(5)
        assert E([1]).element_at_or_default(5) is None
        assert E([1]).element_at_or_default(5, "d") == "d"

    def test_find_is_first_with_predicate(self):
        assert E([1, 2, 3]).find(lambda n: n > 1) == 2
        assert E([1]).find(lambda n: n > 5, default=None) is None


class TestPredicatesAndCounting:
    def test_count(self):
        assert E([None, 3]).count(lambda x: x is None) == 1
        assert E([1, 2, 3]).count() == 3
        assert E([1, 2]).long_count() == 2

    def test_all_any(self):
        assert E([]).all(lambda x: False) is True
        assert E([]).any() is False
        assert E([0]).any() is True
        assert E([1, 2]).any(lambda n: n > 1) is True

    def test_all_short_circuits(self):
        e = E([1, 2, 3, 4])
        assert e.all(lambda n: n < 2) is False
        assert e.to_list() == [3, 4]

    def test_contains_comparer_receives_item_then_value(self):
        seen = []

        def cmp(item, value):
            seen.append((item, value))
            return item == value

        assert E([1, 2]).contains(2, comparer=cmp) is True
        assert seen[0] == (1, 2)


class TestAggregation:
    def test_fold_reduce(self):
        assert E([1, 2, 3]).fold(lambda t, x: t + x, seed=0) == 6
        assert E([1, 2, 3]).fold(lambda t, x: t + x) == 6
        assert E([1, 2, 3]).reduce(lambda t, x: t + x) == 6
        with pytest.raises(TakeEnumerableException):
            E([]).fold(lambda t, x: t + x)
        assert E([]).fold(lambda t, x: t + x, seed=0) == 0

    def test_aggregate_overloads(self):
        assert E([1, 2, 3]).aggregate(lambda a, b: a + b) == 6
        assert E([1, 2, 3]).aggregate(10, lambda a, b: a + b) == 16
        assert E([1, 2, 3]).aggregate(0, lambda a, b: a + b, lambda r: r * 2) == 12

    def test_scan(self):
        add = lambda a, b: a + b  # noqa: E731
        assert E([1, 2, 3]).scan(add, seed=0).to_list() == [0, 1, 3, 6]
        assert E([1, 2, 3]).scan(add).to_list() == [1, 3, 6]
        assert E([]).scan(add, seed=0).to_list() == [0]
        with pytest.raises(TakeEnumerableException):
            E([]).scan(add).to_list()

    def test_numeric_empties(self):
        assert E([]).sum() == 0
        assert E([]).product() == 1
        with pytest.raises(statistics.StatisticsError):
            E([]).average()
        with pytest.raises(ValueError):
            E([]).min()
        with pytest.raises(ValueError):
            E([]).max()

    def test_numeric_selectors(self):
        assert E(["a", "bb"]).sum(len) == 3
        assert E([1, 2]).average() == 1.5
        assert E(["a", "bbb"]).max(key=len) == "bbb"

    def test_eq_neq_and_comparers(self):
        assert E([1, 2]).eq([1, 2]) is True
        assert E([1, 2]).eq([1]) is False
        assert E([1]).neq([2]) is True
        assert E(["a"]).sequence_equal(
            ["A"], comparer=lambda x, y: x.lower() == y.lower()
        )
        assert E([1]).eq_by(["1"], lambda a, b: str(a) == b) is True

    def test_cmp_family(self):
        assert E([1, 2]).cmp([1, 3]) is Ordering.Less
        assert E([1, 2]).cmp([1, 2]) is Ordering.Equal
        assert E([1, 3]).cmp([1, 2]) is Ordering.Greater
        assert E([1]).cmp([1, 0]) is Ordering.Less
        assert E([1, "a"]).partial_cmp([1, 2]) == Null
        assert E([1, 2]).lt([1, 3]) and E([1, 2]).le([1, 2])
        assert E([2]).gt([1, 9]) and E([2]).ge([2])
        assert Ordering.Less == -1 and Ordering.Greater == 1 and Ordering.Equal == 0

    def test_is_sorted_family(self):
        assert E([1, 2, 2]).is_sorted() is True
        assert E([2, 1]).is_sorted() is False
        assert E([]).is_sorted() is True
        assert E(["a", "bb"]).is_sorted_by_key(len) is True
        assert E([1, 2]).is_sorted_by(lambda a, b: None) is False

    def test_min_max_by_return_option(self):
        assert E([]).max_by_key(len) == Null
        assert E(["a", "bbb", "cc"]).max_by_key(len) == Some("bbb")
        assert E(["a", "bbb", "cc"]).min_by_key(len) == Some("a")
        assert E([3, 1, 2]).max_by(lambda a, b: a - b) == Some(3)
        assert E([]).min_by(lambda a, b: a - b) == Null


class TestUndocumentedChoices:
    """Behavior the docs leave open. Decide, then pin."""

    def test_max_by_key_tie_returns_first_like_linq(self):
        # Rust's max_by_key returns the LAST maximum element.
        assert E(["aa", "bb"]).max_by_key(len) == Some("aa")

    def test_min_by_key_tie_returns_first(self):
        assert E(["aa", "bb"]).min_by_key(len) == Some("aa")

    def test_to_lookup_missing_key_raises_key_error(self):
        # LINQ ILookup returns an empty sequence instead.
        lookup = E([1]).to_lookup(lambda x: x)
        with pytest.raises(KeyError):
            lookup[99]


# --------------------------------------------------------------------------
# Rust-style operations
# --------------------------------------------------------------------------
class TestRustStyle:
    def test_next(self):
        e = E([None, 2, 3])
        assert e.next() == Some(None)
        assert E([]).next() == Null

    def test_next_chunk(self):
        e = E([1, 2, 3])
        assert e.next_chunk(2) == NextChunkResult(items=[1, 2], complete=True)
        assert e.next_chunk(2) == NextChunkResult(items=[3], complete=False)
        with pytest.raises(ValueError):
            E([1]).next_chunk(0)

    def test_advance_by(self):
        e = E([1, 2, 3])
        assert e.advance_by(2) == AdvanceByResult(complete=True, remaining=0)
        assert e.advance_by(5) == AdvanceByResult(complete=False, remaining=4)
        with pytest.raises(ValueError):
            E([1]).advance_by(-1)

    def test_position_and_rposition_count_from_front(self):
        assert E([5, 6, 5]).position(lambda n: n == 5) == Some(0)
        assert E([5, 6, 5]).rposition(lambda n: n == 5) == Some(2)
        assert E([1]).position(lambda n: n == 9) == Null
        assert E([1]).rposition(lambda n: n == 9) == Null

    def test_partition_unzip_collect_into_for_each(self):
        assert E([None, 1]).partition(lambda x: x is not None) == ([1], [None])
        assert E([(1, "a"), (2, "b")]).unzip() == ([1, 2], ["a", "b"])
        target = [0]
        assert E([1, 2]).collect_into(target) is target
        assert target == [0, 1, 2]
        out = []
        E([1, 2]).for_each(out.append)
        assert out == [1, 2]

    def test_is_partitioned_short_circuits(self):
        assert E([1, 1, 2]).is_partitioned(lambda n: n == 1) is True
        e = E([2, 1, 3, 4])
        assert e.is_partitioned(lambda n: n == 1) is False
        assert e.to_list() == [3, 4]
        e = E([1, 2, 1, 9, 9])
        assert e.is_partitioned(lambda n: n == 1) is False
        assert e.to_list() == [9, 9]


# --------------------------------------------------------------------------
# Conversions
# --------------------------------------------------------------------------
class TestConversions:
    def test_to_list_array_hashset(self):
        assert E([1, 2]).to_list() == [1, 2]
        assert E([1, 2]).to_array() == [1, 2]
        assert E([1, 2, 2]).to_hashset() == {1, 2}
        with pytest.raises(TypeError):
            E([[1]]).to_hashset()

    def test_to_dictionary(self):
        assert E([("a", 1), ("b", 2)]).to_dictionary(
            lambda p: p[0], lambda p: p[1]
        ) == {"a": 1, "b": 2}
        with pytest.raises(ValueError):
            E([1, 1]).to_dictionary(lambda x: x)
        with pytest.raises(TypeError):
            E([[1]]).to_dictionary(lambda x: x)

    def test_to_lookup(self):
        assert E([None, 1]).to_lookup(lambda x: x) == {None: [None], 1: [1]}
        assert E([1, 3, 2]).to_lookup(lambda x: x % 2) == {1: [1, 3], 0: [2]}

    def test_try_get_non_enumerated_count(self):
        assert E([1, 2, 3]).try_get_non_enumerated_count() == Null

        class SizedIter:
            def __iter__(self):
                return self

            def __next__(self):
                raise StopIteration

            def __len__(self):
                return 4

        e = E(SizedIter())
        assert e.try_get_non_enumerated_count() == Some(4)


# --------------------------------------------------------------------------
# ControlFlow
# --------------------------------------------------------------------------
class TestControlFlow:
    data = [1, 2, 3, 4]

    def run(self, on_two):
        return (
            E(self.data)
            .control_flow(lambda n: on_two(n) if n == 2 else ControlFlow.ok(n))
            .to_list()
        )

    def test_ok(self):
        assert E(self.data).control_flow(ControlFlow.ok).to_list() == [1, 2, 3, 4]

    def test_skip(self):
        assert self.run(lambda n: ControlFlow.skip()) == [1, 3, 4]

    def test_stop(self):
        assert self.run(lambda n: ControlFlow.stop()) == [1]

    def test_stop_ok(self):
        assert self.run(ControlFlow.stop_ok) == [1, 2]

    def test_yield_control_ok_passes_remainder_untouched(self):
        assert self.run(lambda n: ControlFlow.yield_control_ok(20)) == [1, 20, 3, 4]

    def test_yield_control_skip_drops_item_and_remainder(self):
        assert self.run(lambda n: ControlFlow.yield_control_skip("ignored")) == [1]

    def test_none_is_a_valid_payload(self):
        assert E([1]).control_flow(lambda n: ControlFlow.ok(None)).to_list() == [None]


# --------------------------------------------------------------------------
# Docs conformance: parity matrix must stay in sync with the real API
# --------------------------------------------------------------------------
PARITY = pathlib.Path(__file__).parent.parent / "docs" / "API_PARITY.md"

_SKIP_PREFIXES = ("rustshed.", "operator.", "itertools.")


def _table_rows():
    if not PARITY.exists():
        return []
    rows = []
    for line in PARITY.read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if (
            len(cells) < 3
            or set(cells[0]) <= set("-: ")
            or cells[1] == "Current equivalent"
        ):
            continue
        rows.append(cells)
    return rows


def _referenced_methods():
    names = set()
    for cells in _table_rows():
        for token in re.findall(r"`([^`]+)`", cells[1]):
            if token.startswith(_SKIP_PREFIXES):
                continue
            name = re.split(r"[(=]", token)[0].strip()
            if name.startswith("Enumerable."):
                name = name.split(".", 1)[1]
            if name and name != "Enumerable" and name.isidentifier():
                names.add(name)
    return sorted(names)


@pytest.mark.skipif(not PARITY.exists(), reason="API_PARITY.md not found")
@pytest.mark.parametrize("name", _referenced_methods())
def test_every_method_named_in_parity_matrix_exists(name):
    assert hasattr(Enumerable, name), f"{name} is referenced in API_PARITY.md"


@pytest.mark.skipif(not PARITY.exists(), reason="API_PARITY.md not found")
@pytest.mark.xfail(
    strict=True,
    reason="DOC GAP: the .NET table has no rows for Where or Zip",
)
def test_dotnet_table_covers_where_and_zip():
    families = {cells[0].strip("`") for cells in _table_rows()}
    assert {"Where", "Zip"} <= families


@pytest.mark.skipif(not PARITY.exists(), reason="API_PARITY.md not found")
@pytest.mark.xfail(strict=True, reason="DOC GAP: stray checklist line at end of file")
def test_parity_doc_has_no_stray_numbered_fragment():
    last = PARITY.read_text().strip().splitlines()[-1]
    assert not re.match(r"^\d+\.\s", last)
