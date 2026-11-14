from python_linq import *


class TestCast:
    def test_cast_preserves_items(self):
        assert Enumerable([1, 2, 3]).cast(str).to_list() == [1, 2, 3]
