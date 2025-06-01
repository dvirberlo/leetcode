class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        result = []
        current = []

        def b(target: int, i: int = 0):
            if target <= 0:
                if target == 0:
                    result.append(current.copy())
                return
            for j in range(i, n):
                current.append(candidates[j])
                b(target - candidates[j], j)
                current.pop()

        b(target)
        return result
