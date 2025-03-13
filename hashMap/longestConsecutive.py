class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        indexes: set[int] = set(nums)

        longest = 0
        while indexes:
            e = indexes.pop()
            start, stop = e, e + 1
            while stop in indexes:
                indexes.remove(stop)
                stop += 1
            while (start - 1) in indexes:
                start -= 1
                indexes.remove(start)
            l = stop - start
            if l > longest:
                longest = l
        return longest

    def longestConsecutive2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        print(nums)
        longest = l = 1
        for i in range(n):
            if i + 1 < n and nums[i + 1] == nums[i] + 1:
                l += 1
            elif i + 1 < n and nums[i + 1] == nums[i]:
                continue
            else:
                longest = max(longest, l)
                l = 1
        return longest
