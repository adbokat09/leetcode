from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        path = cost[:2]
        cost.append(0)
        for i in range(2, len(cost)):
            path.append(cost[i] + min(path[i - 1], path[i - 2]))

        return path[-1]


print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
