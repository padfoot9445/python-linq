# Architecture

This document describes the current implementation of `python-linq`. It is
intentionally descriptive rather than a proposal: the separate
[API reference](API.md) describes public behavior, and the
[API parity inventory](API_PARITY.md) compares that behavior with .NET LINQ and
Rust iterators.

## Overview

The library is a synchronous, iterator-backed sequence API. Its main type,
`Enumerable[T]`, combines a set of focused operation mixins with a shared
`BaseEnumerable[T]` implementation. A typical lazy pipeline creates Python
iterators or generator functions and wraps them in another `Enumerable`.

```text
Python Iterable[T]
       |
       | iter(source), once
       v
BaseEnumerable[T] ---- stores one Iterator[T] in .value
       ^
       |
operation mixins
       |
       v
Enumerable[T] ---- public construction/factory type
```

`Enumerable` is a static typing specialization marker as well as a constructor;
`Enumerable[T]` does not validate values at runtime. The package requires
Python 3.15 or newer.

## Source and iteration model

`BaseEnumerable.__init__` calls `iter(source)` immediately and stores the
resulting iterator as `.value`. Its `__iter__` returns that same iterator.
Consequently, an instance is a cursor over one traversal, not a reusable
description of a source:

- Iterating an instance resumes its current position.
- Consuming a terminal operation advances that same cursor.
- Wrapping a list does not make the resulting `Enumerable` replayable.
- Constructing another `Enumerable` from a reusable collection creates a
  separate iterator, but constructing it from a generator uses that generator's
  current state.

The implementation exposes cursor behavior directly in some methods. For
example, `IteratorParityEnumerable.next()` advances `.value`, and
`CopyEnumerable.shallow_copy()` uses `itertools.tee` to split the remaining
cursor and replace `.value` with one tee branch. `by_ref()` returns the same
object. These are distinct operations: `by_ref()` shares position, while
`shallow_copy()` provides two independently advancing branches from the
current position, with `tee` buffering as needed.

There is no general source factory, replay cache, or capability protocol in the
current architecture. A result does not automatically retain information that
its input was sized, indexable, or repeatable.

## Class and mixin organization

The public class assembles behavior from inheritance layers:

```text
BaseEnumerable[T]
├── SelectEnumerable[T]
│   └── WholeSequenceOperationsEnumerable[T]
├── CopyEnumerable[T]
│   └── CountEnumerable[T]
├── FilterEnumerable[T]
├── TypeEnumerable[T]
├── ControlFlowEnumerable[T]
├── CollectEnumerable[T]
└── IteratorParityEnumerable[T]

TakeEnumerable[T] inherits from the operation mixins above
├── AggregateEnumerable[T]
└── PartitionEnumerable[T]

Enumerable[T]
├── AggregateEnumerable[T]
├── PartitionEnumerable[T]
└── WholeSequenceOperationsEnumerable[T]
```

The diagram shows inheritance relationships, not a strict single chain; the
actual composition uses Python multiple inheritance and its method resolution
order. In particular, `TakeEnumerable` combines most of the operation mixins,
and `Enumerable` combines aggregate, partition, and whole-sequence behavior
around that base. Mixins are kept in separate modules to group related
operations, but many inherit from other mixins to make shared methods
available.

### Module responsibilities

| Module | Responsibility |
|---|---|
| `base_enumerable.py` | Stores the iterator and implements iteration. |
| `enumerable.py` | Public `Enumerable` type and empty/range/repeat/sequence factories. |
| `take_enumerable.py` | Core terminals, slicing, peeking, reversal, and related sequence operations; defines `TakeEnumerableException`. |
| `filter_enumerable.py` | Filtering, distinctness, and containment. |
| `select_enumerable.py` | Projection, flattening, concatenation, append/prepend, and inspection callbacks. |
| `count_enumerable.py` | Counting, enumeration, and emptiness checks. |
| `collect_enumerable.py` | Materialization into a list. |
| `copy_enumerable.py` | `shallow_copy()` via `itertools.tee`. |
| `whole_sequence_operations_enumerable.py` | Zip, universal/existential checks, and sequence equality. |
| `aggregate_enumerable.py` | Fold, reduce, aggregate, join-fold, and scan. |
| `partition_enumerable.py` | Splitting a sequence into partitions. |
| `type_enumerable.py` | Typing-oriented cast operation. |
| `control_flow.py` | `ControlFlow` values and control-flow sequence adaptation. |
| `parity_enumerable.py` | Rust-iterator-inspired adaptors and terminals, plus associated result types. |
| `_sentinels.py` | Internal missing-value marker and public `DROP` marker for intentional filtering. |
| `__init__.py` | Public re-exports and the `identity` helper. |

