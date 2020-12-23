from unittest import TestCase
from yahtzee import ask_where_to_apply_points
from unittest.mock import patch


class TestAskWhereToApplyPoints(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_ask_where_to_apply_points_first_item(self, mock_output):
        options = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                   ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1),
                   ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        actual = ask_where_to_apply_points(options)
        expected = ['Ones', 1]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['6'])
    def test_ask_where_to_apply_points_six(self, mock_output):
        player = 'player_one'
        options = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                   ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1),
                   ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        actual = ask_where_to_apply_points(options)
        expected = ['Sixes', 6]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['10'])
    def test_ask_where_to_apply_points_ten(self, mock_output):
        options = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                   ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1),
                   ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        actual = ask_where_to_apply_points(options)
        expected = ['Small Straight', 10]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['13'])
    def test_ask_where_to_apply_points_last_item(self, mock_output):
        options = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                   ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1),
                   ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        actual = ask_where_to_apply_points(options)
        expected = ['Chance', 13]
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['12'])
    def test_ask_where_to_apply_points_YAHTZEE(self, mock_output):
        options = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                   ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1),
                   ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        actual = ask_where_to_apply_points(options)
        expected = ['YAHTZEE', 12]
        self.assertEqual(actual, expected)

