from .. import *


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
