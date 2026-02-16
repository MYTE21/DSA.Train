# Using Stack
"""
Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Stack Solution (traversing the array only once):
    Time complexity (worst-case): ...
        Reason: ...
    Space complexity (extra): ...
        Reason: ...
"""


class Solution:
    @staticmethod
    def largest_rectangle_area(heights: list[int]) -> int:
        heights = [-1] + heights + [-1]
        max_area = 0
        stack = [(0, -1)]

        for i in range(1, len(heights)):
            start = i

            while (
                stack[-1][1] > heights[i]
            ):  # stack[-1][1]: height of the bar on top of stack
                top_index, top_height = stack.pop()
                max_area = max(max_area, top_height * (i - top_index))
                start = top_index

            stack.append((start, heights[i]))

        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # 10
    print(s.largest_rectangle_area([2, 4]))  # 4
