from python_linq import *


class TestFlatMap:
    def test_flat_map_enumerable_returns_correct(self):
        assert Enumerable(range(5)).flat_map(lambda x: (1, x)).to_list() == [
            1,
            0,
            1,
            1,
            1,
            2,
            1,
            3,
            1,
            4,
        ]
