# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(root):
            if root:
                ans.append(root.val)
                if root.left:
                    helper(root.left)
                if root.right:
                    helper(root.right)
        helper(root)
        return ans
