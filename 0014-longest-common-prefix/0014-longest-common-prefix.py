class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=strs[0]
        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix=prefix[:-1]
        return prefix        
        
s=Solution()
t=s.longestCommonPrefix(['flower,flow,flight'])
print(t)                   
    

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna