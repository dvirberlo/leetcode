function minPathSum(grid: number[][]): number {
  const m = grid.length,
    n = grid[0].length;

  let i = m - 1;
  for (let j = n - 2; j >= 0; j--) grid[i][j] += grid[i][j + 1];

  for (let i = m - 2; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      grid[i][j] += Math.min(
        grid[i][j + 1] ?? Number.POSITIVE_INFINITY,
        grid[i + 1][j]
      );
    }
  }
  return grid[0][0];
}
