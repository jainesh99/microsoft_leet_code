from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        def generate_next_cells(row, column):
            return [
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ]

        def in_bound(row, column, rows, columns):
            return 0 <= row < rows and 0 <= column < columns

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    answer += 1
                    queue = deque([(i, j)])  # Can use normal queue as well!
                    while queue:
                        row, column = queue.popleft()
                        if grid[row][column] == "0":
                            continue
                        grid[row][column] = "0"
                        for next_row, next_column in generate_next_cells(row, column):
                            if (
                                in_bound(next_row, next_column, len(grid), len(grid[0]))
                                and grid[next_row][next_column] == "1"
                            ):
                                queue.append((next_row, next_column))

        return answer


solution = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(solution.numIslands(grid))
