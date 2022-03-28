#Calculating Currency conversions

from math import ceil


numbers = [str(x) for x in range(1,1000000)]
t = 0

while True:
    print("Please provide currency in numbers.")
    euro = input("How many Euro's are you exchanging?")
    e_e = input("What is the exchnange rate?")
    t = t + 1
    print(t)
    if euro in numbers and e_e in numbers:
        #Check the logic and break out of the loop
        break

euro = int(euro)
e_e = int(e_e)
r_f = 100

print(f"{euro} euros at an exchange rate of {e_e}.")

amount = ceil(round(euro * e_e/r_f, 2))

print(f"{amount} U.S. dollars")