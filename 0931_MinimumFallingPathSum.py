from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        result_matrix = [[0] * (n + 2) for _ in range(n)]

        for i in range(n):
            result_matrix[0][i + 1] = matrix[0][i]

        for i in range(n):
            result_matrix[i][0] = float('inf')

        for i in range(n):
            result_matrix[i][-1] = float('inf')

        for i in range(1, n):
            for j in range(1,  n + 1):

                result_matrix[i][j] = matrix[i][j - 1] + min(result_matrix[i - 1][j - 1], result_matrix[i - 1][j], result_matrix[i - 1][j + 1])
                # result_matrix[i][j] = matrix[i][j - 1] + min(matrix[i - 1][j - 1], matrix[i - 1][j - 2], matrix[i -1][j - 3])

                # result_matrix[i][j] = min(matrix[i - 1][j + 1], matrix[i - 2][j + 1], matrix[i + 1][j + 2])

                # print(matrix[i])
                # print(matrix[i][j])
        print()
        for row in result_matrix:
            print(row)

        return min(result_matrix[-1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(Solution().minFallingPathSum(matrix))
