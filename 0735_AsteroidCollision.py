from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid >= 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] >= 0:
                    if abs(asteroid) > stack[-1]:
                        stack.pop()
                    elif abs(asteroid) == stack[-1]:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)

        return stack

