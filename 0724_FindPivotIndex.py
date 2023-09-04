from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i in range(len(nums)):
            if left_sum == right_sum - nums[i]:
                return i
            left_sum += nums[i]
            right_sum -= nums[i]

        return -1


print(Solution().pivotIndex([1,7,3,6,5,6]))
