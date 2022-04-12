# https://www.techiedelight.com/sink-nodes-containing-zero-bottom-binary-tree/

from BinaryTree import Node


def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=' ')
    inorder_traversal(node.right)
    
    
def sink(node):
    if node is None:
        return
    if node.left and node.left.data:
        node.data, node.left.data = node.left.data, node.data
        sink(node.left)
    elif node.right and node.right.data:
        node.data, node.right.data = node.right.data, node.data
        sink(node.right)
        

def sink_nodes(root):
    if root is None:
        return
    sink_nodes(root.left)
    sink_nodes(root.right)
    if root.data == 0:
        sink(root)
        
        
if __name__ == '__main__':
    """ Construct the following tree
              0
            /   \
           /     \
          1       0
                /   \
               /     \
              0       2
            /   \
           /     \
          3       4
    """

    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(2)
    root.right.left.left = Node(3)
    root.right.left.right = Node(4)
    
    inorder_traversal(root)
    print()
    sink_nodes(root)
    inorder_traversal(root)
    