"""
Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Divide and Conquer Solution:
    Time complexity (worst-case): O(n^2)
        Reason: each call scans the current subarray to find the minimum (the code does min(heights[low:high+1])
        and index), i.e. O(m) work per call. Recurrence T(n) = T(k) + T(n-k-1) + O(n). If the minimum is always
        at one end (highly unbalanced split) this becomes T(n)=T(n-1)+O(n) → O(n^2).
    Time complexity (best/average, balanced splits): O(n log n)
        Reason: if the minimum splits roughly in half each time, T(n)=2T(n/2)+O(n) → O(n log n).
    Space complexity (extra): O(n) worst-case
        Reason: recursion depth can be O(n) in the worst case. Also, the slice in min(heights[low:high+1])
        produces a temporary list of size O(n) (can be avoided by scanning indices directly).
"""


class Solution:
    def largest_rectangle_area(self,heights: list[int]) -> int:
        return self.rectangle(heights, 0, len(heights)-1)

    def rectangle(self, heights, low, high):
        if low > high:
            return 0
        elif low == high:
            return heights[low]
        else:
            minh = min(heights[low:high+1])
            pos_min = heights.index(minh, low, high+1)
            from_left = self.rectangle(heights, low, pos_min-1)
            from_right = self.rectangle(heights, pos_min+1, high)
            return max(minh*(high-low+1), from_left, from_right)


if __name__ == "__main__":
    s = Solution()
    print(s.largest_rectangle_area([2,1,5,6,2,3])) # 10
    print(s.largest_rectangle_area([2,4])) # 4
