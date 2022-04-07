from BinaryTrees.BinaryTree import Tree


def recursive_inorder_traversal(root):
    if root is None:
        return
    recursive_inorder_traversal(root.left)
    print(root.data, end=' ')
    recursive_inorder_traversal(root.right)


def iterative_inorder_traversal(root):
    if root is None:
        return
    stack, current = [], root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data, end=' ')
            current = current.right
        else:
            break


if __name__ == '__main__':
    recursive_inorder_traversal(root=Tree)
    print()
    iterative_inorder_traversal(root=Tree)
