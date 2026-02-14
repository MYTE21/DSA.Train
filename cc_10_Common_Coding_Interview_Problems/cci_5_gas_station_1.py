"""
Problem Link: https://leetcode.com/problems/gas-station/description/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if self.can_traverse(gas, cost, i):
                return i
        return -1


    def can_traverse(self, gas, cost, start):
        n = len(gas)
        remaining = 0
        i = start
        started = False

        while i != start or not started:
            started = True
            remaining += gas[i] - cost[i]

            if remaining < 0:
                return False

            i = (i + 1) % n

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
    print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1
