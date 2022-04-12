# https://www.techiedelight.com/find-ancestors-of-given-node-binary-tree/


from BinaryTree import Node


def print_ancestors(root, node):
    if root is None:
        return False
    if root == node:
        return True
    
    left = print_ancestors(root.left, node)
    right = print_ancestors(root.right, node)
    
    if left or right:
        print(root.data, end=' ')
    return left or right


if __name__ == '__main__':
    """ Construct the following tree
              1
            /   \
           /     \
          2       3
           \     / \
            4   5   6
               / \
              7   8
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    node = root.right.left.left  # Node 7
    print_ancestors(root, node)
