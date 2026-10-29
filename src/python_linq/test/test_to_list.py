from .. import *


class TestToList:
    def test_to_list_returns_correct(self):
        for items in ([1, 2, 3], [], [1]):
            copy = items.copy()
            assert Enumerable(items).to_list() == copy
