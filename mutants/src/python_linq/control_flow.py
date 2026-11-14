from dataclasses import dataclass
from enum import Enum, auto
from collections.abc import Callable, Iterable
from typing import Any, cast

lazy from .enumerable import Enumerable

lazy from .base_enumerable import BaseEnumerable


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _NoValue:
    __slots__ = ()


_NO_VALUE = _NoValue()


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
mutants_xǁControlFlowǁok__mutmut: MutantDict = {}  # type: ignore
mutants_xǁControlFlowǁskip__mutmut: MutantDict = {}  # type: ignore
mutants_xǁControlFlowǁstop__mutmut: MutantDict = {}  # type: ignore
mutants_xǁControlFlowǁstop_ok__mutmut: MutantDict = {}  # type: ignore
mutants_xǁControlFlowǁyield_control_ok__mutmut: MutantDict = {}  # type: ignore
mutants_xǁControlFlowǁyield_control_skip__mutmut: MutantDict = {}  # type: ignore


@dataclass
class ControlFlow[T]:
    val: T | _NoValue
    state: ControlFlowEnum
    nested_state: ControlFlowNestedState = ControlFlowNestedState.NoNestedState

    def __getitem__(self, _: type[T]) -> type["ControlFlow[Any]"]:
        return ControlFlow

    @classmethod
    @_mutmut_mutated(mutants_xǁControlFlowǁok__mutmut, is_classmethod = True)
    def ok(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.Ok)

    @classmethod
    def xǁControlFlowǁok__mutmut_orig(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.Ok)

    @classmethod
    def xǁControlFlowǁok__mutmut_1(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=None, state=ControlFlowEnum.Ok)

    @classmethod
    def xǁControlFlowǁok__mutmut_2(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=None)

    @classmethod
    def xǁControlFlowǁok__mutmut_3(cls, return_value: T) -> "ControlFlow[T]":
        return cls(state=ControlFlowEnum.Ok)

    @classmethod
    def xǁControlFlowǁok__mutmut_4(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, )

    @classmethod
    @_mutmut_mutated(mutants_xǁControlFlowǁskip__mutmut, is_classmethod = True)
    def skip(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=ControlFlowEnum.Skip)

    @classmethod
    def xǁControlFlowǁskip__mutmut_orig(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=ControlFlowEnum.Skip)

    @classmethod
    def xǁControlFlowǁskip__mutmut_1(cls) -> "ControlFlow[Any]":
        return cls(val=None, state=ControlFlowEnum.Skip)

    @classmethod
    def xǁControlFlowǁskip__mutmut_2(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=None)

    @classmethod
    def xǁControlFlowǁskip__mutmut_3(cls) -> "ControlFlow[Any]":
        return cls(state=ControlFlowEnum.Skip)

    @classmethod
    def xǁControlFlowǁskip__mutmut_4(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, )

    @classmethod
    @_mutmut_mutated(mutants_xǁControlFlowǁstop__mutmut, is_classmethod = True)
    def stop(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=ControlFlowEnum.Stop)

    @classmethod
    def xǁControlFlowǁstop__mutmut_orig(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=ControlFlowEnum.Stop)

    @classmethod
    def xǁControlFlowǁstop__mutmut_1(cls) -> "ControlFlow[Any]":
        return cls(val=None, state=ControlFlowEnum.Stop)

    @classmethod
    def xǁControlFlowǁstop__mutmut_2(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, state=None)

    @classmethod
    def xǁControlFlowǁstop__mutmut_3(cls) -> "ControlFlow[Any]":
        return cls(state=ControlFlowEnum.Stop)

    @classmethod
    def xǁControlFlowǁstop__mutmut_4(cls) -> "ControlFlow[Any]":
        return cls(val=_NO_VALUE, )

    @classmethod
    @_mutmut_mutated(mutants_xǁControlFlowǁstop_ok__mutmut, is_classmethod = True)
    def stop_ok(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.StopOk)

    @classmethod
    def xǁControlFlowǁstop_ok__mutmut_orig(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=ControlFlowEnum.StopOk)

    @classmethod
    def xǁControlFlowǁstop_ok__mutmut_1(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=None, state=ControlFlowEnum.StopOk)

    @classmethod
    def xǁControlFlowǁstop_ok__mutmut_2(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, state=None)

    @classmethod
    def xǁControlFlowǁstop_ok__mutmut_3(cls, return_value: T) -> "ControlFlow[T]":
        return cls(state=ControlFlowEnum.StopOk)

    @classmethod
    def xǁControlFlowǁstop_ok__mutmut_4(cls, return_value: T) -> "ControlFlow[T]":
        return cls(val=return_value, )

    @classmethod
    @_mutmut_mutated(mutants_xǁControlFlowǁyield_control_ok__mutmut, is_classmethod = True)
    def yield_control_ok(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_orig(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_1(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=None,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_2(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=None,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_3(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            nested_state=None,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_4(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_5(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            nested_state=ControlFlowNestedState.Ok,
        )

    @classmethod
    def xǁControlFlowǁyield_control_ok__mutmut_6(cls, return_value: T) -> "ControlFlow[T]":
        return cls(
            val=return_value,
            state=ControlFlowEnum.YieldControl,
            )

    @classmethod
    @_mutmut_mutated(mutants_xǁControlFlowǁyield_control_skip__mutmut, is_classmethod = True)
    def yield_control_skip(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Skip,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_orig(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Skip,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_1(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=None,
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Skip,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_2(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            state=None,
            nested_state=ControlFlowNestedState.Skip,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_3(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            state=ControlFlowEnum.YieldControl,
            nested_state=None,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_4(cls, _: T) -> "ControlFlow[T]":
        return cls(
            state=ControlFlowEnum.YieldControl,
            nested_state=ControlFlowNestedState.Skip,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_5(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            nested_state=ControlFlowNestedState.Skip,
        )

    @classmethod
    def xǁControlFlowǁyield_control_skip__mutmut_6(cls, _: T) -> "ControlFlow[T]":
        return cls(
            val=_NO_VALUE,
            state=ControlFlowEnum.YieldControl,
            )

mutants_xǁControlFlowǁok__mutmut['_mutmut_orig'] = ControlFlow.xǁControlFlowǁok__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowǁok__mutmut['xǁControlFlowǁok__mutmut_1'] = ControlFlow.xǁControlFlowǁok__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowǁok__mutmut['xǁControlFlowǁok__mutmut_2'] = ControlFlow.xǁControlFlowǁok__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowǁok__mutmut['xǁControlFlowǁok__mutmut_3'] = ControlFlow.xǁControlFlowǁok__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowǁok__mutmut['xǁControlFlowǁok__mutmut_4'] = ControlFlow.xǁControlFlowǁok__mutmut_4 # type: ignore # mutmut generated

mutants_xǁControlFlowǁskip__mutmut['_mutmut_orig'] = ControlFlow.xǁControlFlowǁskip__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowǁskip__mutmut['xǁControlFlowǁskip__mutmut_1'] = ControlFlow.xǁControlFlowǁskip__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowǁskip__mutmut['xǁControlFlowǁskip__mutmut_2'] = ControlFlow.xǁControlFlowǁskip__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowǁskip__mutmut['xǁControlFlowǁskip__mutmut_3'] = ControlFlow.xǁControlFlowǁskip__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowǁskip__mutmut['xǁControlFlowǁskip__mutmut_4'] = ControlFlow.xǁControlFlowǁskip__mutmut_4 # type: ignore # mutmut generated

mutants_xǁControlFlowǁstop__mutmut['_mutmut_orig'] = ControlFlow.xǁControlFlowǁstop__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop__mutmut['xǁControlFlowǁstop__mutmut_1'] = ControlFlow.xǁControlFlowǁstop__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop__mutmut['xǁControlFlowǁstop__mutmut_2'] = ControlFlow.xǁControlFlowǁstop__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop__mutmut['xǁControlFlowǁstop__mutmut_3'] = ControlFlow.xǁControlFlowǁstop__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop__mutmut['xǁControlFlowǁstop__mutmut_4'] = ControlFlow.xǁControlFlowǁstop__mutmut_4 # type: ignore # mutmut generated

mutants_xǁControlFlowǁstop_ok__mutmut['_mutmut_orig'] = ControlFlow.xǁControlFlowǁstop_ok__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop_ok__mutmut['xǁControlFlowǁstop_ok__mutmut_1'] = ControlFlow.xǁControlFlowǁstop_ok__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop_ok__mutmut['xǁControlFlowǁstop_ok__mutmut_2'] = ControlFlow.xǁControlFlowǁstop_ok__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop_ok__mutmut['xǁControlFlowǁstop_ok__mutmut_3'] = ControlFlow.xǁControlFlowǁstop_ok__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowǁstop_ok__mutmut['xǁControlFlowǁstop_ok__mutmut_4'] = ControlFlow.xǁControlFlowǁstop_ok__mutmut_4 # type: ignore # mutmut generated

mutants_xǁControlFlowǁyield_control_ok__mutmut['_mutmut_orig'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_ok__mutmut['xǁControlFlowǁyield_control_ok__mutmut_1'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_ok__mutmut['xǁControlFlowǁyield_control_ok__mutmut_2'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_ok__mutmut['xǁControlFlowǁyield_control_ok__mutmut_3'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_ok__mutmut['xǁControlFlowǁyield_control_ok__mutmut_4'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_4 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_ok__mutmut['xǁControlFlowǁyield_control_ok__mutmut_5'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_5 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_ok__mutmut['xǁControlFlowǁyield_control_ok__mutmut_6'] = ControlFlow.xǁControlFlowǁyield_control_ok__mutmut_6 # type: ignore # mutmut generated

mutants_xǁControlFlowǁyield_control_skip__mutmut['_mutmut_orig'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_skip__mutmut['xǁControlFlowǁyield_control_skip__mutmut_1'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_skip__mutmut['xǁControlFlowǁyield_control_skip__mutmut_2'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_skip__mutmut['xǁControlFlowǁyield_control_skip__mutmut_3'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_skip__mutmut['xǁControlFlowǁyield_control_skip__mutmut_4'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_4 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_skip__mutmut['xǁControlFlowǁyield_control_skip__mutmut_5'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_5 # type: ignore # mutmut generated
mutants_xǁControlFlowǁyield_control_skip__mutmut['xǁControlFlowǁyield_control_skip__mutmut_6'] = ControlFlow.xǁControlFlowǁyield_control_skip__mutmut_6 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut: MutantDict = {}  # type: ignore


class ControlFlowEnumerable[T](BaseEnumerable[T]):
    @_mutmut_mutated(mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut)
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_orig(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_1(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = None
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_2(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(None)
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_3(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_4(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield _require_value(val)
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_5(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield _require_value(val)
                    case ControlFlow(state=ControlFlowEnum.Skip):
                        continue
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_6(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_7(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        nested_state=ControlFlowNestedState.Skip,
                    ):
                        yield from self.control_flow(lambda _: ControlFlow.skip())
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_8(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_9(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_10(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield _require_value(None)
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_11(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield _require_value(val)
                    case ControlFlow(state=ControlFlowEnum.Skip):
                        break
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_12(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
        def inner() -> Iterable[T]:
            for i in self:
                val = func(i)
                match val:
                    case ControlFlow(state=ControlFlowEnum.Ok):
                        yield _require_value(val)
                    case ControlFlow(state=ControlFlowEnum.Skip):
                        continue
                    case ControlFlow(state=ControlFlowEnum.Stop):
                        return
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_13(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        yield _require_value(None)
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_14(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        return
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
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_15(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        yield _require_value(None)
                        yield from self
                    case ControlFlow(
                        state=ControlFlowEnum.YieldControl,
                        nested_state=ControlFlowNestedState.Skip,
                    ):
                        yield from self.control_flow(lambda _: ControlFlow.skip())
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_16(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        yield from self.control_flow(None)
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_17(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        yield from self.control_flow(lambda _: None)
                    case _:
                        raise Exception("func did not return ControlFlow object!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_18(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        raise Exception(None)

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_19(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        raise Exception("XXfunc did not return ControlFlow object!XX")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_20(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        raise Exception("func did not return controlflow object!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_21(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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
                        raise Exception("FUNC DID NOT RETURN CONTROLFLOW OBJECT!")

        return Enumerable(inner())
    def xǁControlFlowEnumerableǁcontrol_flow__mutmut_22(self, func: Callable[[T], ControlFlow[T]]) -> "Enumerable[T]":
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

        return Enumerable(None)

mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['_mutmut_orig'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_orig # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_1'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_1 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_2'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_2 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_3'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_3 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_4'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_4 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_5'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_5 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_6'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_6 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_7'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_7 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_8'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_8 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_9'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_9 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_10'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_10 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_11'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_11 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_12'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_12 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_13'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_13 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_14'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_14 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_15'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_15 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_16'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_16 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_17'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_17 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_18'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_18 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_19'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_19 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_20'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_20 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_21'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_21 # type: ignore # mutmut generated
mutants_xǁControlFlowEnumerableǁcontrol_flow__mutmut['xǁControlFlowEnumerableǁcontrol_flow__mutmut_22'] = ControlFlowEnumerable.xǁControlFlowEnumerableǁcontrol_flow__mutmut_22 # type: ignore # mutmut generated
mutants_x__require_value__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__require_value__mutmut)
def _require_value[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(T, flow.val)


def x__require_value__mutmut_orig[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(T, flow.val)


def x__require_value__mutmut_1[T](flow: ControlFlow[T]) -> T:
    if flow.val is not _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(T, flow.val)


def x__require_value__mutmut_2[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(None)
    return cast(T, flow.val)


def x__require_value__mutmut_3[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(None, flow.val)


def x__require_value__mutmut_4[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(T, None)


def x__require_value__mutmut_5[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(flow.val)


def x__require_value__mutmut_6[T](flow: ControlFlow[T]) -> T:
    if flow.val is _NO_VALUE:
        raise ValueError(f"{flow.state.name} control flow requires a value")
    return cast(T, )

mutants_x__require_value__mutmut['_mutmut_orig'] = x__require_value__mutmut_orig # type: ignore # mutmut generated
mutants_x__require_value__mutmut['x__require_value__mutmut_1'] = x__require_value__mutmut_1 # type: ignore # mutmut generated
mutants_x__require_value__mutmut['x__require_value__mutmut_2'] = x__require_value__mutmut_2 # type: ignore # mutmut generated
mutants_x__require_value__mutmut['x__require_value__mutmut_3'] = x__require_value__mutmut_3 # type: ignore # mutmut generated
mutants_x__require_value__mutmut['x__require_value__mutmut_4'] = x__require_value__mutmut_4 # type: ignore # mutmut generated
mutants_x__require_value__mutmut['x__require_value__mutmut_5'] = x__require_value__mutmut_5 # type: ignore # mutmut generated
mutants_x__require_value__mutmut['x__require_value__mutmut_6'] = x__require_value__mutmut_6 # type: ignore # mutmut generated
