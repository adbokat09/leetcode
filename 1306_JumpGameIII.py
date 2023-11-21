from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        que = deque()
        que.append(start)
        visited = set()

        while que:
            for _ in range(len(que)):
                i = que.popleft()

                if arr[i] == 0:
                    return True

                if i in visited:
                    continue

                visited.add(i)

                if i + arr[i] <= len(arr):
                    que.append(i + arr[i])

                if i - arr[i] >= 0:
                    que.append(i - arr[i])

        return False
