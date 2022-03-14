from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count = 0

        for row in grid:
            start_of_negative_index = -1
            for index, item in enumerate(row):

                if item < 0:
                    start_of_negative_index = index
                    break

            if start_of_negative_index >= 0:
                count = count + (len(row) - start_of_negative_index)

        return count


solution = Solution()
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(solution.countNegatives(grid))
