from python_linq import *
import itertools


class TestTakeWhileLossy:
    def test_stops_at_first_failure_and_drops_it(self):
        assert Enumerable([1, 2, 5, 1]).take_while_lossy(lambda x: x < 3).to_list() == [
            1,
            2,
        ]

    def test_all_match(self):
        assert Enumerable([1, 2]).take_while_lossy(lambda x: x < 3).to_list() == [1, 2]

    def test_none_match(self):
        assert Enumerable([5, 6]).take_while_lossy(lambda x: x < 3).to_list() == []

    def test_empty(self):
        assert Enumerable[object]([]).take_while_lossy(lambda x: True).to_list() == []

    def test_infinite_iterable(self):
        assert Enumerable(itertools.count()).take_while_lossy(
            lambda x: x < 3
        ).to_list() == [0, 1, 2]
