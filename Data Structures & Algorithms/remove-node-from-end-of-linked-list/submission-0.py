# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        current=head
        while(current):
            size+=1
            current=current.next
        
        if size == n:
            return head.next
        
        current=head
        i=0
        prev=ListNode()
        while(i<(size-n) and current):
            prev=current
            current=current.next
            i+=1
        
        prev.next=current.next
        return head