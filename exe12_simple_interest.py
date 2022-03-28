#Computing simple interest

def conv_number(num):
    try:
        return float(num)
    except ValueError:
        print("Enter only numbers")

assert conv_number('5') == 5

while True:
    principal = input("Enter the principal amount : ")
    roi = input("Enter the rate of Interest in %: ")
    n = input("Enter number of years : ")

    if conv_number(principal) and conv_number(n) and conv_number(roi):
        principal = conv_number(principal)
        roi = conv_number(roi)
        n = conv_number(n)
        break

amount = principal*(1+ (roi * n)/100)
amount = round(amount,2)

print(f"After {n} years at {roi}%, the investment will be worth {amount}")