from .. import *


class TestJoin:
    def test_join_returns_expected(self):
        assert Enumerable(["a", "b", "c"]).join("d") == "adbdc"
