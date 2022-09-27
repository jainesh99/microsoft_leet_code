from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        number_of_items = m * n
        position = [0, 0]
        touched = {(0, 0): True}
        spiral_order = [matrix[0][0]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        compass = 0

        while len(spiral_order) != number_of_items:

            if (
                0 <= position[0] + directions[compass][0] < m
                and 0 <= position[1] + directions[compass][1] < n
            ):

                new_position = [
                    position[0] + directions[compass][0],
                    position[1] + directions[compass][1],
                ]

                if not touched.get((new_position[0], new_position[1]), None):
                    touched[(new_position[0], new_position[1])] = True
                    position = new_position
                    spiral_order.append(matrix[position[0]][position[1]])
                else:
                    if compass >= len(directions) - 1:
                        compass = 0
                    else:
                        compass += 1

            else:
                if compass >= len(directions) - 1:
                    compass = 0
                else:
                    compass += 1

        return spiral_order


solution = Solution()
solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
