class Solution(object):
    def plusOne(self, digits):
        result=int("".join(map(str,digits)))
        s=result+1
        t=list(map(int,str(s)))
        return t
        
s=Solution()        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna