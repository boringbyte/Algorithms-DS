# Read the problem solution carefully
import collections
from BinaryTree import Node


class DLL:
    def __init__(self, prev=None, next=None):
        self.data = []
        self.prev = prev
        self.next = next


def collect_nodes(mid, result):
    while mid and mid.prev:
        mid = mid.prev
    head = mid
    while head:
        result.append(head.data)
        head = head.next


def dfs_vertical_order(root):

    result = []

    def dfs(node, current):
        if node is None:
            return
        current.data.append(node.data)
        if node.left and current.prev is None:
            current.prev = DLL(None, current)
        if node.right and current.next is None:
            current.next = DLL(current, None)
        dfs(node.left, current.prev)
        dfs(node.right, current.next)

    current = DLL()
    dfs(root, current)
    collect_nodes(current, result)
    return result


def bfs_vertical_order(root):

    def bfs(node, current):
        if node is None:
            return

        queue = collections.deque([(root, current)])
        while queue:
            node, current = queue.popleft()
            current.data.append(node.data)
            if node.left:
                if current.prev is None:
                    current.prev = DLL(None, current)
                queue.append((node.left, current.prev))
            if node.right:
                if current.next is None:
                    current.next = DLL(current, None)
                queue.append((node.right, current.next))
        return current

    current, result = DLL(), []
    bfs(root, current)
    collect_nodes(current, result)
    return result


if __name__ == '__main__':
    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
                /   \
               /     \
              5       6
            /   \
           /     \
          7       8
                /   \
               /     \
              9      10
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.left.right.left = Node(9)
    root.right.left.right.right = Node(10)

    print(dfs_vertical_order(root))
    print(bfs_vertical_order(root))
