from dataclasses import dataclass
from enum import Enum, auto
from collections.abc import Callable, Iterable
from typing import Any, cast

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable

_NO_VALUE = sentinel("_NO_VALUE")


class ControlFlowEnum(Enum):
    Ok = auto()
    Skip = auto()
    Stop = auto()
    StopOk = auto()
    YieldControl = auto()


class ControlFlowNestedState(Enum):
    NoNestedState = auto()
    Ok = auto()
    Skip = auto()


@dataclass
class ControlFlow[T]:
    val: T | _NO_VALUE
    state: ControlFlowEnum
    nested_state: ControlFlowNestedState = ControlFlowNestedState.NoNestedState

    def __getitem__(self, _: type[T]) -> type["ControlFlow[Any]"]:
        return ControlFlow

    @classmethod
    def ok(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.Ok)

    @classmethod
    def skip(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=ControlFlowEnum.Skip)

    @classmethod
    def stop(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=ControlFlowEnum.Stop)

    @classmethod
    def stop_ok(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.StopOk)

    @classmethod
    def yield_control_ok(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def yield_control_skip(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Skip,
        )


class ControlFlowEnumerable[T](BaseEnumerable[T]):
    def control_flow(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield _require_value(val)
                    case ControlFlow(state=ControlFlowEnum.Skip):
                        continue
                    case ControlFlow(state=ControlFlowEnum.Stop):
                        break
                    case ControlFlow(state=ControlFlowEnum.StopOk):
                        yield _require_value(val)
                        break
                    case ControlFlow(
                        state=ControlFlowEnum.YieldControl,
                        nested_state=ControlFlowNestedState.Ok,
                    ):
                        yield _require_value(val)
                        yield from self
                    case ControlFlow(
                        state=ControlFlowEnum.YieldControl,
                        nested_state=ControlFlowNestedState.Skip,
                    ):
                        yield from self.control_flow(lambda _: ControlFlow.skip())
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())


def _require_value[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(T, flow.val)
