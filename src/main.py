# main.py
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    # Find all empty cells
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)

def main():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            print(f"Player {current_player}'s turn.")
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] != " ":
                    print("Cell is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
        else:
            print("Computer's turn.")
            move = computer_move(board)
            if move:
                row, col = move

        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()