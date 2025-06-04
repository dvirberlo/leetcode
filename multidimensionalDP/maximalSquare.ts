// function maximalSquare(matrix: number[][]): number {
//   const m = matrix.length,
//     n = matrix[0].length;
//   const k = Math.min(n, m);
//   let includesOne = false;
//   for (let i = 0; i < m; i++)
//     for (let j = 0; j < n; j++)
//       if ((matrix[i][j] as unknown as string) === "1") {
//         matrix[i][j] = 1;
//         includesOne = true;
//       } else matrix[i][j] = 0;

//   let last,
//     current = matrix;
//   let result = includesOne ? 1 : 0;
//   for (let t = 1; t < k && includesOne; t++) {
//     includesOne = false;
//     last = current;
//     current = Array.from({ length: m - t }, () => Array(n - t).fill(0));
//     for (let i = 0; i < m - t; i++)
//       for (let j = 0; j < n - t; j++) {
//         if (
//           (last[i][j] &
//             last[i + 1][j] &
//             last[i][j + 1] &
//             last[i + 1][j + 1]) ===
//           1
//         ) {
//           current[i][j] = 1;
//           includesOne = true;
//         }
//       }
//     if (includesOne) result = (t + 1) * (t + 1);
//   }
//   return result;
// }

function maximalSquare(matrix: number[][]): number {
  const m = matrix.length,
    n = matrix[0].length;
  for (let i = 0; i < m; i++)
    for (let j = 0; j < n; j++)
      matrix[i][j] = (matrix[i][j] as unknown as string) === "1" ? 1 : 0;

  for (let i = m - 2; i >= 0; i--)
    for (let j = n - 2; j >= 0; j--) {
      if (matrix[i][j] === 1)
        matrix[i][j] =
          1 +
          Math.min(matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]);
    }

  let maxSquare = 0;
  for (let i = 0; i < m; i++)
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] > maxSquare) maxSquare = matrix[i][j];
    }
  return maxSquare * maxSquare;
}
