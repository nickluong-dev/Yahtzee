from unittest import TestCase
from yahtzee import update_scorecard


class TestUpdateScorecard(TestCase):
    def test_update_scorecard_ones(self):
        combo = 4
        update_choice = ['Ones', 1]
        scorecard = {'player_one': {'Ones': -1, 'Twos': 4, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                    'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                    'Small Straight': -1, 'Large Straight': 40, 'Chance': -1, 'YAHTZEE': -1}}
        player = 'player_one'
        update_scorecard(combo, update_choice, scorecard, player)
        new_scorecard = {'player_one': {'Ones': 4, 'Twos': 4, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                        'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                        'Small Straight': -1, 'Large Straight': 40, 'Chance': -1, 'YAHTZEE': -1}}
        self.assertEqual(scorecard, new_scorecard)

    def test_update_scorecard_small_straight(self):
        combo = 25
        update_choice = ['Small Straight', 10]
        scorecard = {'player_one': {'Ones': -1, 'Twos': 4, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                    'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                    'Small Straight': -1, 'Large Straight': -1, 'Chance': -1, 'YAHTZEE': -1}}
        player = 'player_one'
        update_scorecard(combo, update_choice, scorecard, player)
        new_scorecard = {'player_one': {'Ones': -1, 'Twos': 4, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                        'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                        'Small Straight': 25, 'Large Straight': -1, 'Chance': -1, 'YAHTZEE': -1}}
        self.assertEqual(scorecard, new_scorecard)

    def test_update_scorecard_first_yahtzee(self):
        combo = 50
        update_choice = ['YAHTZEE', 12]
        scorecard = {'player_one': {'Ones': -1, 'Twos': -1, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                    'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                    'Small Straight': -1, 'Large Straight': -1, 'Chance': -1, 'YAHTZEE': -1}}
        player = 'player_one'
        update_scorecard(combo, update_choice, scorecard, player)
        new_scorecard = {'player_one': {'Ones': -1, 'Twos': -1, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                        'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                        'Small Straight': -1, 'Large Straight': -1, 'Chance': -1, 'YAHTZEE': 50}}
        self.assertEqual(scorecard, new_scorecard)

    def test_update_scorecard_second_yahtzee(self):
        combo = 100
        update_choice = ['YAHTZEE', 12]
        scorecard = {'player_one': {'Ones': 4, 'Twos': -1, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                    'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                    'Small Straight': -1, 'Large Straight': -1, 'Chance': -1, 'YAHTZEE': 50}}
        player = 'player_one'
        update_scorecard(combo, update_choice, scorecard, player)
        new_scorecard = {'player_one': {'Ones': 4, 'Twos': -1, 'Threes': 3, 'Fours': 4, 'Fives': -1, 'Sixes': -1,
                                        'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                                        'Small Straight': -1, 'Large Straight': -1, 'Chance': -1, 'YAHTZEE': 150}}
        self.assertEqual(new_scorecard, scorecard)