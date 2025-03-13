class Solution:
    def jump(self, nums: list[int]) -> int:
        for i, e in enumerate(nums):
            if i == 0:
                continue
            nums[i] = max(i + e, nums[i - 1])

        jumps = 0
        i = 0
        while i < len(nums) - 1:
            i = nums[i]
            jumps += 1
        return jumps
