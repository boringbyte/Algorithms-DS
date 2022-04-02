from BinaryTree import Tree


def recursive_post_order_traversal(root):
    if root is None:
        return
    recursive_post_order_traversal(root.left)
    recursive_post_order_traversal(root.right)
    print(root.data, end=' ')


def iterative_post_order_traversal(root):
    if root is None:
        return
    stack1, stack2, current = [root], [], None
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        current = stack2.pop()
        print(current.data, end=' ')


if __name__ == '__main__':
    recursive_post_order_traversal(root=Tree)
    print()
    iterative_post_order_traversal(root=Tree)
