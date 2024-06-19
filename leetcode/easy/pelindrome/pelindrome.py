class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return 0 if x is negative
        if x<0:
            return False
    
        # reverse the number base
        rev = 0
        y=x
        while x!=0: # run till x get zero
            rev = (rev * 10) + x%10
            x //= 10
        return rev==y
