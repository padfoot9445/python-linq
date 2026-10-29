import pytest

from python_linq import (
    DROP,
    ControlFlow,
    ControlFlowNestedState,
    Enumerable,
    identity,
)
from rustshed import Some


def test_none_is_a_valid_item_for_terminal_operations():
    assert Enumerable([None]).first() is None
    assert Enumerable([None]).last() is None
    assert Enumerable([None]).single() is None
    assert not Enumerable([None]).is_empty()


def test_none_can_be_an_explicit_default():
    assert Enumerable[int]([]).first(default=None) is None
    assert Enumerable[int]([]).last(default=None) is None
    assert Enumerable[int]([]).single(default=None) is None
    assert Enumerable([1]).exact(2, default=None).to_list() == [1, None]


def test_none_is_not_used_as_sequence_equality_padding():
    assert Enumerable([None]).eq([None])
    assert not Enumerable([None]).eq([])
    assert not Enumerable([]).eq([None])


def test_none_survives_projection_zip_and_peek():
    assert Enumerable([None]).map(lambda value: value).to_list() == [None]
    assert Enumerable([None]).zip([None]).to_list() == [(None, None)]
    values = Enumerable([None])
    assert values.try_peek() == Some(None)
    assert values.to_list() == [None]


def test_filter_map_can_emit_none_and_uses_drop_sentinel():
    assert Enumerable([0, 1, 2]).filter_map(
        lambda value: None if value == 0 else value if value == 1 else DROP
    ).to_list() == [None, 1]


def test_none_survives_sequence_operators_and_group_keys():
    values = Enumerable([None, 1, None])

    assert values.where(lambda item: item is None).to_list() == [None, None]
    assert Enumerable([None, 1]).flat_map(lambda item: [item]).to_list() == [None, 1]
    assert Enumerable([None, 1]).append(None).prepend(None).to_list() == [
        None,
        None,
        1,
        None,
    ]
    assert Enumerable([None, 1]).enumerate().to_list() == [(0, None), (1, 1)]
    assert Enumerable([None, 1]).chunk(1).to_list() == [[None], [1]]
    assert Enumerable([None, 1]).reverse().to_list() == [1, None]
    assert Enumerable([None, 1]).group_by(lambda _: None).to_list() == [
        (None, [None, 1])
    ]
    assert Enumerable([None, 1]).order_by(
        key=lambda item: 0 if item is None else 1
    ).to_list() == [None, 1]


def test_none_survives_iterator_adaptors_and_copying():
    assert Enumerable([None, 1]).select(lambda item: item).to_list() == [None, 1]
    assert Enumerable([[None], [1]]).flatten().to_list() == [None, 1]
    assert Enumerable([None]).concat([None]).chain([1]).to_list() == [None, None, 1]
    assert Enumerable([None, 1]).take(1).to_list() == [None]
    assert Enumerable([None, 1]).skip(1).to_list() == [1]
    assert Enumerable([None, 1]).islice(0, 1).to_list() == [None]
    assert Enumerable([None, 1]).take_last(1).to_list() == [1]
    assert Enumerable([None, 1]).skip_last(1).to_list() == [None]

    seen = []
    assert Enumerable([None, 1]).tee(seen.append).to_list() == [None, 1]
    assert seen == [None, 1]
    values = Enumerable([None, 1])
    copy = values.shallow_copy()
    assert next(iter(copy)) is None
    assert next(iter(values)) is None
    assert values.to_list() == [1]
    assert Enumerable([None]).cast().to_list() == [None]


def test_none_is_supported_by_predicates_and_terminals():
    assert Enumerable([None, 1, None]).filter(lambda item: item is None).count() == 2
    assert Enumerable([None, 1, None]).any(lambda item: item is None)
    assert Enumerable([None, 1, None]).all(lambda item: item is None or item == 1)
    assert Enumerable([None, 1, None]).neq([None, 1])
    assert Enumerable([None, 1, None]).sequence_equal([None, 1, None])
    assert Enumerable([None, 1, None]).first(lambda item: item is None) is None
    assert Enumerable([None, 1, None]).single(lambda item: item == 1) == 1
    assert Enumerable([None, 1, None]).last(lambda item: item is None) is None
    assert Enumerable([None, 1, None]).nth(0) is None
    assert Enumerable([None, 1, None]).find(lambda item: item is None) is None
    assert Enumerable([None, 1, None]).default_if_empty(None).to_list() == [
        None,
        1,
        None,
    ]
    assert Enumerable[object]([]).default_if_empty(None).to_list() == [None]


