from .node import Node

def findMiddle(node):
    head = node
    # Handle edge case for empty list
    if head is None:
        return
    slow = head
    fast = head
    #  Move fast pointer two steps and slow pointer one step until fast reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # When fast pointer reaches the end, slow pointer will be at the middle
    return slow

node1 = Node(1)
node2 = node1.next = Node(2)
node3 = node2.next = Node(3)
node4 = node3.next = Node(4)

findMiddle(node1)
# The middle node in this case would be the node with value 3
# Time Complexity: O(n)
# Space Complexity: O(1)
