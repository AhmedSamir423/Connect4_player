import numpy as np
class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)

    def play_disc(self, player, column):
        if self.valid_move(column):
            for row in range(self.rows - 1, -1, -1):
                if self.board[row][column] == 0:
                    self.board[row][column] = player.symbol
                    break

    def valid_move(self, column):
        return self.board[0][column] == 0

    def get_valid_moves(self):
        return [col for col in range(self.cols) if self.valid_move(col)]

    def undo_move(self, column):
        for row in range(self.rows):
            if self.board[row][column] != 0:
                self.board[row][column] = 0
                break

    def print_board(self):
        for row in self.board:
            print(" ".join(str(int(cell)) if cell != 0 else '.' for cell in row))

    def is_full(self):
        return np.all(self.board != 0)

    def check_line(self, start_row, start_col, delta_row, delta_col, player_symbol):
        count = 0
        for i in range(4):
            row = start_row + i * delta_row
            col = start_col + i * delta_col
            if 0 <= row < self.rows and 0 <= col < self.cols and self.board[row][col] == player_symbol:
                count += 1
            else:
                break
        return count == 4

    def count_connected_fours(self, player_symbol):
        """Count all connected fours for the given player symbol."""
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == player_symbol:
                    # Check all directions
                    if self.check_line(row, col, 0, 1, player_symbol):  # Horizontal
                        count += 1
                    if self.check_line(row, col, 1, 0, player_symbol):  # Vertical
                        count += 1
                    if self.check_line(row, col, 1, 1, player_symbol):  # Diagonal /
                        count += 1
                    if self.check_line(row, col, 1, -1, player_symbol):  # Diagonal \
                        count += 1
        return count

    def evaluate_board(self, ai_symbol, opponent_symbol):
        """Evaluate the board based on the number of connected fours."""
    
        ai_score = self.count_connected_fours(ai_symbol)
        opponent_score = self.count_connected_fours(opponent_symbol)
        return ai_score - opponent_score