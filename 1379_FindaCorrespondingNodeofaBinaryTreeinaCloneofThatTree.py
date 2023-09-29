class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        if not original:
            return

        original_stack = [original]
        cloned_stack = [cloned]

        while original_stack:
            origin_node = original_stack.pop()
            cloned_node = cloned_stack.pop()

            if origin_node is target:
                return cloned_node

            if origin_node.left:
                cloned_stack.append(cloned_node.left)
                original_stack.append(origin_node.left)

            if origin_node.right:
                cloned_stack.append(cloned_node.right)
                original_stack.append(origin_node.right)


