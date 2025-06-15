from heapq import nlargest


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        profits, stack = [], []
        i = 0
        if n < 2 or k == 0:
            return 0

        while i < n:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = i

            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = i

            if valley < i:
                # clean up overlapping transactions
                while stack and prices[valley] < prices[stack[-1][0]]:
                    v, p = stack.pop()
                    profits.append(prices[p] - prices[v])

                # when we either have one long transaction or 2 smaller ones that can be merged,
                # we as a profit the incremental gain from splitting the transaction
                # and update valley, to add (later) the profit from the long transaction
                while stack and prices[i] >= prices[stack[-1][1]]:
                    v, p = stack.pop()
                    profits.append(prices[p] - prices[valley])
                    valley = v

                stack.append((valley, peak))

            i = peak + 1

        while stack:
            v, p = stack.pop()
            profits.append(prices[p] - prices[v])

        return sum(profits) if k >= len(profits) else sum(nlargest(k, profits))


# Complexity Analysis
# Linearly finding pairs of valleys and peaks takes O(n) time.
# Notice each pair of valley and peak added and removed from the stack at most once.
# Thus, gathering profits from the stack takes O(n) time.
# Gathering and summing up the k largest profits can be done using Selection and Partition algorithms in O(n + k) time.
# Thus, the overall time complexity is O(n + k).
# Space complexity is O(n) for storing the profits and stack.

# Summing up, this algorithm runs in O(n + k) time and O(n) space.
# While the DP solution runs in O(n * k) time and O(k) space.
