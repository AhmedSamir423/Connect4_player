# Connect 4 Game with AI

A Connect 4 game implementation with both Human and AI players. The game includes a graphical user interface (GUI) built with Tkinter, allowing players to play against each other or an AI. The AI is powered by various algorithms, such as Minimax and AlphaBeta, to simulate intelligent decision-making.

## Features

- **Human vs Human Mode**: Two players can play against each other on the same device.
- **Human vs AI Mode**: Play against an AI with configurable algorithms.
- **AI Algorithms**: Choose between different algorithms like Minimax, AlphaBeta, and others for the AI.
- **GUI Interface**: A visually appealing Tkinter-based interface to interact with the game.
- **Move Timer**: Displays the time taken by the AI to make a move.
- **Game Stats**: Tracks and displays the current score and move time.
- **Reset Function**: Allows resetting the game at any time.
- **Game Over Detection**: Automatically detects and displays the winner or if it's a draw.

## Technologies Used

- **Python**: The main programming language.
- **Tkinter**: For the graphical user interface (GUI).
- **NumPy**: Used to handle the board's data structure efficiently.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/AhmedSamir423/Connect4_player.git
    ```

2. Navigate to the project folder:

    ```bash
    cd connect4-ai
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    **Note**: `requirements.txt` may contain dependencies such as `numpy` and `tkinter`. If `tkinter` is not installed, you can install it via:

    ```bash
    sudo apt-get install python3-tk   # On Linux
    brew install python-tk            # On macOS
    ```

## Running the Game

To start the game, run the `game.py` script:

```bash
python GUI.py
```

This will open the GUI where you can select the AI algorithm and start playing.

## Gameplay

- The game consists of two players: **Human** and **AI**.
- **Human**: The player interacts with the game through the GUI by clicking on the columns to drop their discs.
- **AI**: The AI will automatically make its moves using the selected algorithm (Minimax, AlphaBeta, etc.).
- The game ends when the board is full or when one player connects four discs in a row (horizontally, vertically, or diagonally).
- The game will display the winner and the final score at the end.

## Algorithms

The AI can be configured with different algorithms for decision-making:

1. **Minimax**: A basic algorithm that searches for the best move by simulating all possible moves and their outcomes.
2. **AlphaBeta Pruning**: An optimized version of Minimax, reducing the number of possible moves to evaluate by pruning branches that do not need to be explored.

You can choose the algorithm through the GUI at the start of the game.

## Screenshots

![image](https://github.com/user-attachments/assets/50422d55-b913-4f44-869d-648b523bf8fe)


## Contributing

If you would like to contribute to the project, feel free to fork the repository and submit a pull request. Contributions can include:

- Bug fixes
- New features (such as additional AI algorithms)
- UI improvements
- Documentation updates

Please ensure that your contributions follow the project's coding standards.
