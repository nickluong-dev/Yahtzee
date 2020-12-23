from unittest import TestCase
from yahtzee import check_combos


class TestCheckCombos(TestCase):
    def test_check_ones(self):
        apply_choice = ['Ones', 1]
        die_on_table = [1, 2, 4, 2]
        die_in_hand = [1]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['1', '1', '2', '2', '4'], 2), ([], 10), ([], 10), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['1', '1', '2', '2', '4'], 10)]
        self.assertEqual(expected, actual)

    def test_check_twos(self):
        apply_choice = ['Twos', 2]
        die_on_table = [2, 2, 4, 2]
        die_in_hand = [3]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['2', '2', '2', '3', '4'], 6), (['2'], 13), ([], 13), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['2', '2', '2', '3', '4'], 13)]
        self.assertEqual(expected, actual)

    def test_check_threes(self):
        apply_choice = ['Threes', 3]
        die_on_table = [2, 2, 4, 2]
        die_in_hand = [3]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['2', '2', '2', '3', '4'], 3), (['2'], 13), ([], 13), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['2', '2', '2', '3', '4'], 13)]
        self.assertEqual(expected, actual)

    def test_check_fours(self):
        apply_choice = ['Fours', 4]
        die_on_table = [2, 2, 4, 2]
        die_in_hand = [3]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['2', '2', '2', '3', '4'], 4), (['2'], 13), ([], 13), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['2', '2', '2', '3', '4'], 13)]
        self.assertEqual(expected, actual)

    def test_check_fives(self):
        apply_choice = ['Fives', 5]
        die_on_table = [5, 5, 4, 2]
        die_in_hand = [3]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['2', '3', '4', '5', '5'], 10), ([], 19), ([], 19), ([], 25), (['23455'], 30), ([], 40), ([], 50),
                    (['2', '3', '4', '5', '5'], 19)]
        self.assertEqual(expected, actual)

    def test_check_sixes(self):
        apply_choice = ['Sixes', 6]
        die_on_table = [5, 6, 4, 6]
        die_in_hand = [6]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['4', '5', '6', '6', '6'], 18), (['6'], 27), ([], 27), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['4', '5', '6', '6', '6'], 27)]
        self.assertEqual(expected, actual)

    def test_check_three_of_a_kind(self):
        apply_choice = ['Three of a Kind', 7]
        die_on_table = [5, 6, 4, 6]
        die_in_hand = [6]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['4', '5', '6', '6', '6'], 0), (['6'], 27), ([], 27), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['4', '5', '6', '6', '6'], 27)]
        self.assertEqual(expected, actual)

    def test_check_four_of_a_kind(self):
        apply_choice = ['Four of a Kind', 8]
        die_on_table = [2, 6, 2, 2]
        die_in_hand = [2]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['2', '2', '2', '2', '6'], 0), (['2'], 14), (['2'], 14), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['2', '2', '2', '2', '6'], 14)]
        self.assertEqual(expected, actual)

    def test_check_full_house(self):
        apply_choice = ['Full House', 9]
        die_on_table = [3, 3, 2, 2]
        die_in_hand = [2]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['2', '2', '2', '3', '3'], 0), (['2'], 12), ([], 12), ([('2', '3')], 25), ([], 30), ([], 40),
                    ([], 50), (['2', '2', '2', '3', '3'], 12)]
        self.assertEqual(expected, actual)

    def test_check_small_straight(self):
        apply_choice = ['Small Straight', 10]
        die_on_table = [2, 1, 2, 3]
        die_in_hand = [4]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['1', '2', '2', '3', '4'], 0), ([], 12), ([], 12), ([], 25), (['12234'], 30), ([], 40), ([], 50),
                    (['1', '2', '2', '3', '4'], 12)]
        self.assertEqual(expected, actual)

    def test_check_large_straight(self):
        apply_choice = ['Large Straight', 11]
        die_on_table = [5, 1, 2, 3]
        die_in_hand = [4]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['1', '2', '3', '4', '5'], 0), ([], 15), ([], 15), ([], 25), ([], 30), (['12345'], 40), ([], 50),
                    (['1', '2', '3', '4', '5'], 15)]
        self.assertEqual(expected, actual)

    def test_check_yahtzee(self):
        apply_choice = ['Large Straight', 12]
        die_on_table = [5, 5, 5]
        die_in_hand = [5, 5]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['5', '5', '5', '5', '5'], 0), (['5'], 25), (['5'], 25), ([('5', '5')], 25), ([], 30), ([], 40),
                    (['5'], 50), (['5', '5', '5', '5', '5'], 25)]
        self.assertEqual(expected, actual)

    def test_check_chance(self):
        apply_choice = ['Chance', 13]
        die_on_table = [3, 1, 2, 3]
        die_in_hand = [3]
        actual = check_combos(apply_choice, die_on_table, die_in_hand)
        expected = [(['1', '2', '3', '3', '3'], 0), (['3'], 12), ([], 12), ([], 25), ([], 30), ([], 40), ([], 50),
                    (['1', '2', '3', '3', '3'], 12)]
        self.assertEqual(expected, actual)


