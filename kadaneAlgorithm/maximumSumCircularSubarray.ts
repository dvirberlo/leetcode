function maxSubarraySumCircular(nums: number[]): number {
  const n = nums.length;
  let I = nums[n - 1],
    E = Number.NEGATIVE_INFINITY;
  let mI = -nums[n - 1],
    mE = Number.NEGATIVE_INFINITY;
  let sum = nums[n - 1];

  for (let i = n - 2; i >= 0; i--) {
    sum += nums[i];

    E = Math.max(I, E);
    I = nums[i] + Math.max(0, I);

    mE = Math.max(mI, mE);
    mI = -nums[i] + Math.max(0, mI);
  }
  const minSubarraySum = -Math.max(mI, mE);
  if (minSubarraySum === sum) return Math.max(I, E);
  return Math.max(I, E, sum + mI, sum + mE);
}
