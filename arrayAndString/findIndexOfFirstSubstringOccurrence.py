# TODO: KMP algorithm


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            matching = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    matching = False
                    break
            if matching:
                return i
        return -1
