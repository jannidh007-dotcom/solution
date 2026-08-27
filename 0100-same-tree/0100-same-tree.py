# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        # If one node is empty or values are different
        if p is None or q is None or p.val != q.val:
            return False

        # Check left and right subtrees
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna