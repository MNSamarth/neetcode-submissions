# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i,n1=0,0
        while(l1):
            n1+=l1.val*(10**i)
            l1=l1.next
            i+=1
        
        j,n2=0,0
        while(l2):
            n2+=l2.val*(10**j)
            l2=l2.next
            j+=1
        
        sum=n1+n2
        head=ListNode(0)
        current=head

        if sum==0:
            return head

        while(sum):
            temp=ListNode(sum%10)
            current.next=temp
            sum=sum//10
            current=current.next
        
        return head.next
