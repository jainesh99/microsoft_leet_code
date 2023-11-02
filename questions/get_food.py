from collections import deque
from typing import List


class Solution:
    def get_available_positions(
        self, grid, position, number_of_rows, number_of_columns
    ):
        available_positions = []

        if position[1] + 1 < number_of_columns:
            if grid[position[0]][position[1] + 1] != "X":
                available_positions.append((position[0], position[1] + 1))

        if position[0] + 1 < number_of_rows:
            if grid[position[0] + 1][position[1]] != "X":
                available_positions.append((position[0] + 1, position[1]))

        if position[1] - 1 >= 0:
            if grid[position[0]][position[1] - 1] != "X":
                available_positions.append((position[0], position[1] - 1))

        if position[0] - 1 >= 0:
            if grid[position[0] - 1][position[1]] != "X":
                available_positions.append((position[0] - 1, position[1]))

        return available_positions

    def getFood(self, grid: List[List[str]]) -> int:
        num_of_rows = len(grid)
        num_of_columns = len(grid[0])
        start_position = set()
        bfs_queue = deque()
        visited = {}

        for row in range(num_of_rows):
            if "*" in grid[row]:
                start_position = (row, grid[row].index("*"))
                break

        bfs_queue.append((start_position, 1))

        while bfs_queue:
            position, steps = bfs_queue.popleft()
            visited[position] = position
            available_positions = self.get_available_positions(
                grid, position, num_of_rows, num_of_columns
            )

            for position in available_positions:
                if position not in visited.keys():
                    if grid[position[0]][position[1]] == "#":
                        return steps

                    grid[position[0]][position[1]] = "X"
                    bfs_queue.append((position, steps + 1))

        return -1


solution = Solution()
grid = [["O", "*"], ["#", "O"]]
print(solution.getFood(grid))
print(grid)
