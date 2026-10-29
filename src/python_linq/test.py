from rustshed import Null, Some

from . import *
import pytest
from .take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase
import itertools


class TestFirst:
    def test_returns_first_item(self):
        assert Enumerable([1, 2, 3]).first() == 1

    def test_with_predicate(self):
        assert Enumerable([1, 2, 3, 4]).first(lambda x: x > 2) == 3

    def test_empty_raises_not_enough_items(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).first()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_predicate_with_no_match_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).first(lambda x: x > 10)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_only_consumes_one_item(self):
        it = iter([1, 2, 3])
        assert Enumerable(it).first() == 1
        assert next(it) == 2

    def test_works_on_infinite_iterable(self):
        assert Enumerable(itertools.count(5)).first() == 5

    def test_default_on_empty(self):
        assert Enumerable[int]([]).first(default=99) == 99

    def test_default_with_predicate_no_match(self):
        assert Enumerable([1, 2, 3]).first(lambda x: x > 10, default=99) == 99

    def test_default_ignored_when_item_exists(self):
        assert Enumerable([1, 2]).first(default=99) == 1

    def test_none_is_a_valid_default(self):
        assert Enumerable[int]([]).first(default=None) is None

    def test_falsy_default_is_returned(self):
        assert Enumerable[int]([]).first(default=0) == 0

    def test_first_with_filter_returns_correct(self):
        assert Enumerable([1, 2, 3]).first(lambda x: x == 2) == 2

    def test_first_empty_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).first()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems

    def test_first_with_filter_no_match_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 3]).first(lambda x: x == 2)
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems


class TestSingle:
    def test_single_item(self):
        assert Enumerable([42]).single() == 42

    def test_with_predicate(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x == 2) == 2

    def test_empty_raises_not_enough_items(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).single()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_multiple_raises_too_many_items(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2]).single()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_too_many_reports_actual_total(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single()
        assert "3" in str(exc.value)

    def test_predicate_matching_multiple_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3, 4]).single(lambda x: x > 2)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_predicate_matching_none_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single(lambda x: x > 10)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_default_on_empty(self):
        assert Enumerable[object]([]).single(default=99) == 99

    def test_default_with_predicate_no_match(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x > 10, default=99) == 99

    def test_default_ignored_when_exactly_one(self):
        assert Enumerable([5]).single(default=99) == 5

    def test_default_does_not_suppress_too_many(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2]).single(default=99)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_default_with_predicate_does_not_suppress_too_many(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single(lambda x: x > 1, default=99)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.TooManyItems

    def test_none_is_a_valid_default(self):
        assert Enumerable[object]([]).single(default=None) is None

    def test_single_returns_correct(self):
        assert Enumerable([1]).single() == 1

    def test_single_filtered_returns_correct(self):
        assert Enumerable([1, 2, 3]).single(lambda x: x == 2) == 2

    def test_single_empty_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).single()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems

    def test_single_with_filter_no_match_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 3]).single(lambda x: x == 2)
        assert exc.value.exception_case is TakeEnumerableExceptionCase.NotEnoughItems

    def test_single_too_long_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 3]).single()
        assert exc.value.exception_case is TakeEnumerableExceptionCase.TooManyItems

    def test_single_with_filter_too_many_matches_list_throws(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable([1, 2, 2, 3]).single(lambda x: x == 2)
        assert exc.value.exception_case is TakeEnumerableExceptionCase.TooManyItems


class TestLast:
    def test_returns_last_item(self):
        assert Enumerable([1, 2, 3]).last() == 3

    def test_single_element(self):
        assert Enumerable([7]).last() == 7

    def test_empty_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).last()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_last_item_may_be_none(self):
        assert Enumerable([1, None]).last() is None

    def test_with_predicate(self):
        assert Enumerable([1, 2, 3, 4, 5]).last(lambda x: x % 2 == 0) == 4

    def test_predicate_with_no_match_raises(self):
        with pytest.raises(TakeEnumerableException):
            Enumerable([1, 2, 3]).last(lambda x: x > 10)

    def test_default_on_empty(self):
        assert Enumerable[object]([]).last(default=99) == 99

    def test_default_with_predicate_no_match(self):
        assert Enumerable([1, 2, 3]).last(lambda x: x > 10, default=99) == 99

    def test_default_ignored_when_items_exist(self):
        assert Enumerable([1, 2, 3]).last(default=99) == 3

    def test_none_is_a_valid_default(self):
        assert Enumerable[object]([]).last(default=None) is None

    def test_falsy_default_is_returned(self):
        assert Enumerable[object]([]).last(default=0) == 0


