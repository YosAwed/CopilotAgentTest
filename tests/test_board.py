import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board(self):
        self.assertEqual(self.board.display(), [[' ' for _ in range(3)] for _ in range(3)])

    def test_update_board(self):
        self.board.update(0, 0, 'X')
        self.assertEqual(self.board.display()[0][0], 'X')

    def test_is_full(self):
        for i in range(3):
            for j in range(3):
                self.board.update(i, j, 'X')
        self.assertTrue(self.board.is_full())

    def test_display(self):
        self.board.update(0, 0, 'X')
        self.board.update(1, 1, 'O')
        expected_display = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.board.display(), expected_display)

if __name__ == '__main__':
    unittest.main()