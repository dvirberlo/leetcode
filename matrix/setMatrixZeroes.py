class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstCol = firstRow = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j == 0 or i == 0:
                        if j == 0:
                            firstCol = True
                        if i == 0:
                            firstRow = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
