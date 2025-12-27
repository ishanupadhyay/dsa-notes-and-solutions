from .node import Node

def insertNodeAtEnd(head, node):
    # If the linked list is empty, set the new node as the head
    if head is None:
        head = node
        return head
    curr = head
    # Traverse to the end of the linked list
    while curr.next:
        curr = curr.next  
    curr.next = node

    return head

node1 = Node(1)
node2 = node1.next = Node(2)
node3 = node2.next = Node(3)
node4 = node3.next = Node(4)
new_head = insertNodeAtEnd(node1, Node(5))
