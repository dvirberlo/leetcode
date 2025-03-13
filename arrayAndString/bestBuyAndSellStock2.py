class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        prev = prices[0]
        for current in prices:
            if current >= prev:
                profit += current - prev
            prev = current
        return profit
