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

    def test_adaptor_created_before_copy_uses_original_branch(self):
        source = Enumerable([1, 2, 3])
        mapped = source.map(lambda item: item)

        assert source.is_empty() is False
        assert mapped.to_list() == [1, 2, 3]

    def test_iterator_in_progress_survives_copy(self):
        source = Enumerable([1, 2, 3])
        observed = []

        for item in source:
            observed.append(item)
            if item == 1:
                copy = source.shallow_copy()
                assert copy.to_list() == [2, 3]

        assert observed == [1, 2, 3]

    def test_peek_and_is_empty_inside_loop_do_not_skip_items(self):
        source = Enumerable([1, 2, 3])
        observed = []

        for item in source:
            observed.append(item)
            if item == 1:
                assert source.peek() == 2
                assert source.is_empty() is False

        assert observed == [1, 2, 3]
