# https://www.techiedelight.com/check-given-binary-tree-symmetric-structure-not/

from BinaryTree import Node


def is_symmetric(node1, node2):  # symmetric is not mirror. Both are different.
    if node1 is None and node2 is None:
        return True
    return (node1 is not None and node2 is not None) and \
        is_symmetric(node1.left, node2.right) and is_symmetric(node1.right, node2.left)


def symmetric_tree(root):
    if root is None:
        return True
    return is_symmetric(root.left, root.right)


if __name__ == '__main__':
    """ Construct the following tree
          1
        /   \
       /     \
      2       3
       \     /
        5   6
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)

    if symmetric_tree(root):
        print('The binary tree is symmetric')
    else:
        print('The binary tree is not symmetric')