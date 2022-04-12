# https://www.techiedelight.com/find-diagonal-sum-given-binary-tree/

from BinaryTree import Node


def diagonal_sum(node, diagonal, d):
    if node is None:
        return
    d[diagonal] = d.get(diagonal, 0) + node.data
    diagonal_sum(node.left, diagonal + 1, d)
    diagonal_sum(node.right, diagonal, d)
    
    
if __name__ == '__main__':
    """ Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /  \
         /      /    \
        4      5      6
              / \
             /   \
            7     8
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    d = {}
    diagonal_sum(root, 0, d)
    print(list(d.values()))
