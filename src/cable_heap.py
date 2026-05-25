"""Algorithm for the minimum cable connection cost using a min-heap."""

import heapq


def validate_cables(cables: list[int]) -> None:
    """Validate the input cables list.
    
    Args:
        cables: A list of cable lengths.
        
    Raises:
        TypeError: If the input is not a list, or if any element is not an int.
        ValueError: If any cable length is negative.
    """
    if not isinstance(cables, list):
        raise TypeError("Input must be a list.")
        
    for cable in cables:
        if not isinstance(cable, int) or isinstance(cable, bool):
            raise TypeError("All cable lengths must be integers.")
        if cable < 0:
            raise ValueError("Cable lengths cannot be negative.")


def minimum_cable_connection_cost(cables: list[int]) -> int:
    """Calculate the minimum total cost to connect all cables using a heap.
    
    Args:
        cables: A list of cable lengths.
        
    Returns:
        The minimum total cost of connecting all cables.
        Returns 0 if the list is empty or has only one cable.
    """
    validate_cables(cables)
    
    if len(cables) <= 1:
        return 0
        
    heap = list(cables)
    heapq.heapify(heap)
    
    total_cost = 0
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        merged = first + second
        total_cost += merged
        
        heapq.heappush(heap, merged)
        
    return total_cost


def minimum_cable_connection_plan(cables: list[int]) -> tuple[int, list[tuple[int, int, int]]]:
    """Calculate the minimum total cost and provide the merge plan.
    
    Args:
        cables: A list of cable lengths.
        
    Returns:
        A tuple containing the total cost and a list of merge operations.
        Each operation is represented as (cable1, cable2, merged_length).
    """
    validate_cables(cables)
    
    if len(cables) <= 1:
        return 0, []
        
    heap = list(cables)
    heapq.heapify(heap)
    
    total_cost = 0
    plan = []
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        merged = first + second
        total_cost += merged
        plan.append((first, second, merged))
        
        heapq.heappush(heap, merged)
        
    return total_cost, plan


def minimum_cable_connection_cost_sorted_simulation(cables: list[int]) -> int:
    """Simulate the greedy logic using repeated sorting.
    
    This is less efficient than the heap implementation (O(n^2 log n) vs O(n log n))
    but is included for educational comparison.
    
    Args:
        cables: A list of cable lengths.
        
    Returns:
        The minimum total cost of connecting all cables.
    """
    validate_cables(cables)
    
    if len(cables) <= 1:
        return 0
        
    cables_copy = sorted(cables)
    total_cost = 0
    
    while len(cables_copy) > 1:
        first = cables_copy.pop(0)
        second = cables_copy.pop(0)
        
        merged = first + second
        total_cost += merged
        
        cables_copy.append(merged)
        cables_copy.sort()
        
    return total_cost
