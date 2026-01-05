from .node import Node

def postorder_traversal(root:Node) -> list:
    result = []
    def traverse(node):
        if node is None:
            return None
        
        result.append(node.val)
        traverse(node.right)
        traverse(node.left)
    
    traverse(root)
    
    return result

#Post order traversal is used for deleting tree / evaluate expressions