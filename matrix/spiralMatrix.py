class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def rotate(self):
        if self.x != 0:
            self.y = -self.x
            self.x = 0
        else:
            self.x = self.y
            self.y = 0

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def subAbs(self, other):
        self.x -= abs(other.x)
        self.y -= abs(other.y)

    def atMatrix(self, matrix: list[list[int]]) -> int:
        return matrix[self.x][self.y]

    def nonNegative(self) -> bool:
        return self.x > 0 and self.y > 0

    def prod(self, other) -> int:
        return self.x * other.x + self.y * other.y

    # def __str__(self):
    # return f"Point({self.x}, {self.y})"


class Solution:

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        lengths = Point(len(matrix), len(matrix[0]))
        dir = Point(0, 1)
        current: Point = Point(0, -1)
        result = []
        while lengths.nonNegative():
            for _ in range(abs(lengths.prod(dir))):
                current += dir
                # print(current, dir, lengths)
                result.append(current.atMatrix(matrix))
            dir.rotate()
            lengths.subAbs(dir)
        return result
