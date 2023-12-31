class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        row1 = matrix[0]
        row2 = matrix[1]
        row3 = matrix[2]
        row4 = matrix[3]
        row5 = matrix[4]
        row6 = matrix[5]

        el = 0

        for i in range(1, len(s1)):
            el += ord(s1[i - 1])
            matrix[0][i] = el

        el = 0
        for i in range(1, len(s2) + 1):
            el += ord(s2[i - 1])
            matrix[i][0] = el

        for i1 in range(1, len(s1) + 1):
            for i2 in range(1, len(s2) + 1):
                if s1[i1 - 1] == s2[i2 - 1]:
                    matrix[i1][i2] = matrix[i1 - 1][i2 - 1]
                else:
                    matrix[i1][i2] = min(matrix[i1 - 1][i2] + ord(s1[i1 - 1]), matrix[i1][i2 - 1] + ord(s2[i2 - 1]))

        return matrix[-1][-1]

'''
            word 1
          s  e  a 
        e 0  0  0 
word 2  a 0  0  0
        t 0  0  0  

'''
# for row in Solution().minimumDeleteSum('delete', 'leet'):
#     for el in row:
#         print(el, end=' ')
#     print()
print(Solution().minimumDeleteSum('delete', 'leet'))
