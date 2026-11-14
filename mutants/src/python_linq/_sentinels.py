from enum import Enum, auto


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _Missing:
    __slots__ = ()


MISSING = _Missing()


class FilterMapDrop(Enum):
    DROP = auto()


DROP = FilterMapDrop.DROP
