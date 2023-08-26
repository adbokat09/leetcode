class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        get_area = lambda x1, x2: min(height[x1], height[x2]) * (x2 - x1)
        max_area = get_area(i, j)
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

            area = get_area(i, j)
            if area > max_area:
                max_area = area
        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
