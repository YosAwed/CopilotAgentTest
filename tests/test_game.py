import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_start_game(self):
        self.game.start_game()
        self.assertEqual(self.game.current_turn, 'X')
        self.assertFalse(self.game.is_game_over)

    def test_make_move(self):
        self.game.start_game()
        self.game.make_move(0, 0)  # X moves
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_turn, 'O')

    def test_make_move_invalid(self):
        self.game.start_game()
        self.game.make_move(0, 0)  # X moves
        result = self.game.make_move(0, 0)  # Invalid move
        self.assertFalse(result)

    def test_check_winner(self):
        self.game.start_game()
        self.game.make_move(0, 0)  # X
        self.game.make_move(1, 0)  # O
        self.game.make_move(0, 1)  # X
        self.game.make_move(1, 1)  # O
        self.game.make_move(0, 2)  # X wins
        self.assertTrue(self.game.check_winner('X'))

if __name__ == '__main__':
    unittest.main()