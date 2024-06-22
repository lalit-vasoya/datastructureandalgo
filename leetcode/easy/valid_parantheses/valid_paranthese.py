class Solution:
    def isValid(self, s: str) -> bool:
        mapped = {"(": ")", "{":"}", "[":"]"}
        stack = []
    
        for char in s:
            val = mapped.get(char)
            if val:
                stack.append(val)
            elif len(stack)==0 or stack.pop() != char:  # correct order
                return False
    
        return len(stack)==0

