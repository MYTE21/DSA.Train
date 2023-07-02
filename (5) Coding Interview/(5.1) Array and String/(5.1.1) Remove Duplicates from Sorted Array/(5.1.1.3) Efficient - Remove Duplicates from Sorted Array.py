"""
Solution: Without using extra memory.
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    count = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[count] = nums[i + 1]
            count += 1

    return count


if __name__ == "__main__":
    numbers_list = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]

    for numbers in numbers_list:
        ans = remove_duplicates(numbers)
        print("Ans:", ans)
