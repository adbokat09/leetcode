from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zeroes, l = 0, 0

        for r in range(len(nums)):
            zeroes += nums[r] == 0

            if zeroes > k:
                zeroes -= nums[l] == 0
                l += 1

        return r - l + 1


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))

