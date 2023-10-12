class Solution:
    def pivotInteger(self, n: int) -> int:
        for el in range(1, n + 1):

            left_sum = (1 + el) / 2 * el
            right_sum = (el + n) / 2 * (n - el + 1)
            if left_sum == right_sum:
                return el

        return -1
