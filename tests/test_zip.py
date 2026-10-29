from python_linq import *


class TestZip:
    def test_zip(self):
        assert Enumerable(range(10)).zip(range(2, 5)).to_list() == list(
            zip(range(10), range(2, 5))
        )
