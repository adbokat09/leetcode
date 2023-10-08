from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        counter = 0
        left_sum = 0
        for num in nums:
            left_sum += num
            counter += sums[left_sum - k]
            sums[left_sum] += 1

        return counter
