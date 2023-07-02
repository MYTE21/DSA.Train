"""
Solution: Using two separate loops.
Time Complexity: O(n x log n).
Space Complexity: O(n)
"""
from typing import List


def maximum_gap(num_list: List[int]) -> int:
    numbers = []
    for i, num in enumerate(num_list):
        numbers.append((num, i))

    numbers.sort()

    max_gap = 0
    min_number = numbers[0][1]

    for item in numbers:
        num = item[1]
        if num <= min_number:
            min_number = num
        else:
            max_gap = max(max_gap, num - min_number)

    return max_gap


if __name__ == "__main__":
    nums = [3, 5, 4, 2]
    print(maximum_gap(nums))
