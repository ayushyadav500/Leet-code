# from itertools import combinations
# arr = [1,2,34,5,56]
# tar = 35
# comb = combinations(arr,2)

# for i in list(comb):
#     if sum(i) == tar:
#         print(i) 
    
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].'''

def twoSum(self, nums: List[int], target: int) -> List[int]:       
    n = len(nums)
    for i in range(0,n-1):        
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                 return i,j
                
            


