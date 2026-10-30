# Design proposal: capability-aware replayable views

## Summary

Keep the existing `Enumerable[T]` contract unchanged: it wraps one iterator,
and iterating it resumes that cursor. Add an explicit `ReplayableEnumerableView`
for callers that want independent traversals and logical indexing. Back it with
a lazy, memoizing source abstraction that assigns stable logical addresses to
items as they are discovered.

An adaptor such as `where` can preserve replayability and indexed access by
building a new logical address space over its parent. It cannot generally
preserve the parent's exact length or map a filtered index directly to a source
index. Instead it discovers accepted values on demand and records their
addresses. Exact length is available only after exhaustion (or after an
operation deliberately exhausts the view).

This is an opt-in stronger contract, not an optimization silently applied to
existing `Enumerable` instances. Capabilities are properties of a view's source
and pipeline, not guarantees inferred from an arbitrary Python `Iterable`.

## Observed implementation constraints

- `BaseEnumerable.__init__` calls `iter(source)` once, stores that iterator as
  `.value`, and `__iter__` returns that same iterator.
- `FilterEnumerable.where` currently constructs `Enumerable(filter(...))`;
  like many operators, this produces another one-shot iterator-backed result.
- `element_at` uses sequential traversal for nonnegative indices and materializes
  for negative indices. `try_get_non_enumerated_count` only succeeds when the
  stored iterator is `Sized`.
- Some mixins access `.value` directly. Merely subclassing `Enumerable` and
  overriding `__iter__` would not make inherited methods consistently preserve
  view behavior.
- `docs/API.md` documents one-shot semantics, so the existing contract and
  examples must remain valid.

## Goals

1. Retain all current behavior for ordinary `Enumerable` and existing
   constructors/operators.
2. Provide an explicit view whose repeated traversals return the same logical
   sequence without rerunning already-evaluated pipeline callbacks.
3. Give replayable views lazy indexing and a way to ask for exact length, while
   making potentially linear work and memory costs explicit.
4. Preserve replayability through supported lazy adaptors, including filtering.
5. Keep `None` a normal element and represent “not found/not known” distinctly.
6. Keep static typing strict and public APIs understandable without requiring
   callers to inspect private source implementations.

## Non-goals

- Do not make every `Enumerable` implicitly replayable.
- Do not promise constant-time indexing or length for arbitrary pipelines.
- Do not promise that filtering retains the input's exact length or direct index
  mapping.
- Do not deep-copy cached objects, freeze mutable inputs, or make callback
  side-effects reversible.
- Do not add concurrent iteration guarantees in the first version.
- Do not change the semantics of existing operators to favor optimization over
  their current laziness, ordering, exceptions, or one-shot behavior.

## Proposed model

### 1. Keep the existing enumerable as the one-shot adapter

`Enumerable[T]` remains the compatibility type. Its public constructor continues
to capture one iterator. Existing methods continue to consume that iterator
exactly as documented.

Refactor implementation internals so operators request iteration through a
small source/access abstraction rather than reaching into `.value`. This is
necessary for correctness when an operation is invoked on a view, but it must
not alter the behavior of ordinary instances. Keep `.value` compatibility
where required by existing code/tests during migration; remove internal direct
access incrementally and only consider deprecating the attribute separately.

### 2. Add an explicit replayable view

Expose a constructor/factory such as:

```python
view = Enumerable(source).replay()
```

The precise public spelling should be finalized against the package's naming
conventions. The returned object is a `ReplayableEnumerableView[T]` (or
equivalent explicit replayable type), with:

- `iter(view)` creating an independent logical traversal from index zero;
- `view[index]`/`element_at(index)` resolving a logical index lazily;
- a replay-specific exact-length operation that may consume the rest of the
  upstream source to establish the result;
- a known-length query that reports unknown until exact length is established.

The view may be implemented as an `Enumerable` subtype so the existing
operator API remains available, but subclassing alone is not the design: the
source/access layer and operator construction hooks are what preserve
capabilities. Every inherited operation that consumes the source must use
those hooks rather than `.value` directly.

Calling `replay()` on a one-shot source creates a memoizing view over that
source. It does not restart the source. It can replay only values observed
since the view was created; a source cursor already advanced before wrapping
cannot be rewound.

### 3. Use logical addresses backed by a lazy memoizing source

The replay source owns:

- one upstream iterator;
- a cache of values discovered so far;
- an exhausted flag;
- a way to resolve a nonnegative logical address, extending the cache only as
  far as required.

