class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram")) # True
    print(s.isAnagram("rat", "car")) # False
    print(s.isAnagram("aacc", "ccac")) # False