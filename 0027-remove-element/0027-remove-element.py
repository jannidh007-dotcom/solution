class Solution(object):
    def removeElement(self, nums, val):
        k=0
        while val in nums:
            nums.remove(val)
        return len(nums)       
s=Solution()                

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna