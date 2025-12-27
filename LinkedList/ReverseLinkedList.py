from .node import Node

def reverse_linked_list(node):
    prev = None
    head = node
    curr = head
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

node1 = Node(1)
node2 = node1.next = Node(2)
node3 = node2.next = Node(3)
node4 = node3.next = Node(4)
node5 = node4.next = Node(5)
reversed_head = reverse_linked_list(node1)
