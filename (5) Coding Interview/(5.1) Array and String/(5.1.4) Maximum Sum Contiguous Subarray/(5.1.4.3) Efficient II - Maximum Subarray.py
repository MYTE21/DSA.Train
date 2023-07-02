"""
Solution: Using only one loop and max method.
Time Complexity: O(n).
Space Complexity: O(1).
"""
from typing import List


def maximum_subarray(nums: List[int]) -> int:
    max_sum = float("-inf")
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

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