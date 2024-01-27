# Calculating Currency conversions
from my_functions import conv_numbers
from math import ceil

while True:
    print("Please provide currency in numbers.")
    euro = conv_numbers(input("How many Euro's are you exchanging?"))
    e_e = conv_numbers(input("What is the exchnange rate?"))
    if euro and e_e:
        # Check the input available the break out of the loop
        break

print(f"{euro} euros at an exchange rate of {e_e}.")

amount = ceil(round(euro / e_e, 2))

print(f"{amount} U.S. dollars")
