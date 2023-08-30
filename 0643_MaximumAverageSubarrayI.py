from typing import List


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):
            total_sum = sum(nums[i:i + k])
            avg = total_sum / k
            if avg > max_avg:
                max_avg = avg

        return max_avg


print(Solution().findMaxAverage([int(x) for x in input().split()], int(input())))
