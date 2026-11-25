# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 

        self.dfs(root)

        return self.max_diameter

    def dfs(self, node):
        if not node:
            return 0

        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        current_diameter = left_height + right_height
        self.max_diameter = max(current_diameter, self.max_diameter)

        return 1 + max(left_height, right_height)