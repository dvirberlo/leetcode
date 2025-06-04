function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  const m = obstacleGrid.length,
    n = obstacleGrid[0].length;

  for (let i = 0; i < m; i++)
    for (let j = 0; j < n; j++) obstacleGrid[i][j] = 1 - obstacleGrid[i][j];

  let i = m - 1;
  for (let j = n - 2; j >= 0; j--)
    obstacleGrid[i][j] = obstacleGrid[i][j] * obstacleGrid[i][j + 1];

  for (let i = m - 2; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      obstacleGrid[i][j] =
        obstacleGrid[i][j] *
        (obstacleGrid[i + 1][j] + (obstacleGrid[i][j + 1] ?? 0));
    }
  }
  return obstacleGrid[0][0];
}
