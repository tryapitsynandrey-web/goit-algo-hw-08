import pytest

from src.binary_search_tree import BinarySearchTree


def test_empty_tree():
    tree = BinarySearchTree()
    assert tree.is_empty()
    assert len(tree) == 0
    assert tree.inorder() == []


def test_single_node_tree():
    tree = BinarySearchTree()
    tree.insert(5)
    assert not tree.is_empty()
    assert len(tree) == 1
    assert tree.inorder() == [5]
    assert tree.root is not None
    assert tree.root.value == 5


def test_multiple_values():
    values = [20, 10, 30, 5, 15, 25, 35]
    tree = BinarySearchTree.from_iterable(values)
    assert len(tree) == 7
    assert tree.inorder() == [5, 10, 15, 20, 25, 30, 35]


def test_duplicate_values():
    values = [10, 10, 5, 15, 15]
    tree = BinarySearchTree.from_iterable(values)
    assert len(tree) == 5
    assert tree.inorder() == [5, 10, 10, 15, 15]


def test_non_integer_input():
    tree = BinarySearchTree()
    with pytest.raises(TypeError, match="Only integers are supported."):
        tree.insert("string")  # type: ignore


def test_preorder_traversal():
    values = [20, 10, 30, 5, 15]
    tree = BinarySearchTree.from_iterable(values)
    assert tree.preorder() == [20, 10, 5, 15, 30]


def test_postorder_traversal():
    values = [20, 10, 30, 5, 15]
    tree = BinarySearchTree.from_iterable(values)
    assert tree.postorder() == [5, 15, 10, 30, 20]


def test_level_order_traversal():
    values = [20, 10, 30, 5, 15, 25, 35]
    tree = BinarySearchTree.from_iterable(values)
    assert tree.level_order() == [20, 10, 30, 5, 15, 25, 35]