Conceptually, `get(i)` returns the cached item at logical address `i`, or pulls
and caches upstream values until `i` exists or the upstream is exhausted.
Each new address is assigned once and remains stable for the lifetime of the
view. Iterators maintain their own logical address, so consumers may advance
independently while sharing the cache and upstream pulls.

The internal lookup result must distinguish absence from a present `None`.
Use an existing tagged option type if its static typing cleanly supports
`Some(None)`; otherwise introduce a small private result type or `(found, value)`
representation. Never use `None` alone to indicate end-of-view.

### 4. Adaptors create new logical address spaces

Each supported adaptor builds a view over its parent, with its own logical
addresses and memoized outputs. It requests parent items by address and caches
its own results. This gives a compositional model:

```text
one-shot source -> replay cache -> where view -> select view
```

Important cases:

- **One-to-one `select`/`map`:** output address `i` is derived from parent
  address `i`. Cache the projected value so the callback runs once per logical
  item, even if traversals overlap or repeat.
- **`where`/`filter`:** output address `j` is the `j`-th accepted parent item.
  Keep a scan cursor into the parent and a cache of accepted outputs. To satisfy
  `get(j)`, scan only until the `j`-th match is found or the parent ends.
  Evaluate the predicate once per scanned parent item and cache accepted values.
- **`take(n)`:** has a known upper bound `n`; its exact length is `min(n,
  parent_length)` when parent length is known, otherwise exact only after the
  relevant prefix/exhaustion is observed.
- **`skip(n)`:** logical address `i` maps to parent address `i+n`, subject to
  bounds.
- **`concat`/`chain`:** may resolve the first source directly; the second is
  entered only after the first is known exhausted. Exact length is known only
  when both source lengths are known.
- **`flat_map`, `distinct`, joins, and global ordering/grouping:** require
  operation-specific caches/state and may buffer substantially. Preserve
  replayability only when a correct memoized adaptor is implemented; otherwise
  explicitly materialize or return the existing one-shot result. Do not claim a
  capability that the implementation cannot uphold.

This design supports per-operation specialization (for example, indexed
`element_at` on a replayable view) while keeping generic fallbacks. Special
behavior belongs behind shared operator/access hooks, not duplicated ad hoc
subclass overrides.

## Capability and cost semantics

Replayability, indexability, and known exact length are distinct properties:

| Property | Replayable view guarantee | Typical cost |
|---|---|---|
| Replayability | Every traversal sees the same logical values in the same order. Cached callbacks are not repeated. | Retains discovered output values. |
| Nonnegative indexing | `get(i)` resolves the logical item or reports out-of-range. | O(1) for cached addresses; may pull/scan O(n) new input. |
| Exact length | Returns the exact number of logical outputs. | O(remaining input); may evaluate the full pipeline and retain all outputs. |
| Negative indexing | Can be resolved after exact length is known. | Usually forces exhaustion, then O(1) cache lookup. |
| Reverse traversal | Can traverse cached logical outputs backwards after length is known. | Usually forces exhaustion and retains outputs. |

Do not overload one “capability” bit to imply all of these. Internally, represent
known length as unknown-or-exact and make address resolution a separate
operation. The public API should avoid exposing a misleading `Sized` behavior
when obtaining length could be unexpectedly expensive; use explicit methods
such as `try_get_non_enumerated_count()` for non-forcing knowledge and
`length()`/`count()` for an operation that is allowed to force traversal.

The policy for standard `len(view)` remains open pending API review: Python's
`len` convention suggests a cheap, already-known length, but an opt-in view
could also choose to exhaust. Prefer not to make `len()` unexpectedly execute
user callbacks. If exact length is unknown, `len()` should either raise
`TypeError` or be unavailable until known; a named forcing operation is clearer.

## Callback, mutation, and exception behavior

- A replayable view memoizes the *outputs* of each adaptor. For `where`, this
  means each scanned parent's predicate is called once, and accepted values are
  cached. Repeated traversals do not repeat those predicate calls.
- Stateful callbacks therefore have “evaluate once on first demand” semantics
  in this view. This is intentionally different from a recomputing factory
  view, and must be documented as part of the opt-in API.
- Cache object references, not deep copies. Mutating a cached mutable object is
  visible through later traversals, as it is when the same object is yielded
  repeatedly from a source.
