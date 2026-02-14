"""
Problem Link: https://leetcode.com/problems/gas-station/description/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remaining, candidate = 0, 0

        for i in range(len(gas)):
            remaining += gas[i] - cost[i]
            if remaining < 0:
                candidate = i + 1
                remaining = 0

        prev_remaining = sum(gas[:candidate]) - sum(cost[:candidate])

        if candidate == len(gas) or remaining + prev_remaining < 0:
            return -1

        return candidate


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
    print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1
