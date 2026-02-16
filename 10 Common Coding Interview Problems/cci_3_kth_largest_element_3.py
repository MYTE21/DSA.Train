"""
Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]

        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2)) # 5
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
    print(s.findKthLargest([1], 1)) # 1
