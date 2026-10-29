from .enumerable import Enumerable as Enumerable
from .control_flow import ControlFlow as ControlFlow
from .take_enumerable import TakeEnumerableExceptionCase as TakeEnumerableExceptionCase
from .take_enumerable import TakeEnumerableException as TakeEnumerableException


def identity[T](x: T) -> T:
    return x
