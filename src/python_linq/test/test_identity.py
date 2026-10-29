from .. import *


class TestIdentity:
    def test_identity_returns_value(self):
        value = object()
        assert identity(value) is value
