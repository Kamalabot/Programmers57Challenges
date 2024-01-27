# Computing Compound interest
from my_functions import conv_numbers

while True:
    principal = conv_numbers(input("What is the principal amount : "))
    roi = conv_numbers(input("What is the rate of Interest in %: "))
    n = conv_numbers(input("How many years : "))
    c = conv_numbers(input("How many times compounded : "))

    if principal and n and roi and c:
        break

roi = roi / 100

amount = principal*(1 + (roi / c)) ** (c*n)

amount = round(amount, 2)

print(f"""After {n} years at {roi * 100}% with {c} 
        compounding per year, the investment will be 
        worth {amount}""")
