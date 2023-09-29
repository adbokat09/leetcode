# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = deque()
        stack.append((1, root))

        max_depth = 1

        while stack:
            depth, node = stack.pop()

            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))

            max_depth = max(max_depth, depth)

        return max_depth


def tree_from_list(lst) -> TreeNode:
    if not lst:
        return
    n = len(lst)
    lst = [TreeNode(x) if x is not None else None for x in lst]

    stack = deque()
    stack.append((0, lst[0]))

    while stack:
        i, node = stack.pop()
        l, r = i * 2 + 1, i * 2 + 2
        if l < n and lst[l] is not None:
            node.left = lst[l]
            stack.append((l, lst[l]))
        if r < n and lst[r] is not None:
            node.right = lst[r]
            stack.append((r, lst[r]))

    return lst[0]


rood = tree_from_list([3,9,20,None,None,15,7])
print(Solution().maxDepth(rood))
