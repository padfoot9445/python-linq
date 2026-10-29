from .. import *


class TestTakeWhileInclusive:
    def test_includes_first_failing_item(self):
        assert Enumerable([1, 2, 5, 1]).take_while_inclusive(
            lambda x: x < 3
        ).to_list() == [1, 2, 5]

    def test_all_match(self):
        assert Enumerable([1, 2]).take_while_inclusive(lambda x: x < 3).to_list() == [
            1,
            2,
        ]

    def test_first_item_fails(self):
        assert Enumerable([5, 1, 2]).take_while_inclusive(
            lambda x: x < 3
        ).to_list() == [5]

    def test_empty(self):
        assert (
            Enumerable[object]([]).take_while_inclusive(lambda x: True).to_list() == []
        )
