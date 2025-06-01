function singleNumber1(nums: number[]): number {
  const arr: number[] = [];
  for (let num of nums) {
    let i = 0;
    while (num != 0) {
      if (num & 1) arr[i] = (arr[i] ?? 0) + 1;
      num = num >>> 1;
      i++;
    }
  }
  let result = 0;
  arr.forEach((v, i) => {
    if (v % 3 != 0) result |= 1 << i;
  });
  return result;
}

function singleNumber(nums: number[]): number {
  let oneBits1 = 0,
    oneBits2 = 0;
  for (let num of nums) {
    let toMark1 = ~oneBits1 & num;
    oneBits1 |= toMark1;
    num &= ~toMark1;

    let toMark2 = ~oneBits2 & num;
    oneBits2 |= toMark2;
    num &= ~toMark2;

    if (num !== 0) {
      oneBits1 &= ~num;
      oneBits2 &= ~num;
    }
  }
  return oneBits1 | oneBits2;
}
