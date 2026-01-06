# max depth
from .node import Node

def height_of_binary_tree(root: Node):

    height = [0]

    def traverse(node):
        if node is None:
            return 0
        
        left = traverse(node.left)
        right = traverse(node.right)
        height[0] = max(left, right) + 1
        return height[0]
    
    traverse(root)
    return height[0]
