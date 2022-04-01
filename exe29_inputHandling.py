#Bad Input handlings

from my_functions import conv_numbers

while True:
    re = conv_numbers(input('What is the rate of return : '))
    if re == 0:
        print("Rate cannot be 0...")
    elif re:
        break
    else:
        print("Enter valid input")

print(f"You will double the investment in {72/re} years")