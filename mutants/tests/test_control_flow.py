from typing import Callable, cast

import pytest

from python_linq import *


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

    def test_stop_ok_yields_value_then_stops(self):
        assert Enumerable(range(5)).control_flow(
            lambda x: (
                ControlFlow[int].stop_ok(x) if x == 2 else ControlFlow[int].ok(x)
            )
        ).to_list() == [0, 1, 2]

    def test_yield_control_ok_yields_value_then_remaining_source(self):
        seen: list[int] = []

        def control(x: int) -> ControlFlow[int]:
            seen.append(x)
            return (
                ControlFlow[int].yield_control_ok(10)
                if x == 1
                else ControlFlow[int].ok(x)
            )

        assert Enumerable(range(5)).control_flow(control).to_list() == [0, 10, 2, 3, 4]
        assert seen == [0, 1]
        print("RAN")

    def test_yield_control_skip_consumes_remainder(self):
        source = iter(range(5))
        assert Enumerable(source).control_flow(
            lambda x: (
                ControlFlow[int].yield_control_skip(x)
                if x == 2
                else ControlFlow[int].ok(x)
            )
        ).to_list() == [0, 1]
        assert list(source) == []

    def test_invalid_callback_result_raises(self):
        def invalid_callback(_: int) -> None:
            return None

        with pytest.raises(Exception, match="func did not return ControlFlow object!"):
            Enumerable([1]).control_flow(
                cast(Callable[[int], ControlFlow[int]], invalid_callback)
            ).to_list()
