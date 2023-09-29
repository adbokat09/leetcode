from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        if not root:
            return 0

        stack = deque()
        stack.append((root.val, root))

        while stack:
            max_val, node = stack.pop()

            if node.val >= max_val:
                total += 1

            if node.left:
                stack.append((max(max_val, node.left.val), node.left))

            if node.right:
                stack.append((max(max_val, node.right.val), node.right))

        return total



