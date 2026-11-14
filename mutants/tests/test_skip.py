from python_linq import *
import itertools


class TestSkip:
    def test_default_skips_one(self):
        assert Enumerable([1, 2, 3]).skip().to_list() == [2, 3]

    def test_skip_n(self):
        assert Enumerable([1, 2, 3, 4, 5]).skip(3).to_list() == [4, 5]

    def test_skip_zero(self):
        assert Enumerable([1, 2, 3]).skip(0).to_list() == [1, 2, 3]

    def test_skip_equal_to_length(self):
        assert Enumerable([1, 2, 3]).skip(3).to_list() == []

    def test_skip_more_than_length(self):
        assert Enumerable([1, 2, 3]).skip(10).to_list() == []

    def test_skip_on_empty(self):
        assert Enumerable[object]([]).skip(2).to_list() == []

    def test_is_lazy_on_infinite_iterable(self):
        assert Enumerable(itertools.count()).skip(5).first() == 5

    def test_skip_exhausts_correctly(self):
        enumerable = Enumerable(range(10))
        assert enumerable.skip(3).first() == 3
