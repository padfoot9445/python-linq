from .. import *
from ..take_enumerable import TakeEnumerableException, TakeEnumerableExceptionCase


class TestExceptions:
    def test_not_enough_items_message(self):
        exception = TakeEnumerableException.not_enough_items(3, 1)
        assert exception.exception_case == TakeEnumerableExceptionCase.NotEnoughItems
        assert "at least 3" in str(exception) and "only 1" in str(exception)

    def test_not_enough_items_defaults(self):
        exception = TakeEnumerableException.not_enough_items()
        assert "unknown(not provided)" in str(exception)

    def test_too_many_items_case_and_message(self):
        exception = TakeEnumerableException.too_many_items(1, 4)
        assert exception.exception_case == TakeEnumerableExceptionCase.TooManyItems
        assert "at most 1" in str(exception)

    def test_too_many_items_defaults(self):
        exception = TakeEnumerableException.too_many_items()
        assert "unknown(not provided)" in str(exception)

    def test_extra_positional_args_are_accepted(self):
        exception = TakeEnumerableException(
            TakeEnumerableExceptionCase.NotEnoughItems, "a", "b"
        )
        assert exception.exception_case == TakeEnumerableExceptionCase.NotEnoughItems
        assert exception.args == ("a", "b")
