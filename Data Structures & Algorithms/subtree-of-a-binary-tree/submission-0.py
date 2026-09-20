# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            que1=deque()
            que2=deque()
            que1.append(p)
            que2.append(q)
            while(que1 and que2):
                node1=que1.popleft()
                node2=que2.popleft()
                if node1 and not node2:
                    return False
                if node2 and not node1:
                    return False
                if node1 and node2:
                    if node1.val!=node2.val:
                        return False
                    que1.append(node1.left)
                    que1.append(node1.right)
                    que2.append(node2.left)
                    que2.append(node2.right)
            
            return True

        q=deque()
        q.append(root)
        while(q):
            node=q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            if node and node.val==subRoot.val:
                if check(node,subRoot):
                    return True
                

        return False