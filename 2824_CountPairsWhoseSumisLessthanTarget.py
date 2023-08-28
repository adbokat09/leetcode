from typing import List


class Solution:

    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if 0 <= i < j < n and nums[i] + nums[j] < target:
                    count += 1

        return count


print(Solution().countPairs([int(x) for x in input().split()], int(input())))
