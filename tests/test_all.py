from python_linq import *


class TestAll:
    def test_all(self):
        assert Enumerable(range(10)).all(lambda x: x >= 0)
        assert not Enumerable(range(10)).all(lambda x: x >= 5)
