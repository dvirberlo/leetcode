class Solution:
    def totalNQueens1(self, n: int) -> int:
        result = 0
        current = []

        def attacking(a: tuple[int, int], b: tuple[int, int]):
            return (
                a[0] == b[0]
                or a[1] == b[1]
                or (a[0] - a[1]) == (b[0] - b[1])
                or (a[0] + a[1]) == (b[0] + b[1])
            )

        def b(x: int = 0, y: int = 0):
            nonlocal result, current
            if len(current) == n:
                # print(current)
                result += 1
                return
            for i in range(x, n):
                for j in range(y, n):
                    nq = (i, j)
                    if any(attacking(nq, q) for q in current):
                        continue
                    current.append(nq)
                    b(i + 1, 0)
                    current.pop()

        b()
        return result

    def totalNQueens2(self, n: int) -> int:
        result = 0
        cols, d1, d2 = set(), set(), set()

        def b(x: int = 0, y: int = 0, l: int = 0):
            nonlocal result, cols, d1, d2
            if l == n:
                result += 1
                return
            for i in range(x, n):
                for j in range(y, n):
                    if j in cols or i + j in d1 or i - j in d2:
                        continue
                    cols.add(j)
                    d1.add(i + j)
                    d2.add(i - j)
                    b(i + 1, 0, l + 1)
                    cols.remove(j)
                    d1.remove(i + j)
                    d2.remove(i - j)

        b()
        return result

    def totalNQueens3(self, n: int) -> int:
        result = 0
        cols, d1, d2 = set(), set(), set()

        def b(x: int = 0, y: int = 0, l: int = 0):
            nonlocal result, cols, d1, d2
            if l == n:
                result += 1
                return
            for j in range(y, n):
                _d1 = x + j
                _d2 = x - j
                if j in cols or _d1 in d1 or _d2 in d2:
                    continue
                cols.add(j)
                d1.add(_d1)
                d2.add(_d2)
                b(x + 1, 0, l + 1)
                cols.remove(j)
                d1.remove(_d1)
                d2.remove(_d2)

        b()
        return result
