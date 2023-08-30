from typing import List


class Solution:

    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                total += j - i
                i += 1
            else:
                j -= 1

        return total


print(Solution().countPairs([int(x) for x in input().split()], int(input())))
