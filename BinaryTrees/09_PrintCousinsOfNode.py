# https://www.techiedelight.com/print-cousins-of-given-node-binary-tree/
from BinaryTree import Node


def find_level(root, x, index=1, level=0):
    if root is None or level != 0:
        return level
    if root == x:
        level = index
    level = find_level(root.left, x, index+1, level)
    level = find_level(root.right, x, index+1, level)
    return level


def print_level(root, node, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=' ')
        return
    if not (root.left is not None and root.left == node or root.right is not None and root.right == node):
        print_level(root.left, node, level - 1)
        print_level(root.right, node, level - 1)


def print_all_cousins(root, node):
    if not root or root == node:
        return
    level = find_level(root, node)
    print_level(root, node, level)


if __name__ == '__main__':
    """ Construct the following tree
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
    """

    Tree = Node(1)
    Tree.left = Node(2)
    Tree.right = Node(3)
    Tree.left.left = Node(4)
    Tree.left.right = Node(5)
    Tree.right.left = Node(6)
    Tree.right.right = Node(7)

    print_all_cousins(Tree, Tree.left.right)
