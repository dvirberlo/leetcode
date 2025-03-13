class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        answer: list[int] = [0] * l
        answer[0] = nums[0]
        for i in range(1, l):
            answer[i] = nums[i] * answer[i - 1]
        prod_right = 1
        for i in reversed(range(1, l)):
            prod_left = answer[i - 1]
            answer[i] = prod_left * prod_right
            prod_right *= nums[i]
        answer[0] = prod_right
        return answer
