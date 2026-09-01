from datetime import UTC, datetime

import pytest

from python_by_tests.attributes import Label
from python_by_tests.closures import late_bound_callbacks
from python_by_tests.copies import deep, shallow
from python_by_tests.dataclasses_example import Ticket
from python_by_tests.datetimes import naive_at, utc_at
from python_by_tests.defaults import append_item
from python_by_tests.equality import ProductCode
from python_by_tests.exception_chaining import required_setting
from python_by_tests.generators import doubled
from python_by_tests.identity import same_identity, same_value
from python_by_tests.iterators import numbers
from python_by_tests.none_values import is_missing
from python_by_tests.protocols import Printer, Renderable
from python_by_tests.references import independent_rows, shared_rows
from python_by_tests.resources import TrackedResource
from python_by_tests.runtime_typing import repeat


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


def test_list_multiplication_shares_nested_list_references() -> None:
    shared = shared_rows()
    shared[0].append("x")
    assert shared == [["x"], ["x"], ["x"]]

    independent = independent_rows()
    independent[0].append("x")
    assert independent == [["x"], [], []]


def test_none_is_checked_by_identity() -> None:
    assert is_missing(None)
    assert not is_missing("")


def test_iterator_advances_and_raises_after_consumption() -> None:
    iterator = numbers()
    assert next(iterator) == 1
    assert list(iterator) == [2, 3]
    with pytest.raises(StopIteration):
        next(iterator)


def test_exception_chaining_preserves_the_original_cause() -> None:
    with pytest.raises(ValueError) as caught:
        required_setting({})
    assert str(caught.value) == "region must be configured"
    assert isinstance(caught.value.__cause__, KeyError)


def test_instance_assignment_shadows_but_does_not_change_class_attribute() -> None:
    left, right = Label(), Label()
    left.value = "local"
    assert left.value == "local"
    assert right.value == "shared"
    assert Label.value == "shared"


def test_custom_equality_without_hash_is_not_hashable() -> None:
    assert ProductCode("A-1") == ProductCode("A-1")
    with pytest.raises(TypeError):
        {ProductCode("A-1")}


def test_dataclass_generates_value_equality_and_readable_repr() -> None:
    assert Ticket(1, "fix") == Ticket(1, "fix")
    assert repr(Ticket(1, "fix")) == "Ticket(id=1, title='fix')"


def test_type_hints_are_not_runtime_argument_validation() -> None:
    assert repeat(3) == 6  # type: ignore[arg-type, return-value]


def test_protocol_accepts_structure_without_explicit_inheritance() -> None:
    printer = Printer()
    assert isinstance(printer, Renderable)
    assert printer.render() == "printed"


def test_timezone_aware_datetimes_compare_but_naive_and_aware_do_not() -> None:
    assert utc_at(9) < datetime(2026, 1, 1, 10, tzinfo=UTC)
    with pytest.raises(TypeError):
        _ = utc_at(9) < naive_at(10)
