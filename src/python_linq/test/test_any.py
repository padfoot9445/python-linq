from .. import *


class TestAny:
    def test_any(self):
        assert Enumerable(range(10)).any(lambda x: x == 3)
        assert not Enumerable(range(10)).any(lambda x: x == 100)
