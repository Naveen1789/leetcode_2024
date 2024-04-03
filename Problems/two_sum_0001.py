'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

# Sort and search
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       sorted_nums = sorted(nums)
       left = 0
       right = len(nums) - 1

       while (left < right):
           sum = sorted_nums[left] + sorted_nums[right]
           if sum == target:
               i = nums.index(sorted_nums[left])
               nums.pop(i)
               j = nums.index(sorted_nums[right])
               if (i <= j):
                   return [i, j+1]
               else:
                   return [i,j]
           elif sum < target:
               left = left + 1
           else:
                right = right - 1

# Brute force
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        dict={}
#        len_of_nums = len(nums)
#        for i in range (len_of_nums - 1):
#            temp = nums[i]
#            for j in range (i+1, len_of_nums):
#                if (temp + nums[j]) == target:
#                    return [i,j]

# Two-pass Hash Table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        dict={}
#        for i in range (len(nums)):
#            dict[nums[i]]=i #Storing index value as value and value as key
#        for i in range (len(nums)):
#             if target-nums[i] in dict and dict[target-nums[i]]!=i:
#                 return[i,dict[target-nums[i]]]

# One-pass Hash Table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        dict={}
#        for i in range (len(nums)):
#            if target-nums[i] in dict and dict[target-nums[i]]!=i:
#                return [i,dict[target-nums[i]]]
#            dict[nums[i]]=i #Storing index value as value and value as key
