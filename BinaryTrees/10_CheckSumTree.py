# https://www.techiedelight.com/check-given-binary-tree-sum-tree-not/
# https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/
from BinaryTree import Node


def calculate_sum(node):
    if node is None:
        return 0
    return calculate_sum(node.left) + node.data + calculate_sum(node.right)


def is_sum_tree(node):
    if node is None or (node.left is None and node.right is None):
        return True
    if node.data == calculate_sum(node.left) + calculate_sum(node.right) and \
            is_sum_tree(node.left) and is_sum_tree(node.right):
        return True
    return False


if __name__ == '__main__':
    """ Construct the following tree
             44
            /  \
           /    \
          9     13
         / \    / \
        4   5  6   7
    """

    Tree = Node(44)
    Tree.left = Node(9)
    Tree.right = Node(13)
    Tree.left.left = Node(4)
    Tree.left.right = Node(5)
    Tree.right.left = Node(6)
    Tree.right.right = Node(7)

    if is_sum_tree(Tree):
        print('Binary tree is a sum tree')
    else:
        print('Binary tree is not a sum tree')
