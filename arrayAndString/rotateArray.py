class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(arr)
        k = k % l
        print(arr)
        self.reverse(arr, 0, l - 1)
        print(arr)
        self.reverse(arr, 0, k - 1)
        print(arr)
        self.reverse(arr, k, l - 1)

    def reverse(self, arr: list[int], start: int, end: int):
        l = end - start + 1
        for k in range(l // 2):
            i = start + k
            j = end - k
            arr[i], arr[j] = arr[j], arr[i]
