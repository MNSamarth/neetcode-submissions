# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
        list3=ListNode()
        current3=list3
        while(current1 and current2):
            if current1.val<=current2.val:
                temp_node=ListNode(current1.val,None)
                current3.next=temp_node
                current1=current1.next
            else:
                temp_node=ListNode(current2.val,None)
                current3.next=temp_node
                current2=current2.next
            current3=current3.next
        # while(current1):
        #     temp_node=ListNode(current1.val,None)
        #     current3.next=temp_node
        #     current1=current1.next
        #     current3=current3.next
        # while(current2):
        #     temp_node=ListNode(current2.val,None)
        #     current3.next=temp_node
        #     current2=current2.next
        #     current3=current3.next
        #This can be replaced in one line by linking the node itself
        current3.next=current1 if current1 else current2
        return list3.next