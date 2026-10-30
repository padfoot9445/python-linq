# python-linq

`python-linq` is a typed, synchronous sequence API inspired by .NET LINQ and Rust's iterator adaptors. It operates on Python iterables and favors lazy pipelines.

Requires Python 3.15 or newer.

[Complete API reference](docs/API.md) documents the public methods and their behavior with examples executed by pytest. The [API parity inventory](docs/API_PARITY.md) compares method families with .NET 10 LINQ-to-Objects and stable Rust `Iterator`, including deliberate adaptations and non-portable guarantees.

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

## Parity-oriented operators

The API also includes:

- Lazy Rust-style adaptors: `step_by`, `intersperse`, `intersperse_with`, `map_while`, `inspect`, `fuse`, `cycle`, `array_chunks`, and `map_windows`. `array_chunks` drops an incomplete final chunk; unlike `chunk`, it emits only full chunks. `cycle` caches the first pass, so an infinite input keeps yielding but grows its cache without bound.
- Rust-style terminals: `next`, `next_chunk`, `advance_by`, `position`, `rposition`, `min_by`/`max_by`, `min_by_key`/`max_by_key`, lexicographic comparisons, sortedness checks, `partition`, `is_partitioned`, `product`, and `unzip`. Option-valued results use `rustshed.Some`/`Null`, so a present `None` is represented as `Some(None)`.
- `by_ref()` returns the same one-shot enumerable so consuming an adaptor advances its shared position; Python cannot enforce the borrow lifetime guaranteed by Rust. This differs from `shallow_copy()`, which tees the iterator.
- LINQ set/grouping operators: `distinct_by`, `union`/`union_by`, `except_`/`except_by`, `intersect`/`intersect_by`, `count_by`, `aggregate_by`, and selector/comparer forms of `group_by`. Equality scans preserve encounter order and can support unhashable keys, at the cost of quadratic comparisons in the worst case.
- LINQ join/conversion operators: `join_on` (the existing `join` name remains the aggregate fold), `group_join`, `left_join`, `right_join`, `full_join`, `to_array`, `to_hashset`, `to_dictionary`, and `to_lookup`. Joins buffer the inner side as needed; unmatched outer/inner values are tagged with `Null`, not represented by `None`.
- Ordering and factory additions: `order`, `order_descending`, `order_by_descending`, `then_by`, `then_by_descending`, `of_type`, `Enumerable.empty`, `Enumerable.range`, `Enumerable.repeat`, `Enumerable.sequence`, and `Enumerable.infinite_sequence`. Secondary ordering is stable and requires an `order_by` result.

## API behavior

Unless noted as a terminal, operators returning an `Enumerable` do not consume the main source until the result is iterated. These iterators are single-pass. Callback execution follows source order; if iteration stops early, callbacks and source elements after that point are not processed, except where an operator explicitly buffers.

