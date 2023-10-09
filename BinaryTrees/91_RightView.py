import collections
from BinaryTree import Node


def pre_order(node, level, d):
    if node is None:
        return
    d[level] = node.data
    pre_order(node.left, level + 1, d)
    pre_order(node.right, level + 1, d)


def dfs_right_view(root):
    level_dict = dict()
    pre_order(root, 1, level_dict)
    return list(level_dict.values())


def bfs_right_view(node):
    if node is None:
        return
    queue, result = collections.deque([node]), []
    while queue:
        i, size = 0, len(queue)
        while i < size:
            i += 1
            current = queue.popleft()
            if i == size:
                result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return result


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print(bfs_right_view(root))
    print(dfs_right_view(root))
