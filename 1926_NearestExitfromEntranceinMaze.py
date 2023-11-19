from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        if n == 1 and m == 2:
            return -1

        deq = deque()
        visited = set()

        deq.append(entrance)
        level = 0

        while deq:
            for _ in range(len(deq)):
                i, j = deq.popleft()

                if (i in (0, n - 1) or j in (0, m - 1)) and level > 0:
                    return level

                if (i, j) in visited:
                    continue

                visited.add((i, j))

                if i != n and maze[i + 1][j] == '.' and (i + 1, j) not in visited:
                    deq.append((i + 1, j))

                if j != m and maze[i][j + 1] == '.' and (i, j + 1) not in visited:
                    deq.append((i, j + 1))

                if i != 0 and maze[i - 1][j] == '.' and (i - 1, j) not in visited:
                    deq.append((i - 1, j))

                if j != 0 and maze[i][j - 1] == '.' and (i, j - 1) not in visited:
                    deq.append((i, j - 1))

                level += 1
        return -1


print(Solution().nearestExit([[".", "+"]], [0, 0]))




