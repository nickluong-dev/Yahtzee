from unittest import TestCase
from yahtzee import create_options


class TestCreateOptions(TestCase):
    def test_create_options_fully_complete_scorecard(self):
        test_player = 'one_player'
        score = {test_player: {'Ones': 1, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25, 'Small Straight': 30,
                               'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19, 'Bonus': 35}}
        actual = create_options(score, test_player)
        expected = [('Ones', 1), ('Twos', 8), ('Threes', 9), ('Fours', 4), ('Fives', 25), ('Sixes', 30),
                    ('Three of a Kind', 12), ('Four of a Kind', 16), ('Full House', 25), ('Small Straight', 30),
                    ('Large Straight', 40), ('YAHTZEE', 0), ('Chance', 19)]
        self.assertEqual(expected, actual)

    def test_create_options_with_some_empty_values(self):
        test_player = 'one_player'
        score = {test_player: {'Ones': -1, 'Twos': 8, 'Threes': 9, 'Fours': -1, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25, 'Small Straight': 30,
                               'Large Straight': 40, 'YAHTZEE': -1, 'Chance': 19, 'Bonus': 35}}
        actual = create_options(score, test_player)
        expected = [('Ones', -1), ('Twos', 8), ('Threes', 9), ('Fours', -1), ('Fives', 25), ('Sixes', 30),
                    ('Three of a Kind', 12), ('Four of a Kind', 16), ('Full House', 25), ('Small Straight', 30),
                    ('Large Straight', 40), ('YAHTZEE', -1), ('Chance', 19)]
        self.assertEqual(expected, actual)

    def test_create_options_with_all_empty_values(self):
        test_player = 'one_player'
        score = {test_player: {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1,
                               'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1, 'Small Straight': -1,
                               'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1, 'Bonus': -1}}
        actual = create_options(score, test_player)
        expected = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                    ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1),
                    ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        self.assertEqual(expected, actual)
