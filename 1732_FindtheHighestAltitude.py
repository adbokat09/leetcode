from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_height = 0
        max_height = 0
        for height in gain:
            current_height = current_height + height
            max_height = max(current_height, max_height)

        return max_height


print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
