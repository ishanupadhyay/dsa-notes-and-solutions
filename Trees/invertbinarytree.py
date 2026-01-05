from .node import Node
def invert_binary_tree(root: Node) -> Node:
    if root is None:
        return None
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root
