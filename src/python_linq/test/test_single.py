from .. import *
import pytest
from ..take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase


class TestSingle:
    def test_single_item(self):
        assert Enumerable([42]).single() == 42

    def test_with_predicate(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x == 2) == 2

    def test_empty_raises_not_enough_items(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).single()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_multiple_raises_too_many_items(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2]).single()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_too_many_reports_actual_total(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single()
        assert "3" in str(exc.value)

    def test_predicate_matching_multiple_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3, 4]).single(lambda x: x > 2)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_predicate_matching_none_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single(lambda x: x > 10)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_default_on_empty(self):
        assert Enumerable[object]([]).single(default=99) == 99

    def test_default_with_predicate_no_match(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x > 10, default=99) == 99

    def test_default_ignored_when_exactly_one(self):
        assert Enumerable([5]).single(default=99) == 5

    def test_default_does_not_suppress_too_many(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2]).single(default=99)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_default_with_predicate_does_not_suppress_too_many(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single(lambda x: x > 1, default=99)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_none_is_a_valid_default(self):
        assert Enumerable[object]([]).single(default=None) is None

    def test_single_returns_correct(self):
        assert Enumerable([1]).single() == 1

    def test_single_filtered_returns_correct(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x == 2) == 2

    def test_single_empty_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).single()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems

    def test_single_with_filter_no_match_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 3]).single(lambda x: x == 2)
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems

    def test_single_too_long_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.TooManyItems

    def test_single_with_filter_too_many_matches_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 2, 3]).single(lambda x: x == 2)
        assert exc.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
