from typing import Iterator


class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        n = len(arr)
        arr.sort()
        last = arr[0] - 1
        for i, a in enumerate(arr):
            if a == last:
                continue
            last = a
            for b, c in self.twoSum(arr, -a, i + 1, n):
                result.append([a, b, c])
        return result

    def twoSum(
        self, arr: list[int], x: int, start: int, stop: int
    ) -> Iterator[tuple[int, int]]:
        l, r = start, stop - 1
        while l < r:
            if arr[l] + arr[r] == x:
                yield arr[l], arr[r]
                cur = arr[l]
                while l < r and arr[l] == cur:
                    l += 1
            if arr[l] + arr[r] > x:
                r -= 1
            else:
                l += 1
