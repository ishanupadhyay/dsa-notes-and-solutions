from .node import Node
def insert_at_begin(head, node):
    new_node = node
    new_node.next = head
    head = new_node
    return head

node1 = Node(10)
node2 = node1.next = Node(20)
node3 = node2.next = Node(30)
node4 = node3.next = Node(40)
new_head = insert_at_begin(node1, Node(5))
