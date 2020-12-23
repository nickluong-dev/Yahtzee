"""
Assignment - YAHTZEE FINAL
Nick Luong
A00972523
"""


import random
import re


def PRINT_ERROR():
    """
    Print a error message to the user if there is an invalid input in any point of the program.

    :postcondition: print a error message

    >>> PRINT_ERROR()
    Hey you made a wrong choice >:( Don't do it again. . .
    """

    print("Hey you made a wrong choice >:( Don't do it again. . .")


def YAHTZEE():
    """
    Return score of first yahtzee.

    :return: 50 as int
    """
    return 50


def ANOTHER_YAHTZEE():
    """
    Return bonus of 100 points.

    :return: 100 as int
    """
    return 100


def LARGE_STRAIGHT():
    """
    Return score of large straight.

    :return: 40 as int
    """
    return 40


def SMALL_STRAIGHT():
    """
    Return score of small straight.

    :return: 30 as int
    """
    return 30


def FULL_HOUSE():
    """
    Return score of full house.

    :return: 25 as int
    """
    return 25


def ONES_TO_SIXES_INDEX():
    """
    Return a 6 because there are 6 combos in the upper half of the score card (ones, twos, threes, fours, fives, sixes)
    which is calculated in one combo. The one combo is in check_combo().

    :return: 6 as int
    """

    return 6


def NO_POINTS():
    """
    Return a -1 to represent a blank point value.

    :return: -1 as an int
    """

    return -1


def ZERO_POINTS():
    """
    Return a 0 to represent no points

    :return: 0 as an int
    """

    return 0


def CREATE_SCORECARD(player: str) -> dict:
    """
    Create dictionary with possible score combinations as keys and possible score as values.

    A new scorecard is generated for each player at the start of the match. Keys are possible combinations and the
    values are blank placeholders for future scores.

    :param player: a string (player_one or player_two)
    :precondition: player is a string
    :postcondition: creates a scorecard for each user
    :return: a dictionary representing the scorecard
    >>> test_player = 'player_one'
    >>> CREATE_SCORECARD(test_player) # doctest: +NORMALIZE_WHITESPACE
        {'player_one': {'Ones': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1,
        'Three of a Kind': -1, 'Four of a Kind': -1, 'Full House': -1, 'Small Straight': -1, 'Large Straight': -1,
        'YAHTZEE': -1, 'Chance': -1}}
    """

    player_scorecard = {player: {'Ones': NO_POINTS(), 'Twos': NO_POINTS(), 'Threes': NO_POINTS(), 'Fours': NO_POINTS(),
                                 'Fives': NO_POINTS(), 'Sixes': NO_POINTS(),'Three of a Kind': NO_POINTS(),
                                 'Four of a Kind': NO_POINTS(), 'Full House': NO_POINTS(),
                                 'Small Straight': NO_POINTS(), 'Large Straight': NO_POINTS(), 'YAHTZEE': NO_POINTS(),
                                 'Chance': NO_POINTS()}}

    return player_scorecard


def check_bonus(scorecard: dict, player: str):
    """
    Calculate sum of score and check for possible bonus (if one to six >= 63).

    Checks the upper half of the scorecard (ones to sixes). If the upper half is filled in, the scorecard is updated
    to include a bonus of either 0 or 35 points.

    :param player: a string (player_one or player_two)
    :param scorecard: a dictionary that represents the Yahtzee scorecard
    :precondition: scorecard must be a dictionary with yahtzee combos as keys, player must be a string
    :postcondition: updates the scorecard with the new key value

    * no doctest because no print or return *
    """

    # turns values of dict to list and takes the first 6 items
    values_of_ones_to_sixes = list(scorecard[player].values())[0:6]
    if NO_POINTS() not in values_of_ones_to_sixes:

        if sum(values_of_ones_to_sixes) >= 63:
            scorecard[player]['Bonus'] = 35
        else:
            scorecard[player]['Bonus'] = 0


