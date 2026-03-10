"""
This is O(2^n) solution only using recursion.

Only Recursion Solution:

Time complexity (worst-case): O(2^n)
    Each call branches into two recursive calls: calculate(n-1) and calculate(n-2),
    producing an exponential recursion tree similar to Fibonacci.

Time complexity (best/average): O(2^n)
    There is no input variation that reduces the recursion tree because
    no memoization is used. The same subproblems are recomputed repeatedly.

Space complexity (extra): O(n)
    Due to the recursion call stack. The maximum depth of recursion is n.
 """
class Solution:
    def calculate(self, num: int):
        if num <= 2:
            return num

        return self.calculate(num - 1) + self.calculate(num - 2)

    def climbStairs(self, n: int) -> int:
        return self.calculate(n)


if __name__ == "__main__":
    solution = Solution()

    try:
        assert solution.climbStairs(2) == 2, "⚠️ Test 1 Failed: For 2 steps, there should be 2 ways to climb!"
        assert solution.climbStairs(3) == 3, "⚠️ Test 2 Failed: For 3 steps, there should be 3 ways to climb!"
        assert solution.climbStairs(44) == 1134903170, "⚠️ Test 3 Failed: For 44 steps, there should be 1134903170 ways to climb!"
        print("✅ All tests passed!")
    except AssertionError as e:
        print(f"❌ Test Failed: \n{e}")
