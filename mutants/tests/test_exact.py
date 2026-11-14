import pytest

from python_linq import *


class TestExact:
    def test_exact_equal(self):
        assert Enumerable([1, 2, 3]).exact(3).to_list() == [1, 2, 3]

    def test_exact_less_than_length_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).exact(10).to_list()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems
        assert "at least 10" in str(exc.value)
        assert "only 3" in str(exc.value)

    def test_exact_more_than_length_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable(list(range(10))).exact(3).to_list()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
        assert "at most 3" in str(exc.value)

    def test_exact_with_default_fills_shortfall(self):
        result = Enumerable([1, 2]).exact(5, default=99)
        assert result.to_list() == [1, 2, 99, 99, 99]

    def test_exact_single_element(self):
        assert Enumerable([42]).exact(1).to_list() == [42]

    def test_exact_zero_does_not_raise(self):
        result = Enumerable[int]([]).exact(0)
        assert result.to_list() == []
