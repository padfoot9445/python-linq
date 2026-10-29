from .. import *


class TestSkipLast:
    def test_skip_last_one(self):
        assert Enumerable([1, 2, 3, 4, 5]).skip_last(1).to_list() == [1, 2, 3, 4]

    def test_skip_last_two(self):
        assert Enumerable([1, 2, 3, 4, 5]).skip_last(2).to_list() == [1, 2, 3]

    def test_skip_last_zero(self):
        assert Enumerable([1, 2, 3]).skip_last(0).to_list() == [1, 2, 3]

    def test_skip_last_all(self):
        assert Enumerable([1, 2, 3]).skip_last(3).to_list() == []

    def test_skip_last_exceeds_length(self):
        assert Enumerable([1, 2, 3]).skip_last(5).to_list() == []
