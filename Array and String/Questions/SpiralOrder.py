"""
    LeetCode
    - 54. Spiral Matrix
    - Problem Link: https://leetcode.com/problems/spiral-matrix/
"""
from typing import List  # Type hinting -> List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    up, down, right, left = False, False, True, False
    r, c = 0, 1
    count = 1
    rows = len(matrix)
    columns = len(matrix[0])
    total_length = rows * columns
    spiral_list = [matrix[0][0]]
    matrix[0][0] = False

    while True:
        if count == total_length:
            break

        if up:
            if r > -1 and matrix[r][c] != False:
                spiral_list.append(matrix[r][c])
                matrix[r][c] = False
                r -= 1
                count += 1
            else:
                r += 1
                c += 1
                right = True
                up = False

        if down:
            if r < rows and matrix[r][c] != False:
                spiral_list.append(matrix[r][c])
                matrix[r][c] = False
                r += 1
                count += 1
            else:
                r -= 1
                c -= 1
                down = False
                left = True

        if right:
            if c < columns and matrix[r][c] != False:
                spiral_list.append(matrix[r][c])
                matrix[r][c] = False
                c += 1
                count += 1
            else:
                c -= 1
                r += 1
                right = False
                down = True

        if left:
            if c > -1 and matrix[r][c] != False:
                spiral_list.append(matrix[r][c])
                matrix[r][c] = False
                c -= 1
                count += 1
            else:
                c += 1
                r -= 1
                left = False
                up = True

    return spiral_list


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
