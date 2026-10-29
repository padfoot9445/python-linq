import pytest

from python_linq import (
    Enumerable,
    TakeEnumerableException,
    TakeEnumerableExceptionCase,
)


def tracked_source(consumed: list[int]):
    for item in range(4):
        consumed.append(item)
        yield item


def test_sequence_operations_defer_source_consumption_and_callbacks():
    for build, expected_consumed in (
        (lambda values, seen: values.map(lambda item: seen.append(item) or item), 4),
        (lambda values, seen: values.where(lambda item: seen.append(item) is None), 4),
        (
            lambda values, seen: values.flat_map(
                lambda item: seen.append(item) or [item]
            ),
            4,
        ),
        (lambda values, seen: values.reverse(), 4),
        (lambda values, seen: values.take_last(2), 4),
        (lambda values, seen: values.chunk(2), 4),
        (lambda values, seen: values.group_by(lambda item: item % 2), 4),
        (lambda values, seen: values.order_by(), 4),
        (lambda values, seen: values.default_if_empty(), 4),
        (
            lambda values, seen: values.filter_map(
                lambda item: seen.append(item) or item
            ),
            4,
        ),
        (
            lambda values, seen: values.distinct(
                key=lambda item: seen.append(item) or item
            ),
            4,
        ),
        (lambda values, seen: values.exact(4), 4),
        (lambda values, seen: values.take_while_lossless(lambda item: item < 2), 3),
    ):
        consumed: list[int] = []
        callbacks: list[int] = []
        result = build(Enumerable(tracked_source(consumed)), callbacks)

        assert consumed == []
        assert callbacks == []
        result.to_list()

        assert len(consumed) == expected_consumed


def test_take_last_zero_does_not_consume_source():
    consumed: list[int] = []
    result = Enumerable(tracked_source(consumed)).take_last(0)

    assert result.to_list() == []
    assert consumed == []


def test_exact_defers_validation_until_iteration():
    consumed: list[int] = []
    result = Enumerable(tracked_source(consumed)).exact(2)

    assert consumed == []
    with pytest.raises(TakeEnumerableException) as exc:
        result.to_list()
    assert exc.value.exception_case is TakeEnumerableExceptionCase.TooManyItems
    assert consumed == [0, 1, 2]
