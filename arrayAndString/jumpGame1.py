class Solution:
    def canJump(self, nums: list[int]) -> bool:
        nums.reverse()
        min_required = 0
        for e in nums:
            if e >= min_required:
                min_required = 0
            min_required += 1
        return min_required == 1
