from .. import *


class TestFilter:
    def test_filter_is_correct(self):
        assert all(
            x % 2 == 0 for x in Enumerable(range(1000)).filter(lambda x: x % 2 == 0)
        )
