# Dice drawings based on code from leogama
# https://stackoverflow.com/questions/26702996/drawing-dice-with-python

top    = "┌─────────┐  ┌─────────┐"
bottom = "└─────────┘  └─────────┘"
# Separation between 2 dice
sep    = "  "
blank  = "|         |"
left   = "|  ●      |"
middle = "|    ●    |"
right  = "|      ●  |"
both   = "|  ●   ●  |"

dice = [
    (blank, middle, blank),
    (left, blank, right),
    (left, middle, right),
    (both, blank, both),
    (both, middle, both),
    (both, both, both),
]


def print_dice(a, b):
    print(top)
    # Creates both dice at once layer by layer (top to bottom)
    print("\n".join(a + sep + b for a, b in zip(dice[a - 1], dice[b - 1])))
    print(bottom)
