import itertools

import pytest
from rustshed import Null, Some

from python_linq import DROP, Enumerable, Ordering


def test_rust_adaptors_are_lazy_and_preserve_none():
    assert Enumerable([None, 1, None]).step_by(2).to_list() == [None, None]
    assert Enumerable([None, 1]).intersperse(None).to_list() == [None, None, 1]

    calls = []
    assert Enumerable([1, 2, 3]).intersperse_with(
        lambda: calls.append("separator") or 0
    ).to_list() == [1, 0, 2, 0, 3]
    assert calls == ["separator", "separator"]

    assert Enumerable([1, 2, 3]).map_while(
        lambda item: None if item == 1 else item if item == 2 else DROP
    ).to_list() == [None, 2]
    assert Enumerable([0, 1, 2]).find_map(
        lambda item: None if item == 0 else item if item == 1 else DROP
    ) == Some(None)

    seen = []
    assert Enumerable([None, 1]).inspect(seen.append).to_list() == [None, 1]
    assert seen == [None, 1]
    assert Enumerable([None, 1]).cycle().take(5).to_list() == [None, 1, None, 1, None]
    assert Enumerable([]).cycle().take(3).to_list() == []
    assert list(itertools.islice(Enumerable([1, 2]).fuse(), 3)) == [1, 2]


def test_rust_chunk_and_window_adaptors():
    assert Enumerable([None, 1, 2, 3, 4]).array_chunks(2).to_list() == [
        [None, 1],
        [2, 3],
    ]
    assert Enumerable([1, 2, 3, 4]).map_windows(
        3, lambda window: tuple(window)
    ).to_list() == [(1, 2, 3), (2, 3, 4)]
    assert Enumerable([1, 2, 3]).array_chunks(2).to_list() == [[1, 2]]
    with pytest.raises(ValueError):
        Enumerable([1]).array_chunks(0)
    with pytest.raises(ValueError):
        Enumerable([1]).map_windows(0, tuple)


def test_rust_terminals_and_comparisons_use_tagged_results():
    values = Enumerable([None, 2, 3])
    assert values.next() == Some(None)
    assert values.next_chunk(2).items == [2, 3]
    assert values.next_chunk(2).complete is False
    assert Enumerable([1, 2]).advance_by(3).remaining == 1
    assert Enumerable([1, 2]).position(lambda item: item == 2) == Some(1)
    assert Enumerable([1, 2, 1]).rposition(lambda item: item == 1) == Some(2)
    assert Enumerable([None]).min_by_key(lambda _: 0) == Some(None)
    assert Enumerable([]).max_by_key(lambda item: item) == Null
    assert Enumerable([1, 3, 2]).max_by(lambda a, b: a - b) == Some(3)
    assert Enumerable([1, 3, 2]).min_by(lambda a, b: a - b) == Some(1)
    assert Enumerable([1, 2]).product() == 2
    assert Enumerable([]).product() == 1

    assert Enumerable([1, 2]).cmp([1, 3]) is Ordering.Less
    assert Enumerable([1, 2]).cmp([1, 2]) is Ordering.Equal
    assert Enumerable([1, 3]).cmp([1, 2]) is Ordering.Greater
    assert Enumerable([1, 2]).partial_cmp([1, None]) == Null
    assert Enumerable([1, 2]).eq_by([1, 2], lambda left, right: left == right)
    assert Enumerable([1, 2]).lt([1, 3])
    assert Enumerable([1, 2]).le([1, 2])
    assert Enumerable([1, 3]).gt([1, 2])
    assert Enumerable([1, 3]).ge([1, 3])
    assert Enumerable([1, 2, 2]).is_sorted()
    assert not Enumerable([1, 3, 2]).is_sorted()
    assert Enumerable([None, 1]).is_sorted_by_key(lambda item: 0 if item is None else 1)


def test_rust_partition_and_collection_helpers():
    visited = []
    Enumerable([None, 1, 2]).for_each(visited.append)
    assert visited == [None, 1, 2]
    assert Enumerable([None, 1, 2]).partition(lambda item: item is not None) == (
        [1, 2],
        [None],
    )
    assert Enumerable([1, 2, 3]).is_partitioned(lambda item: item < 3)
    assert not Enumerable([1, 3, 2]).is_partitioned(lambda item: item < 3)

    target: list[int] = [0]
    assert Enumerable([1, 2]).collect_into(target) is target
    assert target == [0, 1, 2]
    borrowed = Enumerable([1, 2, 3])
    assert borrowed.by_ref().take(2).to_list() == [1, 2]
    assert borrowed.to_list() == [3]


