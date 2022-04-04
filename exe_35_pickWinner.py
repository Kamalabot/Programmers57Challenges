#Lets pick a winner from the lot

"""This program picks a winner from the lot
for a contest or prize draw."""

print("Enter a list of names")

names = []

import random
from my_functions import conv_numbers

while True:
    num_names = conv_numbers(input("How many names? "))
    if num_names:
        break

for _ in range(num_names):
    name = input("Enter a name: ")
    if name != "":
        names.append(name)
    else:
        break

lot = random.randint(0, len(names) - 1)

print("The winner is:", names.pop(lot))

print(f"The remaining names for winner are: {names}")

while True:
    get_choice = input("Do you want to pick another winner? (y/n) ")

    if get_choice == 'y':
        lot = random.randint(0, len(names) - 1)
        print("The winner is:", names.pop(lot))
        print(f"The remaining names for winner are: {names}")
    else:
        print("Thank you for using this program. See you next time")
        break