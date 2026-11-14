from collections.abc import Iterable, Iterator
from typing import cast

lazy from .take_enumerable import TakeEnumerable

lazy from .enumerable import Enumerable

sentinel = object()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPartitionEnumerableǁsplit__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPartitionEnumerableǁ_split_no_separator__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPartitionEnumerableǁ_split__mutmut: MutantDict = {}  # type: ignore


class PartitionEnumerable[T](TakeEnumerable[T]):

    @_mutmut_mutated(mutants_xǁPartitionEnumerableǁsplit__mutmut)
    def split(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(T, sep)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_orig(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(T, sep)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_1(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is not sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(T, sep)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_2(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                None
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_3(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(None, sep)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_4(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(T, None)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_5(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(sep)]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    def xǁPartitionEnumerableǁsplit__mutmut_6(self, sep: T | object = sentinel) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()
        else:
            return self.split_multiple(
                [cast(T, )]
            )  # safety: a random object instance should not be passed into sep unless object is a permissible value for T to take

    @_mutmut_mutated(mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut)
    def split_multiple(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_orig(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_1(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is not sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_2(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = None
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_3(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(None)
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_4(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(None, sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_5(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], None))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_6(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_7(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], ))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_8(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], sep))
            if separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_9(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(None)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁsplit_multiple__mutmut_10(
        self, sep: Iterable[T] | object = sentinel
    ) -> "Enumerable[Enumerable[T]]":
        if sep is sentinel:
            return self._split_no_separator()

        def inner() -> Iterator[Enumerable[T]]:
            separators = list(cast(Iterable[T], sep))
            if not separators:
                yield from self._split_no_separator()
            else:
                yield from self._split(separators)

        return Enumerable(None)

    @_mutmut_mutated(mutants_xǁPartitionEnumerableǁ_split_no_separator__mutmut)
    def _split_no_separator(self) -> "Enumerable[Enumerable[T]]":
        return self.map(lambda x: Enumerable([x]))

    def xǁPartitionEnumerableǁ_split_no_separator__mutmut_orig(self) -> "Enumerable[Enumerable[T]]":
        return self.map(lambda x: Enumerable([x]))

    def xǁPartitionEnumerableǁ_split_no_separator__mutmut_1(self) -> "Enumerable[Enumerable[T]]":
        return self.map(None)

    def xǁPartitionEnumerableǁ_split_no_separator__mutmut_2(self) -> "Enumerable[Enumerable[T]]":
        return self.map(lambda x: None)

    def xǁPartitionEnumerableǁ_split_no_separator__mutmut_3(self) -> "Enumerable[Enumerable[T]]":
        return self.map(lambda x: Enumerable(None))

    @_mutmut_mutated(mutants_xǁPartitionEnumerableǁ_split__mutmut)
    def _split(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_orig(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_1(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = None

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_2(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(None)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_3(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = None
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_4(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(None)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_5(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) or buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_6(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) > len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_7(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[+len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_8(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] != sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_9(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(None)
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_10(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: +len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_11(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = None
            yield Enumerable(buffer)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_12(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(None)

        return Enumerable(inner())

    def xǁPartitionEnumerableǁ_split__mutmut_13(self, sep: Iterable[T]) -> Enumerable[Enumerable[T]]:
        sep = list(sep)

        def inner() -> Iterator[Enumerable[T]]:
            buffer: list[T] = []
            for item in self:
                buffer.append(item)
                if len(buffer) >= len(sep) and buffer[-len(sep) :] == sep:
                    yield Enumerable(buffer[: -len(sep)])
                    buffer = []
            yield Enumerable(buffer)

        return Enumerable(None)

mutants_xǁPartitionEnumerableǁsplit__mutmut['_mutmut_orig'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit__mutmut['xǁPartitionEnumerableǁsplit__mutmut_1'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit__mutmut['xǁPartitionEnumerableǁsplit__mutmut_2'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit__mutmut['xǁPartitionEnumerableǁsplit__mutmut_3'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit__mutmut['xǁPartitionEnumerableǁsplit__mutmut_4'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit__mutmut['xǁPartitionEnumerableǁsplit__mutmut_5'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit__mutmut['xǁPartitionEnumerableǁsplit__mutmut_6'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit__mutmut_6 # type: ignore # mutmut generated

mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['_mutmut_orig'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_1'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_2'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_3'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_4'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_5'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_6'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_7'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_8'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_9'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁsplit_multiple__mutmut['xǁPartitionEnumerableǁsplit_multiple__mutmut_10'] = PartitionEnumerable.xǁPartitionEnumerableǁsplit_multiple__mutmut_10 # type: ignore # mutmut generated

mutants_xǁPartitionEnumerableǁ_split_no_separator__mutmut['_mutmut_orig'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split_no_separator__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split_no_separator__mutmut['xǁPartitionEnumerableǁ_split_no_separator__mutmut_1'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split_no_separator__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split_no_separator__mutmut['xǁPartitionEnumerableǁ_split_no_separator__mutmut_2'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split_no_separator__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split_no_separator__mutmut['xǁPartitionEnumerableǁ_split_no_separator__mutmut_3'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split_no_separator__mutmut_3 # type: ignore # mutmut generated

mutants_xǁPartitionEnumerableǁ_split__mutmut['_mutmut_orig'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_1'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_2'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_3'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_4'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_5'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_6'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_7'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_8'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_9'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_10'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_11'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_12'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPartitionEnumerableǁ_split__mutmut['xǁPartitionEnumerableǁ_split__mutmut_13'] = PartitionEnumerable.xǁPartitionEnumerableǁ_split__mutmut_13 # type: ignore # mutmut generated
