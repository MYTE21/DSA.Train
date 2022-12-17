"""
    LeetCode
    - 59. Spiral Matrix II
    - Problem Link: https://leetcode.com/problems/spiral-matrix-ii/
"""
from typing import List


def square_spiral(n: int) -> List[List[int]]:
    left, right, top, bottom = 0, n - 1, 0, n - 1
    direction_list = ['left to right', 'top to bottom', 'right to left', 'bottom to top']
    direction_index = 0
    direction = direction_list[direction_index]
    incrementer = 1
    # Initial result list
    result = [[0]*n for i in range(n)]      # FIXME: Why [[]*n]*n is not working instead of it.

    while top <= bottom and left <= right:
        if direction == 'left to right':
            for i in range(left, right + 1):
                result[top][i] = incrementer
                incrementer += 1
            top += 1
        elif direction == 'top to bottom':
            for i in range(top, bottom + 1):
                result[i][right] = incrementer
                incrementer += 1
            right -= 1
        elif direction == 'right to left':
            for i in range(right, left - 1, -1):
                result[bottom][i] = incrementer
                incrementer += 1
            bottom -= 1
        else:       # direction == 'bottom to top'
            for i in range(bottom, top - 1, -1):
                result[i][left] = incrementer
                incrementer += 1
            left += 1

        direction_index = (direction_index + 1) % 4
        direction = direction_list[direction_index]

    return result


if __name__ == "__main__":
    for n in range(1, 5):
        print(square_spiral(n))