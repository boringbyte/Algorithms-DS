from BinaryTrees.BinaryTree import Tree


def recursive_inorder(root):
    if root is None:
        return
    recursive_inorder(root.left)
    print(root.data, end=' ')
    recursive_inorder(root.right)


def iterative_inorder(root):
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
    recursive_inorder(root=Tree)
    print()
    iterative_inorder(root=Tree)
