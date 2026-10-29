# python-linq

`python-linq` is a typed, synchronous sequence API inspired by .NET LINQ and Rust's iterator adaptors. It operates on Python iterables and favors lazy pipelines.

Requires Python 3.15 or newer.

```python
from python_linq import Enumerable

evens = (
    Enumerable(range(10))
    .where(lambda value: value % 2 == 0)
    .select(lambda value: value * 10)
)
print(evens.to_list())  # [0, 20, 40, 60, 80]
```

## Execution and consumption

An `Enumerable` wraps a single iterator. It is single-pass: consuming an operation advances the wrapped iterator, and a second iteration does not replay the original source. Sequence-producing operations defer source consumption and callbacks until their result is iterated where feasible. Operations that need global knowledge, such as `reverse`, `take_last`, grouping, and ordering, buffer when iterated. Scalar operations such as `first`, `count`, `all`, and `fold` consume immediately.

`exact(n)` is a sequence-producing validation operation and validates when its result is iterated. `skip`/`take` and their `islice` primitive use Python's non-negative slice-index constraints.

## Current operators

| Area | Operators |
| --- | --- |
| Filter/project | `where`/`filter`, `select`/`map`, `flat_map`, `filter_map`, `flatten`, `distinct`, `contains` |
| Compose | `append`, `prepend`, `concat`/`chain`, `zip`, `enumerate`, `split` |
| Take/skip | `take`, `skip`, `take_last`, `skip_last`, `take_while`/`take_while_lossy`, `take_while_inclusive`, `take_while_lossless`, `skip_while`, `peek`, `peek_n`, `peek_while`, `reverse`, `exact` |
| Group/order | `chunk`, `group_by`, `order_by`, `default_if_empty` |
| Aggregate | `fold`/`reduce`, `scan`, `join`, `sum`, `average`, `min`, `max`, `count` |
| Terminal/query | `first`, `single`, `last`, `find`, `nth`, `is_empty`, `all`, `any` (with or without a predicate), `eq`/`sequence_equal`, `neq`, `to_list`, `cast` |

`fold`/`scan` without a seed use the first item as the initial accumulator; a seeded `scan` yields the seed first. `cast(type)` is a type-checker cast only: it neither converts nor validates runtime values. `filter_map` uses a callback result of `None` to mean “discard”; `map`/`select` preserve `None` as an ordinary item.

`None` is valid sequence data. Omitted defaults are distinguished from explicit `default=None`; missing values are not detected by truthiness. `ControlFlow.ok(None)` and `stop_ok(None)` are payload-bearing outcomes, distinct from skip/stop.

Scalar absence behavior is package-specific: `first`, `single`, `last`, `find`, and `nth` raise `TakeEnumerableException` when no value is found unless a default is supplied. `single` still raises when more than one item matches. `zip` truncates by default; pass `strict=True` to reject unequal lengths.

## Deliberate differences and remaining gaps

- LINQ's `IEnumerable<T>` is commonly re-enumerable; this package intentionally wraps and consumes a single iterator, closer to Rust's `Iterator`.
- A seeded `scan` yields its seed before accumulated values (like `itertools.accumulate(initial=...)`), unlike Rust's `scan`.
- Reversal, `take_last`, grouping, and ordering are deferred but need to buffer when iteration begins. Rust's `rev` instead requires a double-ended iterator.
- This is not exhaustive LINQ/Rust parity. Notable omissions include secondary ordering (`then_by`), set operators (`union`, `intersect`, `except`), joins/group joins, `to_dictionary`, and Rust adaptors such as `step_by`, `intersperse`, and `cycle`. Provider/database query APIs are out of scope.

## Typing and checks

The package ships `py.typed`. Strict Pyright and mypy both check package code and consumer-style typing examples:

```sh
uv run pyright
uv run mypy
uv run pytest
```

CI runs the test suite and both type-check gates.

## Comparison scope

The API borrows common query operators from LINQ and lazy adaptor patterns from Rust's `Iterator`, without claiming full parity. It does not implement `IQueryable` providers, database query translation, Rust trait bounds, or replayable LINQ-style enumeration. Python iterators are single-pass, and some operations necessarily buffer.
