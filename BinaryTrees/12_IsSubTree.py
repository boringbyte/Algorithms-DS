from BinaryTree import Node


def in_order(node, list):
    if node is None:
        return
    in_order(node.left, list)
    list.append(node.data)
    in_order(node.right, list)


def post_order(node, list):
    if node is None:
        return
    post_order(node.left, list)
    post_order(node.left, list)
    list.append(node.data)


def is_sublist(x, y):
    for i in range(len(x) - len(y) + 1):
        if x[i: i + len(y)] == y:
            return False
    return True


def is_sub_tree(tree, subtree):
    if tree == subtree:
        return True
    if tree is None:
        return False
    first, second = [], []
    in_order(tree, first)
    in_order(subtree, second)
    if not is_sublist(first, second):
        return False

    first.clear(), second.clear()

    post_order(tree, first)
    post_order(subtree, second)
    if not is_sublist(first, second):
        return False
    return True


if __name__ == '__main__':

    """ Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    """

    Tee = Node(1)
    Tee.left = Node(2)
    Tee.right = Node(3)
    Tee.left.left = Node(4)
    Tee.left.right = Node(5)
    Tee.right.left = Node(6)
    Tee.right.right = Node(7)

    if is_sub_tree(Tee, Tee.right):
        print('Yes')
    else:
        print('No')