| API | Behavior |
| --- | --- |
| `where(predicate)` / `filter(predicate)` | Lazily yields items whose predicate is true. |
| `select(callback)` / `map(callback)` | Lazily transforms each item; returned `None` is preserved as an item. |
| `flat_map(callback)` | Lazily maps each item to an iterable and yields that iterable's contents. |
| `flatten()` | Lazily flattens one iterable level. |
| `filter_map(callback)` | Lazily maps items; `python_linq.DROP` discards a callback result, while `None` is yielded as ordinary data. |
| `tee(callback)` | Calls the callback for each consumed item and yields that same item. The callback's return value is ignored. |
| `distinct(key=None)` | Lazily yields the first item for each equality-distinct key (the item itself by default). Keys need not be hashable; equality is used and retained keys consume memory. |
| `contains(value, comparer=None)` | Eagerly searches until a matching item is found or the source ends. |
| `append(item)` / `prepend(item)` | Lazily add one item at the end or beginning. |
| `concat(other)` / `chain(other)` | Yields this source, then `other`; the other iterable is not entered until the first source is exhausted. |
| `zip(other, strict=False)` | Lazily yields pairs until either side ends. `strict=True` raises `ValueError` if lengths differ; it can consume an unmatched item while detecting the mismatch. |
| `enumerate()` | Lazily yields `(zero_based_index, item)` pairs. |
| `take(n=1)` / `skip(n=1)` | Lazily take a prefix or skip a prefix. Underlying `itertools.islice` rejects negative bounds; `take` also asserts that `n` is an integer. |
| `islice(start, stop, step=1)` | Python `itertools.islice` behavior: bounds must be non-negative when provided and step must be positive. Argument validation occurs when called; elements are consumed when iterated. |
| `skip_while(predicate)` | Drops the initial matching prefix, then yields the first nonmatch and the remaining source without further predicate calls. |
| `take_while(predicate)` / `take_while_lossy(predicate)` | Yields matching prefix and drops the first failing item from this enumerable. |
| `take_while_inclusive(predicate)` | Yields matching prefix and also yields the first failing item. |
| `take_while_lossless(predicate)` | Yields matching prefix and leaves the first failing item available on the original enumerable. |
| `peek()` / `try_peek()` | Look at the next item without consuming it from the original enumerable. `peek` raises `TakeEnumerableException` on empty input; `try_peek` returns `rustshed.Null` or `rustshed.Some(item)`, including `Some(None)`. |
| `peek_n(n)` / `peek_while(predicate)` | Non-consuming views of at most the next `n` items or the next matching prefix. For `n <= 0`, `peek_n` yields no items. |
| `shallow_copy()` | Returns a second iterator over the current position using `itertools.tee`; both iterators can advance independently, with memory retained until the slower copy catches up. |
| `reverse()` / `take_last(n=1)` / `skip_last(n=1)` | Deferred but buffer the source when iterated. `skip_last` is composed from reverse/skip/reverse. Negative counts raise `ValueError`; `take_last(0)` does not consume the source. |
| `exact(n, default=MISSING)` | Returns a deferred sequence of exactly `n` items. It raises `ValueError` for negative `n`, `TakeEnumerableException` for too many/few items, or repeats the explicit default to fill a shortfall. Validation is on iteration; at most `n + 1` source items are consumed to validate. |
| `chunk(size)` | Lazily yields lists of up to `size` items, including a final short chunk. `size <= 0` raises `ValueError` at call time. |
| `group_by(key_selector, element_selector=None, result_selector=None, comparer=None)` | On iteration, consumes the entire source into insertion-ordered groups and then yields group pairs or result-selector values. Equality scans allow unhashable keys; an optional comparer defines key grouping. |
| `order_by(key=None, reverse=False)` / `then_by(key)` | On iteration, consumes and stably sorts the whole source. Without a key, items must be mutually orderable. `then_by` is only valid on an `order_by` result. |
| `default_if_empty(default=None)` | Lazily passes through a nonempty source unchanged; on an empty source yields exactly the provided default (or `None`). |
| `first(predicate=None, default=MISSING)` | Eagerly consumes the first item, or the first predicate match. Raises `TakeEnumerableException` if absent and no default is given. |
| `single(predicate=None, default=MISSING)` | Eagerly validates exactly one item/match. Uses the default only when there are none; multiple matches always raise `TakeEnumerableException`. |
| `last(predicate=None, default=MISSING)` | Eagerly consumes the whole source and returns its last item/match. Raises `TakeEnumerableException` if absent and no default is given. |
| `find(predicate, default=MISSING)` | Same behavior as `first(predicate, default=...)`. |
| `nth(n, default=MISSING)` | Eagerly consumes through zero-based index `n`. Negative `n` raises `ValueError`; a missing index raises `TakeEnumerableException` unless a default is supplied. |
| `count()` | Eagerly consumes the rest of the source and returns its item count. |
| `is_empty()` | Checks emptiness without consuming items from the original enumerable, using a shallow tee copy. |
| `all(predicate)` / `any(predicate)` | Eager short-circuiting terminals. `all` is true on empty input; predicate-free `any()` checks for at least one item. |
| `eq(other, comparer=...)` / `sequence_equal(other, comparer=...)` | Eagerly compares items in order and also checks equal lengths. The default comparison uses `==`; an optional comparer can compare differing types. |
| `neq(other, comparer=...)` | Negation of `eq`, with the same default comparison/comparer behavior. |
| `fold(aggregator, seed=MISSING)` / `reduce(aggregator)` | Eagerly accumulates the source. Without a seed, the first item initializes the accumulator and empty input raises `TakeEnumerableException`. `reduce` is the no-seed form. |
| `scan(aggregator, seed=MISSING)` | Lazily yields intermediate accumulator values. Without a seed, the first item is yielded as the initial accumulator; an empty source raises `TakeEnumerableException` when iterated. With a seed, the seed itself is yielded first, even for empty input. |
| `join(separator, aggregator=operator.add)` | Folds items into one value, placing `separator` between adjacent items. It requires at least one item; an empty source raises `TakeEnumerableException`. |
| `sum(selector=None)` / `average(selector=None)` / `min()` / `max()` | Eager numeric/order terminals using Python built-ins (`average` uses `statistics.fmean`). Empty `sum` returns zero; empty average raises `StatisticsError`; empty min/max raise `ValueError`. Types must support the corresponding Python operation. |
| `split()` | Lazily yields one single-item enumerable per source item; empty input yields no segments. |
| `split(separator)` / `split_multiple(separator)` | Lazily split at non-overlapping separator occurrences; delimiters are removed and leading, adjacent, and trailing delimiters produce empty segments. An empty separator is treated like `split()` (single-item segments). Empty input with an explicit separator produces one empty segment. `split_multiple` materializes its separator iterable when the result is iterated. |
| `cast(type)` | Static typing cast only; does not convert or validate runtime values. |
| `to_list()` | Eagerly consumes the remaining source into a list. |
| `identity(value)` | Returns the same value unchanged. |
| `control_flow(callback)` | Lazily interprets `ControlFlow.ok(value)` as yield, `skip()` as drop, `stop()` as stop, `stop_ok(value)` as yield then stop, `yield_control_ok(value)` as yield then pass the remaining source through unchanged, and `yield_control_skip(value)` as consume/drop the remainder (its argument is ignored). Payload-bearing states may carry `None`; `ControlFlowNestedState` represents the nested mode separately from payload values. |
| `TakeEnumerableException` | Raised for insufficient or excess items by exact/single-style operations; inspect `exception_case` for `NotEnoughItems` or `TooManyItems`. |

