from .. import *


class TestTakeWhileLossless:
    def test_takes_leading_matches(self):
        assert Enumerable([1, 2, 3, 4, 1]).take_while_lossless(
            lambda x: x < 4
        ).to_list() == [1, 2, 3]

    def test_all_match(self):
        assert Enumerable([1, 2, 3]).take_while_lossless(
            lambda x: x < 10
        ).to_list() == [1, 2, 3]

    def test_none_match(self):
        assert Enumerable([5, 6]).take_while_lossless(lambda x: x < 3).to_list() == []

    def test_empty(self):
        assert (
            Enumerable[object]([]).take_while_lossless(lambda x: True).to_list() == []
        )

    def test_failing_item_is_not_lost(self):
        enumerable = Enumerable(iter([1, 2, 3, 4, 5]))
        assert enumerable.take_while_lossless(lambda x: x < 3).to_list() == [1, 2]
        assert enumerable.to_list() == [3, 4, 5]
