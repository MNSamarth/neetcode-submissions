# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}

        for i, value in enumerate(inorder):
            inorder_index[value] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            # Next preorder value is the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find root position in inorder in O(1)
            mid = inorder_index[root_value]

            # Everything left of mid belongs to left subtree
            root.left = build(left, mid - 1)

            # Everything right of mid belongs to right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
