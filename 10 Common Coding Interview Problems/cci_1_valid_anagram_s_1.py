"""
Problem Link: https://neetcode.io/problems/is-anagram/question?list=blind75
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram")) # True
    print(s.isAnagram("rat", "car")) # False
    print(s.isAnagram("aacc", "ccac")) # False

