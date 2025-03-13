class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        counts = [0 for _ in range(n + 1)]
        for citation in citations:
            counts[min(citation, n)] += 1

        for i in reversed(range(n)):
            counts[i] += counts[i + 1]

        h = n
        while counts[h] < h:
            h -= 1
        return h
