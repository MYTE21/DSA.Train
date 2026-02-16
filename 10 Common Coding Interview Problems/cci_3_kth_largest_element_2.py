"""
Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k-1):
            nums.remove(max(nums))
        return max(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2)) # 5
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
    print(s.findKthLargest([1], 1)) # 1
