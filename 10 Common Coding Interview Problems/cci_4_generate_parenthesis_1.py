"""
Problem Link: https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []
        self.rec(2 * n, 0, [], combs)
        return combs

    def rec(self, n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append("".join(comb))
        else:
            comb.append("(")
            self.rec(n-1, diff+1, comb, combs)
            comb.pop()
            comb.append(")")
            self.rec(n-1, diff-1, comb, combs)
            comb.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(1)) # ["()"]