def print_scorecard(scorecard: dict, player: str):
    """
    Take scorecard as param and prints score table for user each round.

    Prints out a neatly formatted scorecard for the players each turn.

    :param player: a string (player_one or player_two)
    :param scorecard: a dictionary
    :precondition: scorecard must be a dictionary
    :postcondition: print out the dictionary in neat format

    >>> test_player = 'player_one'
    >>> score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30, \
                 'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25, \
                 'Small Straight': 30, 'Large Straight': 40, 'Chance': 19, 'YAHTZEE': 0, 'Bonus': 35}}
    >>> print_scorecard(score, test_player) # doctest: +NORMALIZE_WHITESPACE
    player_one's Scorecard
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
    Chance                      19
    YAHTZEE                      0
    Bonus                       35
    """

    print(f"{player}'s Scorecard")
    print('-' * 30)
    for keys, values in scorecard[player].items():
        if values == -1:
            print('{:<15s}{:>15}'.format(keys, ''))
        else:
            print('{:<15s}{:>15}'.format(keys, values))


def roll_die(available_dice: int) -> list:
    """
    Roll a number of die based on how many die have been kept and output a list of rolled die.

    Rolls dice and returns a list of ints as strings. The number of dice rolled is subtracted from how many dice are in
    the users inventory from being kept/removed.

    :param available_dice: an int based on how many die the player has in their inventory
    :precondition: available_dice must be equal to or less than 5 but greater than 0. 5 >= available_dice > 0
    :postcondition: randomly rolls 1-5 die based on available_die
    :return:a list of randomly rolled die

    * cannot doctest random *
    """

    rolls = random.sample(range(1, 7), available_dice)
    rolls_string = [num for num in rolls]
    return rolls_string


def ask_remove_keep(function, *args):
    """
    Ask user if they want to remove/keep any of the die and executes the function.

    Takes a function (keep() or remove()) as a parameter. The question to remove/keep die will depend on which function
    is passed. If the user answers 'Y', the function will be called, otherwise the function will break.

    :param function: a function (keep() or remove())
    :param args:
        arg1 - inventory: a list representing the die a player has in their possession
        arg2 - rolls: a list of randomly rolled die depending on the number of available die left to roll
    :precondition: function must be keep() or remove(). Inventory and rolls must be lists of numbers as strings.
    :postcondition: execute the function

    * no return, doctest, or unit test applicable. cannot doctest input *
    """

    while True:
        name_of_function = 'remove' if function == remove else 'keep'
        ask = input(f"Do you want to {name_of_function} any die? (Y/N) \n").strip().lower()

        if ask == 'y':

            # since keep and remove take 2 parameters, inventory and rolls
            function(args[0], args[1])
            break

        elif ask == 'n':
            break


def keep(inventory: list, rolls: list):
    """
    Ask the user what die they would like to keep and updates the player inventory and rolls on the (virtual) table. If
    the choice is invalid, the user will be prompted with an error message. If the user inputs nothing, the function
    returns the updated inventory.

    :param inventory: a list for the players kept die
    :param rolls: a list of rolled die
    :precondition: inventory and rolls must be both list
    :postcondition: updates the inventory and rolls
    """

    str_rolls = [str(nums) for nums in rolls]
    while True:
        ask_keep = input('What die value do you want to keep? Type the value. Type nothing to skip.')

        if ask_keep in str_rolls:
            rolls.remove(int(ask_keep))
            inventory.append(int(ask_keep))
        elif ask_keep == '':
            break
        else:
            PRINT_ERROR()


def remove(inventory: list, rolls: list):
    """
    Ask the user what die they would like to remove and updates the player inventory and rolls on the (virtual) table.
    If the choice is invalid, the user will be prompted with an error message. If the user inputs nothing, the function
    returns the updated inventory.

    :param inventory: a list for the players kept die
    :param rolls: a list of rolled die
    :precondition: inventory and rolls must be both list
    :postcondition: updates the inventory and rolls
    """

    str_rolls = [str(nums) for nums in inventory]
    while True:
        ask_remove = input('What die value do you want to keep? Type the value. Type nothing to skip.')

        if ask_remove in str_rolls:
            inventory.remove(int(ask_remove))
            rolls.append(int(ask_remove))
        elif ask_remove == '':
            break
        else:
            PRINT_ERROR()


