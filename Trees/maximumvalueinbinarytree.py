from .node import Node

def max_value_in_binary_tree(root: Node):

    maxvalue = [float('-inf')]

    def traverse(node):
        if node is None:
            return None
        
        maxvalue[0] = max(maxvalue[0], node.val)
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    return maxvalue[0]
