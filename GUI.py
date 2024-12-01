import tkinter as tk
from tkinter import messagebox
from Game import Game

class ConnectFourGUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Connect Four")
        
        # Create a canvas to draw the board
        self.canvas = tk.Canvas(self.window, width=700, height=600)
        self.canvas.pack()

        # Set up the grid
        self.cell_size = 100
        self.create_board()

        # Add buttons for each column
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack()

        # Create buttons for each column
        self.column_buttons = []
        for col in range(self.game.board.cols):
            button = tk.Button(self.buttons_frame, text=f"Column {col + 1}", 
                               command=lambda c=col: self.make_move(c))
            button.grid(row=0, column=col, padx=5)
            self.column_buttons.append(button)

    def create_board(self):
        # Draw the empty grid for the board
        for row in range(self.game.board.rows):
            for col in range(self.game.board.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="lightblue")

    def update_gui(self, row, col, player_symbol):
        # Determine the color based on the player symbol
        color = "red" if player_symbol == 1 else "yellow"
        
        # Draw the new disc in the corresponding cell
        self.canvas.create_oval(
            col * self.cell_size + 10, 
            row * self.cell_size + 10,
            (col + 1) * self.cell_size - 10, 
            (row + 1) * self.cell_size - 10,
            fill=color, outline=color
        )


    def make_move(self, col):
        if self.game.game_over:  # Check if the game is over
            return

        # If it's a human player's turn, get the column from the button press directly
        row = self.game.current_player.make_move(self.game.board)  # Pass the board object
        if row is not None:  # If the move was successful (row returned)
            self.update_board(row, col)  # Update the board on the GUI
            if self.game.is_game_over():  # Check if the game is over after the move
                self.display_winner()  # Display the winner







    def display_winner(self):
        # Show a message box with the winner
        winner = "Player 1" if self.game.current_player == 2 else "Player 2"
        messagebox.showinfo("Game Over", f"{winner} wins!")

    def reset_board(self):
        # Clear the board from the canvas
        self.canvas.delete("all")
        self.create_board()

    def run(self):
        self.window.mainloop()


# Assuming Game class is available as provided
if __name__ == "__main__":
    game = Game(algorithm="minimax")  # Choose AI algorithm
    gui = ConnectFourGUI(game)
    gui.run()
