class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        result = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

    def insert2(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        i = 0
        while i < len(intervals) and intervals[i][0] <= newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)
        i = 0
        while i < len(intervals):
            if i + 1 < len(intervals) and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals
