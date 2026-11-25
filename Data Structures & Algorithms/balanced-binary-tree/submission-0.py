# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        return self.dfs(root) != -1

    def dfs(self, node):
        if not node:
            return 0

        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
            return -1
        
        return 1 + max(left_height, right_height)



