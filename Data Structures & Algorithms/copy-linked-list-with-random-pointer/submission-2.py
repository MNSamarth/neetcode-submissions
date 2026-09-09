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
        if not head:
            return None

        lookup={}
        current=head
        while(current):
            lookup[current]=Node(current.val)
            current=current.next
        
        current=head

        while(current):
            copy=lookup[current]

            if current.next:
                copy.next=lookup[current.next]
            
            if current.random:
                copy.random=lookup[current.random]
            
            current=current.next
        
        return lookup[head]