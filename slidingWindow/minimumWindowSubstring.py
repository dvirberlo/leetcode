from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounting = defaultdict(int)
        for c in t:
            tCounting[c] += 1
        n = len(s)
        shortestStart, shortestLen = 0, n + 1
        counting = defaultdict(int)
        start, stop = 0, 0
        while start <= stop < n:
            while not self.countingEquals(counting, tCounting) and stop < n:
                print(start, stop)
                c = s[stop]
                # if c in tCounting:
                counting[c] += 1
                stop += 1
            while self.countingEquals(counting, tCounting) and start < stop:
                print(start, stop)
                if stop - start < shortestLen:
                    shortestStart, shortestLen = start, stop - start
                # print(start, stop - start, s[start:stop])
                c = s[start]
                # if c in tCounting:
                counting[c] -= 1
                start += 1
        return (
            s[shortestStart : shortestStart + shortestLen] if shortestLen <= n else ""
        )

    def countingEquals(self, counting: defaultdict, tCounting: defaultdict) -> bool:
        for c in tCounting:
            if counting[c] < tCounting[c]:
                return False
        return True
