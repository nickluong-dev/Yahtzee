from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_scorecard


class TestPrintScorecard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scorecard_all_fields_complete(self, mock_output):
        test_player = 'player_one'
        score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25,
                               'Small Straight': 30, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19,
                               'Bonus': 35}}
        print_scorecard(score, test_player)
        expected = """player_one's Scorecard
------------------------------
Ones                         2
Twos                         8
Threes                       9
Fours                        4
Fives                       25
Sixes                       30
Three of a Kind             12
Four of a Kind              16
Full House                  25
Small Straight              30
Large Straight              40
YAHTZEE                      0
Chance                      19
Bonus                       35\n"""

        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scorecard_missing_fields(self, mock_output):
        test_player = 'player_one'
        score = {test_player: {'Ones': -1, 'Twos': 8, 'Threes': -1, 'Fours': 4, 'Fives': 25, 'Sixes': 30,
                               'Three of a Kind': 12, 'Four of a Kind': -1, 'Full House': 25,
                               'Small Straight': 30, 'Large Straight': -1,  'YAHTZEE': 0, 'Chance': 19,
                               'Bonus': 35}}
        print_scorecard(score, test_player)
        expected = """player_one's Scorecard
------------------------------
Ones                          
Twos                         8
Threes                        
Fours                        4
Fives                       25
Sixes                       30
Three of a Kind             12
Four of a Kind                
Full House                  25
Small Straight              30
Large Straight                
YAHTZEE                      0
Chance                      19
Bonus                       35\n"""

        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scorecard_no_bonus(self, mock_output):
        test_player = 'player_one'
        score = {test_player: {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6,
                               'Three of a Kind': 12, 'Four of a Kind': 9, 'Full House': 25,
                               'Small Straight': 30, 'Large Straight': -1,  'YAHTZEE': 0, 'Chance': 19}}
        print_scorecard(score, test_player)
        expected = """player_one's Scorecard
------------------------------
Ones                         1
Twos                         2
Threes                       3
Fours                        4
Fives                        5
Sixes                        6
Three of a Kind             12
Four of a Kind               9
Full House                  25
Small Straight              30
Large Straight                
YAHTZEE                      0
Chance                      19\n"""

        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_empty_scorecard(self, mock_output):
        test_player = 'player_one'
        score = {test_player: {'One': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1,
                               'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1,
                               'Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1}}
        print_scorecard(score, test_player)
        expected = """player_one's Scorecard
------------------------------
One                           
Twos                          
Threes                        
Fours                         
Fives                         
Sixes                         
Three of a Kind               
Four of a Kind                
Full House                    
Small Straight                
Large Straight                
YAHTZEE                       
Chance                        
"""

        self.assertEqual(expected, mock_output.getvalue())
