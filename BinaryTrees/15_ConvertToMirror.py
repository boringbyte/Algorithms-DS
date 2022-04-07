# https://www.techiedelight.com/convert-binary-tree-to-its-mirror/

from BinaryTree import Node


def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


# def swap(root):
#     if root is None:
#         return
#     root.left, root.right = root.right, root.left


def convert_to_mirror(root):
    if root is None:
        return
    convert_to_mirror(root.left)
    convert_to_mirror(root.right)
    root.left, root.right = root.right, root.left


if __name__ == '__main__':
    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    preorder(root)
    convert_to_mirror(root)
    print()
    preorder(root)
