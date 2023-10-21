from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins.sort()

        for i in range(1, amount + 1):
            result_count = float('inf')
            for coin in coins:
                if coin > i:
                    break
                result_count = min(result_count, 1 + dp[i - coin])
            dp[i] = result_count

        return dp[-1] if dp[-1] != float('inf') else -1


print(Solution().coinChange([2], 3))
