# https://www.techiedelight.com/print-bottom-view-of-binary-tree/
from BinaryTree import Tree


def pre_order_traversal(root, distance, level, d):
    if root is None:
        return
    if distance not in d or level >= d[distance][1]:
        d[distance] = (root.data, level)
    pre_order_traversal(root.left, distance-1, level+1, d)
    pre_order_traversal(root.right, distance+1, level+1, d)


def bottom_view(root):
    d = dict()
    pre_order_traversal(root, 0, 0, d)
    for key in sorted(d.keys()):
        print(d.get(key)[0], end=' ')


if __name__ == '__main__':
    bottom_view(root=Tree)
