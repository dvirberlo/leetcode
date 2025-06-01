class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n <= 1:
            return [nums]
        result = []
        for i in range(n):
            x = nums.pop(i)
            result.extend([x] + l for l in self.permute(nums))
            nums.insert(i, x)
        return result
