from collections import defaultdict
from typing import Iterator


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result: list[int] = []
        wordsSet = set(words)
        wordsCount, wordLen = len(words), len(words[0])
        # store occurrences of each word in `words` array
        correctCounts: dict[str, int] = defaultdict(int)
        for w in words:
            correctCounts[w] += 1

        # m + m\cdot 2n = m (1 + 2n) \in O(mn)
        # where `m` is words length, and `n` is string length

        # search for starting indexes with any offset
        for offset in range(wordLen):
            counts: dict[str, int] = defaultdict(int)
            segments = Solution.Segmenter(s, wordLen, offset)
            start = 0
            for i, w in enumerate(segments):
                if w in wordsSet:
                    counts[w] += 1
                    while counts[w] > correctCounts[w]:
                        # too much from this word, move `start` forward and update `count`
                        counts[segments.get(start)] -= 1
                        start += 1
                else:
                    while start < i + 1:
                        # current word not in `wordSet`. move `start` over the current word and update `count`
                        counts[segments.get(start)] -= 1
                        start += 1

                if i + 1 - start == wordsCount:
                    # we got a correct concatenated string. add it to result and step `start` forward
                    result.append(offset + start * wordLen)
                    counts[segments.get(start)] -= 1
                    start += 1
        return result

    class Segmenter:
        """splits a given string `s` into segments of length `size`, starting from the given `offset`"""

        def __init__(self, s: str, size: int, offset=0):
            self.s = s
            self.size = size
            self.offset = offset

        def get(self, i: int) -> str:
            return self.s[
                self.offset + i * self.size : self.offset + (i + 1) * self.size
            ]

        def __iter__(self) -> Iterator[str]:
            for i in range((len(self.s) - self.offset) // self.size):
                yield self.get(i)

    def findSubstring2(self, s: str, words: list[str]) -> list[int]:
        result: list[int] = []
        k, m, n = len(words), len(words[0]), len(s)
        lastSeen: dict[str, int] = dict((w, -1) for w in words)
        segments = Solution.Segmenter(s, m)
        start = 0
        for i, w in enumerate(segments):
            if w in lastSeen:
                seen = lastSeen[w]
                if seen >= start:
                    start = seen + 1
                lastSeen[w] = i
            else:
                start = i + 1

            if i + 1 - start == k:
                result.append(start * m)
                start += 1
        return result
