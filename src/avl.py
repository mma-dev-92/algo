"""Simple implementation of AVL tree."""

from typing import Iterable, List, Self


class BinarySearchTreeError(Exception):
    """Exception class for BinarySearchTree operations."""


class BinaryTreeNode:
    """AVL tree node implementation."""

    def __init__(
        self,
        item: int,
        left: Self | None = None,
        right: Self | None = None,
        parent: Self | None = None,
    ) -> None:
        """
        Binary tree node.

        Args:
            left: BinaryTreeNode | None - left child node of self
            right: BinaryTreeNode | None - right child node of self
            parent: BinaryTreeNode | None - parent node of self
            item: Any - an item that is contained in self
        """
        self.left = left
        self.right = right
        self.parent = parent
        self.item = item


class BinarySearchTree:
    """Set implementation using binary tree data structure (example code)."""

    def __init__(self) -> None:
        """Create empty instance of a set."""
        self._root: BinaryTreeNode | None = None
        self._size = 0

    @property
    def size(self) -> int:
        """Size of a tree."""
        return self._size

    def sequence(self) -> List[int]:
        """Return sorted list containing all set elements."""
        result: List[int] = list()
        node = self._root
        S: List[int] = list()
        while node is not None or len(S) > 0:
            # go left as much as you can
            if node is not None:
                # if you can - push current node to S
                S.append(node)
                # and go left
                node = node.left
            # if going left is not an option
            else:
                # take the last visited node
                node = S.pop()
                # push it to the resulting list
                result.append(node)
                # and go right
                node = node.right

        return result

    def add_items(self, items: Iterable[int]) -> None:
        """Add multiple items to a set, existing items will be skipped."""
        raise NotImplementedError

    def add_item(self, item: int) -> None:
        """Add an item to a set it is not contained in a set already."""
        pass

    def remove(self, item: int) -> None:
        """Remove item from the tree."""
        raise NotImplementedError

    def __contains__(self, key: int) -> bool:
        """Check if a given key is in the tree."""
        node = self._root
        while node is not None:
            if key < node.item:
                node = node.left
            elif key > node.item:
                node = node.right
            else:
                break
        return node is not None

    def find_preious(self, key: int) -> int | None:
        """
        Biggest lower bound of given key in the set.

        Args:
            key: int - key to find in a tree

        Returns:
            If key is found in the set, key is returned else biggest lower
            bound of the key is returned, if there is no lower bound of the
            given key in the set, None is returned.

        """
        prev_node = self._find_previous_node(key, self._root)
        return prev_node if prev_node.item <= key else None

    def find_next(self, key: int) -> int | None:
        """
        Smallest upper bound of given key in the set.

        Args:
            key: int - key to find in a tree

        Returns:
            If key is found in the set, key is returned else smallest upper
            bound of the key is returned, if there is no upper bound of the
            given key in the set, None is returned.

        """
        next_node = self._find_next_node(key, self._root)
        return next_node.item if next_node.item >= key else None

    def _find_previous_node(
        self, key: int, root: BinaryTreeNode | None
    ) -> BinaryTreeNode | None:
        """
        Find previous node in the tree assuming in-order traversal order.

        If tree contains node with item == key, that node is returned, if not
        node with biggest lower bound of key is returned, if such node does not
        exist in the tree, node with minimal node.item is returned.

        If root = None, function will return None.

        Args:
            key: int - key to look for in the tree
            root: BinaryTreeNode | None - root of the subtree to search in

        Returns:
            Previous node with respect to a given key in the given subtree, if
            such node does not exist, None is returned.

        """
        node: BinaryTreeNode = root
        result: BinaryTreeNode | None = None
        while node is not None:
            # if lower bound has been found
            if node.item < key:
                # remember the lower bound
                result = node
                # go right, maybe you will find bigger lower bound
                node = node.right
            # if node.item is to big
            elif key < node.item:
                # if you can go left - do it
                if node.left is not None:
                    node = node.left
                # if you can not go to the left
                else:
                    # no lower bound for given key: return minimal node
                    return node
            # if you have found node, such that node.item == key
            else:
                # return it
                return node
        return result

    def _find_next_node(self, key: int, root: BinaryTreeNode) -> BinaryTreeNode | None:
        """
        Find next node in the tree assuming in-order traversal order.

        If tree contains node with item == key, that node is returned, if not
        node with smallest upper bound of key is returned, if such node does
        not exist in the tree, node with maximal node.item is returned.

        If root = None, function will return None.

        Args:
            key: int - key to look for in the tree
            root: BinaryTreeNode | None - root of the subtree to search in

        Returns:
            Next node with respect to a given key in the given subtree, if
            such node does not exist, None is returned.

        """
        node: BinaryTreeNode = root
        result: BinaryTreeNode | None = None
        while node is not None:
            # if upper bound has been found
            if node.item > key:
                # remember the upper bound
                result = node
                # go left, maybe you will find smaller upper bound
                node = node.left
            # if node.item is to small
            elif key > node.item:
                # if you can go right - do it
                if node.right is not None:
                    node = node.right
                # if you can not go to the right
                else:
                    # no upper bound for given key: return maximal node
                    return node
            # if you have found node, such that node.item == key - return it
            else:
                return node

        return result