def test_none_is_preserved_by_while_peek_and_identity_operations():
    assert Enumerable([None, None, 1]).skip_while(
        lambda item: item is None
    ).to_list() == [1]
    assert Enumerable([None, 1]).take_while(lambda item: item is None).to_list() == [
        None
    ]
    assert Enumerable([None, 1]).take_while_inclusive(
        lambda item: item is None
    ).to_list() == [None, 1]

    values = Enumerable([None, 1])
    assert values.take_while_lossless(lambda item: item is None).to_list() == [None]
    assert values.to_list() == [1]
    assert Enumerable([None, 1]).peek_n(2).to_list() == [None, 1]
    assert Enumerable([None, 1]).peek_while(lambda item: item is None).to_list() == [
        None
    ]
    assert Enumerable([None]).peek() is None
    assert Enumerable([None]).is_empty() is False
    assert Enumerable([None]).min(key=lambda _: 0) is None
    assert Enumerable([None]).max(key=lambda _: 0) is None


def test_none_is_supported_by_split_and_aggregate_seed_paths():
    assert Enumerable([None, 1, None]).split(None).map(
        lambda segment: segment.to_list()
    ).to_list() == [[], [1], []]
    assert Enumerable([None, 1, None]).split_multiple([None]).map(
        lambda segment: segment.to_list()
    ).to_list() == [[], [1], []]

    assert Enumerable([None, 1]).fold(lambda _acc, item: item, seed=None) == 1
    assert Enumerable([None, 1]).scan(lambda _acc, item: item, seed=None).to_list() == [
        None,
        None,
        1,
    ]
    assert Enumerable([None, 1]).reduce(lambda _acc, item: item) == 1
    assert Enumerable([None, 1]).join(None, aggregator=lambda _left, right: right) == 1


def test_numeric_operations_reject_none_when_python_operation_requires_numbers():
    with pytest.raises(TypeError):
        Enumerable([None]).sum()
    with pytest.raises(TypeError):
        Enumerable([None]).average()
    with pytest.raises(TypeError):
        Enumerable([None, 1]).min()
    with pytest.raises(TypeError):
        Enumerable([None, 1]).max()
    with pytest.raises(TypeError):
        Enumerable([None, 1]).order_by().to_list()


def test_none_is_rejected_only_where_the_operator_requires_another_capability():
    with pytest.raises(TypeError):
        Enumerable([None]).flat_map(lambda _: None).to_list()
    with pytest.raises(TypeError):
        Enumerable([None]).flatten().to_list()
    assert Enumerable([None]).group_by(lambda _: []).to_list() == [([], [None])]
    with pytest.raises(TypeError):
        Enumerable([None]).to_dictionary(lambda _: [])


def test_none_items_work_with_distinct_and_contains():
    values = Enumerable([None, 1, None])

    assert values.distinct().to_list() == [None, 1]
    assert Enumerable([None]).contains(None)


def test_control_flow_can_yield_none():
    values = Enumerable([None, 1]).control_flow(
        lambda value: ControlFlow[object].ok(value)
    )

    assert values.to_list() == [None, 1]

    stopped = Enumerable([None, 1]).control_flow(
        lambda value: (
            ControlFlow[object].stop_ok(None)
            if value is None
            else ControlFlow[object].ok(value)
        )
    )
    assert stopped.to_list() == [None]


def test_control_flow_skip_has_no_none_payload():
    skipped = ControlFlow.skip()

    assert skipped.val is not None
    assert Enumerable([None, 1]).control_flow(
        lambda value: ControlFlow.skip() if value is None else ControlFlow.ok(value)
    ).to_list() == [1]


def test_control_flow_flags_do_not_use_none_as_a_missing_payload():
    assert ControlFlow.ok(None).val is None
    assert ControlFlow.stop_ok(None).val is None
    assert ControlFlow.yield_control_ok(None).val is None
    assert ControlFlow.ok(None).nested_state is ControlFlowNestedState.NoNestedState
    assert ControlFlow.yield_control_skip(None).val is not None
    assert Enumerable([None, 1]).control_flow(
        lambda value: (
            ControlFlow[object].yield_control_ok(value)
            if value is None
            else ControlFlow[object].ok(value)
        )
    ).to_list() == [None, 1]
    assert (
        Enumerable([None, 1])
        .control_flow(
            lambda value: (
                ControlFlow.stop() if value is None else ControlFlow[object].ok(value)
            )
        )
        .to_list()
        == []
    )
    assert (
        Enumerable([None, 1])
        .control_flow(
            lambda value: (
                ControlFlow.yield_control_skip(value)
                if value is None
                else ControlFlow.ok(value)
            )
        )
        .to_list()
        == []
    )
    assert identity(None) is None
