from unittest import TestCase
from yahtzee import create_scorecard


class TestCreateScorecard(TestCase):
    def test_create_scorecard(self):
        actual = create_scorecard('player_one')
        expected = {'player_one': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '', 'Fives': '', 'Sixes': '',
                                   'Three of a Kind': '', 'Four of a Kind': '', 'Full House': '', 'Small Straight': '',
                                   'Large Straight': '', 'Chance': '', 'YAHTZEE': ''}}
        self.assertEqual(expected, actual)