class TestToList:
    def test_to_list_returns_correct(self):
        for items in ([1, 2, 3], [], [1]):
            copy = items.copy()
            assert Enumerable(items).to_list() == copy


class TestCount:
    def test_count_returns_correct(self):
        for items in ([1, 2, 3], [], [1]):
            assert Enumerable(items).count() == len(items)


class TestFilter:
    def test_filter_is_correct(self):
        assert all(
            x % 2 == 0 for x in Enumerable(range(1000)).filter(lambda x: x % 2 == 0)
        )


class TestSelect:
    def test_select_enumerable_returns_correct(self):
        assert Enumerable(range(5)).select(lambda x: x**2).to_list() == [0, 1, 4, 9, 16]


class TestFlatMap:
    def test_flat_map_enumerable_returns_correct(self):
        assert Enumerable(range(5)).flat_map(lambda x: (1, x)).to_list() == [
            1,
            0,
            1,
            1,
            1,
            2,
            1,
            3,
            1,
            4,
        ]


class TestFold:
    def test_fold_returns_expected(self):
        assert Enumerable(range(5)).fold(lambda acc, x: acc + x) == sum(range(5))
        assert Enumerable(range(5)).map(str).fold(
            lambda acc, x: acc + int(x), 0
        ) == sum(range(5))
        assert Enumerable(range(5)).fold(lambda acc, x: acc + x, 5) == sum(range(5)) + 5


class TestJoin:
    def test_join_returns_expected(self):
        assert Enumerable(["a", "b", "c"]).join("d") == "adbdc"


class TestControlFlow:
    def test_control_flow(self):
        source = (i for i in range(10000))
        assert Enumerable(source).control_flow(
            lambda x: (
                ControlFlow.skip()
                if x <= 10
                else (ControlFlow[int].ok(x) if x <= 20 else ControlFlow.stop())
            )
        ).to_list() == list(range(11, 21))
        assert next(source) == 22


class TestSkip:
    def test_default_skips_one(self):
        assert Enumerable([1, 2, 3]).skip().to_list() == [2, 3]

    def test_skip_n(self):
        assert Enumerable([1, 2, 3, 4, 5]).skip(3).to_list() == [4, 5]

    def test_skip_zero(self):
        assert Enumerable([1, 2, 3]).skip(0).to_list() == [1, 2, 3]

    def test_skip_equal_to_length(self):
        assert Enumerable([1, 2, 3]).skip(3).to_list() == []

    def test_skip_more_than_length(self):
        assert Enumerable([1, 2, 3]).skip(10).to_list() == []

    def test_skip_on_empty(self):
        assert Enumerable[object]([]).skip(2).to_list() == []

    def test_is_lazy_on_infinite_iterable(self):
        assert Enumerable(itertools.count()).skip(5).first() == 5

    def test_skip_exhausts_correctly(self):
        enumerable = Enumerable(range(10))
        assert enumerable.skip(3).first() == 3


class TestSkipWhile:
    def test_skips_leading_matches(self):
        assert Enumerable([1, 2, 3, 1]).skip_while(lambda x: x < 3).to_list() == [3, 1]

    def test_nothing_matches(self):
        assert Enumerable([5, 6]).skip_while(lambda x: x < 3).to_list() == [5, 6]

    def test_everything_matches(self):
        assert Enumerable([1, 2]).skip_while(lambda x: x < 3).to_list() == []

    def test_empty(self):
        assert Enumerable[object]([]).skip_while(lambda x: True).to_list() == []


