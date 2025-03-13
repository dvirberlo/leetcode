class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        total = n
        up = down = peak = 0
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                down = 0
                peak = up = up + 1
                total += up
            elif ratings[i - 1] == ratings[i]:
                peak = up = down = 0
            else:
                up = 0
                down += 1
                total += down - (0 if down > peak else 1)
        return total
