# https://www.techiedelight.com/determine-two-nodes-are-cousins/
from BinaryTree import Node


class ParentNodeInfo:
    def __init__(self, node, parent, level):
        self.node = node
        self.level = level
        self.parent = parent


def update_level_and_parent(child, x, y, parent=None, level=1):
    if child is None:
        return

    update_level_and_parent(child.left, x, y, child, level + 1)
    if child == x.node:
        x.level, x.parent = level, parent

    if child == y.node:
        y.level, y.parent = level, parent
    update_level_and_parent(child.right, x, y, child, level + 1)


def check_cousins(root, node1, node2):
    if root is None:
        return False
    level, parent = 1, None
    x, y = ParentNodeInfo(node1, parent, level), ParentNodeInfo(node2, parent, level)
    update_level_and_parent(root, x, y)
    return x.level == y.level and x.parent != y.parent


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if check_cousins(root, root.left.right, root.right.left):
        print('Nodes are cousins of each other')
    else:
        print('Nodes are not cousins of each other')
