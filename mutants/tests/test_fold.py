from python_linq import *


class TestFold:
    def test_fold_returns_expected(self):
        assert Enumerable(range(5)).fold(lambda acc, x: acc + x) == sum(range(5))
        assert Enumerable(range(5)).map(str).fold(
            lambda acc, x: acc + int(x), 0
        ) == sum(range(5))
        assert Enumerable(range(5)).fold(lambda acc, x: acc + x, 5) == sum(range(5)) + 5
