import random as rand

character = ["rock", "paper", "scissor"]
comp = rand.choice(character)

table = {
    "rock": "paper",
    "paper": "scissor",
    "scissor": "rock"
}


def print_table():
    print("+====+=========+")
    print("+ no + char    +")
    print("+====+=========+")
    print("+ 01 + rock    +")
    print("+ 02 + paper   +")
    print("+ 03 + scissor +")
    print("+====+=========+")


def calcWin(player, comp):
    if player == comp:
        print(f"you chose: {player}\ncomp chose: {comp}\nDraw")
    elif player == table[comp]:
        print(f"you chose: {player}\ncomp chose: {comp}\nYou won")
    else:
        print(f"you chose: {player}\ncomp chose: {comp}\nYou lose")


def is_valid_input(player_input):
    if 0 <= player_input <= 2:
        return True
    print("Please enter the right number!")
    return False


# Main loop
again = ""
while again.capitalize() != "N":
    print_table()

    player_input = int(input("choose character number: ")) - 1
    if is_valid_input(player_input):
        calcWin(character[player_input], comp)
        again = input("Do you want to play again[Y/N]: ")
