class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = sum(range(1, n + 1))

        for el in range(1, n + 1):
            left_sum += el

            if left_sum == right_sum:
                return el

            right_sum -= el
        return -1
