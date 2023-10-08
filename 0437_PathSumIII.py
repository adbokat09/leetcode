from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        sums = defaultdict(int)
        stack = [(0, sums, root)]
        sums[0] = 1

        count = 0

        while stack:
            cur_sum, sums, node = stack.pop()
            cur_sum += node.val

            count += sums[cur_sum - targetSum]

            sums[cur_sum] += 1

            if node.left:
                stack.append((cur_sum, sums.copy(), node.left))
            if node.right:
                stack.append((cur_sum, sums.copy(), node.right))

        return count

