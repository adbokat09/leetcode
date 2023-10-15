from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        matrix = [[0] * m for _ in range(n)]

        matrix[0][0] = grid[0][0]

        for i in range(1, m):
            matrix[0][i] = matrix[0][i - 1] + grid[0][i]

        for i in range(1, n):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]

        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = grid[i][j] + min(matrix[i - 1][j], matrix[i][j - 1])

        return matrix[-1][-1]
