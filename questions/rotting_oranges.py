from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit, curr = set(), deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr:
            for _ in range(len(curr)):
                i, j = curr.popleft()
                for coord in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if coord in visit:
                        visit.remove(coord)
                        curr.append(coord)
            result += 1
        return -1 if visit else result


# class Solution:
# def get_new_rotten_oranges(self, row, column, num_of_rows, num_of_columns, grid):
#     temp = []
#
#     if row + 1 < num_of_rows:
#
#         if grid[row + 1][column] == 1:
#             temp.append((row + 1, column))
#
#     if row - 1 >= 0:
#
#         if grid[row - 1][column] == 1:
#             temp.append((row - 1, column))
#
#     if column + 1 < num_of_columns:
#
#         if grid[row][column + 1] == 1:
#             temp.append((row, column + 1))
#
#     if column - 1 >= 0:
#
#         if grid[row][column - 1] == "1":
#             temp.append((row, column - 1))
#
#     return temp
#
# def orangesRotting(self, grid: List[List[int]]) -> int:
#
#     minute = -1
#     rows = len(grid)
#     columns = len(grid[0])
#     queue = []
#     rotten_oranges = []
#     row = 0
#
#     for item in grid:
#         rotten_locations = [
#             (row, index) for index, value in enumerate(item) if value == 2
#         ]
#         rotten_oranges = rotten_oranges + rotten_locations
#         row += 1
#
#     for location in rotten_oranges:
#         queue.append(location)
#
#     while queue:
#         new_rotten_oranges = []
#         for row, column in queue:
#
#             temp = self.get_new_rotten_oranges(row, column, rows, columns, grid)
#             new_rotten_oranges = new_rotten_oranges + temp
#
#         queue.clear()
#         minute += 1
#
#         for row, column in new_rotten_oranges:
#             queue.append((row, column))
#             grid[row][column] = 2
#
#     sum2, sum1, sum0 = 0, 0, 0
#
#     for item in grid:
#
#         sum2 = sum2 + item.count(2)
#         sum1 = sum1 + item.count(1)
#         sum0 = sum0 + item.count(0)
#
#     if sum1 > 0 and sum2 == 0:
#         return -1
#     if sum0 > sum2 == 0:
#         return 0
#
#     return minute


solution = Solution()
grid = [[0]]
print(solution.orangesRotting(grid))
