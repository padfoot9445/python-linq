import pytest

from python_linq import DROP, Enumerable


def test_composition_is_lazy_and_preserves_order():
    assert Enumerable([1, 2]).append(3).to_list() == [1, 2, 3]
    assert Enumerable([2, 3]).prepend(1).to_list() == [1, 2, 3]
    assert Enumerable([1]).concat([2, 3]).to_list() == [1, 2, 3]
    assert Enumerable([1]).chain([2, 3]).to_list() == [1, 2, 3]


def test_filter_map_discards_drop_sentinel_and_flatten_flattens_one_level():
    assert Enumerable([0, 1, 2]).filter_map(
        lambda value: str(value) if value else DROP
    ).to_list() == ["1", "2"]
    assert Enumerable([[1, 2], [], [3]]).flatten().to_list() == [1, 2, 3]


def test_distinct_supports_unhashable_keys_and_preserves_first_occurrences():
    values = Enumerable([{"id": 1}, {"id": 1}, {"id": 2}])

    assert values.distinct(key=lambda item: item["id"]).to_list() == [
        {"id": 1},
        {"id": 2},
    ]


def test_contains_and_sequence_equal_accept_comparers():
    assert Enumerable([1, 2]).contains(2)
    assert Enumerable([1, 2]).contains(
        "2", comparer=lambda item, value: str(item) == value
    )
    assert Enumerable([1, 2]).sequence_equal(
        [1, "2"], comparer=lambda a, b: str(a) == str(b)
    )
    assert not Enumerable([1, 2]).sequence_equal([1])


def test_any_without_predicate_handles_none_as_an_item():
    assert Enumerable([None]).any()
    assert not Enumerable[object]([]).any()
    assert Enumerable([1, 2]).any(lambda item: item == 2)


def test_nth_and_find_support_defaults():
    assert Enumerable([1, 2, 3]).nth(1) == 2
    assert Enumerable([1, 2, 3]).nth(9, default=None) is None
    assert Enumerable([1, 2, 3]).find(lambda item: item > 1) == 2
    assert Enumerable([1, 2, 3]).find(lambda item: item > 9, default=None) is None
    with pytest.raises(ValueError):
        Enumerable([1]).nth(-1)


def test_take_last_and_chunk():
    assert Enumerable(range(5)).take_last(2).to_list() == [3, 4]
    assert Enumerable(range(5)).chunk(2).to_list() == [[0, 1], [2, 3], [4]]
    with pytest.raises(ValueError):
        Enumerable([1]).chunk(0)


def test_group_by_order_by_and_default_if_empty():
    assert Enumerable([1, 2, 3]).group_by(lambda value: value % 2).to_list() == [
        (1, [1, 3]),
        (0, [2]),
    ]
    assert Enumerable([3, 1, 2]).order_by().to_list() == [1, 2, 3]
    assert Enumerable([{"n": 2}, {"n": 1}]).order_by(
        key=lambda item: item["n"]
    ).to_list() == [{"n": 1}, {"n": 2}]
    assert Enumerable[int]([]).default_if_empty(42).to_list() == [42]
    assert Enumerable[int]([]).default_if_empty().to_list() == [None]
    assert Enumerable[int]([]).default_if_empty(None).to_list() == [None]


def test_numeric_terminals_and_reduce():
    assert Enumerable([1, 2, 3]).sum() == 6
    assert Enumerable([1, 2, 3]).average() == 2.0
    assert Enumerable([1, 2, 3]).min() == 1
    assert Enumerable([1, 2, 3]).max() == 3
    assert Enumerable([1, 2, 3]).reduce(lambda acc, item: acc + item) == 6
    with pytest.raises(ValueError):
        Enumerable[int]([]).average()
