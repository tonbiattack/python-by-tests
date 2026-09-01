from python_by_tests.closures import late_bound_callbacks
from python_by_tests.copies import deep, shallow
from python_by_tests.defaults import append_item
from python_by_tests.generators import doubled
from python_by_tests.identity import same_identity, same_value
from python_by_tests.resources import TrackedResource


def test_is_and_equals_have_different_contracts() -> None:
    left, right = ["python"], ["python"]
    assert not same_identity(left, right)
    assert same_value(left, right)


def test_mutable_default_argument_is_shared_between_calls() -> None:
    append_item.__defaults__[0].clear()  # type: ignore[index]
    assert append_item("first") == ["first"]
    assert append_item("second") == ["first", "second"]


def test_shallow_copy_shares_nested_objects_but_deep_copy_does_not() -> None:
    original = [["before"]]
    shallow_copy, deep_copy = shallow(original), deep(original)
    original[0][0] = "after"
    assert shallow_copy == [["after"]]
    assert deep_copy == [["before"]]


def test_closure_late_binding_reads_the_final_loop_value() -> None:
    assert [callback() for callback in late_bound_callbacks()] == [2, 2, 2]


def test_generator_is_lazy_and_is_consumed_once() -> None:
    calls: list[int] = []
    values = doubled([1, 2], calls)
    assert calls == []
    assert list(values) == [2, 4]
    assert calls == [1, 2]
    assert list(values) == []


def test_context_manager_calls_exit_after_the_with_block() -> None:
    events: list[str] = []
    with TrackedResource(events):
        events.append("use")
    assert events == ["enter", "use", "exit"]
