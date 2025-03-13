class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            if target == numbers[i] + numbers[j]:
                return [i + 1, j + 1]
            elif target > numbers[i] + numbers[j]:
                i += 1
            else:
                j -= 1
        raise Exception("no pair found")
