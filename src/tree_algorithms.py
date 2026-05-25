"""Algorithms for calculating sums and finding minimum values in a binary tree."""

from collections import deque
from src.binary_search_tree import Node


# --- TASK 1: FIND MINIMUM VALUE IN A BST ---

def find_min_iterative_bst(root: Node | None) -> int:
    """Find the minimum value in a BST iteratively.
    
    Optimal for BST since the minimum is always the leftmost leaf.
    
    Args:
        root: The root node of the BST.
        
    Returns:
        The minimum integer value.
        
    Raises:
        ValueError: If the tree is empty.
    """
    if root is None:
        raise ValueError("Cannot find minimum of an empty tree.")
        
    current = root
    while current.left is not None:
        current = current.left
        
    return current.value


def find_min_recursive_bst(root: Node | None) -> int:
    """Find the minimum value in a BST recursively.
    
    Args:
        root: The root node of the BST.
        
    Returns:
        The minimum integer value.
        
    Raises:
        ValueError: If the tree is empty.
    """
    if root is None:
        raise ValueError("Cannot find minimum of an empty tree.")
        
    if root.left is None:
        return root.value
        
    return find_min_recursive_bst(root.left)


def find_min_general_dfs_recursive(root: Node | None) -> int:
    """Find the minimum value in a general binary tree using recursive DFS.
    
    Does not rely on BST properties, searches the whole tree.
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The minimum integer value.
        
    Raises:
        ValueError: If the tree is empty.
    """
    if root is None:
        raise ValueError("Cannot find minimum of an empty tree.")
        
    min_val = root.value
    
    if root.left is not None:
        min_val = min(min_val, find_min_general_dfs_recursive(root.left))
    if root.right is not None:
        min_val = min(min_val, find_min_general_dfs_recursive(root.right))
        
    return min_val


def find_min_general_dfs_iterative(root: Node | None) -> int:
    """Find the minimum value in a general binary tree using iterative DFS (stack).
    
    Does not rely on BST properties, searches the whole tree.
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The minimum integer value.
        
    Raises:
        ValueError: If the tree is empty.
    """
    if root is None:
        raise ValueError("Cannot find minimum of an empty tree.")
        
    min_val = root.value
    stack = [root]
    
    while stack:
        current = stack.pop()
        if current.value < min_val:
            min_val = current.value
            
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
            
    return min_val


def find_min_general_bfs(root: Node | None) -> int:
    """Find the minimum value in a general binary tree using BFS (queue).
    
    Does not rely on BST properties, searches the whole tree.
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The minimum integer value.
        
    Raises:
        ValueError: If the tree is empty.
    """
    if root is None:
        raise ValueError("Cannot find minimum of an empty tree.")
        
    min_val = root.value
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        if current.value < min_val:
            min_val = current.value
            
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
            
    return min_val


# --- TASK 2: CALCULATE SUM OF ALL VALUES IN A TREE ---

def sum_recursive_dfs(root: Node | None) -> int:
    """Calculate the sum of all values in a tree using recursive DFS.
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The sum of all values. Returns 0 for an empty tree.
    """
    if root is None:
        return 0
    return root.value + sum_recursive_dfs(root.left) + sum_recursive_dfs(root.right)


def sum_iterative_dfs(root: Node | None) -> int:
    """Calculate the sum of all values in a tree using iterative DFS (stack).
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The sum of all values. Returns 0 for an empty tree.
    """
    if root is None:
        return 0
        
    total_sum = 0
    stack = [root]
    
    while stack:
        current = stack.pop()
        total_sum += current.value
        
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
            
    return total_sum


def sum_iterative_bfs(root: Node | None) -> int:
    """Calculate the sum of all values in a tree using iterative BFS (queue).
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The sum of all values. Returns 0 for an empty tree.
    """
    if root is None:
        return 0
        
    total_sum = 0
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        total_sum += current.value
        
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
            
    return total_sum


def sum_morris_traversal(root: Node | None) -> int:
    """Calculate the sum of all values using Morris Inorder Traversal.
    
    Achieves O(1) space complexity by temporarily modifying the tree structure
    and restoring it before completing traversal.
    
    Args:
        root: The root node of the tree.
        
    Returns:
        The sum of all values. Returns 0 for an empty tree.
    """
    if root is None:
        return 0
        
    total_sum = 0
    current: Node | None = root
    
    while current is not None:
        if current.left is None:
            total_sum += current.value
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right
                
            if pre.right is None:
                # Thread creation: link predecessor to current
                pre.right = current
                current = current.left
            else:
                # Thread destruction: restore tree structure
                pre.right = None
                total_sum += current.value
                current = current.right
                
    return total_sum
