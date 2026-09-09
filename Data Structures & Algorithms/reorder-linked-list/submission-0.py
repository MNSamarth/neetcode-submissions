# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q=deque()
        current=head
        while(current):
            temp=current.next
            current.next=None
            q.append(current)
            current=temp
        current=head
        i=2
        q.popleft()
        while(q):
            if i%2==0:
                current.next=q.pop()
            else:
                current.next=q.popleft()
            i+=1
            current=current.next