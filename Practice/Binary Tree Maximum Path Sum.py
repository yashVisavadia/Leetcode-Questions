# Definition for a binary tree node.
from sys import maxsize
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self, maxi = -1001):
    #     self.maxi = maxi

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [-maxsize]

        def helper(root):
            if not root:
                return 0

            ls = max(0, helper(root.left))
            rs = max(0, helper(root.right))
            maxi[0] = max(maxi[0], ls + rs + root.val)

            return root.val + max(ls, rs)

        helper(root)
        return maxi[0]
