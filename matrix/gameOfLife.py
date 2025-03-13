from typing import Iterator
import os
import time


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                population = sum(
                    board[a][b] % 10 for a, b in self.toroidalNeighbors(i, j, m, n)
                )
                current = board[i][j]
                if current == 1 and (population < 2 or population > 3):
                    board[i][j] += 0
                elif current == 0 and population == 3:
                    board[i][j] += 10
                else:
                    board[i][j] += current * 10

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] // 10

    def neighbors(self, i: int, j: int, m: int, n: int) -> Iterator[tuple[int, int]]:
        up, left = i - 1 >= 0, j - 1 >= 0
        down, right = i + 1 < m, j + 1 < n
        if up:
            if left:
                yield i - 1, j - 1
            yield i - 1, j
            if right:
                yield i - 1, j + 1
        if right:
            yield i, j + 1
        if down:
            if right:
                yield i + 1, j + 1
            yield i + 1, j
            if left:
                yield i + 1, j - 1
        if left:
            yield i, j - 1

    def toroidalNeighbors(
        self, i: int, j: int, m: int, n: int
    ) -> Iterator[tuple[int, int]]:
        yield (i - 1 + m) % m, (j - 1 + n) % n
        yield (i - 1 + m) % m, (j + n) % n
        yield (i - 1 + m) % m, (j + 1 + n) % n
        yield (i + m) % m, (j + 1 + n) % n
        yield (i + 1 + m) % m, (j + 1 + n) % n
        yield (i + 1 + m) % m, (j + n) % n
        yield (i + 1 + m) % m, (j - 1 + n) % n
        yield (i + m) % m, (j - 1 + n) % n

    def printBoard(self, board: list[list[int]]):
        for row in board:
            for cell in row:
                # █ ■
                print("██" if cell == 1 else "  ", end="")
            print("|")
        print("_" * len(board[0]) * 2 + "|")

    def animate(self, board: list[list[int]], times=100, sleep=0.25):
        for _ in range(times):
            os.system("cls" if os.name == "nt" else "clear")
            self.printBoard(board)
            r = self.gameOfLife(board)
            time.sleep(sleep)
