from rustshed import Null, Some
from python_linq import *
import pytest
import itertools


class TestPeek:
    def test_peek_returns_next_without_consuming(self):
        enumerable = Enumerable([1, 2, 3])
        assert enumerable.peek() == 1
        assert enumerable.peek() == 1
        assert enumerable.to_list() == [1, 2, 3]

    def test_peek_on_empty_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).peek()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_try_peek_some(self):
        enumerable = Enumerable([1, 2])
        assert enumerable.try_peek() == Some(1)
        assert enumerable.to_list() == [1, 2]

    def test_try_peek_empty_is_null(self):
        assert Enumerable[object]([]).try_peek() == Null

    def test_peek_n(self):
        enumerable = Enumerable([1, 2, 3, 4])
        assert enumerable.peek_n(2).to_list() == [1, 2]
        assert enumerable.to_list() == [1, 2, 3, 4]

    def test_peek_n_more_than_length(self):
        assert Enumerable([1, 2]).peek_n(5).to_list() == [1, 2]

    def test_peek_n_zero(self):
        assert Enumerable([1, 2]).peek_n(0).to_list() == []

    def test_peek_while(self):
        enumerable = Enumerable([1, 2, 3, 1])
        assert enumerable.peek_while(lambda x: x < 3).to_list() == [1, 2]
        assert enumerable.to_list() == [1, 2, 3, 1]

    def test_peek_on_infinite_iterable(self):
        enumerable = Enumerable(itertools.count())
        assert enumerable.peek_n(3).to_list() == [0, 1, 2]
        assert enumerable.first() == 0

    def test_peek_while_returns_matching_prefix(self):
        enumerable = Enumerable((i for i in range(10)))
        assert enumerable.peek() == 0
        assert enumerable.peek_n(4).to_list() == [0, 1, 2, 3]
        assert enumerable.peek_while(lambda x: x < 8).to_list() == list(range(8))
        assert enumerable.to_list() == list(range(10))
