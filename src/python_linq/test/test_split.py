import itertools

import pytest

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
        result = Enumerable[int]([]).split(0).map(list)
        assert result.single() == []

    def test_split_separator_at_end(self):
        segments = list(Enumerable([1, 2, 0]).split(0))
        assert len(segments) == 2
        assert segments[0].to_list() == [1, 2]
        assert segments[1].is_empty()


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
        result = Enumerable[int]([]).split_multiple([0]).map(list)
        assert result.single() == []


class TestSplitStreaming:
    def test_infinite_source_yields_segments(self):
        source = itertools.cycle([1, 2, 0])
        assert Enumerable(source).split(0).take(3).map(list).to_list() == [[1, 2]] * 3

    def test_segment_emitted_as_soon_as_separator_is_read(self):
        consumed: list[int] = []

        def source():
            for x in [1, 2, 0, 3, 4, 0, 5]:
                consumed.append(x)
                yield x

        segments = iter(Enumerable(source()).split(0))
        assert next(segments).to_list() == [1, 2]
        assert consumed == [1, 2, 0]  # nothing read past the separator
        assert next(segments).to_list() == [3, 4]
        assert consumed == [1, 2, 0, 3, 4, 0]

    def test_nothing_consumed_until_iterated(self):
        consumed: list[int] = []

        def source():
            for x in [1, 0, 2]:
                consumed.append(x)
                yield x

        Enumerable(source()).split(0)
        assert consumed == []

    def test_empty_separator_returns_correct(self):
        assert Enumerable([1, 2, 3]).split_multiple([]).map(list).to_list() == [
            [1],
            [2],
            [3],
        ]

    def test_overlapping_separator_is_non_overlapping(self):
        # mirrors "aaa".split("aa") == ["", "a"]
        assert Enumerable([1, 1, 1]).split_multiple([1, 1]).map(list).to_list() == [
            [],
            [1],
        ]

    def test_partial_match_prefix_is_kept(self):
        result = Enumerable([1, 2, 1, 2, 3, 9]).split_multiple([1, 2, 3])
        assert result.map(list).to_list() == [[1, 2], [9]]

    def test_only_separator_gives_two_empty_segments(self):
        assert Enumerable([0]).split(0).map(list).to_list() == [[], []]
