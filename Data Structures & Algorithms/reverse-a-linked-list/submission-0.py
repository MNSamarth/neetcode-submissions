# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prev=None
        while(current):
            if prev:
                temp_node=ListNode(current.val,prev)
                prev=temp_node
            else:
                prev=ListNode(current.val,None)
            current=current.next
        return prev
            
