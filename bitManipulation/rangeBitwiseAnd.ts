/**
 * Intuition:
 * If the difference is greater than 1, the 0th bit will always be 0 in the result.
 * If the difference is greater than 2, the 1st bit will alway be 0, in the result.
 * ...
 * If the difference is greater than 2^n, the n-th bit will always be 0 in the result.
 * Therefore, if the difference is greater than 2^n, all the first n bits will be 0 in the result.
 * Meaning, the rightmost bit of the difference, and all bits to the right of it, will be 0 in the result.
 *
 * On the other hand, if the difference is less or equal to 2^n, and the n-th bit is 1 in both left and right,
 * then the n-th bit will be 1 in the result, and all bits to the right of it will be 0 in the result.
 *
 * Formally:
 * The n-th bit of the result will be 1
 * if and only if
 * the n-th bit of both left and right is 1, and the difference is less or equal to 2^n.
 */
function rangeBitwiseAnd(left: number, right: number): number {
  let diff = right - left;
  // make diff a power of two minus one (fill with 1s all bits to the right of the highest bit)
  diff |= diff >> 1;
  diff |= diff >> 2;
  diff |= diff >> 4;
  diff |= diff >> 8;
  diff |= diff >> 16;

  return left & right & ~diff;
}
