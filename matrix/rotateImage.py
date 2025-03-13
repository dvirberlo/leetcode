from typing import Iterator


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = n - n // 2
        k = n - m
        for i in range(k):
            for j in range(m):
                last = current = matrix[i][j]
                for a, b in self.rotations(i, j, n, m, k):
                    current = matrix[a][b]
                    matrix[a][b] = last
                    last = current
                matrix[i][j] = last

    def rotations(
        self, i: int, j: int, n: int, m: int, k: int
    ) -> Iterator[tuple[int, int]]:
        a, b = m - 1 - i, m - 1 - j
        yield j, a + k
        yield a + k, b + k
        yield b + k, i
