'''Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        r=0
        while x >0:
            s=x%10
            r=r*10+s
            x=int(x/10)
        if n == r:
            return True
        else:
            return False
        
