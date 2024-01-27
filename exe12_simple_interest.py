# Computing simple interest
from my_functions import conv_numbers

while True:
    principal = conv_numbers(input("Enter the principal amount : "))
    roi = conv_numbers(input("Enter the rate of Interest in %: "))
    n = conv_numbers(input("Enter number of years : "))

    if principal and roi and n:
        break

amount = principal * (1 + (roi * n) / 100)
amount = round(amount, 2)

print(f"After {n} years at {roi}%, the investment will be worth {amount}")
