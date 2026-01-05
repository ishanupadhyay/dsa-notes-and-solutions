#Level order traversal = BFS = Queue
#Real life analogy
#Imagine people standing in a line for a bus
#First person enters
#Then the people that person invited
#Then the people they invited
#Therefore it is first come first serve (queue)

from .node import Node
from collections import deque

def levelorder_traversal(root:Node) -> list:
    result = []

    if root is None:
        return []
    
    q = deque([root])

    while q:
        current = q.popleft()
        result.append(current.val)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return result
