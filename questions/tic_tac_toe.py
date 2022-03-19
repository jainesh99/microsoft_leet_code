class TicTacToe:
    # def __init__(self, n: int):
    #     self._players = {1: 0, 2: 0}
    #     self._player_symbol = {1: "X", 2: "0"}
    #     self._board = [["" for i in range(n)] for j in range(n)]
    #     self._dimension = n
    #     self._diagonal_1 = [(index, index) for index in range(n)]
    #     self._diagonal_2 = []
    #     self._corner = [0, self._dimension - 1]
    #     self._diagonal_2.append((self._corner[0], self._corner[1]))
    #
    #     while len(self._diagonal_2) != self._dimension:
    #         self._corner[0] += 1
    #         self._corner[1] -= 1
    #         self._diagonal_2.append((self._corner[0], self._corner[1]))
    #
    # def move(self, row: int, col: int, player: int) -> int:
    #
    #     self._board[row][col] = self._player_symbol[player]
    #     self._players[player] += 1
    #
    #     if self._players[player] >= self._dimension:
    #         if self._check_win(row, col, player):
    #             return player
    #
    #     return 0
    #
    # def _check_win(self, row: int, col: int, player: int):
    #
    #     winning_set = set(self._player_symbol[player])
    #     column_win = {self._board[index][col] for index in range(self._dimension)}
    #     row_win = {self._board[row][index] for index in range(self._dimension)}
    #     diagonal_1_win = {self._board[index][index] for index in range(self._dimension)}
    #     diagonal_2_win = {self._board[row][col] for row, col in self._diagonal_2}
    #
    #     if (
    #         column_win == winning_set
    #         or row_win == winning_set
    #         or diagonal_1_win == winning_set
    #         or diagonal_2_win == winning_set
    #     ):
    #         return True
    #
    #     return False
    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = [0] * 2

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.diagonal[0] += 1
            if row + col == self.n - 1:
                self.diagonal[1] += 1
            if (
                self.row[row] == self.n
                or self.col[col] == self.n
                or self.diagonal[0] == self.n
                or self.diagonal[1] == self.n
            ):
                return 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.diagonal[0] -= 1
            if row + col == self.n - 1:
                self.diagonal[1] -= 1
            if (
                self.row[row] == -self.n
                or self.col[col] == -self.n
                or self.diagonal[0] == -self.n
                or self.diagonal[1] == -self.n
            ):
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# n = 3
# ticTacToe = TicTacToe(n)
# win_list = [
#     ticTacToe.move(0, 0, 1),
#     ticTacToe.move(0, 2, 2),
#     ticTacToe.move(2, 2, 1),
#     ticTacToe.move(1, 1, 2),
#     ticTacToe.move(2, 0, 1),
#     ticTacToe.move(1, 0, 2),
#     ticTacToe.move(2, 1, 1),
# ]

n = 2
ticTacToe = TicTacToe(n)
win_list = [
    ticTacToe.move(0, 1, 1),
    ticTacToe.move(1, 1, 2),
    ticTacToe.move(1, 0, 1),
]
print(win_list)
