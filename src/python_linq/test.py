from typing import Iterable, cast

lazy from .take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase

from . import *

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


def test_control_flow():
    j = (i for i in range(10000))
    assert Enumerable(j).control_flow(
        lambda x: (
            ControlFlow.skip()
            if x <= 10
            else (ControlFlow[int].ok(x) if x <= 20 else ControlFlow.stop())
        )
    ).to_list() == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert next(j) == 22


def test_skip_while_and_take_while():
    assert Enumerable(range(10000000000)).skip_while(lambda x: x < 5).take_while(
        lambda x: x < 10
    ).to_list() == [5, 6, 7, 8, 9]


def test_skip_and_take():
    assert Enumerable(range(100000000)).skip(10).take(10).to_list() == [
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
    ]


def test_no_copy():
    j = (i for i in range(10))
    x1 = Enumerable(j)
    x2 = x1
    assert x1.to_list() == list(range(10))
    assert x2.to_list() == []


def test_copy():
    j = (i for i in range(10))
    x1 = Enumerable(j)
    x2 = x1.shallow_copy()
    assert x1.to_list() == list(range(10))
    assert x2.to_list() == list(range(10))


def test_peek():
    x = Enumerable((i for i in range(10)))
    assert x.peek() == 0
    assert x.peek_n(4).to_list() == [0, 1, 2, 3]
    assert x.peek_while(lambda y: y < 8).to_list() == list(range(8))
    assert x.to_list() == list(range(10))


def test_zip():
    assert Enumerable(range(10)).zip(range(2, 5)).to_list() == list(
        zip(range(10), range(2, 5))
    )


def test_all():
    assert Enumerable(range(10)).all(lambda x: x >= 0)
    assert not Enumerable(range(10)).all(lambda x: x >= 5)


def test_any():
    assert Enumerable(range(10)).any(lambda x: x == 3)
    assert not Enumerable(range(10)).any(lambda x: x == 100)


def test_neq():
    assert Enumerable(range(10)).neq(Enumerable(range(11)))
    assert not Enumerable(range(10)).neq(Enumerable(range(10)))


def test_eq():

    assert not Enumerable(range(10)).eq(Enumerable(range(11)))
    assert Enumerable(range(10)).eq(Enumerable(range(10)))
