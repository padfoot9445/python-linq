# .NET LINQ and Rust Iterator API parity

This inventory compares the public method families documented by [.NET 10 `System.Linq.Enumerable`](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable?view=net-10.0) with the [stable Rust `std::iter::Iterator` trait](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html). Entries group overloads under their method name; overload-specific behavior is called out in the notes. `Enumerable` remains a single-pass Python iterator wrapper. The matrix does not claim that Python can reproduce LINQ replayability or Rust's static trait, borrowing, or ownership guarantees.

Disposition:

- **Present**: current API provides the method or a documented direct equivalent.
- **Adapted**: behavior is available with explicit Python semantics or different naming.
- **Limited**: only the generic behavior can be offered; a source-language capability/guarantee is not expressible.
- **Not portable**: source-language semantics rely on a type system or runtime contract without a faithful Python equivalent.
- **Out of scope**: outside the confirmed in-memory/synchronous reference target.

## .NET 10 `Enumerable`

The documentation catalog's overload variants are grouped by name. `FirstOrDefault`, `SingleOrDefault`, and similar APIs explicitly distinguish overloads that take predicates, explicit defaults, or neither. .NET's static extension-method placement is represented as instance methods/factories where appropriate.

| .NET method family | Current equivalent | Disposition and gap |
|---|---|---|
| `Aggregate` | `aggregate`, `fold`, `reduce`, `scan` | Adapted; supports seed/no-seed and result-selector forms. |
| `AggregateBy` | `aggregate_by`, `aggregate_by_seed_selector` | Adapted; returns insertion-ordered `(key, accumulator)` pairs, accepts an equality comparer, and supports unhashable keys. |
| `All` | `all` | Present; predicate required. |
| `Any` | `any` | Present; supports predicate-free form. |
| `Append` | `append` | Present. |
| `AsEnumerable` | `Enumerable(iterable)` | Adapted; constructor wraps a one-shot iterator. |
| `Average` | `average` | Adapted; accepts a selector; Python numeric/empty/null semantics differ from overloaded .NET numeric variants. |
| `Cast` | `cast` | Adapted; typing-only and does not perform runtime validation/conversion. |
| `Chunk` | `chunk` | Present; returns lists, rather than arrays. |
| `Concat` | `concat` / `chain` | Present. |
| `Contains` | `contains` | Present; comparer callable replaces `IEqualityComparer`. |
| `Count` | `count` | Present; predicate overload included. |
| `CountBy` | `count_by` | Adapted; returns insertion-ordered `(key, count)` pairs and accepts an equality comparer. |
| `DefaultIfEmpty` | `default_if_empty` | Present; explicit `None` default is supported. |
| `Distinct` | `distinct` | Present; equality scan permits unhashable values, unlike set-backed implementations. |
| `DistinctBy` | `distinct_by` | Adapted; comparer callable replaces `IEqualityComparer`. |
| `ElementAt` | `element_at` | Adapted; zero-based integers, with negative integers indexing from the end. |
| `ElementAtOrDefault` | `element_at_or_default` | Adapted; omitted default is `None`, and negative integers index from the end. |
| `Empty` | `Enumerable.empty()` | Adapted; returns an empty single-pass enumerable. |
| `Except` | `except_` | Adapted; underscore avoids Python keyword conflict; equality scan preserves order and supports unhashable items. |
| `ExceptBy` | `except_by` | Adapted; equality scan supports unhashable keys. |
| `First` | `first` | Present; predicate overload. |
| `FirstOrDefault` | `first_or_default` | Adapted; defaults to `None`, supports explicit defaults and keyword-only predicate selection. |
| `FullJoin` | `full_join` | Adapted; unmatched rows use `rustshed.Null`, preserving actual `None` values. |
| `GroupBy` | `group_by` | Adapted; key/element/result selectors and equality comparer; supports unhashable keys. |
| `GroupJoin` | `group_join` | Adapted; buffers the inner iterable and produces a list of matches per outer item. |
| `Index` | `enumerate` | Adapted; lazily yields `(index, element)` pairs, matching .NET's tuple order. |
| `InfiniteSequence` | `Enumerable.infinite_sequence` | Adapted; returns a lazy arithmetic sequence. |
| `Intersect` | `intersect` | Adapted; equality scan preserves first-source order and supports unhashable items. |
| `IntersectBy` | `intersect_by` | Adapted; equality scan supports unhashable keys. |
| `Join` | `join_on` | Adapted; existing `join` remains the aggregate fold; inner join buffers the second iterable. |
| `Last` | `last` | Present; predicate overload. |
| `LastOrDefault` | `last_or_default` | Adapted; defaults to `None`, supports explicit defaults and keyword-only predicate selection. |
| `LeftJoin` | `left_join` | Adapted; unmatched rows use `rustshed.Null`, preserving actual `None` values. |
| `LongCount` | `long_count` | Adapted; Python integers do not have a separate fixed-width long-count type. |
| `Max` | `max` | Adapted; selector/comparer overloads and nullable numeric rules differ. |
| `MaxBy` | `max_by_key` | Adapted; returns `rustshed.Option`, matching Rust-style empty handling rather than LINQ's nullable default. |
| `Min` | `min` | Adapted; selector/comparer overloads and nullable numeric rules differ. |
| `MinBy` | `min_by_key` | Adapted; returns `rustshed.Option`, matching Rust-style empty handling rather than LINQ's nullable default. |
| `OfType` | `of_type` | Adapted; lazy Python runtime type filtering. |
| `Order` | `order_by()` | Adapted. |
| `OrderBy` | `order_by(key=...)` | Present for primary ascending key order. |
| `OrderByDescending` | `order_by(reverse=True)` | Adapted. |
| `OrderDescending` | `order_descending` | Adapted. |
| `Prepend` | `prepend` | Present. |
| `Range` | `Enumerable.range` | Adapted; takes start and count rather than start and exclusive end. |
| `Repeat` | `Enumerable.repeat` | Adapted; finite count required. |
| `Reverse` | `reverse` | Adapted; buffers instead of requiring a reverse-capable source. |
| `RightJoin` | `right_join` | Adapted; unmatched rows use `rustshed.Null`, preserving actual `None` values. |
| `Select` | `select` / `map` / `select_indexed` | Adapted; indexed selector is a separate method to keep callback arity explicit. |
| `SelectMany` | `flat_map` / `select_many` | Adapted; `select_many` includes the result-selector overload. |
| `Sequence` | `Enumerable.sequence` / `Enumerable.infinite_sequence` | Adapted; finite factory takes start/count/step; infinite factory is lazy. |
| `SequenceEqual` | `sequence_equal` | Present; comparer callable replaces `IEqualityComparer`. |
| `Shuffle` | `shuffle` | Adapted; deferred until iteration, then buffers before random permutation. |
| `Single` | `single` | Present; predicate overload. |
| `SingleOrDefault` | `single_or_default` | Adapted; defaults to `None`, supports explicit defaults and keyword-only predicate selection. |
| `Skip` | `skip` | Present; Python rejects negative indices rather than treating them as zero. |
| `SkipLast` | `skip_last` | Present; buffers due to implementation strategy. |
| `SkipWhile` | `skip_while` / `skip_while_indexed` | Adapted; indexed callback receives `(item, index)`. |
| `Sum` | `sum` | Adapted; accepts a selector, but has no .NET primitive overload/overflow/nullable behavior. |
| `Take` | `take` / `islice` | Adapted; use Python `islice` bounds for range-like slicing; negative bounds are rejected. |
| `TakeLast` | `take_last` | Present; buffers on iteration. |
| `TakeWhile` | `take_while` / `take_while_indexed` | Adapted; callback receives `(item, index)` for the indexed form; the failing item is consumed. |
| `ThenBy` | `then_by` | Adapted; stable multi-key sorting; raises `TypeError` unless called on an `order_by` result. |
| `ThenByDescending` | `then_by_descending` | Adapted; stable multi-key sorting; raises `TypeError` unless called on an `order_by` result. |
| `ToArray` | `to_array` | Adapted; Python lists are the collection result. |
| `ToDictionary` | `to_dictionary` | Adapted; keys must be hashable and duplicates raise `ValueError`; selector results are typed; custom equality comparers are not supported by Python dictionaries. |
| `ToHashSet` | `to_hashset` | Adapted; Python set/hashability semantics. |
| `ToList` | `to_list` | Present. |
| `ToLookup` | `to_lookup` | Adapted; dictionary of lists; keys must be hashable; custom equality comparers are not supported by Python dictionaries. |
| `TryGetNonEnumeratedCount` | `try_get_non_enumerated_count` | Limited; returns `Some(len(source_iterator))` only when the wrapped iterator is exactly `Sized`, otherwise `Null`. |
| `Union` | `union` | Adapted; stable equality scan; streams the first source before entering the second. |
| `UnionBy` | `union_by` | Adapted; stable equality scan; streams the first source before entering the second. |

