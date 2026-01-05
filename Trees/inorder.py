from .node import Node
def inorder_traversal(root: Node) -> list:
    result = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result

# inorder traversal is used in BST -> gives sorted order.
