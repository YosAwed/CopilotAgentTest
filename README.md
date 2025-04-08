# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to take turns marking their spaces on a 3x3 grid until one player wins or the game ends in a draw.

## Project Structure

```
tic-tac-toe
├── src
│   ├── main.py        # Entry point of the game
│   ├── game.py        # Game logic and state management
│   ├── board.py       # Board representation and management
│   └── utils.py       # Utility functions
├── tests
│   ├── test_game.py   # Unit tests for the Game class
│   ├── test_board.py  # Unit tests for the Board class
│   └── test_utils.py  # Unit tests for utility functions
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## How to Run the Game

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing:
   ```
   python src/main.py
   ```

## Features

- Two-player mode
- Input validation
- Displays the game board after each move
- Checks for a winner or a draw

## Testing

To run the tests, ensure you have the necessary testing libraries installed and execute:
```
pytest
```

## License

This project is open-source and available under the MIT License.