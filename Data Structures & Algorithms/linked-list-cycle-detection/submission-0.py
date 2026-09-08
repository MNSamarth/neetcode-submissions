# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head and head.next and head.next.next:
            slow=head.next
            fast=head.next.next
            while(fast):
                if slow==fast:
                    return True
                if slow.next:
                    slow=slow.next
                else:
                    break
                if fast.next and fast.next.next:
                    fast=fast.next.next
                else:
                    break
        return False