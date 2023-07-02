"""
Solution: Using two nested-loops.
Time Complexity: O(n^2).
Space Complexity: O(1)
"""
from typing import List


def maximum_gap(num_list: List[int]) -> int:
    max_gap = 0

    for i in range(len(num_list) - 1):
        num_x = num_list[i]
        for j in range(i + 1, len(num_list)):
            num_y = num_list[j]
            if num_x <= num_y and max_gap < j - i:
                max_gap = j - i

    return max_gap


if __name__ == "__main__":
    nums = [3, 5, 4, 2]
    print(maximum_gap(nums))
