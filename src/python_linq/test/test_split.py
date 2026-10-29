from .. import *


class TestSplit:
    def test_split_with_separator(self):
        segments = list(Enumerable([1, 2, 3, 0, 4, 5, 6]).split(0).map(list))
        assert segments == [[1, 2, 3], [4, 5, 6]]

    def test_split_with_multiple_separators(self):
        segments = list(Enumerable([1, 2, 3, 4, 5]).split_multiple([2, 3]).map(list))
        count = len(segments)
        assert count == 2
        assert segments[0] == [1]
        assert segments[1] == [4, 5]

    def test_split_with_no_separator(self):
        segments = list(Enumerable([1, 2, 3]).split().map(list))
        assert segments == [[1], [2], [3]]

    def test_split_empty(self):
        result = Enumerable[int]([]).split(0)
        count = result.count()
        assert count == 0

    def test_split_separator_at_end(self):
        segments = list(Enumerable([1, 2, 0]).split(0))
        assert len(segments) == 2
        assert segments[0].to_list() == [1, 2]
        assert segments[0].is_empty()


class TestSplitMultiple:
    def test_split_multiple_basic(self):
        segments = list(Enumerable([1, 2, 3, 4, 5]).split_multiple([1, 3]))
        count = len(segments)
        assert count == 1
        assert segments[0].to_list() == [1, 2, 3, 4, 5]

    def test_split_multiple_with_single_element_list(self):
        segments = list(Enumerable([1, 1, 2]).split_multiple([1]))
        # Should split at each occurrence of [1]
        count = len(segments)
        assert count == 3
        assert segments[0].to_list() == []
        assert segments[1].to_list() == []
        assert segments[2].to_list() == [2]

    def test_split_multiple_empty_input(self):
        result = Enumerable[int]([]).split_multiple([0])
        assert result.is_empty()
