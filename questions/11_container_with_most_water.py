from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left = left + 1
            else:
                area = (right - left) * height[right]
                right = right - 1

            max_area = max(max_area, area)

        return max_area


solution = Solution()
height = [1, 1]
print(solution.maxArea(height))
