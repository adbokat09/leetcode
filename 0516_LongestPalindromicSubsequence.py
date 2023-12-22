class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            matrix[i][i] = 1

        start_i, start_j = 0, 1
        i, j = start_i, start_j

        while j < n:
            if s[i] == s[j]:
                matrix[i][j] = matrix[i + 1][j-1] + 2
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i + 1][j])

            if j == n - 1:
                i, j = start_i, start_j + 1
                start_j += 1
            else:
                i += 1
                j += 1

        return matrix[0][n - 1]


print(Solution().longestPalindromeSubseq(input()))

''''
 1 -1 -1 
-1  1  1
-1 -1  1 


'''
