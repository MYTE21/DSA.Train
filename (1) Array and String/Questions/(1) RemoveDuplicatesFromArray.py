""" LeetCode
    Difficulty: Easy
    - 26. Remove Duplicates from Sorted Array
    - Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List  # Type hinting -> List


def remove_duplicates(nums: List[int]) -> int:
    count = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[count] = nums[i+1]
            count += 1

    return count


if __name__ == "__main__":
    numbers = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]
    for num in numbers:
        print(remove_duplicates(num))
