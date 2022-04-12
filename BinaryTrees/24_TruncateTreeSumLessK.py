# https://www.techiedelight.com/truncate-given-binary-tree-remove-nodes-lie-path-sum-less-k/


from BinaryTree import Node


def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=' ')
    inorder_traversal(node.right)
    
    
def is_leaf(node):
    return node.left is None and node.right is None


def truncate(node, k, target=0):
    if node is None:
        return
    target = target + node.data
    node.left = truncate(node.left, k, target)
    node.right = truncate(node.right, k, target)
    if target < k and is_leaf(node):
        return
    return node


if __name__ == '__main__':
    """ Construct the following tree
              6
            /   \
           /     \
          3       8
                /   \
               /     \
              4       2
            /   \      \
           /     \      \
          1       7      3
    """

    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.right.left = Node(4)
    root.right.right = Node(2)
    root.right.left.left = Node(1)
    root.right.left.right = Node(7)
    root.right.right.right = Node(3)

    k = 20
    inorder_traversal(root)
    print()
    root = truncate(root, k)
    inorder_traversal(root)
