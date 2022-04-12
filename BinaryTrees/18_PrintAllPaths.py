# https://www.techiedelight.com/print-all-paths-from-root-to-leaf-nodes-binary-tree/

from BinaryTree import Node
from collections import deque


def print_all_paths(node, path=deque()):  # Similar to BackTracking
    if node is None:
        return
    path.append(node.data)
    if node.left is None and node.right is None:
        print(list(path))
    print_all_paths(node.left, path)
    print_all_paths(node.right, path)
    path.pop()


if __name__ == '__main__':
    """ Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
               /     \
              8       9
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)

    # print all root-to-leaf paths
    print_all_paths(root)
