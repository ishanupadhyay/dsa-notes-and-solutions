from node import Node

def traveselinkedlist(node):
    head = node
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    return

node1 = Node(1)
node2 = node1.next = Node(2)
node3 = node2.next = Node(3)
node4 = node3.next = Node(4)

traveselinkedlist(node1)
