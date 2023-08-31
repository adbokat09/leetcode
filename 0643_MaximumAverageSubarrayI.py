from typing import List


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        max_sum = sum_

        for i in range(k, len(nums)):
            sum_ = sum_ - nums[i - k] + nums[i]
            max_sum = max(max_sum, sum_)

        return max_sum / k


print(Solution().findMaxAverage([int(x) for x in input().split()], int(input())))
