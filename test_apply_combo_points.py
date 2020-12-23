from unittest import TestCase
from yahtzee import apply_combo_points


class Test(TestCase):
    def test_apply_combo_points_small_straight(self):
        test_choice = ['Small Straight', 10]
        test_player = 'player_one'
        score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                               'Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19, 'Bonus': 35}}

        combo = [(['1', '2', '3', '4', '5'], 0), ([], 0), ([], 0), ([], 25), (['1234'], 30), (['12345'], 40),
                 ([], 50), (['1', '2', '3', '4', '5'], 15)]

        actual = apply_combo_points(test_choice, score, test_player, combo)
        expected = 30
        self.assertEqual(expected, actual)

    def test_apply_combo_points_chance(self):
        test_choice = ['Chance', 13]
        test_player = 'player_one'
        score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                               'Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': -1, 'Bonus': 35}}

        combo = [(['1', '2', '3', '4', '5'], 0), ([], 0), ([], 0), ([], 25), (['1234'], 30), (['12345'], 40),
                 ([], 50), (['1', '2', '3', '4', '5'], 15)]

        actual = apply_combo_points(test_choice, score, test_player, combo)
        expected = 15
        self.assertEqual(expected, actual)

    def test_apply_combo_points_yahtzee(self):
        test_choice = ['YAHTZEE', 12]
        test_player = 'player_one'
        score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                               'Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': -1, 'Chance': 19, 'Bonus': 35}}

        combo = [(['1', '2', '3', '4', '5'], 0), ([], 0), ([], 0), ([], 25), (['1234'], 30), (['12345'], 40),
                 ([], 50), (['1', '2', '3', '4', '5'], 15)]

        actual = apply_combo_points(test_choice, score, test_player, combo)
        expected = 0
        self.assertEqual(expected, actual)

    def test_apply_combo_points_ones(self):
        test_choice = ['Ones', 1]
        test_player = 'player_one'
        score = {test_player: {'Ones': -1, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                               'Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': -1, 'Chance': 19, 'Bonus': 35}}

        combo = [(['1', '2', '3', '4', '5'], 1), ([], 0), ([], 0), ([], 25), (['1234'], 30), (['12345'], 40),
                 ([], 50), (['1', '2', '3', '4', '5'], 15)]

        actual = apply_combo_points(test_choice, score, test_player, combo)
        expected = 1
        self.assertEqual(expected, actual)