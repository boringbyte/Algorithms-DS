from BinaryTree import Tree


def pre_order(node, horizontal_dist, level, d):
    if node is None:
        return
    if horizontal_dist not in d or level < d[horizontal_dist][1]:
        d[horizontal_dist] = [node.data, level]
    pre_order(node.left, horizontal_dist - 1, level + 1, d)
    pre_order(node.right, horizontal_dist + 1, level + 1, d)


def top_view(tree):
    h_dist_map = dict()
    pre_order(node=tree, horizontal_dist=0, level=0, d=h_dist_map)
    for key in sorted(h_dist_map.keys()):
        print(h_dist_map.get(key)[0], end=' ')


if __name__ == '__main__':
    top_view(tree=Tree)
