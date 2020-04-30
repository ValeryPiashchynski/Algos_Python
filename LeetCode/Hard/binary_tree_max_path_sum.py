class Solution:
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal ms
            if not node:
                return 0
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)

            n = node.val + left + right
            ms = max(ms, n)
            return node.val + max(left, right)

        ms = float('-inf')
        max_gain(root)
        return ms