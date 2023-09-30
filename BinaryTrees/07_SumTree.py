# https://www.techiedelight.com/inplace-convert-a-tree-sum-tree/
from BinaryTree import Tree


def pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def sum_tree(root):
    if root is None:
        return 0
    old = root.data
    root.data = sum_tree(root.left) + sum_tree(root.right)
    return root.data + old


if __name__ == '__main__':
    pre_order(Tree)
    print()
    sum_tree(Tree)
    pre_order(Tree)
