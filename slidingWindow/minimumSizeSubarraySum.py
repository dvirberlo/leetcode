class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if sum(nums) < target:
            return 0
        for r in range(1, n):
            nums[r] += nums[r - 1]
        minLen = n
        for r in range(n):
            lMin = nums[r] - target
            if lMin < 0:
                continue
            l = self.maxIndex(nums, r, lMin)
            if r - l < minLen:
                minLen = r - l
        return minLen

    def maxIndex(self, nums: list[int], stop: int, x: int) -> int:
        if x < nums[0]:
            return -1
        a, b = 0, stop - 1
        while b - a > 1:
            c = (a + b) // 2
            if nums[c] <= x:
                a = c
            else:
                b = c
        return b if nums[b] <= x else a
