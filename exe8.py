# Let's do pizza party
from my_functions import conv_numbers

t = 0
while True:
    print("Please provide the valid numbers")
    people = conv_numbers(input("How many people?"))
    pizza = conv_numbers(input("How many pizza you have?"))
    t = t + 1
    print(t)
    if pizza and people:
        # Check the logic and break out of the loop
        break

slice = 8

print(f"{people} people with {pizza} pizza")

print(f"Each person gets {round(pizza * slice / people, 1)}")

print(f"{pizza * slice % people} slices leftover")

# Program can be refactored to calculate the number of 
# pizza required from the people and their needs...

get_people = conv_numbers(input("How many people? "))
# create list to hold how many slices people need
# we can avoid hold this in list and directly hold the sum
get_needs = []

# get the requirement of each person
for num in range(get_people):
    slice = conv_numbers(input(f"How many slices does {num} guy want?"))
    # append the slices and guy num to get_needs list
    get_needs.append({f'guy{num}': slice})

# print(get_needs)
# get the sum of all the slices required
total_slice = sum([list(need.values())[0] for need in get_needs])
# print(total_slice)
total_pizza = round(total_slice / slice, 1)
print(f"Total number of pizza required is {total_pizza}")
