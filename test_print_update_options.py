from unittest import TestCase
from yahtzee import print_update_options
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_update_options_partial_scores(self, mock_output):
        test_options = [('Ones', 4), ('Twos', 6), ('Threes', 12), ('Fours', 16), ('Fives', 25), ('Sixes', 30),
                        ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1),
                        ('Small Straight', -1), ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1), ('Bonus', 35)]
        print_update_options(test_options)
        expected = """1    Ones                4              
2    Twos                6              
3    Threes              12             
4    Fours               16             
5    Fives               25             
6    Sixes               30             
7    Three of a Kind                    
8    Four of a Kind                     
9    Full House                         
10   Small Straight                     
11   Large Straight                     
12   YAHTZEE                            
13   Chance                             
14   Bonus               35             
"""

        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_update_options_complete_scores(self, mock_output):
        test_options = [('Ones', 4), ('Twos', 6), ('Threes', 12), ('Fours', 16), ('Fives', 25), ('Sixes', 30),
                        ('Three of a Kind', 13), ('Four of a Kind', 15), ('Full House', 25),
                        ('Small Straight', 30), ('Large Straight', 40), ('YAHTZEE', 0), ('Chance', 19), ('Bonus', 35)]
        print_update_options(test_options)
        expected = """1    Ones                4              
2    Twos                6              
3    Threes              12             
4    Fours               16             
5    Fives               25             
6    Sixes               30             
7    Three of a Kind     13             
8    Four of a Kind      15             
9    Full House          25             
10   Small Straight      30             
11   Large Straight      40             
12   YAHTZEE             0              
13   Chance              19             
14   Bonus               35             
"""

        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_update_options_all_empty_scores(self, mock_output):
        test_options = [('Ones', -1), ('Twos', -1), ('Threes', -1), ('Fours', -1), ('Fives', -1), ('Sixes', -1),
                        ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1),
                        ('Small Straight', -1), ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1)]
        print_update_options(test_options)
        expected = """1    Ones                               
2    Twos                               
3    Threes                             
4    Fours                              
5    Fives                              
6    Sixes                              
7    Three of a Kind                    
8    Four of a Kind                     
9    Full House                         
10   Small Straight                     
11   Large Straight                     
12   YAHTZEE                            
13   Chance                             
"""

        self.assertEqual(expected, mock_output.getvalue())