- If upstream iteration or a callback raises, do not report exhaustion or
  silently substitute a successful result. Specify whether the failure is
  sticky and replayed at the same logical position or whether subsequent access
  retries. Recommended first version: cache a terminal failure at the point of
  failure and re-raise it consistently, avoiding repeated side effects and
  undefined cursor recovery.
- A predicate may reject many values before the next logical output is found;
  requesting an index can therefore perform arbitrary work or not terminate
  for an infinite source with no further match. This follows ordinary lazy
  filtering and should be documented.

## API compatibility and subclass strategy

Use the replayable view as a public, explicit type, but do not rely on concrete
type checks in downstream callers. A private typed source protocol should
provide iteration/address operations and known-length information. Operator
factories should inspect or preserve those capabilities internally.

Subclassing is reasonable for public method reuse and per-view method behavior,
but current mixins access `.value` and eagerly construct plain `Enumerable`
instances. Before a subtype is safe:

1. Centralize source iteration and result construction.
2. Replace internal direct cursor access where necessary.
3. Audit each operator for whether it preserves replayability, preserves
   indexing, preserves a known length, or deliberately drops capabilities.
4. Add tests proving behavior through inherited methods, not just overridden
   `__iter__`.

Do not silently make `Enumerable(list)` replayable. Users opt into this
stronger, caching behavior explicitly. A later factory-backed view may be added
for repeatable sources that should recompute callbacks, but it must be a
separate contract because callback side effects and changing sources differ.

## `None` safety and static typing

- `None` is always a valid `T`, including at index zero and as a filtered or
  projected result.
- End-of-view, unknown-length, and failed lookup states use tagged values, not
  `None`.
- Add typing tests for `ReplayableEnumerableView[int | None]`,
  `Some(None)`, callbacks producing optional values, and overloads for indexing
  and length methods.
- Preserve strict Pyright and mypy gates. Add new public modules to the existing
  type-check configuration and ensure the package's runtime test suite,
  doctests, formatting, and build remain green.

## Rollout plan

1. **Inventory and contract tests**
   - Enumerate direct `.value` usages and operations that construct plain
     `Enumerable` results.
   - Add regression tests locking current one-shot behavior, including
     partially consumed sources, `None`, callback invocation counts, and
     exceptions.
2. **Internal source abstraction**
   - Introduce typed source/address and lookup-result primitives.
   - Route `BaseEnumerable` iteration and relevant operators through the
     abstraction without changing ordinary `Enumerable`.
   - Run all tests, Pyright, and mypy before adding the new public API.
3. **Replayable indexed cache**
   - Implement explicit `.replay()` (or selected equivalent) and independent
     logical iterators backed by one cache/upstream cursor.
   - Implement positive indexing and exact-length discovery; negative indexing
     and reverse use the discovered cache.
   - Define and test sticky failure behavior.
4. **Capability-preserving adaptors**
   - Start with `where`, `select`, `take`, `skip`, and `concat`, each with
     accurate known-length behavior and memoization.
   - Audit remaining operators; preserve the view only where semantics and
     costs are explicit, otherwise retain the current `Enumerable` fallback.
5. **Public docs and typing**
   - Extend `docs/API.md` with view creation, replay/index/length semantics,
     callback timing, mutation, cache growth, and `None`-safe examples.
   - Update `docs/API_PARITY.md` only where this changes parity claims.
   - Add type-check examples and keep strict mypy/Pyright in the validation
     gate.
6. **Validation**
   - Run focused replay/view tests, the complete pytest/doctest suite, strict
     type checks, formatting, `git diff --check`, and package build.
   - Add instrumentation tests proving laziness (only the needed prefix is
     consumed), memoization (callbacks run once), replay consistency, and
     equivalent values/order/errors against the existing generic path.

## Acceptance criteria

- Existing `Enumerable` construction, consumption, and one-shot pipeline
  behavior remain unchanged.
- Explicit replay views create independent traversals and return stable values
  for already-discovered logical addresses.
- Filtering preserves replayability and indexing via a cached logical-to-source
  address map, without claiming the source's exact length or O(1) access.
- Requesting exact length has explicit, tested exhaustion behavior; a
  non-forcing count query distinguishes unknown from known zero.
- `None` is never mistaken for end-of-view, unknown length, or missing index.
- Repeated traversal does not repeat completed callbacks or upstream pulls.
- Capability-preserving adaptors are documented and tested; unsupported
  adaptors do not falsely advertise stronger guarantees.
- Strict Pyright and mypy, runtime tests/doctests, formatting, and package build
  pass.
