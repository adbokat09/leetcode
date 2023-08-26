class Solution:
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area
        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
