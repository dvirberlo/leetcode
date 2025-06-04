class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        for row in range(n - 2, -1, -1):
            for i in range(row + 1):
                print(row, i, n)
                triangle[row][i] += min(triangle[row + 1][i], triangle[row + 1][i + 1])
        return triangle[0][0]
