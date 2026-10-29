from .. import *
import pytest
from ..take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase
import itertools


class TestFirst:
    def test_returns_first_item(self):
        assert Enumerable([1, 2, 3]).first() == 1

    def test_with_predicate(self):
        assert Enumerable([1, 2, 3, 4]).first(lambda x: x > 2) == 3

    def test_empty_raises_not_enough_items(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).first()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_predicate_with_no_match_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).first(lambda x: x > 10)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_only_consumes_one_item(self):
        it = iter([1, 2, 3])
        assert Enumerable(it).first() == 1
        assert next(it) == 2

    def test_works_on_infinite_iterable(self):
        assert Enumerable(itertools.count(5)).first() == 5

    def test_default_on_empty(self):
        assert Enumerable[int]([]).first(default=99) == 99

    def test_default_with_predicate_no_match(self):
        assert Enumerable([1, 2, 3]).first(lambda x: x > 10, default=99) == 99

    def test_default_ignored_when_item_exists(self):
        assert Enumerable([1, 2]).first(default=99) == 1

    def test_none_is_a_valid_default(self):
        assert Enumerable[int]([]).first(default=None) is None

    def test_falsy_default_is_returned(self):
        assert Enumerable[int]([]).first(default=0) == 0

    def test_first_with_filter_returns_correct(self):
        assert Enumerable([1, 2, 3]).first(lambda x: x == 2) == 2

    def test_first_empty_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).first()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems

    def test_first_with_filter_no_match_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 3]).first(lambda x: x == 2)
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
