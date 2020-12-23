from unittest import TestCase
from unittest.mock import patch
from yahtzee import keep


class TestKeep(TestCase):
    @patch('builtins.input', side_effect=['1', '2', ''])
    def test_keep_two_die(self, mock_input):
        inventory = []
        rolls = [1, 2, 4, 5, 2]
        keep(inventory, rolls)
        expected_inv = [1, 2]
        expected_rolls = [4, 5, 2]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['2', '3', '4', '4', ''])
    def test_keep_four_die(self, mock_input):
        inventory = []
        rolls = [2, 3, 4, 4, 2]
        keep(inventory, rolls)
        expected_inv = [2, 3, 4, 4]
        expected_rolls = [2]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=[''])
    def test_keep_end(self, mock_input):
        inventory = []
        rolls = [1, 2, 3, 4, 6]
        keep(inventory, rolls)
        expected_inv = []
        expected_rolls = [1, 2, 3, 4, 6]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['6', '5', '5', '4', '3', ''])
    def test_keep_all(self, mock_input):
        inventory = []
        rolls = [6, 5, 5, 4, 3]
        keep(inventory, rolls)
        expected_inv = [6, 5, 5, 4, 3]
        expected_rolls = []
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['6', '6', '6', '6', '6', ''])
    def test_keep_repeating_die(self, mock_input):
        inventory = []
        rolls = [6, 6, 6, 6, 6]
        keep(inventory, rolls)
        expected_inv = [6, 6, 6, 6, 6]
        expected_rolls = []
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)

    @patch('builtins.input', side_effect=['a', '9', '!', 'asdf', ''])
    def test_keep_invalid_choices(self, mock_input):
        inventory = []
        rolls = [5, 4, 4, 1, 3]
        keep(inventory, rolls)
        expected_inv = []
        expected_rolls = [5, 4, 4, 1, 3]
        self.assertEqual(expected_inv, inventory)
        self.assertEqual(expected_rolls, rolls)



