class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            currentArea = min(height[l], height[r]) * (r - l)
            if currentArea > maxArea:
                maxArea = currentArea

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
