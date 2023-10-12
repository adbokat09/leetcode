from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()

        while stack:
            room = stack.pop()

            if room in visited:
                continue

            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)

        return len(rooms) == len(visited)
