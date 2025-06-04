// def maxSubArray(self, nums: List[int]) -> int:
//     n = len(nums)
//     memoI, memoE = [None] * n, [None] * n
//     def I(l: int):
//         if not (l < n):
//             return - float("inf")
//         if memoI[l] is None:
//             memoI[l] =  nums[l] + max(0, I(l+1))
//         return memoI[l]
//     def E(l: int):
//         if not (l < n):
//             return - float("inf")
//         if memoE[l] is None:
//             memoE[l] =  max(I(l+1), E(l+1))
//         return memoE[l]
//     return max(I(0), E(0))

// def maxSubArray(self, nums: List[int]) -> int:
//     n = len(nums)
//     last = nums[-1]
//     memoI, memoE = [last] * n, [-float("inf")] * n
//     i = n-2
//     while i >= 0:
//         memoI[i] = nums[i] + max(0, memoI[i+1])
//         memoE[i] =  max(memoI[i+1], memoE[i+1])
//         i -= 1
//     return max(memoI[0], memoE[0])

function maxSubArray(nums: number[]): number {
  const n = nums.length;
  let Ii,
    IiP1 = nums[n - 1];
  let Ei,
    EiP1 = Number.NEGATIVE_INFINITY;

  for (let i = n - 2; i >= 0; i--) {
    Ii = nums[i] + Math.max(0, IiP1);
    Ei = Math.max(IiP1, EiP1);
    IiP1 = Ii;
    EiP1 = Ei;
  }
  return Math.max(IiP1, EiP1);
}
