// function minDistance(word1: string, word2: string): number {
//   const memo: number[][] = Array.from({ length: word1.length + 1 }, () =>
//     Array(word2.length + 1).fill(-1)
//   );
//   const dist = (i: number, j: number): number => {
//     let result = memo[i][j];
//     if (result !== -1) return result;
//     else if (i >= word1.length) result = word2.length - j;
//     else if (j >= word2.length) result = word1.length - i;
//     else if (word1[i] === word2[j]) result = dist(i + 1, j + 1);
//     else
//       result = Math.min(
//         1 + dist(i + 1, j),
//         1 + dist(i, j + 1),
//         1 + dist(i + 1, j + 1)
//       );
//     memo[i][j] = result;
//     return result;
//   };
//   return dist(0, 0);
// }

function minDistance(word1: string, word2: string): number {
  let memo: number[] = Array(word2.length + 1);
  let memoNext: number[] = Array.from(
    { length: word2.length + 1 },
    (_, i) => word2.length - i
  );
  for (let i = word1.length - 1; i >= 0; i--) {
    for (let j = word2.length; j >= 0; j--) {
      if (i === word1.length) memo[j] = word2.length - j;
      else if (j === word2.length) memo[j] = word1.length - i;
      else if (word1[i] === word2[j]) memo[j] = memoNext[j + 1];
      else memo[j] = 1 + Math.min(memoNext[j], memo[j + 1], memoNext[j + 1]);
    }
    [memo, memoNext] = [memoNext, memo];
  }
  return memoNext[0];
}
