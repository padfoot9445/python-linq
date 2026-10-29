from .. import *


class TestEq:
    def test_eq(self):
        assert not Enumerable(range(10)).eq(Enumerable(range(11)))
        assert Enumerable(range(10)).eq(Enumerable(range(10)))
