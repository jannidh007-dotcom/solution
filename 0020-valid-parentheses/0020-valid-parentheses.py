class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')    
            elif i == '[':
                stack.append(']')
            else:
                if not stack or stack.pop()!=i:
                    return False    
        return len(stack)==0

s=Solution()
t=s.isValid("(]")                   


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna