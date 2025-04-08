import unittest
from src.utils import validate_input, display_message
import pytest

class TestUtils(unittest.TestCase):

    def test_validate_input_valid(self):
        self.assertEqual(validate_input('X'), 'X')
        self.assertEqual(validate_input('O'), 'O')

    def test_validate_input_invalid(self):
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input('A')
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input('1')
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input('')
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input(None)

    def test_display_message(self):
        with self.assertLogs(level='INFO') as log:
            display_message("Hello, World!")
            self.assertIn("Hello, World!", log.output[0])

    def test_validate_input_edge_cases(self):
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input('x')  # Lowercase input
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input('o')  # Lowercase input
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input('XO')  # Multiple characters
        with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
            validate_input(' ')  # Whitespace

    def test_display_message_empty(self):
        with self.assertLogs(level='INFO') as log:
            display_message("")
            self.assertIn("", log.output[0])
                with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
                    validate_input('1')
                with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
                    validate_input('')
                with pytest.raises(ValueError, match="Input must be 'X' or 'O'"):
                    validate_input(None)