# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q=deque()
        q.append([root,root.val])
        good=0
        while(q):
            for _ in range(len(q)):
                node,value=q.popleft()
                if node:
                    if node.left:
                        if node.left.val>=value:
                            good+=1
                        q.append([node.left,max(value,node.left.val)])
                    if node.right:
                        if node.right.val>=value:
                            good+=1
                            value=node.right.val
                        q.append([node.right,max(value,node.right.val)])
        
        return good+1

                    