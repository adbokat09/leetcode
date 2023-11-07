from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        visited = set()
        count = 0
        stack = []

        for row in range(n):
            for column in range(m):

                if grid[row][column] == '1':
                    if (row, column) not in visited:
                        count += 1
                    stack.append((row, column))
                    grid[row][column] = '0'

                    while stack:
                        i, j = stack.pop()
                        if (i, j) in visited:
                            continue

                        visited.add((i, j))

                        if i != 0 and grid[i - 1][j] == '1' and (i - 1, j) not in visited:
                            stack.append((i - 1, j))
                            grid[i - 1][j] = '0'

                        if j != 0 and grid[i][j - 1] == '1' and (i, j - 1) not in visited:
                            stack.append((i, j - 1))
                            grid[i][j - 1] = '0'

                        if j != m - 1 and grid[i][j + 1] == '1' and (i, j + 1) not in visited:
                            stack.append((i, j + 1))
                            grid[i][j + 1] = '0'

                        if i != n - 1 and grid[i + 1][j] == '1' and (i + 1, j) not in visited:
                            stack.append((i + 1, j))
                            grid[i + 1][j] = '0'

        return count
