"""
Problem Link: https://leetcode.com/problems/symmetric-tree/description/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.are_symmetric(root.left, root.right)


    def are_symmetric(self, root_1, root_2):
        if root_1 is None and root_2 is None:
            return True
        elif ((root_1 is None) != (root_2 is None)) or root_1.val != root_2.val:
            return False
        else:
            return self.are_symmetric(root_1.left, root_2.right) and self.are_symmetric(root_1.right, root_2.left)


if __name__ == "__main__":
    pass
