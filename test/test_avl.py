import pytest
from src.avl import BinarySearchTree, BinaryTreeNode


@pytest.fixture
def empty_tree() -> BinarySearchTree:
    """Instance of an empty BinarySearchTree."""
    return BinarySearchTree()


@pytest.fixture
def one_node_tree() -> BinarySearchTree:
    """Instance of a single-node BinarySearchTree."""
    result = BinarySearchTree()
    result._root = BinaryTreeNode(item=0)
    return result


def test_sequence_on_empty_tree(empty_tree: BinarySearchTree) -> None:
    """Test if sequence of elements on empty tree is empty list."""
    assert empty_tree.sequence() == []


def test_sequence_on_one_node_tree(one_node_tree) -> None:
    """Test if sequence of elements on single node tree is one element list."""
    assert one_node_tree.sequence() == [one_node_tree._root.item]