Omitted defaults are distinct from explicit `default=None`; `None` is valid sequence and callback-output data and missing values are not detected by truthiness. `filter_map` uses the public `DROP` sentinel to discard results. This replaces its previous `None`-means-drop behavior so callbacks can emit `None`. `first`, `single`, `last`, `find`, and `nth` raise `TakeEnumerableException` on absence by default. `single` still raises when multiple items match.

`fold`/`scan` without a seed use the first item as the initial accumulator; a seeded `scan` yields the seed first. This seeded output matches `itertools.accumulate(initial=...)`, unlike Rust's `scan`.

### `None`-safety contract

`None` is an ordinary item and callback output unless an argument position has an explicitly documented control meaning:

| API group | `None` behavior |
| --- | --- |
| Construction, iteration, `to_list`, `map`/`select`, `tee`, `append`/`prepend`, `concat`/`chain`, `flat_map`/`flatten`, slicing, chunks, reversal, and enumeration | Preserved as sequence data. `flat_map`/`flatten` require each produced value to be iterable; a `None` bundle therefore raises the normal `TypeError`. |
| `where`/`filter`, `skip_while`, `take_while*`, `peek_while`, `all`/`any`, and terminal predicates | Predicates receive `None` like any other item. Whether it passes is determined by the callback. |
| `filter_map` | A returned `None` is yielded; only the exported `DROP` sentinel discards an output. |
| `distinct`, set operators, `contains`, equality, `zip`, `group_by` | Equality/comparer operations accept `None`; grouping/set operations use equality scans and also support unhashable keys. `None` used as an item is not an end/padding marker. |
| `first`/`single`/`last`/`find`/`nth`, `exact`, `default_if_empty`, `fold`/`scan` | `None` items, seeds, and explicit defaults are preserved. Missing-item detection uses a sentinel or an explicit option result, not a `None` value. |
| `peek`/`try_peek`, `is_empty`, `count`, `cast`, `identity`, and control-flow payloads | `None` is preserved. `try_peek` distinguishes empty from a present `None` as `Null` versus `Some(None)`. Control-flow payload absence uses a private marker, and nested modes use `ControlFlowNestedState`. |
| Numeric and ordering terminals (`sum`, `average`, `min`, `max`, `order_by`) | No special null ordering or nullable numeric rule is invented. They follow the corresponding Python operation: unsupported mixed values raise Python's normal `TypeError`; use a key that maps values to comparable keys where applicable. `to_dictionary`/`to_lookup` require hashable keys, while `group_by` and set operations use equality scans. |
| Delimiter and callback-option positions (`split`, `split_multiple`, `predicate=None`, `key=None`, `comparer=None`) | `None` may be a delimiter for `split`; use `[None]` for `split_multiple`. Optional callback parameters use `None` to mean “not provided” and cannot themselves be `None`-accepting callbacks. To delimit on `None` in `split_multiple`, supply an iterable containing it. |

## Deliberate differences and remaining gaps

- LINQ's `IEnumerable<T>` is commonly re-enumerable; this package intentionally wraps and consumes a single iterator, closer to Rust's `Iterator`.
- A seeded `scan` yields its seed before accumulated values (like `itertools.accumulate(initial=...)`), unlike Rust's `scan`.
- Reversal, `take_last`, grouping, and ordering are deferred but need to buffer when iteration begins. Rust's `rev` instead requires a double-ended iterator.
- Full source-language parity is not feasible: Python cannot enforce Rust's trait bounds, borrowing, ownership, or const-generic array lengths, and the package intentionally remains a single-pass iterator rather than LINQ's commonly replayable query. `IQueryable`, provider/database translation, CLR numeric overflow/nullability overloads, and Rust's generic `Try`/`Residual` methods are out of scope. See the [parity matrix](docs/API_PARITY.md) for per-method status and details.

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
