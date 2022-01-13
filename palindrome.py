'''Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true'''

class Solution:
    def isPalindrome(self, x):
        a = True
        b = False
        n = x
        r = 0
        while x > 0:
            s = x % 10
            r = 10*r + s
            x = x // 10
        if r == n:
            return a
        else:
            return b
        
num = int(input('Enter'))
obj = Solution()
p = obj.isPalindrome(num)
print(p)