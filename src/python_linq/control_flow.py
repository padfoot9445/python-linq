from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Callable, Iterable, Type

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable


class ControlFlowEnum(Enum):
    Ok = auto()
    Skip = auto()
    Stop = auto()
    StopOk = auto()
    YieldControl = auto()


@dataclass
class ControlFlow[T]:
    val: T
    state: ControlFlowEnum
    nested_state: ControlFlowEnum | None = None

    def __getitem__(self, _: Type[T]):
        return ControlFlow

    @classmethod
    def ok(cls: Type[ControlFlow[T]], return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.Ok)

    @classmethod
    def skip(cls: Type[ControlFlow[Any]]) -> "ControlFlow[Any]":
        return cls(val=None, state=ControlFlowEnum.Skip)

    @classmethod
    def stop(cls: Type[ControlFlow[Any]]) -> "ControlFlow[Any]":
        return cls(val=None, state=ControlFlowEnum.Stop)

    @classmethod
    def stop_ok(cls: Type[ControlFlow[T]], return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.StopOk)

    @classmethod
    def yield_control_ok(
        cls: Type[ControlFlow[T]], return_value: T
    ) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowEnum.Ok,
        )

    @classmethod
    def yield_control_skip(
        cls: Type[ControlFlow[T]], return_value: T
    ) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowEnum.Skip,
        )

class ControlFlowEnumerable[T](BaseEnumerable[T]):
    def control_flow(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield val.val
                    case ControlFlow(state=ControlFlowEnum.Skip):
                        continue
                    case ControlFlow(state=ControlFlowEnum.Stop):
                        break
                    case ControlFlow(state=ControlFlowEnum.StopOk):
                        yield val.val
                        break
                    case ControlFlow(
                        state=ControlFlowEnum.YieldControl,
                        nested_state=ControlFlowEnum.Ok,
                    ):
                        yield val.val
                        yield from self
                    case ControlFlow(
                        state=ControlFlowEnum.YieldControl,
                        nested_state=ControlFlowEnum.Skip,
                    ):
                        yield from self.control_flow(lambda _: ControlFlow.skip())
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())
