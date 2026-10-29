from typing import Iterable, cast

from .take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase
from . import *

import pytest


class TestToList:
    @pytest.mark.parametrize(
        "l",
        [
            ([1, 2, 3]),
            ([]),
            ([1]),
        ],
    )
    def test_to_list_returns_correct[T](self, l: list[T]):
        copy = l.copy()
        assert Enumerable(l).to_list() == copy


class TestCount:
    @pytest.mark.parametrize(
        "l",
        [
            ([1, 2, 3]),
            ([]),
            ([1]),
        ],
    )
    def test_count_returns_correct[T](self, l: list[T]):
        assert Enumerable(l).count() == len(l)


class TestFilter:
    def test_filter_is_correct(self):
        assert all(
            (x % 2) == 0 for x in Enumerable(range(1000)).filter(lambda x: x % 2 == 0)
        )


class TestSelect:
    def test_select_enumerable_returns_correct(self):
        assert Enumerable(range(5)).select(lambda x: x**2).to_list() == [0, 1, 4, 9, 16]


class TestFlatMap:
    def test_flat_map_enumerable_returns_correct(self):
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


class TestFirst:
    def test_first_returns_correct(self):
        assert Enumerable([1, 2, 3]).first() == 1

    def test_first_with_filter_returns_correct(self):
        assert Enumerable([1, 2, 3]).first(lambda x: x == 2) == 2

    def test_first_empty_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exception:
            source: list[int] = []
            Enumerable(source).first()
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )

    def test_first_with_filter_no_match_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exception:
            Enumerable([1, 3]).first(lambda x: x == 2)
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )


class TestSingle:
    def test_single_returns_correct(self):
        assert Enumerable([1]).single() == 1

    def test_single_filtered_returns_correct(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x == 2) == 2

    def test_single_empty_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exception:
            source: list[int] = []
            Enumerable(source).single()
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )

    def test_single_with_filter_no_match_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exception:
            Enumerable([1, 3]).single(lambda x: x == 2)
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        )

    def test_single_too_long_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exception:
            source: list[int] = [1, 2, 3]
            Enumerable(source).single()
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
        )

    def test_single_with_filter_too_many_matches_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exception:
            Enumerable([1, 2, 2, 3]).single(lambda x: x == 2)
        assert (
            exception.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
        )


class TestFold:
    def test_fold_returns_expected(self):
        assert Enumerable(range(5)).fold(lambda acc, x: acc + x) == sum(range(5))
        assert Enumerable(range(5)).map(str).fold(
            lambda acc, x: acc + int(x), 0
        ) == sum(range(5))
        assert Enumerable(range(5)).fold(lambda acc, x: acc + x, 5) == sum(range(5)) + 5


class TestJoin:
    def test_join_returns_expected(self):
        assert Enumerable(["a", "b", "c"]).join("d") == "adbdc"


class TestControlFlow:
    def test_control_flow(self):
        j = (i for i in range(10000))
        assert Enumerable(j).control_flow(
            lambda x: (
                ControlFlow.skip()
                if x <= 10
                else (ControlFlow[int].ok(x) if x <= 20 else ControlFlow.stop())
            )
        ).to_list() == list(range(11, 21))
        assert next(j) == 22


class TestSkipWhileAndTakeWhile:
    def test_skip_while_and_take_while(self):
        assert Enumerable(range(10000000000)).skip_while(lambda x: x < 5).take_while(
            lambda x: x < 10
        ).to_list() == [5, 6, 7, 8, 9]


class TestSkipAndTake:
    def test_skip_and_take(self):
        assert Enumerable(range(100000000)).skip(10).take(10).to_list() == list(
            range(10, 20)
        )

    def test_take_exhausts_correctly(self):
        enumerable = Enumerable(range(10))
        enumerable.take(3).to_list()
        assert enumerable.first() == 3


class TestCopy:
    def test_no_copy(self):
        j = (i for i in range(10))
        x1 = Enumerable(j)
        x2 = x1
        assert x1.to_list() == list(range(10))
        assert x2.to_list() == []

    def test_copy(self):
        j = (i for i in range(10))
        x1 = Enumerable(j)
        x2 = x1.shallow_copy()
        assert x1.to_list() == list(range(10))
        assert x2.to_list() == list(range(10))


class TestPeek:
    def test_peek(self):
        x = Enumerable((i for i in range(10)))
        assert x.peek() == 0
        assert x.peek_n(4).to_list() == [0, 1, 2, 3]
        assert x.peek_while(lambda y: y < 8).to_list() == list(range(8))
        assert x.to_list() == list(range(10))


class TestZip:
    def test_zip(self):
        assert Enumerable(range(10)).zip(range(2, 5)).to_list() == list(
            zip(range(10), range(2, 5))
        )


class TestAll:
    def test_all(self):
        assert Enumerable(range(10)).all(lambda x: x >= 0)
        assert not Enumerable(range(10)).all(lambda x: x >= 5)


class TestAny:
    def test_any(self):
        assert Enumerable(range(10)).any(lambda x: x == 3)
        assert not Enumerable(range(10)).any(lambda x: x == 100)


class TestNeq:
    def test_neq(self):
        assert Enumerable(range(10)).neq(Enumerable(range(11)))
        assert not Enumerable(range(10)).neq(Enumerable(range(10)))


class TestEq:
    def test_eq(self):
        assert not Enumerable(range(10)).eq(Enumerable(range(11)))
        assert Enumerable(range(10)).eq(Enumerable(range(10)))
