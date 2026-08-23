class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        a=1
        b=2    
        for i in range(3,n+1):    
            ways=a+b
            a=b
            b=ways
        return b           
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna