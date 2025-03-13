class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        left, right = 0, len(height) - 1
        max_left = max_right = 0
        while left <= right:
            if max_left <= max_right:
                current = height[left]
                if current < max_left and current < max_right:
                    total += min(max_left, max_right) - current
                if current > max_left:
                    max_left = current
                left += 1
            else:
                current = height[right]
                if current < max_right and current < max_right:
                    total += min(max_right, max_right) - current
                if current > max_right:
                    max_right = current
                right -= 1
        return total


class Solution2:
    def trap(self, height: list[int]) -> int:
        def h(i):
            return 0 if i < 0 or i >= len(height) else height[i]

        lastLeft, lastRight = 0, len(height) - 1
        l, r = 0, len(height) - 1
        leftBoxes, rightBoxes = 0, 0
        result = 0
        while l <= r:
            if h(lastLeft) <= h(lastRight):
                l += 1
                if h(l) >= h(lastLeft):
                    result += max(
                        (l - lastLeft - 1) * min(h(l), h(lastLeft)) - leftBoxes, 0
                    )
                    leftBoxes = 0
                    lastLeft = l
                else:
                    leftBoxes += h(l)
            else:
                r -= 1
                if h(r) >= h(lastRight):
                    result += max(
                        (lastRight - r - 1) * min(h(r), h(lastRight)) - rightBoxes, 0
                    )
                    rightBoxes = 0
                    lastRight = r
                else:
                    rightBoxes += h(r)
        return result
