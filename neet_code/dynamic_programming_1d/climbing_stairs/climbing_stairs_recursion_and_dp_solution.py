"""
This is O(n) solution using recursion and memoization (DP).
"""
class Solution:
    def __init__(self):
        self.memo = {}

    def calculate(self, num: int):
        if num <= 2:
            return num

        if num in self.memo:
            return self.memo[num]

        self.memo[num] = self.calculate(num -1) + self.calculate(num - 2)

        return self.memo[num]

    def climbStairs(self, n: int) -> int:
        return self.calculate(n)


if __name__ == "__main__":
    solution = Solution()

    steps = 2
    print(f"For {steps} steps, there are {solution.climbStairs(steps)} ways to climb!") # output: 2

    steps = 3
    print(f"For {steps} steps, there are {solution.climbStairs(steps)} ways to climb!") # output: 3

    steps = 44
    print(f"For {steps} steps, there are {solution.climbStairs(steps)} ways to climb!") # output: 1134903170
