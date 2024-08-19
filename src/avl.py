"""Simple implementation of AVL tree."""
from typing import Any
from enum import Enum, auto


class AVLTreeNode:
    """AVL tree node implementation."""

    def __init__(
            self,
            left: 'AVLTreeNode' | None,
            right: 'AVLTreeNode' | None,
            parent: 'AVLTreeNode' | None,
            item: Any
    ) -> None:
        """
        Binary tree node.

        Args:
            left: AVLTreeNode | None - left child node of self
            right: AVLTreeNode | None - right child node of self
            parent: AVLTreeNode | None - parent node of self
            item: Any - an item that is contained in self
        """
        self._left = left
        self._right = right
        self._parent = parent
        self._item = item
        self._height = 0


class TraverseOrder(Enum):
    """Possible tree traverse orders."""

    pre_order = auto()
    in_order = auto()
    post_order = auto()


class AVLTree:
    """AVL tree data structure implementation."""

    @property
    def size(self) -> int:
        """Size of a tree."""
        raise NotImplementedError

    def sequence(self) -> list:
        """Return the list of the items in a given order."""
        raise NotImplementedError

    def add_item(self, item: Any) -> None:
        """Add an item to the tree."""
        raise NotImplementedError

    def remove(self, item: Any) -> None:
        """Remove item from the tree."""
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        """Check if a given key is in the tree."""
        raise NotImplementedError
