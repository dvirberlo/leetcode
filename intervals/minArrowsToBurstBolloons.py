class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        count, last = 0, [1, 0]
        for p in points:
            last = [max(last[0], p[0]), min(last[1], p[1])]
            if last[0] > last[1]:
                count += 1
                last = p
        return count

    def intersection(
        self, a: list[int] | None, b: list[int] | None
    ) -> list[int] | None:
        if a == None or b == None:
            return None
        c = [max(a[0], b[0]), min(a[1], b[1])]
        return c if c[0] <= c[1] else None
