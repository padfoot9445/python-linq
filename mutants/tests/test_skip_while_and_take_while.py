from python_linq import *


class TestSkipWhileAndTakeWhile:
    def test_skip_while_and_take_while_lossy(self):
        assert Enumerable(range(10000000000)).skip_while(
            lambda x: x < 5
        ).take_while_lossy(lambda x: x < 10).to_list() == [5, 6, 7, 8, 9]
