class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        total = 0
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == k:
                total += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1

        return total
