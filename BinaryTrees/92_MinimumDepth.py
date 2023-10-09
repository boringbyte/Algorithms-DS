from BinaryTree import Node
from collections import deque


def dfs_minimum_depth(node):
    if node is None:
        return 0
    l, r = dfs_minimum_depth(node.left), dfs_minimum_depth(node.right)
    if node.left is None:
        return 1 + r
    if node.right is None:
        return 1 + l
    return min(l, r) + 1


def bfs_minimum_depth(node):
    if root is None:
        return 0
    queue = deque([(node, 1)])
    while queue:
        current, depth = queue.popleft()
        if current.left is None and current.right is None:
            return depth
        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.right = Node(8)
    root.left.right.right = Node(9)
    root.right.right.left = Node(10)
    root.right.right.left = Node(11)
    root.left.left.right.right = Node(12)

    print('The minimum depth using DFS is', dfs_minimum_depth(root))
    print('The minimum depth using BFS is', bfs_minimum_depth(root))
