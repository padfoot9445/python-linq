from python_linq import *


class TestIsEmpty:
    def test_is_empty_true(self):
        assert Enumerable([]).is_empty() is True

    def test_is_empty_false(self):
        assert Enumerable([1, 2, 3]).is_empty() is False

    def test_is_empty_single_element(self):
        assert Enumerable([42]).is_empty() is False

    def test_is_empty_list_of_Nones(self):
        assert Enumerable([None, None]).is_empty() is False
