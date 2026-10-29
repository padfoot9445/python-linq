from .. import *
import itertools


class TestTake:
    def test_default_takes_one(self):
        assert Enumerable([1, 2, 3]).take().to_list() == [1]

    def test_take_n(self):
        assert Enumerable([1, 2, 3, 4]).take(3).to_list() == [1, 2, 3]

    def test_take_more_than_length(self):
        assert Enumerable([1, 2]).take(10).to_list() == [1, 2]

    def test_take_equal_to_length(self):
        assert Enumerable([1, 2, 3]).take(3).to_list() == [1, 2, 3]

    def test_take_zero(self):
        assert Enumerable([1, 2, 3]).take(0).to_list() == []

    # def test_take_negative(self):
    #     assert Enumerable([1, 2, 3]).take(-1).to_list() == []

    def test_take_on_empty(self):
        assert Enumerable[object]([]).take(3).to_list() == []

    def test_is_lazy_on_infinite_iterable(self):
        assert Enumerable(itertools.count()).take(4).to_list() == [0, 1, 2, 3]

    def test_preserves_falsy_items(self):
        assert Enumerable([0, None, "", False]).take(4).to_list() == [
            0,
            None,
            "",
            False,
        ]

    def test_does_not_overconsume_source(self):
        it = iter([1, 2, 3, 4, 5])
        assert Enumerable(it).take(2).to_list() == [1, 2]
        assert next(it) == 3

    def test_take_zero_does_not_consume_source(self):
        it = iter([1, 2, 3])
        assert Enumerable(it).take(0).to_list() == []
        assert next(it) == 1

    def test_take_exhausts_correctly(self):
        enumerable = Enumerable(range(10))
        enumerable.take(3).to_list()
        assert enumerable.first() == 3

    def test_skip_and_take(self):
        assert Enumerable(range(100000000)).skip(10).take(10).to_list() == list(
            range(10, 20)
        )
