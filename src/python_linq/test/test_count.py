from .. import *


class TestCount:
    def test_count_returns_correct(self):
        for items in ([1, 2, 3], [], [1]):
            assert Enumerable(items).count() == len(items)
