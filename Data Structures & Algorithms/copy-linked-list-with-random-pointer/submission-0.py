"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        old_to_new = {}

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copied = old_to_new[current]
            if current.next:
                copied.next = old_to_new[current.next]

            if current.random:
                copied.random = old_to_new[current.random]

            current = current.next

        if head:
            return old_to_new[head]

            

        

        