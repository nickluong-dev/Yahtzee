from unittest import TestCase
from yahtzee import check_winner
from unittest.mock import patch
import io


class TestCheckWinner(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_winner_player_one(self, mock_output):
        player_one = 'player_one'
        player_two = 'player_two'
        player_one_score = {player_one: {'Ones': 3, 'Twos': 4, 'Threes': 6, 'Fours': 8, 'Fives': 15, 'Sixes': -6,
                                         'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                                         'Small Straight': 30, 'Large Straight': 40, 'YAHTZEE': 50, 'Chance': 19}}
        player_two_score = {player_two: {'Ones': 4, 'Twos': 4, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
                                         'Three of a Kind': 13, 'Four of a Kind': 16, 'Full House': 25,
                                         'Small Straight': 0, 'Large Straight': 40, 'YAHTZEE': 50, 'Chance': 12}}
        check_winner(player_one, player_one_score, player_two, player_two_score)
        expected = "player_one wins! You scored: 222. You absorb player two's soul and become stronger.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_winner_player_two(self, mock_output):
        player_one = 'player_one'
        player_two = 'player_two'
        player_one_score = {player_one: {'Ones': 3, 'Twos': 4, 'Threes': 6, 'Fours': 8, 'Fives': 15, 'Sixes': -6,
                                         'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                                         'Small Straight': 30, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19}}
        player_two_score = {player_two: {'Ones': 4, 'Twos': 8, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
                                         'Three of a Kind': 13, 'Four of a Kind': 16, 'Full House': 25,
                                         'Small Straight': 0, 'Large Straight': 40, 'YAHTZEE': 50, 'Chance': 12}}
        check_winner(player_one, player_one_score, player_two, player_two_score)
        expected = "player_two wins! You scored: 186. You attack player one's life points directly, \n" \
                   "sending him to the shadow realm.\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_winner_draw(self, mock_output):
        player_one = 'player_one'
        player_two = 'player_two'
        player_one_score = {player_one: {'Ones': 3, 'Twos': 4, 'Threes': 6, 'Fours': 8, 'Fives': 15, 'Sixes': -6,
                                         'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                                         'Small Straight': 30, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19}}
        player_two_score = {player_two: {'Ones': 3, 'Twos': 4, 'Threes': 6, 'Fours': 8, 'Fives': 15, 'Sixes': -6,
                                         'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                                         'Small Straight': 30, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19}}
        check_winner(player_one, player_one_score, player_two, player_two_score)
        expected = "Both players scored 172. . .You both turn to dust, snapped out of existence.\n"
        self.assertEqual(expected, mock_output.getvalue())