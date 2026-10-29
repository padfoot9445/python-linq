from .. import *


class TestReverse:
    def test_reverse_returns_correct(self):
        assert Enumerable([3, 2, 1]).reverse().to_list() == [1, 2, 3]

    def test_reverse_empty(self):
        assert Enumerable([]).reverse().to_list() == []

    def test_reverse_single(self):
        assert Enumerable([5]).reverse().to_list() == [5]

    def test_reverse_two_elements(self):
        assert Enumerable([10, 20]).reverse().to_list() == [20, 10]
