# https://www.techiedelight.com/convert-given-binary-tree-to-full-tree-removing-half-nodes/


from BinaryTree import Node


def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=' ')
    inorder_traversal(node.right)
    

def is_leaf(node):
    return node.left is None and node.right is None


def truncate(node):
    if node is None:
        return
    node.left = truncate(node.left)
    node.right = truncate(node.right)
    if (node.left and node.right) or is_leaf(node):
        return node
    return node.left if node.left else node.right


if __name__ == '__main__':
    """ Construct the following tree
                 0
               /   \
              /     \
             1       2
            /        /
           /        /
          3        4
         /        / \
        /        /   \
       5        6     7
    """

    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.left = Node(4)
    root.left.left.left = Node(5)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)

    inorder_traversal(root)
    print()
    root = truncate(root)
    inorder_traversal(root)
