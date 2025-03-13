class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        count = 0
        for current in nums:
            if count == 0:
                candidate = current
            if candidate == current:
                count += 1
            else:
                count -= 1
        return candidate


class Select:
    THRESHOLD = 5

    @classmethod
    def select(cls, arr: list, start: int, stop: int, k: int) -> int:
        while True:
            if start == stop - 1:
                return arr[start]

            pivot = cls.getPivot(arr, start, stop)
            pivot_index = cls.partition(pivot, arr, start, stop)

            rank = pivot_index - start + 1
            if k == rank:
                return arr[pivot_index]
            elif k < rank:
                stop = pivot_index
            else:
                k -= rank
                start = pivot_index + 1

    @classmethod
    def getPivot(cls, arr: list, start: int, stop: int) -> int:
        n = stop - start
        if n <= cls.THRESHOLD:
            return sorted(arr[start:stop])[n // 2]

        medians = []
        for i in range(start, stop, cls.THRESHOLD):
            group = sorted(arr[i : min(i + cls.THRESHOLD, stop)])
            medians.append(group[len(group) // 2])

        return cls.select(medians, 0, len(medians), len(medians) // 2 + 1)

    @classmethod
    def partition(cls, value: int, arr: list, start: int, stop: int) -> int:
        i = start
        for j in range(start, stop):
            if arr[j] == value:
                arr[j], arr[stop - 1] = arr[stop - 1], arr[j]
                break
        pivot_index = stop - 1

        i = start
        for j in range(start, stop):
            if arr[j] < value:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        return i
