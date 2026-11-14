from .enumerable import Enumerable as Enumerable
from .control_flow import ControlFlow as ControlFlow
from .control_flow import ControlFlowNestedState as ControlFlowNestedState
from ._sentinels import DROP as DROP
from ._sentinels import FilterMapDrop as FilterMapDrop
from .take_enumerable import TakeEnumerableExceptionCase as TakeEnumerableExceptionCase
from .take_enumerable import TakeEnumerableException as TakeEnumerableException
from .parity_enumerable import (
    AdvanceByResult as AdvanceByResult,
    NextChunkResult as NextChunkResult,
    Ordering as Ordering,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def identity[T](x: T) -> T:
    return x
