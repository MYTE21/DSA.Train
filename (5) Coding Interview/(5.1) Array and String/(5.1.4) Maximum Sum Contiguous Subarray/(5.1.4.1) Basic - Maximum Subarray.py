"""
Solution: Brute Force.
Time Complexity: O(n^2).
Space Complexity: O(1).
"""
from typing import List


def maximum_subarray(nums: List[int]) -> int:
    max_sum = float("-inf")

    for i in range(len(nums)):
        if nums[i] > max_sum:
            max_sum = nums[i]
        current_sum = nums[i]
        for j in range(i + 1, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


if __name__ == "__main__":
    numbers = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],    # 6
        [1],                                # 1
        [5, 4, -1, 7, 8],                   # 23
        [-1, -2, 1, 2, 3, -5, 4],           # 6
        [-1, -2, 1, 2, 3, -5, 4, 5]         # 10
    ]

    for items in numbers:
        print(maximum_subarray(items))
