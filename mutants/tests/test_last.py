from python_linq import *
import pytest


class TestLast:
    def test_returns_last_item(self):
        assert Enumerable([1, 2, 3]).last() == 3

    def test_single_element(self):
        assert Enumerable([7]).last() == 7

    def test_empty_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).last()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_last_item_may_be_none(self):
        assert Enumerable([1, None]).last() is None

    def test_with_predicate(self):
        assert Enumerable([1, 2, 3, 4, 5]).last(lambda x: x % 2 == 0) == 4

    def test_predicate_with_no_match_raises(self):
        with pytest.raises(TakeEnumerableException):
            Enumerable([1, 2, 3]).last(lambda x: x > 10)

    def test_default_on_empty(self):
        assert Enumerable[object]([]).last(default=99) == 99

    def test_default_with_predicate_no_match(self):
        assert Enumerable([1, 2, 3]).last(lambda x: x > 10, default=99) == 99

    def test_default_ignored_when_items_exist(self):
        assert Enumerable([1, 2, 3]).last(default=99) == 3

    def test_none_is_a_valid_default(self):
        assert Enumerable[object]([]).last(default=None) is None

    def test_falsy_default_is_returned(self):
        assert Enumerable[object]([]).last(default=0) == 0
