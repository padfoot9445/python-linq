from typing import Iterable

lazy from .take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase

lazy from .enumerable import Enumerable
import pytest


@pytest.mark.parametrize(
    "l",
    [
        ([1, 2, 3]),
        ([]),
        ([1]),
    ],
)
def test_to_list_returns_correct[T](l: list[T]):
    copy = l.copy()

    assert Enumerable(l).to_list() == copy


@pytest.mark.parametrize(
    "l",
    [
        ([1, 2, 3]),
        ([]),
        ([1]),
    ],
)
def test_count_returns_correct[T](l: list[T]):
    assert Enumerable(l).count() == len(l)


def test_filter_is_correct():
    assert all(
        (x % 2) == 0 for x in Enumerable(range(1000)).filter(lambda x: x % 2 == 0)
    )


def test_select_enumerable_returns_correct():
    assert Enumerable(range(5)).select(lambda x: x**2).to_list() == [0, 1, 4, 9, 16]


def test_flat_map_enumerable_returns_correct():
    assert Enumerable(range(5)).flat_map(lambda x: (1, x)).to_list() == [
        1,
        0,
        1,
        1,
        1,
        2,
        1,
        3,
        1,
        4,
    ]


def test_first_returns_correct():
    assert Enumerable([1, 2, 3]).first() == 1


def test_first_with_filter_returns_correct():
    assert Enumerable([1, 2, 3]).first(lambda x: x == 2) == 2


def test_first_empty_list_throws():
    with pytest.raises(TakeEnumerableException) as exception:
        source: list[int] = []
        Enumerable(source).first()
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )


def test_first_with_filter_no_match_list_throws():
    with pytest.raises(TakeEnumerableException) as exception:
        Enumerable([1, 3]).first(lambda x: x == 2)
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )


def test_single_returns_correct():
    assert Enumerable([1]).single() == 1


def test_single_filtered_returns_correct():
    assert Enumerable([1, 2, 3]).single(lambda x: x == 2) == 2


def test_single_empty_list_throws():
    with pytest.raises(TakeEnumerableException) as exception:
        source: list[int] = []
        Enumerable(source).single()
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )


def test_single_with_filter_no_match_list_throws():
    with pytest.raises(TakeEnumerableException) as exception:
        Enumerable([1, 3]).single(lambda x: x == 2)
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )


def test_single_too_long_list_throws():
    with pytest.raises(TakeEnumerableException) as exception:
        source: list[int] = [1, 2, 3]
        Enumerable(source).single()
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
        )


def test_single_with_filter_too_many_matches_list_throws():
    with pytest.raises(TakeEnumerableException) as exception:
        Enumerable([1, 2, 2, 3]).single(lambda x: x == 2)
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
        )


def test_fold_returns_expected():
    assert Enumerable(range(5)).fold(lambda acc, x: acc + x) == sum(range(5))
    assert Enumerable(range(5)).map(str).fold(lambda acc, x: acc + int(x), 0) == sum(
        range(5)
    )
    assert Enumerable(range(5)).fold(lambda acc, x: acc + x, 5) == sum(range(5)) + 5


def test_join_returns_expected():
    assert Enumerable(["a", "b", "c"]).join("d") == "adbdc"
