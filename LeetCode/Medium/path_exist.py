# Definition for a binary tree node.
from typing import List

# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root is None:
            return len(arr) is 0
        return self.rec(root, arr, 0)

    def rec(self, node: TreeNode, arr: List[int], index) -> bool:
        if node.val != arr[index]:
            return False

        if index == len(arr) - 1:
            return node.left is None and node.right is None

        if node.left is not None and self.rec(node.left, arr, index + 1):
            return True
        if node.right is not None and self.rec(node.right, arr, index + 1):
            return True

        return False
