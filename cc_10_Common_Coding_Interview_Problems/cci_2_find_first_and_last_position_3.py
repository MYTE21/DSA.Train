"""
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Solution with Binary Search
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        first_index = self.find_start(nums, target)
        last_index = self.find_end(nums, target)

        return [first_index, last_index]

    def find_start(self, arr, target):
        if arr[0] == target:
            return 0

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target and arr[mid - 1] < target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def find_end(self, arr, target):
        if arr[-1] == target:
            return len(arr) - 1

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target and arr[mid + 1] > target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8)) # [3,4]
    print(s.searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
    print(s.searchRange([1], 1)) # [0, 0]
