from .node import Node

def preorder_traversal(root: Node) -> list:
    result = []
    def traverse(node):
        if node is None:
            return None
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    return result

# preorder traversal is used for copying tree / serialize