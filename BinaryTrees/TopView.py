from BinaryTree import Tree


def pre_order_traversal(root, distance, level, d):
    if root is None:
        return
    if distance not in d or level < d[distance][1]:
        d[distance] = [root.data, level]
    pre_order_traversal(root.left, distance-1, level+1, d)
    pre_order_traversal(root.right, distance+1, level+1, d)


def top_view(tree):
    d = dict()
    pre_order_traversal(root=tree, distance=0, level=0, d=d)
    for key in sorted(d.keys()):
        print(d.get(key)[0], end=' ')


if __name__ == '__main__':
    top_view(tree=Tree)
