from BinaryTrees.BinaryTree import Tree


def recursive_pre_order(root):
    if root is None:
        return
    print(root.data, end=' ')
    recursive_pre_order(root.left)
    recursive_pre_order(root.right)


def recursive_pre_order2(root):
    result = []

    def dfs(node):
        if node:
            result.append(node.data)
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return result


def iterative_pre_order(root):
    if root is None:
        return
    stack, current = [], root
    while True:
        if current is not None:
            print(current.data, end=' ')
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            current = current.right
        else:
            break


if __name__ == '__main__':
    recursive_pre_order(root=Tree)
    print()
    iterative_pre_order(root=Tree)
