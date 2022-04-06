# Author: Tabish Dhsan

import random
from DiceDrawings import print_dice

## Constants ##
WINNING_SCORE = 100

## Classes ##
class Player:
    def __init__(self, name):
        self.name = name
        self.turn_total = 0
        self.total_score = 0

    def clear_score(self):
        self.total_score = 0


## Functions ##
def dice_roll():
    return random.randint(1, 6), random.randint(1, 6)


def no_ones_or_doubles(die1, die2):
    return die1 != 1 and die2 != 1 and die1 != die2


def check_for_valid_doubles(die1, die2):
    # Snake Eyes are not considered valid doubles
    return die1 == die2 and die1 + die2 != 2


def name_input_validation(player_input):
    # Sanitizes input
    input_cleanup = player_input.strip().upper()

    # Repeats until player picks a valid name
    if input_cleanup == "":
        player_answer = input("Invalid Input Try Again!! Name cannot be blank: ")
        return name_input_validation(player_answer)
    else:
        return player_input.strip()


def player_choice_validation(player, player_input):
    # Sanitizes player choice
    input_cleanup = player_input.strip().upper()

    # Runs correct function (next move) based on choice
    if input_cleanup == "HOLD":
        end_turn(player)
    elif input_cleanup == "CONTINUE":
        print(f"{player.name} chose to continue")
        player_turn(player)

    # Repeats until player picks a valid choice
    else:
        player_answer = input(
            'Invalid Input Try Again!! Type "Hold" or "Continue" to continue: '
        )
        player_choice_validation(player, player_answer)


# Checks if a one was rolled and how many
def one_rolled(player, die1, die2):

    # Checks for "Snake Eyes"
    if die1 == 1 and die2 == 1:
        player.total_score = 0
        player.turn_total = 0
        print(
            f"{player.name} rolled Snake Eyes. Their Turn Total is now 0 and their Total Score is now 0"
        )
        end_turn(player)

    # Checks if one was rolled
    elif die1 == 1 or die2 == 1:
        player.turn_total = 0
        print(
            f"{player.name} rolled a 1, their turn total is now 0 and total score is {player.total_score}"
        )
        end_turn(player)


def player_turn(player):
    # Roll Logic
    die1, die2 = dice_roll()
    print_dice(die1, die2)
    print(f"{player.name} just rolled a [{die1}] and a [{die2}]")

    if no_ones_or_doubles(die1, die2):
        # Asks player for choice for next move
        player.turn_total += die1 + die2
        print(f"{player.name}'s turn total is {player.turn_total}")
        player_choice = input(f'Would {player.name} Like To "Hold" or "Continue"?: ')
        player_choice_validation(player, player_choice)

    elif check_for_valid_doubles(die1, die2):
        # Forces another roll
        player.turn_total += die1 + die2
        print(f"Because {player.name} rolled doubles, they must go again!")
        player_turn(player)

    else:
        # One has been rolled
        one_rolled(player, die1, die2)


# Updates total score and sets turn total to 0
def end_turn(player):
    player.total_score += player.turn_total
    player.turn_total = 0
    print(
        f"{player.name}'s Turn Has Ended.\nTheir current Total Score is {player.total_score}\n"
    )


def play_game():

    # Gets names for both players
    player_one_name = name_input_validation(input("Enter Player 1 Username: "))
    player_two_name = name_input_validation(input("Enter Player 2 Username: "))

    # Creates Players
    p1 = Player(player_one_name)
    p2 = Player(player_two_name)

    # Accounts for both players using same name
    if p1.name == p2.name:
        p2.name += "_2"
        print(f"Both players names cannot be the same. Player 2 is now {p2.name}")

    # Runs until someone reaches [WINNING_SCORE] points
    while p1.total_score <= WINNING_SCORE and p2.total_score <= WINNING_SCORE:
        player_turn(p1)
        # Checks to see if player one has won before player 2's turn
        if p1.total_score < WINNING_SCORE:
            player_turn(p2)

    # Announces winner (Congrats for getting this far in the code! Here's a cookie 🍪)
    winner = p1.name if p1.total_score > p2.total_score else p2.name
    print(f"Game has ended. {winner} is the winner! :)")
    print(p1.total_score)
    print(p2.total_score)


play_game()
