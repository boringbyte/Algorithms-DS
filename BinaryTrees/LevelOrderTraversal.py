from BinaryTree import Tree
from collections import deque


def level_order_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.data, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


if __name__ == '__main__':
    level_order_traversal(root=Tree)
