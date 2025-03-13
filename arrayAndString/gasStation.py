class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        l = len(gas)

        start = end = 0
        current = gas[start] - cost[start]
        for _ in range(l - 1):
            if current < 0:
                start = (start - 1) % l
                current += gas[start] - cost[start]
            else:
                end = (end + 1) % l
                current += gas[end] - cost[end]

        if current < 0:
            return -1
        return start