class TestTake:
    def test_default_takes_one(self):
        assert Enumerable([1, 2, 3]).take().to_list() == [1]

    def test_take_n(self):
        assert Enumerable([1, 2, 3, 4]).take(3).to_list() == [1, 2, 3]

    def test_take_more_than_length(self):
        assert Enumerable([1, 2]).take(10).to_list() == [1, 2]

    def test_take_equal_to_length(self):
        assert Enumerable([1, 2, 3]).take(3).to_list() == [1, 2, 3]

    def test_take_zero(self):
        assert Enumerable([1, 2, 3]).take(0).to_list() == []

    # def test_take_negative(self):
    #     assert Enumerable([1, 2, 3]).take(-1).to_list() == []

    def test_take_on_empty(self):
        assert Enumerable[object]([]).take(3).to_list() == []

    def test_is_lazy_on_infinite_iterable(self):
        assert Enumerable(itertools.count()).take(4).to_list() == [0, 1, 2, 3]

    def test_preserves_falsy_items(self):
        assert Enumerable([0, None, "", False]).take(4).to_list() == [
            0,
            None,
            "",
            False,
        ]

    def test_does_not_overconsume_source(self):
        it = iter([1, 2, 3, 4, 5])
        assert Enumerable(it).take(2).to_list() == [1, 2]
        assert next(it) == 3

    def test_take_zero_does_not_consume_source(self):
        it = iter([1, 2, 3])
        assert Enumerable(it).take(0).to_list() == []
        assert next(it) == 1

    def test_take_exhausts_correctly(self):
        enumerable = Enumerable(range(10))
        enumerable.take(3).to_list()
        assert enumerable.first() == 3

    def test_skip_and_take(self):
        assert Enumerable(range(100000000)).skip(10).take(10).to_list() == list(
            range(10, 20)
        )


class TestSkipWhileAndTakeWhile:
    def test_skip_while_and_take_while_lossy(self):
        assert Enumerable(range(10000000000)).skip_while(
            lambda x: x < 5
        ).take_while_lossy(lambda x: x < 10).to_list() == [5, 6, 7, 8, 9]


class TestTakeWhileLossy:
    def test_stops_at_first_failure_and_drops_it(self):
        assert Enumerable([1, 2, 5, 1]).take_while_lossy(lambda x: x < 3).to_list() == [
            1,
            2,
        ]

    def test_all_match(self):
        assert Enumerable([1, 2]).take_while_lossy(lambda x: x < 3).to_list() == [1, 2]

    def test_none_match(self):
        assert Enumerable([5, 6]).take_while_lossy(lambda x: x < 3).to_list() == []

    def test_empty(self):
        assert Enumerable[object]([]).take_while_lossy(lambda x: True).to_list() == []

    def test_infinite_iterable(self):
        assert Enumerable(itertools.count()).take_while_lossy(
            lambda x: x < 3
        ).to_list() == [0, 1, 2]


class TestTakeWhileInclusive:
    def test_includes_first_failing_item(self):
        assert Enumerable([1, 2, 5, 1]).take_while_inclusive(
            lambda x: x < 3
        ).to_list() == [1, 2, 5]

    def test_all_match(self):
        assert Enumerable([1, 2]).take_while_inclusive(lambda x: x < 3).to_list() == [
            1,
            2,
        ]

    def test_first_item_fails(self):
        assert Enumerable([5, 1, 2]).take_while_inclusive(
            lambda x: x < 3
        ).to_list() == [5]

    def test_empty(self):
        assert (
            Enumerable[object]([]).take_while_inclusive(lambda x: True).to_list() == []
        )


class TestTakeWhileLossless:
    def test_takes_leading_matches(self):
        assert Enumerable([1, 2, 3, 4, 1]).take_while_lossless(
            lambda x: x < 4
        ).to_list() == [1, 2, 3]

    def test_all_match(self):
        assert Enumerable([1, 2, 3]).take_while_lossless(
            lambda x: x < 10
        ).to_list() == [1, 2, 3]

    def test_none_match(self):
        assert Enumerable([5, 6]).take_while_lossless(lambda x: x < 3).to_list() == []

    def test_empty(self):
        assert (
            Enumerable[object]([]).take_while_lossless(lambda x: True).to_list() == []
        )

    def test_failing_item_is_not_lost(self):
        enumerable = Enumerable(iter([1, 2, 3, 4, 5]))
        assert enumerable.take_while_lossless(lambda x: x < 3).to_list() == [1, 2]
        assert enumerable.to_list() == [3, 4, 5]


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


