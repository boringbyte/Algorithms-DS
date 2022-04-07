# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
# https://www.techiedelight.com/determine-given-binary-tree-is-subtree-of-another-binary-tree-not/
# https://www.techiedelight.com/find-diameter-of-a-binary-tree/


from BinaryTree import Tree, Node

cache = dict()


def height(node):
    if node is None:
        return 0
    if node in cache:
        return cache[node]
    h = 1 + max(height(node.left), height(node.right))
    cache[node] = h
    return h


def diameter_slow(root):  # n*2 time complexity if cache is not there
    if root is None:
        return 0
    l_height, r_height = height(root.left), height(root.right)
    l_diameter, r_diameter = diameter_slow(root.left), diameter_slow(root.right)
    return max(l_height + r_height + 1, l_diameter, r_diameter)


def diameter_fast(root, diameter=0):
    if root is None:
        return 0, diameter
    l_height, diameter = diameter_fast(root.left, diameter)
    r_height, diameter = diameter_fast(root.right, diameter)
    max_diameter = l_height + r_height + 1
    diameter = max(diameter, max_diameter)
    return max(l_height, r_height) + 1, diameter


if __name__ == '__main__':
    Tree2 = Node(1)
    Tree2.left = Node(2)
    Tree2.right = Node(3)
    Tree2.left.left = Node(4)
    Tree2.left.right = Node(5)
    print(diameter_slow(Tree))
    print(diameter_slow(Tree2))
    print(diameter_fast(Tree)[1])
    print(diameter_fast(Tree2)[1])

