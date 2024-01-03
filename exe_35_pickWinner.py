import random
from my_functions import conv_numbers

# Lets pick a winner from the lot

"""This program picks a winner from the lot
for a contest or prize draw."""

print("Enter a list of names")

names = []

while True:  # get the players
    num_names = conv_numbers(input("How many names? "))
    # Try except the input if its not int type
    if num_names:
        break  # if the input is not a number then break

for _ in range(num_names):  # enumerate on range of num of players 
    name = input("Enter a name: ")  # get name 
    if name != "":  # ensure name is not blank
        names.append(name)  # append the name to names list
    else:
        break  # break even if single name is blank


def pick_winner(name_list):
    """Pick a winer from a list of names"""
    lot = random.randint(0, len(name_list) - 1)
    # pick a player by using random int
    print("The winner is:", name_list.pop(lot))
    # pop that player out of the list
    print(f"The remaining names for winner are: {name_list}") 
    # print remaining names


while True:
    get_choice = input("Do you want to pick a winner? (y/n) ")

    if get_choice == 'y':
        pick_winner(names)
    else:
        print("Thank you for using this program. See you next time")
        break
