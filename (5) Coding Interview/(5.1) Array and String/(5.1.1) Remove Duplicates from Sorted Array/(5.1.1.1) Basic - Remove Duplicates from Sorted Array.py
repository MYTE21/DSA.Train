"""
Solution: Using an extra array.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    unique_nums = [nums[0]]

    n = len(nums)
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            unique_nums.append(nums[i])

    return len(unique_nums)


if __name__ == "__main__":
    numbers_list = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]

    for numbers in numbers_list:
        ans = remove_duplicates(numbers)
        print("Ans:", ans)
