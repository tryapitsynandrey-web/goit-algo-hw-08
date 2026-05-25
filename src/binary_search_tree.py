"""Binary Search Tree implementation."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Node:
    """A node in a Binary Search Tree.
    
    Attributes:
        value: The integer value stored in the node.
        left: Left child node or None.
        right: Right child node or None.
    """
    value: int
    left: Node | None = None
    right: Node | None = None


class BinarySearchTree:
    """A simple Binary Search Tree implementation.
    
    Duplicates are inserted into the right subtree.
    """

    def __init__(self) -> None:
        """Initialize an empty Binary Search Tree."""
        self.root: Node | None = None
        self._size: int = 0

    def insert(self, value: int) -> None:
        """Insert a value into the BST.
        
        Args:
            value: The integer value to insert. Duplicates go to the right.
        """
        if not isinstance(value, int):
            raise TypeError("Only integers are supported.")

        if self.root is None:
            self.root = Node(value)
            self._size += 1
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    self._size += 1
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    self._size += 1
                    break
                current = current.right

    @classmethod
    def from_iterable(cls, values: Iterable[int]) -> BinarySearchTree:
        """Create a BST from an iterable of integers.
        
        Args:
            values: Iterable containing integers.
            
        Returns:
            A new BinarySearchTree instance.
        """
        tree = cls()
        for value in values:
            tree.insert(value)
        return tree

    def inorder(self) -> list[int]:
        """Perform an inorder traversal.
        
        Returns:
            List of values in sorted order.
        """
        result = []
        
        def _traverse(node: Node | None) -> None:
            if node is not None:
                _traverse(node.left)
                result.append(node.value)
                _traverse(node.right)
                
        _traverse(self.root)
        return result

    def preorder(self) -> list[int]:
        """Perform a preorder traversal.
        
        Returns:
            List of values in preorder sequence.
        """
        result = []
        
        def _traverse(node: Node | None) -> None:
            if node is not None:
                result.append(node.value)
                _traverse(node.left)
                _traverse(node.right)
                
        _traverse(self.root)
        return result

    def postorder(self) -> list[int]:
        """Perform a postorder traversal.
        
        Returns:
            List of values in postorder sequence.
        """
        result = []
        
        def _traverse(node: Node | None) -> None:
            if node is not None:
                _traverse(node.left)
                _traverse(node.right)
                result.append(node.value)
                
        _traverse(self.root)
        return result

    def level_order(self) -> list[int]:
        """Perform a level-order (BFS) traversal.
        
        Returns:
            List of values in level-order sequence.
        """
        if self.root is None:
            return []
            
        result = []
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
        return result

    def is_empty(self) -> bool:
        """Check if the tree is empty.
        
        Returns:
            True if empty, False otherwise.
        """
        return self.root is None

    def __len__(self) -> int:
        """Get the number of nodes in the tree.
        
        Returns:
            Number of nodes.
        """
        return self._size
