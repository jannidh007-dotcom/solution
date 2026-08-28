# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def build(left, right):
            
            # Base case
            if left > right:
                return None
            
            # Find middle element
            mid = (left + right) // 2
            
            # Make middle element the root
            root = TreeNode(nums[mid])
            
            # Build left subtree
            root.left = build(left, mid - 1)
            
            # Build right subtree
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna