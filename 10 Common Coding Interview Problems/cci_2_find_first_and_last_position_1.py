"""
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = -1
        last_index = -1

        for i in range(len(nums)):
            if nums[i] == target:
                first_index = i
                break

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == target:
                last_index = i
                break

        if first_index != -1 and last_index == -1:
            return [first_index, first_index]

        return [first_index, last_index]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8)) # [3,4]
    print(s.searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
