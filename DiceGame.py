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

    def add_to_total(self, die1, die2):
        self.turn_total += die1 + die2

    def snake_eyes_rolled(self):
        self.total_score = 0
        self.turn_total = 0
        print(
            f"{self.name} rolled Snake Eyes. Their Turn Total is now 0 and their Total Score is now 0"
        )

    def single_one_rolled(self):
        self.turn_total = 0
        print(
            f"{self.name} rolled a 1, their turn total is now 0 and total score is {self.total_score}"
        )

    # Updates total score and sets turn total to 0
    def end_turn(self):
        self.total_score += self.turn_total
        self.turn_total = 0
        print(
            f"{self.name}'s Turn Has Ended.\nTheir current Total Score is {self.total_score}\n"
        )


## Functions ##
def dice_roll():
    return random.randint(1, 6), random.randint(1, 6)


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
        player.end_turn()
    elif input_cleanup == "CONTINUE":
        print(f"{player.name} chose to continue")
        player_turn(player)

    # Repeats until player picks a valid choice
    else:
        player_answer = input(
            'Invalid Input Try Again!! Type "Hold" or "Continue" to continue: '
        )
        player_choice_validation(player, player_answer)


def player_turn(player):
    # Roll Logic
    die1, die2 = dice_roll()
    print_dice(die1, die2)
    print(f"{player.name} just rolled a [{die1}] and a [{die2}]")

    if die1 == 1 and die2 == 1:
        player.snake_eyes_rolled()
        player.end_turn()

    elif die1 == 1 or die2 == 1:
        # Checks if only one one was rolled
        player.single_one_rolled()
        player.end_turn()

    elif die1 == die2:
        player.add_to_total(die1, die2)
        print(f"Because {player.name} rolled doubles, they must go again!")
        # Forces another roll
        player_turn(player)

    else:
        player.add_to_total(die1, die2)
        # Asks player for choice for next move
        print(f"{player.name}'s turn total is {player.turn_total}")
        player_choice = input(f'Would {player.name} Like To "Hold" or "Continue"?: ')
        player_choice_validation(player, player_choice)


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
    while p1.total_score < WINNING_SCORE and p2.total_score < WINNING_SCORE:
        player_turn(p1)
        # Checks to see if player one has won before player 2's turn
        if p1.total_score < WINNING_SCORE:
            player_turn(p2)

    # Announces winner (Congrats for getting this far in the code! Here's a cookie 🍪)
    winner = p1.name if p1.total_score > p2.total_score else p2.name
    print(f"Game has ended. {winner} is the winner! :)")
    print(f"{p1.name} final score is {p1.total_score}")
    print(f"{p2.name} final score is {p2.total_score}")


play_game()