class TestPeek:
    def test_peek_returns_next_without_consuming(self):
        enumerable = Enumerable([1, 2, 3])
        assert enumerable.peek() == 1
        assert enumerable.peek() == 1
        assert enumerable.to_list() == [1, 2, 3]

    def test_peek_on_empty_raises(self):
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[object]([]).peek()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_try_peek_some(self):
        enumerable = Enumerable([1, 2])
        assert enumerable.try_peek() == Some(1)
        assert enumerable.to_list() == [1, 2]

    def test_try_peek_empty_is_null(self):
        assert Enumerable[object]([]).try_peek() == Null

    def test_peek_n(self):
        enumerable = Enumerable([1, 2, 3, 4])
        assert enumerable.peek_n(2).to_list() == [1, 2]
        assert enumerable.to_list() == [1, 2, 3, 4]

    def test_peek_n_more_than_length(self):
        assert Enumerable([1, 2]).peek_n(5).to_list() == [1, 2]

    def test_peek_n_zero(self):
        assert Enumerable([1, 2]).peek_n(0).to_list() == []

    def test_peek_while(self):
        enumerable = Enumerable([1, 2, 3, 1])
        assert enumerable.peek_while(lambda x: x < 3).to_list() == [1, 2]
        assert enumerable.to_list() == [1, 2, 3, 1]

    def test_peek_on_infinite_iterable(self):
        enumerable = Enumerable(itertools.count())
        assert enumerable.peek_n(3).to_list() == [0, 1, 2]
        assert enumerable.first() == 0

    def test_peek_while_returns_matching_prefix(self):
        enumerable = Enumerable((i for i in range(10)))
        assert enumerable.peek() == 0
        assert enumerable.peek_n(4).to_list() == [0, 1, 2, 3]
        assert enumerable.peek_while(lambda x: x < 8).to_list() == list(range(8))
        assert enumerable.to_list() == list(range(10))


class TestZip:
    def test_zip(self):
        assert Enumerable(range(10)).zip(range(2, 5)).to_list() == list(
            zip(range(10), range(2, 5))
        )


class TestAll:
    def test_all(self):
        assert Enumerable(range(10)).all(lambda x: x >= 0)
        assert not Enumerable(range(10)).all(lambda x: x >= 5)


class TestAny:
    def test_any(self):
        assert Enumerable(range(10)).any(lambda x: x == 3)
        assert not Enumerable(range(10)).any(lambda x: x == 100)


class TestNeq:
    def test_neq(self):
        assert Enumerable(range(10)).neq(Enumerable(range(11)))
        assert not Enumerable(range(10)).neq(Enumerable(range(10)))


class TestEq:
    def test_eq(self):
        assert not Enumerable(range(10)).eq(Enumerable(range(11)))
        assert Enumerable(range(10)).eq(Enumerable(range(10)))


class TestExceptions:
    def test_not_enough_items_message(self):
        exception = TakeEnumerableException.not_enough_items(3, 1)
        assert exception.exception_case == TakeEnumerableExceptionCase.NotEnoughItems
        assert "at least 3" in str(exception) and "only 1" in str(exception)

    def test_not_enough_items_defaults(self):
        exception = TakeEnumerableException.not_enough_items()
        assert "unknown(not provided)" in str(exception)

    def test_too_many_items_case_and_message(self):
        exception = TakeEnumerableException.too_many_items(1, 4)
        assert exception.exception_case == TakeEnumerableExceptionCase.TooManyItems
        assert "at most 1" in str(exception)

    def test_too_many_items_defaults(self):
        exception = TakeEnumerableException.too_many_items()
        assert "unknown(not provided)" in str(exception)

    def test_extra_positional_args_are_accepted(self):
        exception = TakeEnumerableException(
            TakeEnumerableExceptionCase.NotEnoughItems, "a", "b"
        )
        assert exception.exception_case == TakeEnumerableExceptionCase.NotEnoughItems
        assert exception.args == ("a", "b")
