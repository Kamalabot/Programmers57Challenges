from my_functions import conv_numbers
t = 0

# get valid room length and breadth
while True:
    print("Please provide the valid numbers")
    length = conv_numbers(input("What is Length of the room?"))
    # the inputs are checked whether they are convertible to numbers
    breadth = conv_numbers(input("What is the breadth of room?"))
    t = t + 1
    print(t)
    if length and breadth:  # After getting length and breadth break out
        break

print("You entered dimensions of {} feet by {} feet".format(length, breadth))

print("The area is\n")


# Calculations has to be seperate from the output
def calc_area(lnth: int, bdth: int):
    # multiply length with breadth
    area = lnth * bdth
    # convert the area into sq.mt
    area_m = lnth * bdth * 0.092
    return area, area_m


# output is printed by refering to the answered variable
print(f"{calc_area(length, breadth)[0]} square feet\n")
print(f"{calc_area(length, breadth)[1]} square meters\n")
