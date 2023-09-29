from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root: Optional[TreeNode]) -> list:
            if not root:
                return []
            leaves = []

            stack = deque()
            stack.append(root)

            while stack:
                node = stack.pop()

                if not node.right and not node.left:
                    leaves.append(node.val)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)



            return leaves
        return get_leaves(root1) == get_leaves(root2)


def tree_from_list(lst) -> Optional[TreeNode]:
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


root1 = tree_from_list([3,5,1,6,2,9,8,None,None,7,4])
root2 = tree_from_list([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
print(Solution().leafSimilar(root1, root2))
