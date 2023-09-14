class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []

        for symbol in s:
            if symbol == '(':
                stack.append(symbol)
                current_depth = len(stack)
                max_depth = max(max_depth, current_depth)
            elif symbol == ')':
                stack.pop()

        return max_depth


s = "(1)+((2))+(((3)))"
print(Solution().maxDepth(s))
