"""
Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Base Solution:
    Time complexity (worst-case): O(n^2)
        Reason: for each index i the left and right while-loops can each scan up to O(n) elements,
        producing quadratic work in the worst case (e.g., all heights equal).
    Space complexity (extra): O(1)
"""


class Solution:
    @staticmethod
    def largest_rectangle_area(heights: list[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            left = i
            while left-1 >= 0 and heights[left-1] >= heights[i]:
                left -= 1

            right = i
            while right+1 < len(heights) and heights[right+1] >= heights[i]:
                right += 1

            max_area = max(max_area, (right-left+1)*heights[i])


        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.largest_rectangle_area([2,1,5,6,2,3])) # 10
    print(s.largest_rectangle_area([2,4])) # 4
