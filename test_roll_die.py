from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_die


class TestRollDie(TestCase):

    @patch('random.sample', return_value=[2, 3, 4, 5, 5])
    def test_roll_die_five(self, random_output):
        actual = roll_die(5)
        expected = [2, 3, 4, 5, 5]
        self.assertEqual(actual, expected)

    @patch('random.sample', return_value=[3, 4, 5, 5])
    def test_roll_die_four(self, random_output):
        actual = roll_die(4)
        expected = [3, 4, 5, 5]
        self.assertEqual(actual, expected)

    @patch('random.sample', return_value=[2, 1, 1])
    def test_roll_die_three(self, random_output):
        actual = roll_die(3)
        expected = [2, 1, 1]
        self.assertEqual(actual, expected)

    @patch('random.sample', return_value=[4, 6])
    def test_roll_die_two(self, random_output):
        actual = roll_die(2)
        expected = [4, 6]
        self.assertEqual(actual, expected)

    @patch('random.sample', return_value=[5])
    def test_roll_die_one(self, random_output):
        actual = roll_die(1)
        expected = [5]
        self.assertEqual(actual, expected)

    @patch('random.sample', return_value=[''])
    def test_roll_die_none(self, random_output):
        actual = roll_die(0)
        expected = ['']
        self.assertEqual(actual, expected)