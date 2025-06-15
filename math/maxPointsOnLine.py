from collections import defaultdict
import math


class Solution:
    # def maxPoints(self, points: List[List[int]]) -> int:
    #     if not points:
    #         return 0
    #     result = 1
    #     for p1 in points:
    #         x1, y1 = p1
    #         for p2 in points:
    #             if p1 is p2:
    #                 continue
    #             x2, y2 = p2
    #             count = 2
    #             for p3 in points:
    #                 if p1 is p3 or p2 is p3:
    #                     continue
    #                 x3, y3 = p3
    #                 if (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1) == 0:
    #                     count += 1
    #             result = max(result, count)
    #     return result

    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        counts = defaultdict(lambda: defaultdict(int))
        result = 1
        for i in range(n):
            counts.clear()
            m = 0
            for j in range(i + 1, n):
                u1, u2 = self.uniqueForm(points[i], points[j])
                counts[u1][u2] += 1
                m = max(m, counts[u1][u2])
            result = max(result, m + 1)
        return result

    def uniqueForm(self, p1: list[int], p2: list[int]) -> tuple[int, int]:
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
            return (0, 1)
        if dy == 0:
            return (1, 0)
        if dx < 0:
            dx, dy = -dx, -dy
        g = math.gcd(dx, dy)
        return (dx // g, dy // g)
        # return (dx // g, max(0, dy // g), max(0, -(dy // g)))