def test_linq_set_operators_use_equality_and_preserve_order():
    assert Enumerable([None, 1, None, 2]).union([2, 3, None]).to_list() == [
        None,
        1,
        2,
        3,
    ]
    assert Enumerable([1, 2, 1, 3]).except_([2, 4, 2]).to_list() == [1, 3]
    assert Enumerable([1, 2, 1, 3]).intersect([3, 1, 3]).to_list() == [1, 3]
    assert Enumerable([{"k": 1}, {"k": 2}]).union_by(
        [{"k": 2}, {"k": 3}], lambda item: item["k"]
    ).to_list() == [{"k": 1}, {"k": 2}, {"k": 3}]
    assert Enumerable([{"k": 1}, {"k": 2}]).except_by(
        [2], lambda item: item["k"]
    ).to_list() == [{"k": 1}]
    assert Enumerable([{"k": 1}, {"k": 2}]).intersect_by(
        [2], lambda item: item["k"]
    ).to_list() == [{"k": 2}]
    assert Enumerable(["A", "a", "B"]).distinct_by(
        str.lower, comparer=lambda left, right: left == right
    ).to_list() == ["A", "B"]


def test_linq_count_aggregate_and_stable_secondary_ordering():
    assert Enumerable([None, 1, None]).count(lambda item: item is None) == 2
    assert Enumerable(["ant", "ape", "bee"]).count_by(
        lambda item: item[0]
    ).to_list() == [("a", 2), ("b", 1)]
    assert Enumerable(["A", "a", "B"]).count_by(
        lambda item: item, comparer=lambda left, right: left.lower() == right.lower()
    ).to_list() == [("A", 2), ("B", 1)]
    assert Enumerable([("a", 1), ("b", 2), ("a", 3)]).aggregate_by(
        lambda item: item[0], 0, lambda total, item: total + item[1]
    ).to_list() == [("a", 4), ("b", 2)]
    assert Enumerable([("a", 1), ("b", 2)]).aggregate_by_seed_selector(
        lambda item: item[0],
        lambda group: len(group),
        lambda total, item: total + item[1],
    ).to_list() == [("a", 2), ("b", 3)]
    assert Enumerable([("A", 1), ("a", 2)]).aggregate_by(
        lambda item: item[0],
        0,
        lambda total, item: total + item[1],
        comparer=lambda left, right: left.lower() == right.lower(),
    ).to_list() == [("A", 3)]

    assert Enumerable([("a", 2), ("b", 1), ("a", 1)]).order_by(
        key=lambda item: item[0]
    ).then_by(lambda item: item[1]).to_list() == [("a", 1), ("a", 2), ("b", 1)]
    assert Enumerable([("a", 1), ("a", 2), ("b", 1)]).order_by(
        key=lambda item: item[0]
    ).then_by_descending(lambda item: item[1]).to_list() == [
        ("a", 2),
        ("a", 1),
        ("b", 1),
    ]
    assert Enumerable([3, 1, 2]).order_descending().to_list() == [3, 2, 1]
    assert Enumerable([1, 2]).order().to_list() == [1, 2]
    assert Enumerable([1, 2]).order_by_descending().to_list() == [2, 1]
    with pytest.raises(TypeError, match="requires a sequence produced by order_by"):
        Enumerable([1, 2]).then_by(lambda item: item)


def test_linq_joins_keep_absence_distinct_from_none_data():
    assert Enumerable([("a", 1), ("b", None)]).join_on(
        [("a", 10), ("b", 20)],
        lambda item: item[0],
        lambda item: item[0],
        lambda outer, inner: (outer[1], inner[1]),
    ).to_list() == [(1, 10), (None, 20)]
    assert Enumerable([("a", 1), ("b", 2)]).group_join(
        [("a", 10), ("a", 11)],
        lambda item: item[0],
        lambda item: item[0],
        lambda outer, matches: (outer[0], [item[1] for item in matches]),
    ).to_list() == [("a", [10, 11]), ("b", [])]

    left = (
        Enumerable([("a", None), ("b", 2)])
        .left_join(
            [("a", None), ("c", 3)],
            lambda item: item[0],
            lambda item: item[0],
        )
        .to_list()
    )
    assert left == [(("a", None), Some(("a", None))), (("b", 2), Null)]

    right = (
        Enumerable([("a", 1)])
        .right_join(
            [("a", None), ("b", 2)],
            lambda item: item[0],
            lambda item: item[0],
        )
        .to_list()
    )
    assert right == [(Some(("a", 1)), ("a", None)), (Null, ("b", 2))]

    full = (
        Enumerable([("a", None)])
        .full_join(
            [("a", 1), ("b", 2)],
            lambda item: item[0],
            lambda item: item[0],
        )
        .to_list()
    )
    assert full == [
        (Some(("a", None)), Some(("a", 1))),
        (Null, Some(("b", 2))),
    ]


