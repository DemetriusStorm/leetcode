"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index, first_num in enumerate(nums):
            temp_index = first_index
            for second_index, second_num in enumerate(nums):
                if second_index == temp_index or nums[temp_index] + nums[second_index] != target:
                    continue
                return [temp_index, second_index]


a = Solution()
print(a.twoSum([2, 3, 4], 6))  # [0, 2]
print(a.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(a.twoSum([3, 2, 4], 6))  # [1, 2]
print(a.twoSum([3, 3], 6))  # [0, 1]
