from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0] * n for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            matrix[0][i] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break

            matrix[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[-1][-1]
