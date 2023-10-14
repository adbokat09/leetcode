from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        house = [0]
        house.extend(nums[:2])

        for i in range(2, len(nums)):
            house.append(nums[i] + max(house[i - 2], house[i - 3]))

        return max(house[-1], house[-2])
