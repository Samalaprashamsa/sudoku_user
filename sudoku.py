class Sudoku:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        # Check if the number is already in the row or column
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        # Check if the number is already in the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return self.board

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return self.board

                # Backtrack if the current configuration is invalid
                self.board[row][col] = 0

        return None
