# https://www.techiedelight.com/distance-between-given-pairs-of-nodes-binary-tree/


from BinaryTree import Node


def is_node_present(root, node):
    if node is None:
        return False
    if root == node:
        return True
    return is_node_present(root.left, node) or is_node_present(root.right, node)


def find_lca(root, node1, node2):
    if root is None:
        return None
    if root == node1 or root == node2:
        return root
    left = find_lca(root.left, node1, node2)
    right = find_lca(root.right, node1, node2)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right


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

    find_lca(root, root.right.left.left, root.right.right)
    find_lca(root, root.right.left.left, Node(10))
    find_lca(root, root.right.left.left, root.right.left.left)
    find_lca(root, root.right.left.left, root.right.left)
    find_lca(root, root.left, root.right.left)
# LCA is  3
# LCA does not exist
# LCA is  7
# LCA is  5
# LCA is  1