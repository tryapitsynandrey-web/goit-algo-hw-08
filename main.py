
from src.binary_search_tree import BinarySearchTree
from src.cable_heap import (
    minimum_cable_connection_cost,
    minimum_cable_connection_cost_sorted_simulation,
    minimum_cable_connection_plan,
)
from src.tree_algorithms import (
    find_min_general_bfs,
    find_min_general_dfs_iterative,
    find_min_general_dfs_recursive,
    find_min_iterative_bst,
    find_min_recursive_bst,
    sum_iterative_bfs,
    sum_iterative_dfs,
    sum_morris_traversal,
    sum_recursive_dfs,
)


def demonstrate_bst():
    """Demonstrate Task 1 and 2: BST logic, minimum search and sum."""
    print("=" * 50)
    print("TASK 1 & 2: BINARY SEARCH TREE")
    print("=" * 50)

    # 1. Tree Creation
    values = [20, 10, 30, 5, 15, 25, 35]
    print(f"Creating BST from values: {values}")
    tree = BinarySearchTree.from_iterable(values)
    
    # 2. Traversals
    print("\nTraversals:")
    print(f"Inorder:     {tree.inorder()}")
    print(f"Preorder:    {tree.preorder()}")
    print(f"Postorder:   {tree.postorder()}")
    print(f"Level-order: {tree.level_order()}")

    root = tree.root

    # 3. Minimum Search (Task 1)
    print("\nTask 1: Minimum Value Search Approaches")
    print("Expected Minimum: 5")
    print(f"BST Iterative (Optimal): {find_min_iterative_bst(root)}")
    print(f"BST Recursive:           {find_min_recursive_bst(root)}")
    print(f"General DFS Iterative:   {find_min_general_dfs_iterative(root)}")
    print(f"General DFS Recursive:   {find_min_general_dfs_recursive(root)}")
    print(f"General BFS Iterative:   {find_min_general_bfs(root)}")

    # 4. Tree Sum (Task 2)
    print("\nTask 2: Tree Sum Approaches")
    print("Expected Sum: 140")
    print(f"Recursive DFS:     {sum_recursive_dfs(root)}")
    print(f"Iterative DFS:     {sum_iterative_dfs(root)}")
    print(f"Iterative BFS:     {sum_iterative_bfs(root)}")
    print(f"Morris Traversal:  {sum_morris_traversal(root)}  (O(1) space)")
    print()


def demonstrate_cable_heap():
    """Demonstrate Task 3: Minimum Cable Connection Cost using Heaps."""
    print("=" * 50)
    print("TASK 3: MINIMUM CABLE CONNECTION COST")
    print("=" * 50)

    cables = [4, 3, 2, 6]
    print(f"Input Cables: {cables}")
    print("Expected Minimum Total Cost: 29")

    # 1. Heap Implementation (Optimal)
    heap_cost = minimum_cable_connection_cost(cables)
    print(f"\nCost using Min-Heap (O(N log N)): {heap_cost}")

    # 2. Simulation Implementation
    sim_cost = minimum_cable_connection_cost_sorted_simulation(cables)
    print(f"Cost using repeated sorting (O(N^2 log N)): {sim_cost}")

    # 3. Detailed Plan
    _, plan = minimum_cable_connection_plan(cables)
    print("\nMerge Plan:")
    for step, (c1, c2, merged) in enumerate(plan, 1):
        print(f"Step {step}: Connect cable {c1} and cable {c2} -> merged length {merged}")

    print()


def main():
    """Run all demonstrations."""
    demonstrate_bst()
    demonstrate_cable_heap()


if __name__ == "__main__":
    main()
