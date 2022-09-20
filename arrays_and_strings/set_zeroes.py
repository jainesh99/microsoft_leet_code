from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        col_length = len(matrix[0])
        row_length = len(matrix)

        zero_row = [0] * col_length
        row_with_zero, col_with_zero = [], []

        for row_number, row in enumerate(matrix):

            for column_number, column in enumerate(row):

                if column == 0:
                    row_with_zero.append(row_number)
                    col_with_zero.append(column_number)

        for row in row_with_zero:

            matrix[row] = zero_row

        for col in col_with_zero:

            for i in range(row_length):

                matrix[i][col] = 0

        print(matrix)


solution = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix)
