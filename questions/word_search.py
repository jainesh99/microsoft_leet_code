from typing import List


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLUMNS = len(board), len(board[0])
        visited = [[False for _ in board[0]] for _ in board]

        def dfs(r, c, nextIndex):
            if nextIndex == len(word):
                return True
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLUMNS - 1:
                return False
            if word[nextIndex] != board[r][c] or visited[r][c]:
                return False
            visited[r][c] = True

            result = (
                dfs(r - 1, c, nextIndex + 1)
                or dfs(r, c - 1, nextIndex + 1)
                or dfs(r + 1, c, nextIndex + 1)
                or dfs(r, c + 1, nextIndex + 1)
            )
            visited[r][c] = False
            return result

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r, c, 0):
                    return True
        return False


# class Solution:
#     def _check_char_exists(
#         self,
#         row: int,
#         column: int,
#         char: str,
#         row_len: int,
#         column_len: int,
#         board: List[List[str]],
#     ):
#
#         if (row + 1) < row_len:
#             if board[row + 1][column] == char:
#                 return row + 1, column
#         if (row - 1) >= 0:
#             if board[row - 1][column] == char:
#                 return row - 1, column
#         if (column + 1) < column_len:
#             if board[row][column + 1] == char:
#                 return row, column + 1
#         if (column - 1) >= 0:
#             if board[row][column - 1] == char:
#                 return row, column - 1
#         return None
#
#     def exist(self, board: List[List[str]], word: str) -> bool:
#
#         queue = []
#         counter = 0
#         visited = set()
#         column_len = len(board[0])
#         row_len = len(board)
#
#         for row_index, row in enumerate(board):
#
#             if word[0] in row:
#                 for column_index, char in enumerate(row):
#                     if char == word[0]:
#                         queue.append((row_index, column_index))
#                         visited.add((row_index, column_index))
#
#         if queue:
#             counter = 1
#         else:
#             return False
#
#         if len(queue) == len(word):
#             return True
#
#         for char in word[1:]:
#
#             new_queue = [
#                 self._check_char_exists(row, column, char, row_len, column_len, board)
#                 for row, column in queue
#                 if self._check_char_exists(
#                     row, column, char, row_len, column_len, board
#                 )
#             ]
#
#             queue.clear()
#
#             for item in new_queue:
#                 if item not in visited:
#                     visited.add(item)
#                     queue.append(item)
#
#             if queue:
#                 counter += 1
#
#         return counter == len(word)


solution = Solution()
board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
print(solution.exist(board, word))
