class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.p(x, -n)
        return self.p(x, n)

    def p(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        t = self.p(x, n // 2)
        if n % 2 == 0:
            return t * t
        return t * t * x
