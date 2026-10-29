from enum import Enum, auto


class _Missing:
    __slots__ = ()


MISSING = _Missing()


class FilterMapDrop(Enum):
    DROP = auto()


DROP = FilterMapDrop.DROP
