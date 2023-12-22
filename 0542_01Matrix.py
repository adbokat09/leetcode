from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        que = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    que.append((i, j))

        level = 0
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()

                if (i, j) in visited:
                    continue

                visited.add((i, j))

                if mat[i][j] != 0:
                    mat[i][j] = level

                for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ii < n and 0 <= jj < m and mat[ii][jj] != 0 and (ii, jj) not in visited:
                        que.append((ii, jj))

            level += 1

        return mat
