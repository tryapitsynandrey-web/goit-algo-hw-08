import pytest

from src.cable_heap import (
    minimum_cable_connection_cost,
    minimum_cable_connection_cost_sorted_simulation,
    minimum_cable_connection_plan,
)


def test_basic_example():
    cables = [4, 3, 2, 6]
    assert minimum_cable_connection_cost(cables) == 29
    assert minimum_cable_connection_cost_sorted_simulation(cables) == 29


def test_empty_list():
    assert minimum_cable_connection_cost([]) == 0
    assert minimum_cable_connection_cost_sorted_simulation([]) == 0


def test_single_cable():
    assert minimum_cable_connection_cost([5]) == 0
    assert minimum_cable_connection_cost_sorted_simulation([5]) == 0


def test_two_cables():
    assert minimum_cable_connection_cost([5, 10]) == 15
    assert minimum_cable_connection_cost_sorted_simulation([5, 10]) == 15


def test_already_sorted():
    cables = [1, 2, 3, 4, 5]
    # Connect 1, 2 = 3
    # Heap: 3, 3, 4, 5. Connect 3, 3 = 6
    # Heap: 4, 5, 6. Connect 4, 5 = 9
    # Heap: 6, 9. Connect 6, 9 = 15
    # Total cost = 3 + 6 + 9 + 15 = 33
    assert minimum_cable_connection_cost(cables) == 33
    assert minimum_cable_connection_cost_sorted_simulation(cables) == 33


def test_reverse_sorted():
    cables = [5, 4, 3, 2, 1]
    assert minimum_cable_connection_cost(cables) == 33
    assert minimum_cable_connection_cost_sorted_simulation(cables) == 33


def test_duplicate_lengths():
    cables = [2, 2, 2, 2]
    # Connect 2, 2 = 4
    # Heap: 2, 2, 4. Connect 2, 2 = 4
    # Heap: 4, 4. Connect 4, 4 = 8
    # Total cost = 4 + 4 + 8 = 16
    assert minimum_cable_connection_cost(cables) == 16
    assert minimum_cable_connection_cost_sorted_simulation(cables) == 16


def test_zero_length_cables():
    cables = [0, 0, 0]
    assert minimum_cable_connection_cost(cables) == 0
    assert minimum_cable_connection_cost_sorted_simulation(cables) == 0


def test_negative_length():
    with pytest.raises(ValueError, match="Cable lengths cannot be negative."):
        minimum_cable_connection_cost([4, 3, -2, 6])


def test_non_integer_cable():
    with pytest.raises(TypeError, match="All cable lengths must be integers."):
        minimum_cable_connection_cost([4, 3.5, 2, 6])  # type: ignore

    with pytest.raises(TypeError, match="All cable lengths must be integers."):
        minimum_cable_connection_cost([4, "3", 2])  # type: ignore

    with pytest.raises(TypeError, match="All cable lengths must be integers."):
        minimum_cable_connection_cost([4, True, 2])  # type: ignore


def test_non_list_input():
    with pytest.raises(TypeError, match="Input must be a list."):
        minimum_cable_connection_cost((4, 3, 2, 6))  # type: ignore


def test_does_not_mutate_input():
    cables = [4, 3, 2, 6]
    cables_copy = cables.copy()
    minimum_cable_connection_cost(cables)
    assert cables == cables_copy


def test_minimum_cable_connection_plan():
    cables = [4, 3, 2, 6]
    cost, plan = minimum_cable_connection_plan(cables)
    assert cost == 29
    assert plan == [
        (2, 3, 5),
        (4, 5, 9),
        (6, 9, 15)
    ]
