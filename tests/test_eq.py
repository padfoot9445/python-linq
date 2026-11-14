from python_linq import *


class TestEq:
    def test_eq(self):
        assert not Enumerable(range(10)).eq(Enumerable(range(11)))
        assert Enumerable(range(10)).eq(Enumerable(range(10)))

    def test_eq_longer_self_is_not_equal(self):
        assert not Enumerable([1, 2, 3]).eq(Enumerable([1, 2]))
        assert not Enumerable([1, 2]).eq(Enumerable([1, 2, 3]))

    def test_eq_empty(self):
        assert Enumerable[int]([]).eq(Enumerable[int]([]))
        assert not Enumerable([1]).eq(Enumerable[int]([]))
        assert not Enumerable[int]([]).eq(Enumerable([1]))

    def test_eq_accepts_any_iterable(self):
        assert Enumerable([1, 2, 3]).eq([1, 2, 3])

    def test_eq_with_comparer(self):
        assert Enumerable([1, 2]).eq(["1", "2"], comparer=lambda a, b: str(a) == b)

    def test_eq_length_mismatch_does_not_call_comparer_on_padding(self):
        compared = []
        comparer = lambda left, right: compared.append((left, right)) or True

        assert not Enumerable([1]).eq([1, 2], comparer=comparer)
        assert compared == [(1, 1)]

        compared.clear()
        assert not Enumerable([1, 2]).eq([1], comparer=comparer)
        assert compared == [(1, 1)]

    def test_neq_longer_self(self):
        assert Enumerable([1, 2, 3]).neq(Enumerable([1, 2]))
