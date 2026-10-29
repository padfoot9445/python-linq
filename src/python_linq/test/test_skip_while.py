from .. import *


class TestSkipWhile:
    def test_skips_leading_matches(self):
        assert Enumerable([1, 2, 3, 1]).skip_while(lambda x: x < 3).to_list() == [3, 1]

    def test_nothing_matches(self):
        assert Enumerable([5, 6]).skip_while(lambda x: x < 3).to_list() == [5, 6]

    def test_everything_matches(self):
        assert Enumerable([1, 2]).skip_while(lambda x: x < 3).to_list() == []

    def test_empty(self):
        assert Enumerable[object]([]).skip_while(lambda x: True).to_list() == []
