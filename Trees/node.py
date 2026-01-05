class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.val})"
