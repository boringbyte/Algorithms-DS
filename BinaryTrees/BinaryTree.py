class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


""" 
Construct the following tree
           1
         /   \
        /     \
       2       3
      /      /   \
     /      /     \
    4      5       6
          / \
         /   \
        7     8
"""

Tree = Node(1)
Tree.left = Node(2)
Tree.right = Node(3)
Tree.left.left = Node(4)
Tree.right.left = Node(5)
Tree.right.right = Node(6)
Tree.right.left.left = Node(7)
Tree.right.left.right = Node(8)