### .NET catalog boundaries and notes

- Every overload in the reference page belongs to its method-family row above. Numeric families (especially `Average`, `Min`, `Max`, and `Sum`) include primitive, nullable, and selector overloads; Python numeric operators cannot reproduce CLR overflow and nullable rules exactly.
- `IQueryable`, provider translation, expression trees, parallel LINQ, and database behavior are out of scope.
- LINQ query values may be re-enumerated; this package intentionally keeps its source iterator one-shot.
- Join padding/results use explicit tagged values or an option wrapper, never `None` as an absence marker.

## Stable Rust `Iterator`

| Rust method | Current equivalent | Disposition and gap |
|---|---|---|
| `next` | `next` | Adapted; returns `rustshed.Some(item)` or `Null`, including `Some(None)`. |
| `next_chunk` | `next_chunk` | Adapted; returns a typed result with items and a completion flag rather than an array/`Result`. |
| `size_hint` | `operator.length_hint` | Limited; best-effort only, not a correctness guarantee. |
| `count` | `count` | Present. |
| `last` | `last` | Present; empty case raises instead of returning `Option`. |
| `advance_by` | `advance_by` | Adapted; returns completion and remaining count. |
| `nth` | `nth` | Present for non-negative indices; missing case raises unless default supplied. |
| `step_by` | `step_by` | Present; lazy adaptor, positive step required. |
| `chain` | `chain` | Present. |
| `zip` | `zip` | Present; Python's `strict` option is extra. |
| `intersperse` | `intersperse` | Present; lazy and preserves `None` separators/items. |
| `intersperse_with` | `intersperse_with` | Present; separator callback runs only between items. |
| `map` | `map` | Present. |
| `for_each` | `for_each` | Present; eager terminal. |
| `filter` | `filter` | Present. |
| `filter_map` | `filter_map` | Adapted; Python `DROP` replaces Rust `Option::None`, allowing `None` itself as output data. |
| `enumerate` | `enumerate` | Present. |
| `peekable` | `peek`, `try_peek`, `peek_n` | Adapted. |
| `skip_while` | `skip_while` | Present. |
| `take_while` | `take_while` | Present; Python wrapper is deferred and drops the failing item from its source. |
| `map_while` | `map_while` | Adapted; explicit `DROP` terminates the adaptor while `None` is ordinary output. |
| `skip` | `skip` | Present; Python rejects negative indices. |
| `take` | `take` | Present; Python rejects negative indices. |
| `scan` | `scan` | Adapted; current seeded scan emits initial state. |
| `flat_map` | `flat_map` | Present. |
| `flatten` | `flatten` | Present. |
| `map_windows` | `map_windows` | Adapted; lazy callback receives an immutable tuple view of a dynamically sized window. |
| `fuse` | `fuse` | Adapted; generator wrapper stops permanently after the first exhaustion. |
| `inspect` | `inspect` / `tee` | Adapted; callback receives value instead of a Rust reference. |
| `by_ref` | `by_ref` | Adapted; returns the same one-shot enumerable so adapters advance its shared position; Python cannot enforce Rust's borrow lifetime. `shallow_copy` remains a separate tee-based operation. |
| `collect` | `to_list` | Adapted; caller chooses Python collection via normal constructors. |
| `try_collect` | — | Not portable as a generic `Try`/`Residual` operation; explicit result-specific helpers could be added separately. |
| `collect_into` | `collect_into` | Adapted; extends a mutable collection using its `extend` method. |
| `partition` | `partition` | Adapted; eagerly returns two lists. |
| `partition_in_place` | — | Not portable; requires mutable references and double-ended iterator guarantees. |
| `is_partitioned` | `is_partitioned` | Present; eager and short-circuits on a violation. |
| `try_fold` | `fold` | Not portable as `Try`-generic; Python exceptions already short-circuit. |
| `try_for_each` | `for_each` | Not portable as a `Try`-generic; exceptions already short-circuit. |
| `fold` | `fold` | Adapted; seed is optional and an omitted seed uses the first item. |
| `reduce` | `reduce` | Adapted; empty case raises instead of returning `Option`. |
| `try_reduce` | — | Not portable as a generic `Try` residual operation. |
| `all` | `all` | Present. |
| `any` | `any` | Present; predicate-free extension. |
| `find` | `find` | Present; empty case raises instead of returning `Option`. |
| `find_map` | `find_map` | Adapted; returns `Some(None)` for a found `None` output and uses `DROP` to continue. |
| `try_find` | — | Not portable as a generic `Try` residual operation. |
| `position` | `position` | Adapted; returns `Option[int]`. |
| `rposition` | `rposition` | Limited; buffers because arbitrary Python iterators are not double-ended. |
| `max` | `max` | Adapted; empty case raises, and Python comparison semantics apply. |
| `min` | `min` | Adapted; empty case raises, and Python comparison semantics apply. |
| `max_by_key` | `max_by_key` | Adapted; returns `Option[T]` and uses Python's key ordering. |
| `max_by` | `max_by` | Adapted; comparator returns a negative/zero/positive integer. |
| `min_by_key` | `min_by_key` | Adapted; returns `Option[T]` and uses Python's key ordering. |
| `min_by` | `min_by` | Adapted; comparator returns a negative/zero/positive integer. |
| `rev` | `reverse` | Adapted; buffers rather than requiring `DoubleEndedIterator`. |
| `unzip` | `unzip` | Adapted; eagerly returns two lists. |
| `copied` | — | Not portable as a `Copy` trait bound; Python references are already yielded directly. |
| `cloned` | — | Not portable as a `Clone` trait bound; explicit `copy.copy`/`deepcopy` can be used by callers. |
| `cycle` | `cycle` | Limited; caches the first pass; an infinite source continues yielding but the cache grows without bound. |
| `array_chunks` | `array_chunks` | Adapted; yields full lists and drops a final incomplete chunk, as Rust does. |
| `sum` | `sum` | Adapted; Python arithmetic and empty result semantics. |
| `product` | `product` | Present; empty input returns multiplicative identity `1`. |
| `cmp` | `cmp` | Adapted; returns exported `Ordering`. |
| `cmp_by` | `cmp_by` | Adapted; comparator returns a negative/zero/positive integer. |
| `partial_cmp` | `partial_cmp` | Adapted; returns `Null` when Python comparison raises `TypeError`. |
| `partial_cmp_by` | `partial_cmp_by` | Adapted; comparator returns `None` for incomparable pairs. |
| `eq` | `eq` | Present. |
| `eq_by` | `eq(comparer=...)` | Adapted. |
| `ne` | `neq` | Present. |
| `lt` | `lt` | Adapted; lexicographic comparison. |
| `le` | `le` | Adapted; lexicographic comparison. |
| `gt` | `gt` | Adapted; lexicographic comparison. |
| `ge` | `ge` | Adapted; lexicographic comparison. |
| `is_sorted` | `is_sorted` | Present; Python comparison semantics apply. |
| `is_sorted_by` | `is_sorted_by` | Adapted; comparator can return `None` to mark unordered. |
| `is_sorted_by_key` | `is_sorted_by_key` | Present; Python key comparison semantics apply. |

### Rust trait constraints and non-parity

Rust's `DoubleEndedIterator`, `ExactSizeIterator`, `FusedIterator`, `Copy`, `Clone`, `Try`, `Residual`, and mutable-reference bounds are compile-time contracts. Python can provide buffered or explicit protocol-based operations, but cannot promise those contracts for arbitrary `Iterable`s. `size_hint` is never used for correctness. Const-generic arrays map to Python lists/tuples without a compile-time length guarantee.

## Feasibility summary

- The portable method families in the matrix are implemented with explicitly adapted names or result types where Python differs.
- Exact parity is intentionally unavailable for replayable LINQ queries, C# provider/expression APIs and CLR numeric overload rules, Rust trait bounds/borrowing/ownership/const generics, and generic `Try`/`Residual` propagation.
- Some adaptations necessarily buffer (`order_by`/`then_by`, grouping, joins, `rposition`, `reverse`, `unzip`, and `cycle` caching). Other pipelines remain deferred and short-circuit as consumed.
- The package uses one-shot sources; callers should construct a fresh `Enumerable` when they need a new traversal.
4. Run all runtime, Pyright, mypy, formatting, build, and CI checks.
