from unittest import TestCase
from yahtzee import check_bonus


class TestCheckBonus(TestCase):
    def test_check_bonus_update_bonus_35(self):
        player = 'player_one'
        scorecard = {'player_one': {'Ones': 3, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                                    'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                                    'Small Straight': 30, 'Large Straight': 40, 'Chance': 19, 'YAHTZEE': 0}}
        check_bonus(scorecard, player)

        expected_scorecard = {'player_one': {'Ones': 3, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 25,
                                             'Sixes': 30, 'Three of a Kind': 12, 'Four of a Kind': 16,
                                             'Full House': 25, 'Small Straight': 30, 'Large Straight': 40,
                                             'Chance': 19, 'YAHTZEE': 0, 'Bonus': 35}}

        self.assertEqual(scorecard, expected_scorecard)

    def test_check_bonus_update_bonus_0(self):
        player = 'player_two'
        scorecard = {'player_two': {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
                                    'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                                    'Small Straight': 30, 'Large Straight': 40, 'Chance': 19, 'YAHTZEE': 0}}

        check_bonus(scorecard, player)

        expected_scorecard = {'player_two': {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5,
                                             'Sixes': 6, 'Three of a Kind': 12, 'Four of a Kind': 16,
                                             'Full House': 25, 'Small Straight': 30, 'Large Straight': 40,
                                             'Chance': 19, 'YAHTZEE': 0, 'Bonus': 0}}

        self.assertEqual(scorecard, expected_scorecard)

    def test_check_bonus_update_bonus_scorecard_not_filled(self):
        player = 'player_three'
        scorecard = {'player_three': {'Ones': -1, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25,
                                      'Sixes': 30, 'Three of a Kind': 12, 'Four of a Kind': 16,
                                      'Full House': 25, 'Small Straight': 30, 'Large Straight': 40,
                                      'Chance': 19, 'YAHTZEE': 0}}
        check_bonus(scorecard, player)

        expected_scorecard = {'player_three': {'Ones': -1, 'Twos': 8, 'Threes': 9, 'Fours': 16, 'Fives': 25,
                                               'Sixes': 30, 'Three of a Kind': 12, 'Four of a Kind': 16,
                                               'Full House': 25, 'Small Straight': 30, 'Large Straight': 40,
                                               'Chance': 19, 'YAHTZEE': 0, }}

        self.assertEqual(scorecard, expected_scorecard)
