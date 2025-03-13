class Solution:
    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        print(intervals)
        i = 0
        while i < len(intervals):
            if i + 1 < len(intervals) and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        starts, ends = sorted(i[0] for i in intervals), sorted(i[1] for i in intervals)
        result = []
        a = 0
        for b in range(n):
            if b + 1 >= n or starts[b + 1] > ends[b]:
                result.append([starts[a], ends[b]])
                a = b + 1
        return result
