import pytest

from src.binary_search_tree import BinarySearchTree
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


@pytest.fixture
def balanced_tree():
    return BinarySearchTree.from_iterable([20, 10, 30, 5, 15, 25, 35])


@pytest.fixture
def right_skewed_tree():
    return BinarySearchTree.from_iterable([10, 20, 30, 40, 50])


@pytest.fixture
def left_skewed_tree():
    return BinarySearchTree.from_iterable([50, 40, 30, 20, 10])


@pytest.fixture
def empty_tree():
    return BinarySearchTree()


@pytest.fixture
def tree_with_negatives():
    return BinarySearchTree.from_iterable([10, -5, 20, -10, 0, 15])


# --- Test Find Minimum ---

def test_find_min_balanced(balanced_tree):
    root = balanced_tree.root
    assert find_min_iterative_bst(root) == 5
    assert find_min_recursive_bst(root) == 5
    assert find_min_general_dfs_recursive(root) == 5
    assert find_min_general_dfs_iterative(root) == 5
    assert find_min_general_bfs(root) == 5


def test_find_min_right_skewed(right_skewed_tree):
    root = right_skewed_tree.root
    assert find_min_iterative_bst(root) == 10
    assert find_min_recursive_bst(root) == 10
    assert find_min_general_dfs_recursive(root) == 10
    assert find_min_general_dfs_iterative(root) == 10
    assert find_min_general_bfs(root) == 10


def test_find_min_left_skewed(left_skewed_tree):
    root = left_skewed_tree.root
    assert find_min_iterative_bst(root) == 10
    assert find_min_recursive_bst(root) == 10
    assert find_min_general_dfs_recursive(root) == 10
    assert find_min_general_dfs_iterative(root) == 10
    assert find_min_general_bfs(root) == 10


def test_find_min_with_negatives(tree_with_negatives):
    root = tree_with_negatives.root
    assert find_min_iterative_bst(root) == -10
    assert find_min_recursive_bst(root) == -10
    assert find_min_general_dfs_recursive(root) == -10
    assert find_min_general_dfs_iterative(root) == -10
    assert find_min_general_bfs(root) == -10


def test_find_min_empty_tree(empty_tree):
    root = empty_tree.root
    with pytest.raises(ValueError, match="Cannot find minimum of an empty tree."):
        find_min_iterative_bst(root)
    with pytest.raises(ValueError, match="Cannot find minimum of an empty tree."):
        find_min_recursive_bst(root)
    with pytest.raises(ValueError, match="Cannot find minimum of an empty tree."):
        find_min_general_dfs_recursive(root)
    with pytest.raises(ValueError, match="Cannot find minimum of an empty tree."):
        find_min_general_dfs_iterative(root)
    with pytest.raises(ValueError, match="Cannot find minimum of an empty tree."):
        find_min_general_bfs(root)


def test_find_min_duplicates():
    tree = BinarySearchTree.from_iterable([10, 10, 5, 5, 20])
    assert find_min_iterative_bst(tree.root) == 5


# --- Test Tree Sum ---

def test_sum_balanced(balanced_tree):
    root = balanced_tree.root
    assert sum_recursive_dfs(root) == 140
    assert sum_iterative_dfs(root) == 140
    assert sum_iterative_bfs(root) == 140
    assert sum_morris_traversal(root) == 140


def test_sum_with_negatives(tree_with_negatives):
    root = tree_with_negatives.root
    assert sum_recursive_dfs(root) == 30
    assert sum_iterative_dfs(root) == 30
    assert sum_iterative_bfs(root) == 30
    assert sum_morris_traversal(root) == 30


def test_sum_empty_tree(empty_tree):
    root = empty_tree.root
    assert sum_recursive_dfs(root) == 0
    assert sum_iterative_dfs(root) == 0
    assert sum_iterative_bfs(root) == 0
    assert sum_morris_traversal(root) == 0


def test_sum_single_node():
    tree = BinarySearchTree.from_iterable([42])
    root = tree.root
    assert sum_recursive_dfs(root) == 42
    assert sum_iterative_dfs(root) == 42
    assert sum_iterative_bfs(root) == 42
    assert sum_morris_traversal(root) == 42


def test_sum_duplicates():
    tree = BinarySearchTree.from_iterable([10, 10, 5, 5, 20])
    root = tree.root
    assert sum_recursive_dfs(root) == 50
    assert sum_iterative_dfs(root) == 50
    assert sum_iterative_bfs(root) == 50
    assert sum_morris_traversal(root) == 50


def test_morris_traversal_does_not_break_tree(balanced_tree):
    root = balanced_tree.root
    original_inorder = balanced_tree.inorder()
    
    # Run morris traversal which modifies tree temporarily
    assert sum_morris_traversal(root) == 140
    
    # Check tree is intact
    assert balanced_tree.inorder() == original_inorder
