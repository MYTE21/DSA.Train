class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s, freq_t = {}, {}

        for ch in s:
            if ch in freq_s:
                freq_s[ch] += 1
            else:
                freq_s[ch] = 1

        for ch in t:
            if ch in freq_t:
                freq_t[ch] += 1

            else:
                freq_t[ch] = 1

        for key in freq_s:
            if key not in freq_t or freq_s[key] != freq_t[key]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram")) # True
    print(s.isAnagram("rat", "car")) # False
    print(s.isAnagram("aacc", "ccac")) # False