def test_linq_collection_conversion_and_default_operators():
    assert Enumerable([1, 2]).to_array() == [1, 2]
    assert Enumerable([1, 2]).to_hashset() == {1, 2}
    assert Enumerable([("a", 1), ("b", 2)]).to_dictionary(
        lambda item: item[0], lambda item: item[1]
    ) == {"a": 1, "b": 2}
    assert Enumerable([None, 1, None]).to_lookup(lambda item: item).keys() == {
        None,
        1,
    }
    assert Enumerable([None, 1, "x"]).of_type(int).to_list() == [1]
    assert Enumerable([]).first_or_default() is None
    assert Enumerable([]).last_or_default(default=3) == 3
    assert Enumerable([]).single_or_default(default=None) is None
    assert Enumerable([1, 2, 3]).element_at(-1) == 3
    assert Enumerable([1, 2, 3]).element_at_or_default(10) is None
    assert Enumerable([1, 2, 3]).long_count() == 3
    assert Enumerable([1, 2, 3]).sum(lambda item: item * 2) == 12
    assert Enumerable([1, 2, 3]).average(lambda item: item * 2) == 4.0

    with pytest.raises(ValueError, match="duplicate key"):
        Enumerable([("x", 1), ("x", 2)]).to_dictionary(lambda item: item[0])


def test_linq_factories_are_lazy_sequences():
    assert Enumerable.empty().to_list() == []
    assert Enumerable.range(3, 4).to_list() == [3, 4, 5, 6]
    assert Enumerable.repeat(None, 3).to_list() == [None, None, None]
    assert Enumerable.sequence(2, 4, step=3).to_list() == [2, 5, 8, 11]
    assert Enumerable.infinite_sequence(5, 2).take(4).to_list() == [5, 7, 9, 11]
    with pytest.raises(ValueError):
        Enumerable.range(0, -1)


def test_additional_linq_overloads_and_rust_unzip():
    assert Enumerable(["ant", "ape", "bee"]).group_by(
        lambda item: item[0],
        lambda item: len(item),
        lambda key, values: (key, sum(values)),
    ).to_list() == [("a", 6), ("b", 3)]
    assert Enumerable([[1], [1, 2], [3]]).group_by(
        len, comparer=lambda left, right: left == right
    ).to_list() == [(1, [[1], [3]]), (2, [[1, 2]])]
    assert Enumerable(["ant", "ape"]).group_by(
        lambda item: item[0],
        result_selector=lambda key, values: (key, len(values)),
    ).to_list() == [("a", 2)]

    assert Enumerable([None, 1, 2]).select_many(
        lambda item: [item, item], lambda outer, inner: (outer, inner)
    ).to_list() == [
        (None, None),
        (None, None),
        (1, 1),
        (1, 1),
        (2, 2),
        (2, 2),
    ]
    assert Enumerable([(None, 1), (2, None)]).unzip() == ([None, 2], [1, None])
    assert (
        Enumerable([1, 2, 3]).aggregate(
            0, lambda total, item: total + item, lambda total: total * 2
        )
        == 12
    )
    assert Enumerable([1, 2, 3]).aggregate(lambda left, right: left + right) == 6

    assert (
        Enumerable([None, 1, 2]).first_or_default(predicate=lambda item: item == 1) == 1
    )
    assert (
        Enumerable([None, 1, 2]).last_or_default(
            default="empty", predicate=lambda item: item is None
        )
        is None
    )
    assert (
        Enumerable([1, 2, 3]).single_or_default(
            default="empty", predicate=lambda item: item == 4
        )
        == "empty"
    )


def test_indexed_operators_and_parity_operators_are_deferred():
    source_events = []
    right_events = []

    def left_source():
        for value in (1, 2):
            source_events.append(value)
            yield value

    def right_source():
        for value in (2, 3):
            right_events.append(value)
            yield value

    combined = Enumerable(left_source()).union(right_source())
    assert source_events == []
    assert right_events == []
    assert next(iter(combined)) == 1
    assert source_events == [1]
    assert right_events == []
    assert list(combined) == [2, 3]
    assert source_events == [1, 2]
    assert right_events == [2, 3]

    ordered_events = []

    def ordering_source():
        ordered_events.append("started")
        yield from [("b", 1), ("a", 2), ("a", 1)]

    ordered = (
        Enumerable(ordering_source())
        .order_by(key=lambda item: item[0])
        .then_by(lambda item: item[1])
    )
    assert ordered_events == []
    assert ordered.to_list() == [("a", 1), ("a", 2), ("b", 1)]
    assert ordered_events == ["started"]

    assert Enumerable(["a", "bb", "ccc"]).select_indexed(
        lambda item, index: (index, item)
    ).to_list() == [(0, "a"), (1, "bb"), (2, "ccc")]
    assert Enumerable(["a", "bb", "ccc"]).skip_while_indexed(
        lambda item, index: index < 2
    ).to_list() == ["ccc"]
    assert Enumerable(["a", "bb", "ccc"]).take_while_indexed(
        lambda item, index: index < 2
    ).to_list() == ["a", "bb"]
