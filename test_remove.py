from unittest.mock import patch
from yahtzee import remove
from unittest import TestCase


class TestKeep(TestCase):
    @patch('builtins.input', side_effect=['1', '2', ''])
    def test_remove_two(self, mock_input):
        inventory = [1, 2]
        rolls = [4, 5, 2]
        remove(inventory, rolls)
        expected_inv = []
        expected_rolls = [4, 5, 2, 1, 2]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['1', '2', '4', '5', ''])
    def test_remove_four(self, mock_input):
        inventory = [1, 2, 4, 5]
        rolls = [6]
        remove(inventory, rolls)
        expected_inv = []
        expected_rolls = [6, 1, 2, 4, 5]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=[''])
    def test_remove_end(self, mock_input):
        inventory = [1, 2]
        rolls = [6, 5, 3]
        remove(inventory, rolls)
        expected_inv = [1, 2]
        expected_rolls = [6, 5, 3]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['5', '4', '6', '5', '3', ''])
    def test_remove_all(self, mock_input):
        inventory = [5, 4, 6, 5, 3]
        rolls = []
        remove(inventory, rolls)
        expected_inv = []
        expected_rolls = [5, 4, 6, 5, 3]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['5', '5', '5', '5', '5', ''])
    def test_remove_repeating(self, mock_input):
        inventory = [5, 5, 5, 5, 5]
        rolls = []
        remove(inventory, rolls)
        expected_inv = []
        expected_rolls = [5, 5, 5, 5, 5]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)
