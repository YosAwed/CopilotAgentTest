class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state

    def display(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def update(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def is_full(self):
        return ' ' not in self.board