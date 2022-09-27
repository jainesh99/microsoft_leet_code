from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        number_of_items = m * n
        start = (0, 0)
        touched = {}
        spiral_order = [matrix[0][0]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        compass = 0

        for i in range(number_of_items):

            if i + 1 < number_of_items:

                new_coordinate = (
                    start[0] + directions[compass][0],
                    start[1] + directions[compass][1],
                )
                # TODO: THis is an m x n remember!
                if new_coordinate[0] > n - 1 or new_coordinate[0] > n - 1:
                    new_coordinate = (
                        start[0] - directions[compass][0],
                        start[1] - directions[compass][1],
                    )

                    if compass + 1 > len(directions) - 1:
                        compass = 0
                    else:
                        compass += 1

                elif new_coordinate[0] < 0 or new_coordinate[1] < 0:
                    new_coordinate = (
                        start[0] - directions[compass][0],
                        start[1] - directions[compass][1],
                    )

                    if compass + 1 > len(directions) - 1:
                        compass = 0
                    else:
                        compass += 1

                if not touched.get(new_coordinate, False):

                    touched[new_coordinate] = new_coordinate
                    spiral_order.append(matrix[new_coordinate[0]][new_coordinate[1]])
                    print(matrix[new_coordinate[0]][new_coordinate[1]])
                    start = new_coordinate


solution = Solution()
solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
