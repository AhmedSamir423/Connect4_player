import tkinter as tk
from tkinter import messagebox
import numpy as np

from Game import Game

class Connect4GUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.board = game.board
        self.current_player = game.current_player
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Create buttons for column selection
        for col in range(self.board.cols):
            btn = tk.Button(self.root, text=f"↓", command=lambda c=col: self.drop_disc(c), height=2, width=4)
            btn.grid(row=0, column=col, sticky="nsew")
            self.buttons.append(btn)

        # Create board cells
        self.cell_labels = []
        for row in range(self.board.rows):
            row_labels = []
            for col in range(self.board.cols):
                lbl = tk.Label(self.root, text=".", font=("Arial", 24), width=4, height=2, bg="blue", fg="white", relief="ridge", borderwidth=2)
                lbl.grid(row=row + 1, column=col, sticky="nsew")
                row_labels.append(lbl)
            self.cell_labels.append(row_labels)

        # Add a reset button
        reset_btn = tk.Button(self.root, text="Reset", command=self.reset_game, height=2, width=10)
        reset_btn.grid(row=self.board.rows + 1, columnspan=self.board.cols, sticky="nsew")

        # Add score labels
        self.human_score_label = tk.Label(self.root, text="Human Score: 0", font=("Arial", 14))
        self.human_score_label.grid(row=self.board.rows + 2, column=0, sticky="w")
        self.ai_score_label = tk.Label(self.root, text="AI Score: 0", font=("Arial", 14))
        self.ai_score_label.grid(row=self.board.rows + 2, column=1, sticky="w")

    def drop_disc(self, col):
        if self.board.valid_move(col):
            self.board.play_disc(self.current_player, col)
            self.update_board()

            # Check if the game is over
            if self.check_winner():
                return

            # Switch players
            self.current_player = self.game.player2 if self.current_player == self.game.player1 else self.game.player1

            # If AI, make a move automatically
            if self.current_player.is_ai:
                self.root.after(500, self.ai_move)

        else:
            messagebox.showinfo("Invalid Move", f"Column {col} is full. Try a different one!")

    def ai_move(self):
        self.current_player.make_move(self.board)
        self.update_board()
        if not self.check_winner():
            self.current_player = self.game.player2 if self.current_player == self.game.player1 else self.game.player1

    def update_board(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                cell_value = self.board.board[row][col]
                self.cell_labels[row][col].config(text="⚪" if cell_value == 0 else ("🔴" if cell_value == 1 else "🟡"))

    def check_winner(self):
        # Only check for connected 4 when the board is full
        p1_score = self.board.count_connected_fours(self.game.player1.symbol)
        p2_score = self.board.count_connected_fours(self.game.player2.symbol)

        if self.board.is_full():
            if p1_score > p2_score:
                winner = self.game.player1.name
                message = f"Game Over! Winner: {winner}"
                self.game.player1.score += 1  # Increment score for player 1
            elif p2_score > p1_score:
                winner = self.game.player2.name
                message = f"Game Over! Winner: {winner}"
                self.game.player2.score += 1  # Increment score for player 2
            else:
                message = "Game Over! It's a draw!"

            messagebox.showinfo("Game Over", message)
            self.update_score_labels()
            self.disable_buttons()
            return True
        return False

    def update_score_labels(self):
        self.human_score_label.config(text=f"Human Score: {self.game.player1.score}")
        self.ai_score_label.config(text=f"AI Score: {self.game.player2.score}")

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.board.board = np.zeros((self.board.rows, self.board.cols), dtype=int)
        self.current_player = self.game.player1
        self.update_board()
        self.update_score_labels()  # Reset score labels
        for btn in self.buttons:
            btn.config(state=tk.NORMAL)


# Running the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Connect 4")
    game_instance = Game(algorithm="minimax")  # Use minimax or alphabeta as desired
    app = Connect4GUI(root, game_instance)
    root.mainloop()
