from python_linq import ControlFlow, Enumerable
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
