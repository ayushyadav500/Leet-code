'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

New Addition : Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''
import numpy as np
from itertools import combinations
class Solution:
    def fourSum(self, nums,fsum):
        out = []
        s = sorted(nums)
        c = combinations(s,4)
        #print(len(s))
        # unq = set(c)
        for i in list(c):
            if sum(i) == fsum:
                out.append(list(i))
                print(out)
            
                            
            
                
obj = Solution()
val = obj.fourSum([1,0,-1,0,-2,2],0)
