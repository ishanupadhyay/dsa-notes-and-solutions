# Circle detection in linked list using Floyd's Cycle Detection Algorithm
#from .node import Node

def has_cycle(head):
    """
    Detects if there is a cycle in the linked list using slow and fast pointers.
    
    Args:
        head: The head node of the linked list
        
    Returns:
        bool: True if a cycle is detected, False otherwise
    """
    if head is None:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
