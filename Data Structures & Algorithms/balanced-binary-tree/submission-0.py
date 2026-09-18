class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)

            # Left subtree already found an imbalance
            if left_height == -1:
                return -1

            right_height = dfs(node.right)

            # Right subtree already found an imbalance
            if right_height == -1:
                return -1

            # Current node itself is unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            # Current subtree is balanced.
            # Send its height to the parent.
            return 1 + max(left_height, right_height)

        return dfs(root) != -1