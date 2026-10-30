# API reference

This is the reference for the public API exported by `python_linq`. It describes
the current behavior of the implementation, including its single-pass source
model. The separate [parity matrix](API_PARITY.md) compares these APIs with .NET
LINQ-to-Objects and Rust's stable `Iterator`.

The examples in this document are executable doctests. Run them with the normal
test command:

```sh
uv run pytest
```

## Contents

- [Core model](#core-model)
- [Creating an enumerable](#creating-an-enumerable)
- [Lazy transformations and composition](#lazy-transformations-and-composition)
- [Slicing, peeking, and partitioning](#slicing-peeking-and-partitioning)
- [Grouping, sets, ordering, and joins](#grouping-sets-ordering-and-joins)
- [Terminal operations](#terminal-operations)
- [Rust-style iterator operations](#rust-style-iterator-operations)
- [Conversions and type operations](#conversions-and-type-operations)
- [Control flow and public helper types](#control-flow-and-public-helper-types)
- [Typing, `None`, and errors](#typing-none-and-errors)
- [Behavior index](#behavior-index)

## Core model

`Enumerable[T]` accepts any synchronous iterable. Construction immediately
calls `iter(source)` once and stores that iterator. Iterating the same instance
again resumes the same cursor; it does not restart the source. Construct a new
`Enumerable` for another traversal. There is no implicit replay or materialized
cache based on the input's concrete type. `shallow_copy()` only tees the
remaining cursor; it does not restart the source.

Sequence-producing operations generally defer work until iteration. Scalar
terminals consume immediately. Operations that need global information defer
the work but buffer when their returned sequence is consumed; these include
ordering, grouping, joins, reversal, `take_last`, and `skip_last`. A second
enumeration of a derived result is not guaranteed to replay it either.

```pycon
>>> from python_linq import Enumerable
>>> values = Enumerable([1, 2, 3])
>>> values.take(2).to_list()
[1, 2]
>>> values.to_list()
[3]

```

### Single-pass copying

`shallow_copy()` uses `itertools.tee` at the current cursor position. It directs
the original enumerable to one branch and returns an enumerable wrapping the
other branch. Both can read the same remaining values independently, with
buffered values retained until the slower branch catches up. The original
cursor object remains stable, so iterators and lazy adaptors already obtained
from the enumerable continue to follow its branch after the copy.

```pycon
>>> values = Enumerable([None, 2, 3])
>>> copy = values.shallow_copy()
>>> copy.first()
>>> values.first()
>>> copy.to_list() == [2, 3] and values.to_list() == [2, 3]
True

```

`by_ref()` returns the same enumerable, not a copy. Consuming either reference
advances the shared cursor. Python cannot enforce Rust's borrow lifetime.

## Creating an enumerable

| API | Behavior |
|---|---|
| `Enumerable(val=())` | Wrap the iterable's iterator immediately; `val` defaults to an empty tuple and retains its one-shot behavior. |
| `Enumerable.empty()` | Empty enumerable. |
| `Enumerable.range(start, count)` | Lazy integer range containing `count` values starting at `start`; negative count raises `ValueError`. |
| `Enumerable.repeat(value, count)` | Lazy finite repetition; negative count raises `ValueError`. |
| `Enumerable.sequence(start, count, step=1)` | Lazy finite arithmetic sequence; negative count raises `ValueError`. |
| `Enumerable.infinite_sequence(start=0, step=1)` | Lazy, unbounded arithmetic sequence. |
| `Enumerable[T]` | A static typing specialization marker. It does not construct an enumerable or validate items at runtime. |

```pycon
>>> Enumerable.range(4, 3).to_list()
[4, 5, 6]
>>> Enumerable.repeat(None, 2).to_list()
[None, None]
>>> Enumerable.sequence(2, 3, step=4).to_list()
[2, 6, 10]
>>> Enumerable.infinite_sequence(5, 2).take(4).to_list()
[5, 7, 9, 11]

```

## Lazy transformations and composition

These methods return sequences and perform their main work when the result is
iterated. They consume the source as needed and are not implicitly replayable.

### Projection and filtering

| API | Behavior |
|---|---|
| `where(predicate)` / `filter(predicate)` | Yield items for which `predicate(item)` is true. |
| `select(callback)` / `map(callback)` | Project each item. A callback result of `None` is retained. |
| `select_indexed(callback)` | Call `callback(item, zero_based_index)` and yield its result. |
| `filter_map(callback)` | Yield callback results except the exported `DROP` sentinel. `None` is valid output. |
| `flat_map(callback)` | Lazily map each item to an iterable and yield its elements. |
| `select_many(collection_selector, result_selector=None)` | Like `flat_map`; when provided, call `result_selector(outer, inner)` for each selected element. |
| `flatten()` | Flatten one iterable level. |
| `distinct(key=None)` | Yield the first occurrence of each equality-distinct item or key. |
| `distinct_by(key, comparer=None)` | Yield the first item per selected key, using equality or the supplied comparer. |
| `of_type(target_type)` | Yield items for which `isinstance(item, target_type)` is true. |
| `tee(callback)` / `inspect(callback)` | Call the callback as each item is consumed, then yield that item unchanged. |

Equality-based `distinct*` operations preserve first-occurrence order, accept
unhashable keys, and can require quadratic comparisons and memory proportional
to the number of distinct keys.

```pycon
>>> from python_linq import DROP
>>> Enumerable([1, 2, 3]).filter_map(
...     lambda n: None if n == 1 else n if n == 2 else DROP
... ).to_list()
[None, 2]
>>> Enumerable([{"id": 1}, {"id": 1}, {"id": 2}]).distinct_by(
...     lambda row: row["id"]
... ).to_list()
[{'id': 1}, {'id': 2}]
>>> Enumerable(["a", "bb", "ccc"]).select_indexed(
...     lambda item, index: (index, item)
... ).to_list()
[(0, 'a'), (1, 'bb'), (2, 'ccc')]

```

### Composition

| API | Behavior |
|---|---|
| `append(item)` / `prepend(item)` | Add one item at the end or beginning. |
| `concat(other)` / `chain(other)` | Yield this sequence, then enter `other` only after this sequence is exhausted. |
| `zip(other, strict=False)` | Lazily yield pairs. With `strict=True`, unequal lengths raise `ValueError`; mismatch detection may consume an unmatched item. |
| `enumerate()` | Lazily yield `(zero_based_index, item)` pairs. |
| `by_ref()` | Return the same enumerable/cursor. |
| `default_if_empty(default=MISSING)` | Pass through items unchanged, or yield one default on empty input. Omitted default yields `None`; an explicit `None` default is supported. |

```pycon
>>> Enumerable([1, 2]).prepend(0).append(3).concat([4]).to_list()
[0, 1, 2, 3, 4]
>>> Enumerable([None, 2]).zip(["missing", "two"]).to_list()
[(None, 'missing'), (2, 'two')]
>>> Enumerable[int]([]).default_if_empty(7).to_list()
[7]
>>> Enumerable([None]).default_if_empty(7).to_list()
[None]

```

### Mapping while, cycling, and interspersing

| API | Behavior |
|---|---|
| `step_by(step)` | Yield every `step`th item, starting with the first; `step` must be positive. |
| `intersperse(separator)` | Insert the separator between items, not before or after; empty/singleton inputs have no inserted separator. |
| `intersperse_with(callback)` | Call `callback()` only when a separator is needed between two items. |
| `map_while(callback)` | Map each item until the callback returns `DROP`; that result and the remaining source are omitted. |
| `find_map(callback)` | Eagerly return the first non-`DROP` callback result as `Some(result)`, or `Null` if none exists. |
| `cycle()` | Yield the first pass while caching it, then repeat the cache forever. Empty input stays empty. An infinite source never reaches the repeat phase and grows the cache without bound. |
| `fuse()` | Wrap the source so this output iterator stops permanently on its first exhaustion. |
| `array_chunks(size)` | Yield only full lists of `size`; discard an incomplete final chunk. |
| `map_windows(size, callback)` | Call the callback on each complete sliding window, passed as an immutable tuple view. |

Positive sizes/steps are validated when these methods are called.

```pycon
>>> Enumerable([None, 1, 2]).intersperse(None).to_list()
[None, None, 1, None, 2]
>>> Enumerable([1, 2, 3, 4]).map_windows(
...     3, lambda window: sum(window)
... ).to_list()
[6, 9]
>>> Enumerable([1, 2, 3, 4, 5]).array_chunks(2).to_list()
[[1, 2], [3, 4]]
>>> Enumerable([1, 2]).cycle().take(5).to_list()
[1, 2, 1, 2, 1]

```

## Slicing, peeking, and partitioning

### Slicing and prefix operators

| API | Behavior |
|---|---|
| `take(n=1)` / `skip(n=1)` | Lazy prefix slicing using `itertools.islice`; bounds must be non-negative. |
| `islice(start, stop, step=1)` | Python `itertools.islice` semantics; a provided step must be positive. |
| `take_last(n=1)` / `skip_last(n=1)` | Defer then buffer the source when consumed. Negative counts raise `ValueError`; `take_last(0)` does not consume. |
| `take_while(predicate)` / `take_while_lossy(predicate)` | Yield the matching prefix; consume and discard the first failing item. |
| `take_while_inclusive(predicate)` | Include the first failing item, then stop. |
| `take_while_lossless(predicate)` | Yield the matching prefix while leaving the first failing item available on the original enumerable. |
| `take_while_indexed(predicate)` | Call predicate as `(item, zero_based_index)` and yield the matching prefix. |
| `skip_while(predicate)` | Drop the initial matching prefix, yield the first non-match, then pass the remainder through. |
| `skip_while_indexed(predicate)` | Indexed counterpart; callback arguments are `(item, zero_based_index)`. |
| `chunk(size)` | Yield lists of up to `size`, including a final short chunk; positive size required. |

`take_while_lossless` uses a tee-based view and advances the original only for
items yielded by the result. If the result is abandoned partway through, the
original is positioned immediately after the yielded prefix.

### Peeking and emptiness

| API | Behavior |
|---|---|
| `peek()` | Return the next item without consuming it from the original; raises `TakeEnumerableException` if empty. |
| `try_peek()` | Return `Some(item)` or `Null`; `Some(None)` means a present `None`. |
| `peek_n(n)` | Non-consuming view of up to the next `n` items; non-positive `n` yields nothing. |
| `peek_while(predicate)` | Non-consuming view of the matching prefix. |
| `is_empty()` | Check whether any item remains without advancing the original, using `shallow_copy()`. |
| `shallow_copy()` | Tee the remaining cursor as described in [single-pass copying](#single-pass-copying). |

```pycon
>>> from rustshed import Null, Some
>>> values = Enumerable([None, 4])
>>> values.try_peek() == Some(None)
True
>>> values.peek_n(2).to_list()
[None, 4]
>>> _ = values.first()
>>> values.is_empty()
False

```

### Splitting

| API | Behavior |
|---|---|
| `split()` | Yield one single-item enumerable per item; empty input yields no segments. |
| `split(separator)` | Split on non-overlapping occurrences; omit delimiters. |
| `split_multiple(separators)` | Split on a sequence of values. The separator iterable is materialized when the result is first iterated. |

Leading, repeated, and trailing separators produce empty segments. An empty
separator sequence behaves like `split()`. Empty input with an explicit
non-empty separator produces one empty segment. `None` may be a separator;
`split_multiple` takes an iterable such as `[None]`.

```pycon
>>> [part.to_list() for part in Enumerable([1, 0, 0, 2, 0]).split(0)]
[[1], [], [2], []]
>>> [part.to_list() for part in Enumerable([None, 1, None]).split_multiple([None])]
[[], [1], []]

```

## Grouping, sets, ordering, and joins

### Grouping and set operations

| API | Behavior |
|---|---|
| `group_by(key_selector, element_selector=None, result_selector=None, comparer=None)` | Buffer all source items on iteration; preserve first-seen group order and item order within groups. Uses equality scans, supports unhashable keys, and optionally accepts a key comparer. |
| `count_by(key, comparer=None)` | Eagerly group/count items when iterated; yield `(first_seen_key, count)` pairs in first-seen order. |
| `aggregate_by(key, seed, aggregator, comparer=None)` | Buffer/group on iteration; call `aggregator(seed, item)` for each new key and update each group's accumulator. |
| `aggregate_by_seed_selector(key, seed_selector, aggregator, comparer=None)` | As above, but call `seed_selector(key)` for the first item of each group. |
| `union(other, comparer=None)` / `union_by(other, key, comparer=None)` | Stream unique first-source items before entering the second iterable; then yield new unique second-source items. Preserve encounter order. |
| `except_(other, comparer=None)` / `except_by(other, key, comparer=None)` | Buffer the second iterable at iteration start; yield unique first-source items whose values/keys are absent from it. |
| `intersect(other, comparer=None)` / `intersect_by(other, key, comparer=None)` | Buffer the second iterable at iteration start; yield unique matching first-source items in first-source order. |

These equality-scan operations support unhashable keys but may use quadratic
comparisons. They use equality (`==`) unless a comparer is supplied.

```pycon
>>> Enumerable(["ant", "ape", "bee"]).group_by(
...     lambda word: word[0]
... ).to_list()
[('a', ['ant', 'ape']), ('b', ['bee'])]
>>> Enumerable(["ant", "ape", "bee"]).count_by(
...     lambda word: word[0]
... ).to_list()
[('a', 2), ('b', 1)]
>>> Enumerable([None, 1, None]).union([1, None, 2]).to_list()
[None, 1, 2]

```

### Ordering

| API | Behavior |
|---|---|
| `order(key=None, reverse=False)` | Alias for primary ordering. |
| `order_descending()` | Sort values descending. |
| `order_by(key=None, reverse=False)` | Deferred stable sort of the complete source. Without a key, values must be mutually orderable. |
| `order_by_descending(key=None)` | Descending primary sort, optionally by key. |
| `then_by(key)` / `then_by_descending(key)` | Stable secondary ordering; valid only on a result directly produced by `order_by` or another `then_by*`. |
| `shuffle()` | Defer, buffer all values, then shuffle the list. |
| `reverse()` | Defer and buffer all values, then yield them in reverse order. |

The source is consumed only when an ordered sequence is iterated. Sorting needs
memory proportional to the source size. Ordering follows Python comparison
semantics; supply a key to order nullable or otherwise incomparable values.

```pycon
>>> Enumerable([("a", 2), ("b", 1), ("a", 1)]).order_by(
...     key=lambda row: row[0]
... ).then_by(lambda row: row[1]).to_list()
[('a', 1), ('a', 2), ('b', 1)]
>>> Enumerable([1, 2, 3]).reverse().to_list()
[3, 2, 1]

```

### Joins

| API | Behavior |
|---|---|
| `join_on(other, outer_key, inner_key, result_selector, comparer=None)` | Inner join; buffer `other` when iteration begins, then emit result-selector values in outer/inner encounter order. |
| `group_join(other, outer_key, inner_key, result_selector, comparer=None)` | Buffer `other`; call result selector once per outer item with a list of matching inner items. |
| `left_join(other, outer_key, inner_key, comparer=None)` | Emit `(outer, Some(inner))` for each match or `(outer, Null)` when unmatched. |
| `right_join(other, outer_key, inner_key, comparer=None)` | Emit `(Some(outer), inner)` per match or `(Null, inner)` when unmatched. |
| `full_join(other, outer_key, inner_key, comparer=None)` | Emit matching option pairs, then unmatched outer/inner rows tagged with `Null`. |

Join methods use equality unless a comparer is provided. `None` is valid in
either input and in keys. `Some(None)` is distinct from `Null`, which denotes
absence. The existing `join(separator, aggregator=operator.add)` is an
aggregate fold; `join_on` is the relational inner join to avoid a name
collision.

```pycon
>>> from rustshed import Null, Some
>>> Enumerable([("x", None), ("y", 2)]).left_join(
...     [("x", 10)], lambda row: row[0], lambda row: row[0]
... ).to_list()
[(('x', None), Some(value=('x', 10))), (('y', 2), NullType())]

```

## Terminal operations

Terminal operations consume the current cursor immediately, unless explicitly
noted. After a terminal has consumed items, subsequent operations see only the
remaining suffix.

### Selection, counting, and predicates

| API | Behavior |
|---|---|
| `first(predicate=None, default=MISSING)` | Return first item/match. Without an explicit default, missing input raises `TakeEnumerableException`. |
| `single(predicate=None, default=MISSING)` | Require exactly one item/match; missing uses explicit default if given, multiple matches always raise. |
| `last(predicate=None, default=MISSING)` | Consume all remaining items and return last item/match; missing raises unless a default is supplied. |
| `find(predicate, default=MISSING)` | Alias for `first(predicate, default=...)`. |
| `first_or_default(default=None, *, predicate=None)` | Return first item/match or the supplied default; omitted default is `None`. |
| `last_or_default(default=None, *, predicate=None)` | Return last item/match or default; consumes the remaining source. |
| `single_or_default(default=None, *, predicate=None)` | Return sole item/match or default; multiple matches raise. |
| `nth(n, default=MISSING)` | Return zero-based item `n`; negative `n` raises `ValueError`; absent item raises unless default supplied. |
| `element_at(index)` | Non-negative indices are zero-based; negative indices count from the end by buffering. An out-of-range index raises `TakeEnumerableException`. |
| `element_at_or_default(index, default=None)` | Return indexed item or default when absent. |
| `count(predicate=None)` / `long_count()` | Consume and count all remaining items, optionally filtering by predicate. Python integers have arbitrary precision. |
| `all(predicate)` / `any(predicate=None)` | Eager short-circuiting terminals. `all` is true on empty input; predicate-free `any` checks for one item. |
| `contains(value, comparer=None)` | Search until a match or end; comparer receives `(item, value)`. |
| `is_empty()` | Non-consuming check; see [peeking and emptiness](#peeking-and-emptiness). |

`MISSING` in signatures above is explanatory notation for a private omitted
argument marker; it is not exported. Explicit `default=None` is different from
omitting a default.

```pycon
>>> Enumerable([None, 3]).first()
>>> Enumerable([None, 3]).count(lambda item: item is None)
1
>>> Enumerable[int]([]).first_or_default()
>>> Enumerable[int]([]).first(default=None) is None
True

```

`single` raises when there are multiple matching items, even if a default is
provided. The no-match default is used only when there are zero matches.

```pycon
>>> from python_linq import TakeEnumerableException
>>> try:
...     Enumerable[int]([]).first()
... except TakeEnumerableException as error:
...     error.exception_case.name
'NotEnoughItems'

```

### Aggregation and comparison

| API | Behavior |
|---|---|
| `fold(aggregator, seed=MISSING)` / `reduce(aggregator)` | Eager accumulation. Without seed, first item initializes the accumulator; empty input raises `TakeEnumerableException`. |
| `aggregate(aggregator)` | No-seed aggregate form. |
| `aggregate(seed, aggregator, result_selector=None)` | Seeded aggregate with optional final result projection. |
| `scan(aggregator, seed=MISSING)` | Lazy intermediate accumulators. Without seed, first item is yielded as the initial accumulator; with seed, seed is yielded first, including on empty input. |
| `join(separator, aggregator=operator.add)` | Eager fold that places a separator between adjacent items; empty input raises. |
| `sum(selector=None)` | Eager Python sum; empty input returns `0`. |
| `average(selector=None)` | Eager `statistics.fmean`; empty input raises `StatisticsError`. |
| `min(key=None)` / `max(key=None)` | Eager Python extrema; empty input raises `ValueError`. |
| `product()` | Eager product; empty input returns `1`. |
| `eq(other, comparer=...)` / `sequence_equal(other, comparer=...)` | Compare equal-length sequences elementwise; comparer can compare differing types. |
| `neq(other, comparer=...)` | Negation of `eq`. |
| `eq_by(other, comparer)` | Equality with explicit comparer. |
| `cmp(other)` / `cmp_by(other, compare)` | Lexicographic comparison returning `Ordering`. |
| `partial_cmp(other)` / `partial_cmp_by(other, compare)` | Partial lexicographic comparison; return `Null` for incomparable values. |
| `lt(other)` / `le(other)` / `gt(other)` / `ge(other)` | Lexicographic relational comparisons. |
| `is_sorted()` / `is_sorted_by(compare)` / `is_sorted_by_key(key)` | Eager sortedness checks. `is_sorted_by` treats a `None` comparison result as unordered/not sorted. |
| `min_by(compare)` / `max_by(compare)` | Return `Some(item)` or `Null`; comparator returns negative/zero/positive integer. |
| `min_by_key(key)` / `max_by_key(key)` | Key-based Rust-style extrema returning `Some(item)` or `Null`. |

Python's numeric and ordering operations define the behavior for types such as
`None`; no implicit null ordering, numeric coercion, or CLR overflow rules are
added.

## Rust-style iterator operations

| API | Behavior |
|---|---|
| `next()` | Consume and return `Some(item)` or `Null`. |
| `next_chunk(size)` | Consume up to `size` items and return `NextChunkResult(items, complete)`; positive size required. An incomplete result retains the items already read. |
| `advance_by(count)` | Consume up to `count` items and return `AdvanceByResult(complete, remaining)`; negative count raises `ValueError`. |
| `position(predicate)` | Return `Some(zero_based_index)` for the first match, else `Null`. |
| `rposition(predicate)` | Buffer all remaining items, then search backward; return `Some(index)` or `Null`. |
| `for_each(callback)` | Eagerly call callback on every remaining item. |
| `partition(predicate)` | Eagerly return `(matching_items, nonmatching_items)` as two lists. |
| `is_partitioned(predicate)` | Check whether all matching items precede all nonmatching items; short-circuit on violation. |
| `collect_into(collection)` | Extend and return a collection implementing `extend(iterable)`. |
| `unzip()` | For pair items, eagerly return two lists. |

`Ordering` is an `IntEnum` with `Less = -1`, `Equal = 0`, and `Greater = 1`.
`AdvanceByResult` and generic `NextChunkResult[T]` are frozen dataclasses.

```pycon
>>> from python_linq import Ordering
>>> values = Enumerable([None, 2, 3])
>>> values.next() == Some(None)
True
>>> values.next_chunk(2)
NextChunkResult(items=[2, 3], complete=True)
>>> Enumerable([1, 2]).cmp([1, 3]) is Ordering.Less
True
>>> Enumerable([]).next() == Null
True

```

```pycon
>>> Enumerable([1, 2, 3]).fold(lambda total, item: total + item, seed=0)
6
>>> Enumerable([1, 2, 3]).scan(
...     lambda total, item: total + item, seed=0
... ).to_list()
[0, 1, 3, 6]
>>> Enumerable([1, 2, 3]).position(lambda item: item == 2) == Some(1)
True
>>> Enumerable([None, 1]).partition(lambda item: item is not None)
([1], [None])

```

## Conversions and type operations

| API | Behavior |
|---|---|
| `to_list()` / `to_array()` | Eagerly consume remaining items into a Python list. |
| `to_hashset()` | Eagerly consume into a Python `set`; items must be hashable. |
| `to_dictionary(key_selector, element_selector=None)` | Eagerly build a dictionary; keys must be hashable and duplicate keys raise `ValueError`. |
| `to_lookup(key_selector, element_selector=None)` | Eagerly build a dictionary from keys to lists; keys must be hashable. |
| `cast(type=None)` | Static typing cast only; does not convert or validate runtime values. |
| `identity(value)` | Return `value` unchanged. |
| `try_get_non_enumerated_count()` | Return `Some(len(iterator))` only if the wrapped source iterator implements `Sized`; otherwise `Null`. Does not consume. A normal list iterator may not expose this capability even when its original list has a known length. |

Custom equality comparers are supported by grouping and sequence set operations,
but not by Python dict/set conversion methods. Duplicate dictionary keys are
reported as `ValueError`.

```pycon
>>> Enumerable([("a", 1), ("b", 2)]).to_dictionary(
...     lambda pair: pair[0], lambda pair: pair[1]
... )
{'a': 1, 'b': 2}
>>> Enumerable([1, 2, 2]).to_hashset()
{1, 2}
>>> Enumerable([None, 1]).to_lookup(lambda item: item)
{None: [None], 1: [1]}
>>> Enumerable([None, "x", 3]).of_type(int).to_list()
[3]

```

## Control flow and public helper types

`ControlFlow[T]` describes how `control_flow(callback)` handles each item:

| Factory | Effect |
|---|---|
| `ControlFlow.ok(value)` | Yield the value and continue invoking the callback. |
| `ControlFlow.skip()` | Drop this item and continue. |
| `ControlFlow.stop()` | Stop without yielding a value. |
| `ControlFlow.stop_ok(value)` | Yield the value and stop. |
| `ControlFlow.yield_control_ok(value)` | Yield the value, then pass the untouched remainder through. |
| `ControlFlow.yield_control_skip(value)` | Drop this item and the untouched remainder. The argument is intentionally ignored. |

Values may be `None`. The no-payload states use a private marker, while the
public `ControlFlowNestedState` enum describes nested behavior. Construct flows
with the factory methods instead of manually choosing internal state fields.

Other exports:

| Export | Purpose |
|---|---|
| `DROP` | Explicit callback output used by `filter_map` to discard or by `map_while` to stop. |
| `FilterMapDrop` | Enum type of `DROP`. |
| `Ordering` | Lexicographic comparison result. |
| `AdvanceByResult` | `complete` and `remaining` counts from `advance_by`. |
| `NextChunkResult[T]` | `items` already consumed and whether the requested chunk was complete. |
| `TakeEnumerableException` | Error for exact/single-item count expectations. |
| `TakeEnumerableExceptionCase` | Enum exposed as `exception.exception_case` (`NotEnoughItems` or `TooManyItems`). |
| `ControlFlow` / `ControlFlowNestedState` | Control-flow values and nested-mode enum. |
| `identity(value)` | Generic identity function. |

`TakeEnumerableException` is also raised by `first`, `last`, `single`, `find`,
and `nth` when required items are absent and no default is supplied.

```pycon
>>> from python_linq import ControlFlow, identity
>>> Enumerable([1, 2, 3]).control_flow(
...     lambda n: ControlFlow.stop_ok(n) if n == 2 else ControlFlow.ok(n)
... ).to_list()
[1, 2]
>>> identity(None) is None
True

```

## Typing, `None`, and errors

The package targets Python 3.15+, ships `py.typed`, and is checked with strict
Pyright and mypy. Generic methods preserve item/result types where practical;
the typing suite contains consumer-style `assert_type` examples.

`None` is ordinary sequence data and callback output. Empty results, absent
matches, omitted arguments, and control states are represented by distinct
mechanisms:

- `None` may be yielded, selected, grouped, joined, or used as an explicit
  default.
- `Some(None)` means an option contains an actual `None`; `Null` means no
  option value.
- Omitted defaults use a private sentinel, so omitting a default differs from
  explicitly passing `None`.
- `filter_map` discards only `DROP`; it does not treat `None` as absence.
- `flat_map`/`flatten` require iterable values and raise Python's `TypeError`
  for a non-iterable bundle such as `None`.
- Numeric and ordering operations use Python behavior and can raise `TypeError`
  for unsupported values. Dictionary and set conversions require hashable keys
  or items.

Sequence-producing calls may validate scalar parameters immediately (for
example non-positive chunk sizes or negative counts) while consuming the
source only when iterated. Whole-source operations buffer on first iteration;
scalar terminals consume immediately.

## Behavior index

This table lists the public `Enumerable` methods by family. Detailed contracts
are in the sections above; the method links point into the corresponding
sections.

| Family | Methods |
|---|---|
| Construction | [`empty`](#creating-an-enumerable), [`range`](#creating-an-enumerable), [`repeat`](#creating-an-enumerable), [`sequence`](#creating-an-enumerable), [`infinite_sequence`](#creating-an-enumerable), constructor, `__getitem__` typing marker |
| Projection/filtering | [`where`](#projection-and-filtering), [`filter`](#projection-and-filtering), [`select`](#projection-and-filtering), [`map`](#projection-and-filtering), [`select_indexed`](#projection-and-filtering), [`filter_map`](#projection-and-filtering), [`flat_map`](#projection-and-filtering), [`select_many`](#projection-and-filtering), [`flatten`](#projection-and-filtering), [`distinct`](#projection-and-filtering), [`distinct_by`](#projection-and-filtering), [`of_type`](#projection-and-filtering), [`tee`](#projection-and-filtering), [`inspect`](#projection-and-filtering) |
| Composition | [`append`](#composition), [`prepend`](#composition), [`concat`](#composition), [`chain`](#composition), [`zip`](#composition), [`enumerate`](#composition), [`by_ref`](#composition), [`default_if_empty`](#composition) |
| Lazy adaptors | [`step_by`](#mapping-while-cycling-and-interspersing), [`intersperse`](#mapping-while-cycling-and-interspersing), [`intersperse_with`](#mapping-while-cycling-and-interspersing), [`map_while`](#mapping-while-cycling-and-interspersing), [`cycle`](#mapping-while-cycling-and-interspersing), [`fuse`](#mapping-while-cycling-and-interspersing), [`array_chunks`](#mapping-while-cycling-and-interspersing), [`map_windows`](#mapping-while-cycling-and-interspersing) |
| Slicing/peek/split | [`take`](#slicing-and-prefix-operators), [`skip`](#slicing-and-prefix-operators), [`islice`](#slicing-and-prefix-operators), [`take_last`](#slicing-and-prefix-operators), [`skip_last`](#slicing-and-prefix-operators), [`take_while`](#slicing-and-prefix-operators), [`take_while_lossy`](#slicing-and-prefix-operators), [`take_while_inclusive`](#slicing-and-prefix-operators), [`take_while_lossless`](#slicing-and-prefix-operators), [`take_while_indexed`](#slicing-and-prefix-operators), [`skip_while`](#slicing-and-prefix-operators), [`skip_while_indexed`](#slicing-and-prefix-operators), [`chunk`](#slicing-and-prefix-operators), [`peek`](#peeking-and-emptiness), [`try_peek`](#peeking-and-emptiness), [`peek_n`](#peeking-and-emptiness), [`peek_while`](#peeking-and-emptiness), [`is_empty`](#peeking-and-emptiness), [`shallow_copy`](#single-pass-copying), [`split`](#splitting), [`split_multiple`](#splitting) |
| Group/set/order/join | [`group_by`](#grouping-and-set-operations), [`count_by`](#grouping-and-set-operations), [`aggregate_by`](#grouping-and-set-operations), [`aggregate_by_seed_selector`](#grouping-and-set-operations), [`distinct_by`](#grouping-and-set-operations), [`union`](#grouping-and-set-operations), [`union_by`](#grouping-and-set-operations), [`except_`](#grouping-and-set-operations), [`except_by`](#grouping-and-set-operations), [`intersect`](#grouping-and-set-operations), [`intersect_by`](#grouping-and-set-operations), [`order`](#ordering), [`order_descending`](#ordering), [`order_by`](#ordering), [`order_by_descending`](#ordering), [`then_by`](#ordering), [`then_by_descending`](#ordering), [`shuffle`](#ordering), [`reverse`](#ordering), [`join_on`](#joins), [`group_join`](#joins), [`left_join`](#joins), [`right_join`](#joins), [`full_join`](#joins) |
| Terminals | [`first`](#selection-counting-and-predicates), [`single`](#selection-counting-and-predicates), [`last`](#selection-counting-and-predicates), [`find`](#selection-counting-and-predicates), [`first_or_default`](#selection-counting-and-predicates), [`last_or_default`](#selection-counting-and-predicates), [`single_or_default`](#selection-counting-and-predicates), [`nth`](#selection-counting-and-predicates), [`element_at`](#selection-counting-and-predicates), [`element_at_or_default`](#selection-counting-and-predicates), [`count`](#selection-counting-and-predicates), [`long_count`](#selection-counting-and-predicates), [`all`](#selection-counting-and-predicates), [`any`](#selection-counting-and-predicates), [`contains`](#selection-counting-and-predicates), [`fold`](#aggregation-and-comparison), [`reduce`](#aggregation-and-comparison), [`aggregate`](#aggregation-and-comparison), [`scan`](#aggregation-and-comparison), [`join`](#aggregation-and-comparison), [`sum`](#aggregation-and-comparison), [`average`](#aggregation-and-comparison), [`min`](#aggregation-and-comparison), [`max`](#aggregation-and-comparison), [`product`](#aggregation-and-comparison), [`eq`](#aggregation-and-comparison), [`neq`](#aggregation-and-comparison), [`sequence_equal`](#aggregation-and-comparison), [`eq_by`](#aggregation-and-comparison), [`cmp`](#aggregation-and-comparison), [`cmp_by`](#aggregation-and-comparison), [`partial_cmp`](#aggregation-and-comparison), [`partial_cmp_by`](#aggregation-and-comparison), [`lt`](#aggregation-and-comparison), [`le`](#aggregation-and-comparison), [`gt`](#aggregation-and-comparison), [`ge`](#aggregation-and-comparison), [`is_sorted`](#aggregation-and-comparison), [`is_sorted_by`](#aggregation-and-comparison), [`is_sorted_by_key`](#aggregation-and-comparison), [`min_by`](#aggregation-and-comparison), [`max_by`](#aggregation-and-comparison), [`min_by_key`](#aggregation-and-comparison), [`max_by_key`](#aggregation-and-comparison), [`next`](#rust-style-iterator-operations), [`next_chunk`](#rust-style-iterator-operations), [`advance_by`](#rust-style-iterator-operations), [`position`](#rust-style-iterator-operations), [`rposition`](#rust-style-iterator-operations), [`for_each`](#rust-style-iterator-operations), [`partition`](#rust-style-iterator-operations), [`is_partitioned`](#rust-style-iterator-operations), [`collect_into`](#rust-style-iterator-operations), [`unzip`](#rust-style-iterator-operations) |
| Conversion | [`to_list`](#conversions-and-type-operations), [`to_array`](#conversions-and-type-operations), [`to_hashset`](#conversions-and-type-operations), [`to_dictionary`](#conversions-and-type-operations), [`to_lookup`](#conversions-and-type-operations), [`cast`](#conversions-and-type-operations), [`try_get_non_enumerated_count`](#conversions-and-type-operations) |
| Other | [`control_flow`](#control-flow-and-public-helper-types), [`identity`](#control-flow-and-public-helper-types) |

For comparison status, intentional non-parity, and source-language limitations,
see the [API parity matrix](API_PARITY.md).
