from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        stack = []

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    stack.append((i, j))
                    break
            if stack:
                break

        while stack:
            i, j = stack.pop()
            grid[i][j] = '*'

            if (i, j) in visited:
                continue

            visited.add((i, j))

            for ii, jj in [(i + 1,  j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ii < n and 0 <= jj < m and (ii, jj) not in visited and grid[ii][jj] == 1:
                    stack.append((ii, jj))

        que = deque(visited)
        visited = set()
        level = 0

        while que:
            for _ in range(len(que)):
                i, j = que.popleft()

                if (i, j) in visited:
                    continue

                visited.add((i, j))

                for ii, jj in [(i + 1,  j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= ii < n and 0 <= jj < m and (ii, jj) not in visited:
                        if grid[ii][jj] == 1:
                            return level
                        que.append((ii, jj))

            level += 1


matrix = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

print(Solution().shortestBridge(matrix))

# for row in visited:
#     for el in row:
#         if el == 0:
#             print('.', end='')
#         elif el == 1:
#             print('#', end='')
#         else:
#             print(el, end='')
#     print()
