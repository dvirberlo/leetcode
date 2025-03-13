class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = start = 0
        map = [-1] * 128
        for i, c in enumerate(s):
            c_code = ord(c)
            start = max(map[c_code] + 1, start)
            if i - start + 1 > maxLen:
                maxLen = i - start + 1
            map[c_code] = i
        return maxLen
