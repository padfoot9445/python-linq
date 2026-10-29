from python_linq import *


class TestCopy:
    def test_no_copy(self):
        source = (i for i in range(10))
        first = Enumerable(source)
        second = first
        assert first.to_list() == list(range(10))
        assert second.to_list() == []

    def test_copy(self):
        source = (i for i in range(10))
        first = Enumerable(source)
        second = first.shallow_copy()
        assert first.to_list() == list(range(10))
        assert second.to_list() == list(range(10))
