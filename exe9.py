# Let's calculate the paint
from my_functions import conv_numbers
from math import ceil
t = 0

while True:
    print("Please provide the valid numbers")
    # getting the inputs as numbers
    length = conv_numbers(input("What is wall length?"))
    width = conv_numbers(input("What is wall breadth?"))
    t = t + 1
    print(t)
    if length and width:
        # Check if valid numbers are provided and break out of the loop
        break

# using the ceil to round to the upper function

conv = 350

gallon = ceil((length * width) / conv)

print(f""" You will need to purchase {gallon} gallons
        of paint to cover {length * width} square feet.""")

# Round room will need only radius, while the L shaped room 
# will require more information... How will I get it??