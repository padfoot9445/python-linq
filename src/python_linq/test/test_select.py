from .. import *


class TestSelect:
    def test_select_enumerable_returns_correct(self):
        assert Enumerable(range(5)).select(lambda x: x**2).to_list() == [0, 1, 4, 9, 16]