def print_update_options(options: list):
    """
    Display the options available to the user to apply their points to.

    Takes the player's possible options displays options that are not filled out (aside from Yahtzee).

    :param options: a list
    :precondition: options must be a list of options that respresent the user's scorecard options

    >>> test_options = [('Ones', 4), ('Twos', 6), ('Threes', 12), ('Fours', 16), ('Fives', 25), ('Sixes', 30),\
                   ('Three of a Kind', -1), ('Four of a Kind', -1), ('Full House', -1), ('Small Straight', -1), \
                   ('Large Straight', -1), ('YAHTZEE', -1), ('Chance', -1), ('Bonus', 35)]
    >>> print_update_options(test_options) # doctest: +NORMALIZE_WHITESPACE
    1    Ones                4
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

    for seq, options in enumerate(options, 1):
        if options[1] == -1:
            print('{:<5}{:<20}{:<15}'.format(seq, options[0], ''))
        else:
            print('{:<5}{:<20}{:<15}'.format(seq, options[0], options[1]))


def create_options(scorecard: dict, player: str) -> list:
    """
    Create a list to display the different options for the user to choose from in print_update_options().

    :param scorecard: a dictionary
    :param player: a string
    :precondition: scorecard must be a valid dictionary with keys as ints (-1 for no points)
    :postcondition: create list of tuples for options
    :return: a list of possible options for the user to choose from

    >>> test_player = 'one_player'
    >>> score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30, \
                 'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25, \
                 'Small Straight': 30, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19, 'Bonus': 35}}
    >>> create_options(score, test_player) # doctest: +NORMALIZE_WHITESPACE
    [('Ones', 2), ('Twos', 8), ('Threes', 9), ('Fours', 4), ('Fives', 25), ('Sixes', 30), ('Three of a Kind', 12), \
    ('Four of a Kind', 16), ('Full House', 25), ('Small Straight', 30), ('Large Straight', 40), ('YAHTZEE', 0), \
    ('Chance', 19)]
    """

    options = [(key, value) for key, value in scorecard[player].items()]

    # remove 'bonus' because player can't choose to adjust bonus
    for items in range(len(options)):
        if 'Bonus' in options[items]:
            options.remove(options[items])
    return options


def ask_where_to_apply_points(options: list) -> list:
    """
    Ask which part of they would like to apply their hand/points to.

    Asks the user which part of the scorecard (enumerated list) they want to apply their points. After getting the
    players input, returns a number as a string representing their enumerated choice. Will check if the option the user
    wants to apply their points to already is filled in.

    :param options: a list
    :precondition: options must be a list with valid scoreboard choices
    :postcondition: returns a list
    :return: a list where the first item is a string for the option choice and second item is the index of the option

    * no doctest because of user input *
    """

    print_update_options(options)
    while True:
        try:
            choice = input("What option do you want to apply your hand to? Choose the corresponding number:")

            if int(choice) in range(1, 14):

                # if you get a yahtzee again somehow..
                if options[int(choice) - 1][0] == 'YAHTZEE' and options[int(choice) - 1][1] > ZERO_POINTS():
                    return [options[int(choice) - 1][0], int(choice)]

                # if a choice already is filled in
                elif options[int(choice) - 1][1] != NO_POINTS():
                    PRINT_ERROR()

                else:
                    # eg. ['Three of a Kind', 7]
                    return [options[int(choice) - 1][0], int(choice)]

        except (ValueError, TypeError):
            PRINT_ERROR()


def check_combos(update_choice: list, rolls: list, inventory: list) -> list:
    """
    Check the possible combinations from rolled_die with regex and output a possible a list representing the value of
    a string representing the combo.

    Checks the values of possible combos. After taking the values of die in the players hand/inventory and on the table,
    it will a list of possible score values for the given die in the player hand and table. This info will be applied
    in apply_combo_points(). The outputted information will be a list of the regex findall of the hand for ones to
    sixes, three of a kind, four of a kind, full house, small straight, large straight, yahtzee, and chance.

    :param update_choice: a list representing what the user wants to apply their points to
    :param rolls: a list for what die are left on the table
    :param inventory: a list for what die the player has kept in their hand/inventory
    :return: a list of tuples representing the possible combos and their points that can be applied

    >>> apply_choice = ['Three of a Kind', 7]
    >>> die_on_table = [1, 4, 3]
    >>> die_in_hand = [4, 4]
    >>> check_combos(apply_choice, die_on_table, die_in_hand) # doctest: +NORMALIZE_WHITESPACE
    [(['1', '3', '4', '4', '4'], 0), (['4'], 16), ([], 16), ([], 25), ([], 30), ([], 40), ([], 50),
    (['1', '3', '4', '4', '4'], 16)]

    >>> apply_choice = ['Small Straight', 10]
    >>> die_on_table = [2, 3, 3]
    >>> die_in_hand = [4, 5]
    >>> check_combos(apply_choice, die_on_table, die_in_hand) # doctest: +NORMALIZE_WHITESPACE
    [(['2', '3', '3', '4', '5'], 0), ([], 17), ([], 17), ([], 25), (['23345'], 30), ([], 40), ([], 50),
    (['2', '3', '3', '4', '5'], 17)]
    """

    all_die = "".join(str(nums) for nums in sorted(inventory + rolls))
    apply_points_to_index = update_choice[1]

    # all the ugly regex
    one_to_six = re.compile(r'[1-6]').findall(all_die)
    three_of_a_kind = re.compile(r'([1-6])\1{2}').findall(all_die)
    four_of_a_kind = re.compile(r'([1-6])\1{3}').findall(all_die)
    full_house = re.compile(r'([1-6])\1{2}([1-6])\2').findall(all_die) or \
        re.compile(r'([1-6])\1([1-6])\2{2}').findall(all_die)  # if the three of a kind is first or second
    small_straight = re.compile(r'(11234|12234|12334|12344|22345|23345|23445|23455|33456|34456|34556|34566)')\
        .findall(all_die) 
    large_straight = re.compile(r'(12345|23456)').findall(all_die)
    yahtzee = re.compile(r'([1-6])\1{4}').findall(all_die)

    ones_to_six_points = one_to_six.count(str(apply_points_to_index)) * apply_points_to_index
    chance_three_and_four_of_a_kind_points = sum(rolls + inventory)

    # need to return the findall as well as the actual points. apply_combo_points will check the findall
    combos = [(one_to_six, ones_to_six_points), (three_of_a_kind, chance_three_and_four_of_a_kind_points),
              (four_of_a_kind, chance_three_and_four_of_a_kind_points), (full_house, FULL_HOUSE()),
              (small_straight, SMALL_STRAIGHT()), (large_straight, LARGE_STRAIGHT()), (yahtzee, YAHTZEE()),
               (one_to_six, chance_three_and_four_of_a_kind_points)]

    return combos


def apply_combo_points(update_choice: list, scorecard: dict, player: str, combos: list) -> int:
    """
    Verify the user's update choice against the list of possible combos and returns an int.

    Verifies the update choice to against the entire list of possible combos from check_combo(). The logic will look if
    ones to sixes are in the first item in the list and return the points value. It will look if a three of a kind is in
    the second item and so on. Then it will return an int which represents the combo points.

    :param update_choice: a list for user choice
    :param scorecard: a dict
    :param player: a string
    :param combos: a list of possible combos and their values
    :return: an int for the combo score

    >>> test_choice = ['Small Straight', 10]
    >>> test_player = 'player_one'
    >>> score = {test_player: {'Ones': 2, 'Twos': 8, 'Threes': 9, 'Fours': 4, 'Fives': 25, 'Sixes': 30, \
    'Three of a Kind': 12, 'Four of a Kind': 16, 'Full House': 25, \
    'Small Straight': -1, 'Large Straight': 40, 'YAHTZEE': 0, 'Chance': 19, 'Bonus': 35}}

    # the first item is ones to sixes which sums to 0 because the choice is small straight. Because small straight has
    ['1234'], it will return 30 points.
    >>> combo = [(['1', '2', '3', '4', '5'], 0), ([], 0), ([], 0), ([], 25), (['1234'], 30), (['12345'], 40), \
    ([], 50), (['1', '2', '3', '4', '5'], 15)]


    >>> apply_combo_points(test_choice, score, test_player, combo)
    30
    """
    apply_points_to_index = update_choice[1]
    if apply_points_to_index in [1, 2, 3, 4, 5, 6]:
        return combos[0][1]
    elif update_choice[0] == 'YAHTZEE' and scorecard[player]['YAHTZEE'] > ZERO_POINTS():
        return ANOTHER_YAHTZEE()
    elif combos[apply_points_to_index - 6][0]:
        return combos[apply_points_to_index - ONES_TO_SIXES_INDEX()][1]
    else:
        return ZERO_POINTS()


def update_scorecard(combo: int, update_choice: list, scorecard: dict, player: str):
    """
    Update score card using values from check_combos() and ask_where_to_apply_points().

    Takes a string (where to apply the points) and int (how many points it calculates to) as parameters to update the
    players (a string) individual scorecard (a dict). Will not let the user update an option that has point already
    applied (except Yahtzee).

    :param combo: an int
    :param update_choice: a string
    :param scorecard: a dict
    :param player: a string
    :precondition: combo must be an int, update_choice must be a string and should not be already filled out, scorecard
    is a dict, player is player_one or player_two
    :postcondition: updates the player dictionary with chosen choice

    * no doctest because no print or return. changes state of scorecard *
    """

    if update_choice[0] == 'YAHTZEE' and scorecard[player]['YAHTZEE'] > ZERO_POINTS():
        scorecard[player]['YAHTZEE'] += combo
    else:
        update_string = update_choice[0]
        scorecard[player][update_string] = combo


def check_winner(player_one, player_one_score, player_two, player_two_score):
    """
    Check if both player scorecards have been filled, then compare scores to determine winner and end program.

    :param player_one: a string
    :param player_one_score: first players score card
    :param player_two: a string
    :param player_two_score: second players scorecard
    :precondition: both players must be strings and have scorecard dictionaries
    :postcondition: prints messages to the respective winner and ends the program
    """

    if NO_POINTS() not in player_one_score[player_one].values() and player_two_score[player_two].values():
        p1_score = sum(player_one_score[player_one].values())
        p2_score = sum(player_two_score[player_two].values())

        if p1_score > p2_score:
            print(f"{player_one} wins! You scored: {p1_score}.")
            print(f"{player_two} wins! You scored: {p2_score}.")
        else:
            print(f"Both players scored {p1_score}. That's a tie!")


def turn_manager(scorecard: dict, player: str, options: list, inventory: list):
    """
    Organizes the flow for player turns/die rolls

    :param scorecard: a dictionary
    :param player: a string
    :param options: a list
    :param inventory: a list to represent the player hand
    """
    turns = 3
    while turns > 0:
        rolls = roll_die(5 - len(inventory))
        print(f"{player.capitalize()} rolls the die:"
              f"{' '.join(str(nums) for nums in rolls)}\n")

        ask_remove_keep(keep, inventory, rolls)
        print(f"{player.capitalize()}'s hand: {' '.join(str(nums) for nums in inventory)}")
        print(f"What's on the table: {' '.join(str(nums) for nums in rolls)}\n")

        ask_remove_keep(remove, inventory, rolls)
        print(f"{player.capitalize()}'s hand: {' '.join(str(nums) for nums in inventory)}")

        turns -= 1

        if turns == 0:
            check_bonus(scorecard, player)
            update_choice = ask_where_to_apply_points(options)
            combo = check_combos(update_choice, rolls, inventory)
            apply_points = apply_combo_points(update_choice, scorecard, player, combo)
            update_scorecard(apply_points, update_choice, scorecard, player)
            print_scorecard(scorecard, player)


def play_yahtzee():
    """
    Organize the flow of the entire game. Drives the program.
    """
    player_one, player_two = 'player_one', 'player_two'
    player_one_score, player_two_score = CREATE_SCORECARD(player_one), CREATE_SCORECARD(player_two)

    while True:
        player_one_hand, player_two_hand = [], []
        player_one_options = create_options(player_one_score, player_one)
        player_two_options = create_options(player_two_score, player_two)

        if NO_POINTS() in player_one_score[player_one].values():
            turn_manager(player_one_score, player_one, player_one_options, player_one_hand)
        else:
            continue

        if NO_POINTS() in player_two_score[player_two].values():
            turn_manager(player_two_score, player_two, player_two_options, player_two_hand)
        else:
            continue
        check_winner(player_one, player_one_score, player_two, player_two_score)


def main():
    play_yahtzee()
    # import doctest
    # doctest.testmod()


if __name__ == '__main__':
    main()
