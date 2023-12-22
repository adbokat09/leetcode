class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2, = len(word1), len(word2)
        matrix = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        matrix[0] = list(range(l1 + 1))
        for i in range(l2 + 1):
            matrix[i][0] = i

        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
        return matrix[-1][-1]


for row in Solution().minDistance('horse', 'ros'):
    for el in row:
        print(el, end=' ')
    print()