## How operators are implemented

Most sequence-producing methods are lazy: they define a generator or use a
standard-library iterator such as `map`, `filter`, `zip`, or `itertools.islice`,
then return `Enumerable(generator_or_iterator)`. The source and callbacks are
usually consumed when the returned result is iterated, not when the adaptor is
called.

Examples of this construction pattern include:

- `where` wraps `filter(callback, self)`.
- `select` wraps `map(callback, self)`.
- `concat` creates a generator that yields from each input in order.
- `reverse` and `take_last` defer materialization inside a generator until that
  result is traversed.

This pattern keeps adaptors composable and makes the simple case stream
incrementally. It also means the returned result is generally a fresh
one-shot `Enumerable` backed by the adaptor's iterator. It does not carry
capability metadata or an automatic link to an independently traversable
source.

Scalar terminals such as `first`, `count`, `all`, and `fold` consume the
enumerable immediately. Operations requiring global knowledge—such as
ordering, grouping, joins, reversal, or taking from the end—may buffer when
their deferred result is consumed. Their exact behavior and buffering contracts
are specified in the [API reference](API.md).

Some methods are implemented by composing other public operators rather than
by introducing a separate execution engine. This reuses behavior, but also
means cursor consumption and any buffering follow the semantics of those
composed operations.

## Option values, sentinels, and `None`

`None` is valid sequence data. The implementation therefore uses distinct
representations for a present `None` and for absence or intentional discard:

- `rustshed.Some(value)` and `rustshed.Null` represent option-valued results;
  `Some(None)` means a present item whose value is `None`.
- `MISSING` distinguishes an omitted argument from an explicit `None` in APIs
  such as default-valued terminals.
- `DROP` is the explicit callback result meaning “discard this result” in
  operations such as `filter_map`; returning `None` keeps `None` in the output.
- `ControlFlow` uses a private `_NO_VALUE` marker to distinguish control
  variants that carry no item from variants whose payload may itself be `None`.

These are part of the implementation's type-safety strategy: absence and
control states are tagged rather than inferred from an ordinary item value.

## Typing and validation

The code uses generic classes and functions, Python 3.15 generic syntax,
overloads, protocols, and typed callback signatures. Runtime type validation of
sequence items is not performed by `Enumerable[T]`; the type parameter is for
static analysis.

Strict static checks include both library code and typing tests:

- Pyright uses strict mode and includes `src/python_linq` and `tests/typing`.
- Mypy uses strict mode over the same source and typing-test paths.
- Pytest runs tests under `tests/` and Markdown doctests in `docs/API.md`.

The exact commands and settings are maintained in `pyproject.toml`.

## Current architectural constraints

The one-iterator source model is simple and preserves the existing single-pass
contract, but it has consequences for extending the architecture:

1. A mixin can access `.value` directly, coupling it to the stored cursor.
2. Operators often return `Enumerable(...)` directly, so a subclass-specific
   capability would be lost unless that operator explicitly preserves it.
3. There is no shared mechanism for operator construction, fresh traversals,
   known length, indexing, or reverse access.
4. Optimizations based on a source's concrete type are not propagated
   consistently through pipelines.

Those observations describe current limitations, not commitments about a
future design. The
[capability-aware replayable-view proposal](CAPABILITY_AWARE_ENUMERABLE.md)
explores an opt-in alternative; it is not implemented by the architecture
described here.
