"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        is_even = len(nums3) % 2 == 0
        median = len(nums3) // 2
        return (
            (nums3[median] + nums3[median - 1]) / 2 if is_even else nums3[median]
        )


a = Solution()
print(a.findMedianSortedArrays([1, 3], [2, 4]))
print(a.findMedianSortedArrays([1, 3], [2]))
print(a.findMedianSortedArrays([1, 3], [2, 5, 4]))
print(a.findMedianSortedArrays([1, 3, 6], [2, 5, 4]))
print(a.findMedianSortedArrays([], [1]))
print(a.findMedianSortedArrays([0], []))
