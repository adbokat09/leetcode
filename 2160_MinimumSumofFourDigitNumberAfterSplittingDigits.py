class Solution:
    def minimumSum(self, num: int) -> int:
        lst = list(str(num))
        lst.sort()
        return int(lst[0] + lst[2]) + int(lst[1] + lst[3])


print(Solution().minimumSum(4009))
