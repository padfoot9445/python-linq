from typing import assert_type

from python_linq import ControlFlow, Enumerable

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
    numbers.filter_map(lambda value: str(value) if value > 1 else None), Enumerable[str]
)
assert_type(Enumerable([[1], [2]]).flatten(), Enumerable[int])
assert_type(numbers.chunk(2), Enumerable[list[int]])
assert_type(
    numbers.group_by(lambda value: value % 2), Enumerable[tuple[int, list[int]]]
)
assert_type(numbers.default_if_empty(0), Enumerable[int])
assert_type(numbers.default_if_empty(), Enumerable[int | None])
assert_type(Enumerable[int]([]).nth(0, default=None), int | None)
assert_type(Enumerable[int]([]).find(lambda value: value > 0, default=None), int | None)
assert_type(numbers.any(), bool)
assert_type(
    nullable_numbers.control_flow(lambda value: ControlFlow[int | None].ok(value)),
    Enumerable[int | None],
)
