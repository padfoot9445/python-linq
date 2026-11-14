from python_linq import *


class TestNeq:
    def test_neq(self):
        assert Enumerable(range(10)).neq(Enumerable(range(11)))
        assert not Enumerable(range(10)).neq(Enumerable(range(10)))
