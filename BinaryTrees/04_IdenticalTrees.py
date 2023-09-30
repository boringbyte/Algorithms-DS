# https://www.techiedelight.com/check-if-two-binary-trees-are-identical-not-iterative-recursive/
from BinaryTree import Node
from collections import deque


def is_identical_bfs(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    queue = deque()
    queue.append([tree1, tree2])
    while queue:
        root1, root2 = queue.popleft()
        if root1.data != root2.data:
            return False
        if root1.left and root2.left:
            queue.append([root1.left, root2.left])
        elif root1.left or root2.left:
            return False
        if root1.right and root2.right:
            queue.append([root1.right, root2.right])
        elif root1.right or root2.right:
            return False
    return True


def is_identical_dfs(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    stack = [[tree1, tree2]]
    while stack:
        root1, root2 = stack.pop()
        if root1.data != root2.data:
            return False
        if root1.left and root2.left:
            stack.append([root1.left, root2.left])
        elif root1.left or root2.left:
            return False
        if root1.right and root2.right:
            stack.append([root1.right, root2.right])
        elif root1.right or root2.right:
            return False
    return True


def is_identical_dfs2(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    stack = [[tree1, tree2]]
    while stack:
        node1, node2 = stack.pop()
        if node1 and node2 and node1.data == node2.data:
            stack.append([node1.left, node2.left])
            stack.append([node1.right, node2.right])
        elif node1 or node2:
            return False
    return True


def is_identical_recursive(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.data == root2.data and \
        is_identical_recursive(root1.left, root2.left) and is_identical_recursive(root1.right, root2.right)


if __name__ == '__main__':

    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)

    # construct the second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)

    if is_identical_bfs(x, y):
        print('The given binary trees are identical')
    else:
        print('The given binary trees are not identical')

    if is_identical_dfs(x, y):
        print('The given binary trees are identical')
    else:
        print('The given binary trees are not identical')

    if is_identical_dfs2(x, y):
        print('The given binary trees are identical')
    else:
        print('The given binary trees are not identical')

    if is_identical_recursive(x, y):
        print('The given binary trees are identical')
    else:
        print('The given binary trees are not identical')
