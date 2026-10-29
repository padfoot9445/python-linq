from python_linq import *


class TestTee:
    def test_tee_preserves_items_and_calls_callback(self):
        seen: list[int] = []
        enumerable = Enumerable([1, 2, 3]).tee(seen.append)

        assert seen == []
        assert enumerable.to_list() == [1, 2, 3]
        assert seen == [1, 2, 3]
