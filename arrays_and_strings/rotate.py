from typing import List, NamedTuple, Tuple


class Move(NamedTuple):
    value: int
    position: Tuple[int, int]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        moving_stack = []

        for i in range(n):
            end = n - i - 1

            for j in range(n):
                moving_stack.append(Move(value=matrix[i][j], position=(j, end)))

        for item in moving_stack:
            matrix[item.position[0]][item.position[1]] = item.value


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix)
print(matrix)
