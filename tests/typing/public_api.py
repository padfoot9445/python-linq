from typing import assert_type

from python_linq import (
    DROP,
    ControlFlow,
    ControlFlowNestedState,
    Enumerable,
    Ordering,
)

numbers = Enumerable([1, 2, 3])
nullable_numbers = Enumerable([1, None])

assert_type(numbers.map(str), Enumerable[str])
assert_type(nullable_numbers.first(), int | None)
assert_type(nullable_numbers.last(), int | None)
assert_type(Enumerable[int]([]).first(default=None), int | None)
assert_type(Enumerable[int]([]).single(default=None), int | None)
assert_type(Enumerable[int]([]).last(default=None), int | None)
assert_type(Enumerable[int]([]).exact(2, default=None), Enumerable[int | None])
assert_type(
    numbers.filter_map(lambda value: str(value) if value > 1 else DROP),
    Enumerable[str],
)
assert_type(
    numbers.filter_map(lambda value: None if value > 1 else DROP),
    Enumerable[None],
)
assert_type(Enumerable([[1], [2]]).flatten(), Enumerable[int])
assert_type(numbers.chunk(2), Enumerable[list[int]])
assert_type(
    numbers.group_by(lambda value: value % 2), Enumerable[tuple[int, list[int]]]
)
assert_type(
    numbers.group_by(lambda value: value % 2, lambda value: str(value)),
    Enumerable[tuple[int, list[str]]],
)
assert_type(
    numbers.group_by(
        lambda value: value % 2,
        result_selector=lambda key, values: (key, values),
    ),
    Enumerable[tuple[int, list[int]]],
)
assert_type(
    numbers.group_by(
        lambda value: value % 2,
        lambda value: str(value),
        lambda key, values: (key, values),
    ),
    Enumerable[tuple[int, list[str]]],
)
assert_type(
    numbers.select_indexed(lambda item, index: (item, index)),
    Enumerable[tuple[int, int]],
)
assert_type(numbers.select_many(lambda item: [str(item)]), Enumerable[str])
assert_type(
    numbers.select_many(lambda item: [str(item)], lambda outer, inner: (outer, inner)),
    Enumerable[tuple[int, str]],
)
assert_type(numbers.step_by(2), Enumerable[int])
assert_type(numbers.map_windows(2, len), Enumerable[int])
assert_type(
    numbers.order_by(key=lambda item: item % 2).then_by(lambda item: item),
    Enumerable[int],
)
assert_type(numbers.to_dictionary(lambda item: item), dict[int, int])
assert_type(numbers.to_dictionary(lambda item: item, str), dict[int, str])
assert_type(numbers.to_lookup(lambda item: item), dict[int, list[int]])
assert_type(numbers.to_lookup(lambda item: item, str), dict[int, list[str]])
assert_type(
    numbers.first_or_default(predicate=lambda item: item > 1),
    int | None,
)
assert_type(numbers.aggregate(0, lambda total, item: total + item), int)
assert_type(Enumerable([(1, "one")]).unzip(), tuple[list[int], list[str]])
assert_type(numbers.sum(lambda item: item * 2), int)
assert_type(numbers.average(lambda item: float(item)), float)
assert_type(numbers.default_if_empty(0), Enumerable[int])
assert_type(numbers.default_if_empty(), Enumerable[int | None])
assert_type(Enumerable[int]([]).nth(0, default=None), int | None)
assert_type(Enumerable[int]([]).find(lambda value: value > 0, default=None), int | None)
assert_type(numbers.any(), bool)
assert_type(
    nullable_numbers.control_flow(lambda value: ControlFlow[int | None].ok(value)),
    Enumerable[int | None],
)
assert_type(ControlFlow[None].ok(None).nested_state, ControlFlowNestedState)
assert_type(nullable_numbers.cmp([1, None]), Ordering)
