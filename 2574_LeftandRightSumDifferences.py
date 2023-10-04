from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        answer = []

        for el in nums:
            right_sum -= el

            answer.append(abs(left_sum - right_sum))

            left_sum += el

        return answer
