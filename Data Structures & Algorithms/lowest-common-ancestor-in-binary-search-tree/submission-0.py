# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {root: None}

        que = deque([root])

        # Build parent relationships
        while que:
            node = que.popleft()

            if node.left:
                parent[node.left] = node
                que.append(node.left)

            if node.right:
                parent[node.right] = node
                que.append(node.right)

        # Store p and all of its ancestors
        ancestors = set()

        current = p

        while current:
            ancestors.add(current)
            current = parent[current]

        # Move q upward until we hit
        # something in p's ancestor chain
        current = q

        while current not in ancestors:
            current = parent[current]

        return current