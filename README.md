# BST and Heap Algorithms

Homework project implementing Binary Search Tree algorithms and heap-based cable connection optimization.

## Assignment Overview

This project solves three algorithmic tasks:

1. Find the minimum value in a Binary Search Tree.
2. Calculate the sum of all values in a Binary Search Tree.
3. Find the minimum total cost of connecting network cables using a min-heap.

The project is fully self-contained. It uses a custom Binary Search Tree implementation and does not rely on external tree or algorithm libraries.

## Implemented Algorithms

### Task 1: Minimum Value in a Binary Search Tree

The project includes several approaches for finding the minimum value:

- **Iterative BST search**: Uses the BST property and repeatedly moves to the left child.
- **Recursive BST search**: Recursive version of the same BST-specific logic.
- **General DFS recursive search**: Traverses the entire tree without relying on BST ordering.
- **General DFS iterative search**: Uses a stack to scan all nodes.
- **General BFS search**: Uses a queue to scan the tree level by level.

The BST-specific approaches are more efficient because the minimum value in a BST is always located in the leftmost node.

### Task 2: Sum of All Tree Values

The project includes several approaches for calculating the total sum of tree values:

- **Recursive DFS**.
- **Iterative DFS using a stack**.
- **Iterative BFS using a queue**.
- **Morris inorder traversal** with O(1) auxiliary space.

All approaches return the same result for the same tree. Empty trees return `0`.

### Task 3: Minimum Cable Connection Cost

The project solves the cable connection problem using a greedy min-heap approach.

At each step, the two shortest cables are merged first. This minimizes the accumulated cost because smaller partial sums are reused fewer times in later merge operations.

Implemented approaches:

- **Min-heap solution using `heapq`**.
- **Merge plan generation** showing each cable connection step.
- **Sorted simulation** for educational comparison.

## Project Structure

```text
.
├── .gitignore
├── README.md
├── main.py
├── pyproject.toml
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── binary_search_tree.py
│   ├── cable_heap.py
│   └── tree_algorithms.py
└── tests/
    ├── __init__.py
    ├── test_binary_search_tree.py
    ├── test_cable_heap.py
    └── test_tree_algorithms.py
```

## Algorithmic Complexity

| Task | Algorithm | Time Complexity | Space Complexity |
| --- | ---: | ---: | ---: |
| Minimum search | Iterative BST search | O(h) | O(1) |
| Minimum search | Recursive BST search | O(h) | O(h) |
| Minimum search | General DFS recursive | O(n) | O(h) |
| Minimum search | General DFS iterative | O(n) | O(n) |
| Minimum search | General BFS | O(n) | O(n) |
| Tree sum | Recursive DFS | O(n) | O(h) |
| Tree sum | Iterative DFS | O(n) | O(n) |
| Tree sum | Iterative BFS | O(n) | O(n) |
| Tree sum | Morris traversal | O(n) | O(1) |
| Cable cost | Min-heap | O(n log n) | O(n) |
| Cable cost | Sorted simulation | O(n² log n) | O(n) |

Where:

- `n` is the number of nodes or cables.
- `h` is the height of the tree.

## Environment Setup

The project requires Python 3.11 or newer.

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## How to Run the Project

```bash
python main.py
```

## How to Run Tests

```bash
python -m pytest
```

## Example Input Data

Binary Search Tree values:

```python
[20, 10, 30, 5, 15, 25, 35]
```

Expected minimum value:

```text
5
```

Expected tree sum:

```text
140
```

Cable lengths:

```python
[4, 3, 2, 6]
```

Expected minimum total connection cost:

```text
29
```

## Example Output

```text
TASK 1 & 2: BINARY SEARCH TREE
Creating BST from values: [20, 10, 30, 5, 15, 25, 35]

Traversals:
Inorder:     [5, 10, 15, 20, 25, 30, 35]
Preorder:    [20, 10, 5, 15, 30, 25, 35]
Postorder:   [5, 15, 10, 25, 35, 30, 20]
Level-order: [20, 10, 30, 5, 15, 25, 35]

Task 1: Minimum Value Search Approaches
Expected Minimum: 5
BST Iterative (Optimal): 5
BST Recursive:           5
General DFS Iterative:   5
General DFS Recursive:   5
General BFS Iterative:   5

Task 2: Tree Sum Approaches
Expected Sum: 140
Recursive DFS:     140
Iterative DFS:     140
Iterative BFS:     140
Morris Traversal:  140  (O(1) space)

TASK 3: MINIMUM CABLE CONNECTION COST
Input Cables: [4, 3, 2, 6]
Expected Minimum Total Cost: 29

Cost using Min-Heap (O(N log N)): 29
Cost using repeated sorting (O(N^2 log N)): 29

Merge Plan:
Step 1: Connect cable 2 and cable 3 -> merged length 5
Step 2: Connect cable 4 and cable 5 -> merged length 9
Step 3: Connect cable 6 and cable 9 -> merged length 15
```

## Test Verification

The project was verified with:

```bash
python -m pytest
```

Result:

```text
33 passed
```

The test suite covers:

- empty tree cases;
- single-node trees;
- duplicate values;
- left-skewed and right-skewed trees;
- all minimum-search approaches;
- all tree-sum approaches;
- Morris traversal structure preservation;
- cable connection edge cases;
- invalid cable inputs;
- input immutability.

## Notes for Mentor Review

- The project uses a custom Binary Search Tree implementation.
- Duplicates are inserted into the right subtree.
- Empty-tree minimum search raises `ValueError`.
- Empty-tree sum returns `0`.
- The cable connection solution uses `heapq` from the Python standard library.
- The main heap solution does not mutate the original input list.
- The sorted simulation is included only for comparison with the heap-based solution.
