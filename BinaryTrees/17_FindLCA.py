# https://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/

from BinaryTree import Node


def is_node_present(root, node):
    if root is None:
        return False
    if root == node:
        return True
    return is_node_present(root.left, node) or is_node_present(root.right, node)


def find_lca(root, lca, node1, node2):
    if root is None:
        return False, lca
    if root == node1 or root == node2:
        return True, root
    left, lca = find_lca(root.left, lca, node1, node2)
    right, lca = find_lca(root.right, lca, node1, node2)
    if left and right:
        lca = root
    return (left or right), lca
    
    
def main_find_LCA(root, node1, node2):
    is_valid, lca, = False, None
    if is_node_present(root, node1) and is_node_present(root, node2):
        is_valid, lca = find_lca(root, lca, node1, node2)
    if is_valid:
        print('LCA is ', lca.data)
    else:
        print('LCA does not exist')


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

    main_find_LCA(root, root.right.left.left, root.right.right)
    main_find_LCA(root, root.right.left.left, Node(10))
    main_find_LCA(root, root.right.left.left, root.right.left.left)
    main_find_LCA(root, root.right.left.left, root.right.left)
    main_find_LCA(root, root.left, root.right.left)
