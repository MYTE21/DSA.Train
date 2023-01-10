""" LeetCode
    Difficulty: Medium
    - 54. Spiral Matrix
    - Problem Link: https://leetcode.com/problems/spiral-matrix/
"""
from typing import List  # Type hinting -> List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])
    if m == 0:
        return []

    left, right, top, bottom = 0, n - 1, 0, m - 1
    direction_list = ['left to right', 'top to bottom', 'right to left', 'bottom to top']
    direction_index = 0
    direction = direction_list[0]
    result = []

    while top <= bottom and left <= right:
        if direction == 'left to right':
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif direction == 'top to bottom':
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif direction == 'right to left':
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        else:       # direction == 'bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        direction_index = (direction_index + 1) % 4
        direction = direction_list[direction_index]

    return result


if __name__ == "__main__":
    original_matrix = [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [2, 5],
            [8, 4],
            [0, -1]
        ]
    ]

    for om in original_matrix:
        print(spiral_order(om))
