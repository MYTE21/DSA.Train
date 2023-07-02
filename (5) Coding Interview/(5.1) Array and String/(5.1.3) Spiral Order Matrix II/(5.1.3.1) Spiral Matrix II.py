"""
Solution: Traversing matrix.
Time Complexity: O(m x n).
Space Complexity: O(m x n).
"""
from typing import List


def generate_matrix(number: int) -> List[List[int]]:
    if number == 1:
        return [[1]]

    matrix = [[0] * number for _ in range(number)]
    m, n = number, number

    left, right, top, bottom = 0, n - 1, 0, m - 1
    direction_list = ['left to right', 'top to bottom', 'right to left', 'bottom to top']
    direction_index = 0
    direction = direction_list[0]
    item = 1

    while top <= bottom and left <= right:
        if direction == 'left to right':
            for i in range(left, right + 1):
                matrix[top][i] = item
                item += 1
            top += 1
        elif direction == 'top to bottom':
            for i in range(top, bottom + 1):
                matrix[i][right] = item
                item += 1
            right -= 1
        elif direction == 'right to left':
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = item
                item += 1
            bottom -= 1
        else:    # direction == 'bottom to top'
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = item
                item += 1
            left += 1
        direction_index = (direction_index + 1) % 4
        direction = direction_list[direction_index]

    return matrix


if __name__ == "__main__":
    number_list = [3, 1]

    for num in number_list:
        print("Ans: ", generate_matrix(num))
