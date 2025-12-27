from .node import Node

def pallindrome_linked_list(node):
    """
    Check if a linked list is a palindrome.

    Args:
        head (Node): The head node of the linked list.
    Returns:
        bool: True if the linked list is a palindrome, False otherwise.
    """
    # Handle empty list
    if node is None:
        return True
    
    # Handle single node
    if node.next is None:
        return True
    
    # Handle two nodes
    if node.next.next is None:
        return node.val == node.next.val
    
    # Find middle
    middle = find_middle(node)
    
    # If middle is None (shouldn't happen except for empty list), it's a palindrome
    if middle is None:
        return True
    
    # Reverse second half
    reversed_second_half = reverse_ll(middle.next)
    
    # Compare both halves
    first_half = node
    while reversed_second_half:
        if first_half.val != reversed_second_half.val:
            return False
        reversed_second_half = reversed_second_half.next
        first_half = first_half.next
    
    # If we got here, all comparisons passed, so it's a palindrome
    return True


def find_middle(node):
    # Handle empty list
    if node is None:
        return None
    
    head = node
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def reverse_ll(node):
    # Handle empty list
    if node is None:
        return None
    
    head = node
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# Test example (can be removed in production)
if __name__ == "__main__":
    node1 = Node(1)
    node2 = node1.next = Node(2)
    node3 = node2.next = Node(3)
    node4 = node3.next = Node(2)
    node5 = node4.next = Node(1)
    print(pallindrome_linked_list(node1))  # True
