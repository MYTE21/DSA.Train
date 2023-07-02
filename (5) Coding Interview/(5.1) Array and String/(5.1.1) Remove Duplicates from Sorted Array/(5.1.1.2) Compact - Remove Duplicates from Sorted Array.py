"""
Solution: Using 'set'
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return len(unique_nums)


if __name__ == "__main__":
    numbers_list = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]

    for numbers in numbers_list:
        ans = remove_duplicates(numbers)
        print("Ans:", ans)
