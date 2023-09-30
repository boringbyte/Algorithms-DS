# https://www.techiedelight.com/print-bottom-view-of-binary-tree/
from BinaryTree import Tree


def pre_order(node, horizontal_dist, level, d):
    if node is None:
        return
    if horizontal_dist not in d or level >= d[horizontal_dist][1]:
        d[horizontal_dist] = (node.data, level)
    pre_order(node.left, horizontal_dist - 1, level + 1, d)
    pre_order(node.right, horizontal_dist + 1, level + 1, d)


def bottom_view(root):
    h_dist_map = dict()
    pre_order(root, 0, 0, h_dist_map)
    for key in sorted(h_dist_map.keys()):
        print(h_dist_map.get(key)[0], end=' ')


if __name__ == '__main__':
    bottom_view(root=Tree)
