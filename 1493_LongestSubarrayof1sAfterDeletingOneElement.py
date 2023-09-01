from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones_count = 0
        result = [0]

        for num in nums:
            if num != 0:
                result[-1] += 1
            else:
                result.append(0)

        if len(result) == 1:
            return result[0] - 1

        for i in range(len(result) - 1):
            max_ones_count = max(result[i] + result[i + 1], max_ones_count)

        return max_ones_count


print(Solution().longestSubarray([0,1,1,1,0,1,1,0,0,0,1]))
