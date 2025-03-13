from typing import Iterator


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines: list[str] = []
        n = len(words)
        i = 0
        while i < n:
            currentWidth = -1
            line = []
            while i < n and currentWidth + 1 + len(words[i]) <= maxWidth:
                line.append(words[i])
                currentWidth += 1 + len(words[i])
                i += 1

            if i == n:
                lines.append(" ".join(line) + " " * (maxWidth - currentWidth))
            else:
                lines.append(self.paddedJoin(line, currentWidth, maxWidth))
        return lines

    def paddedJoin(self, line: list[str], currentWidth: int, maxWidth: int) -> str:
        str = line[0]
        padTotal = maxWidth - currentWidth
        wordsCount = len(line)
        if wordsCount <= 1:
            return str + " " * padTotal
        for i, p in self.padding(padTotal, wordsCount - 1):
            str += " " * (p + 1) + line[i + 1]
        return str

    def padding(self, total: int, count: int) -> Iterator[tuple[int, int]]:
        p = total // count
        plusOne = total - count * p
        for i in range(count):
            if i < plusOne:
                yield i, p + 1
            else:
                yield i, p
