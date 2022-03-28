#Computing Compound interest

def conv_number(num):
    try:
        return float(num)
    except ValueError:
        print("Enter only numbers")

assert conv_number('5') == 5

while True:
    principal = conv_number(input("What is the principal amount : "))
    roi = conv_number(input("What is the rate of Interest in %: "))
    n = conv_number(input("How many years : "))
    c = conv_number(input("How many times compounded : "))

    if principal and n and roi and c:
        break

roi = roi / 100

amount = principal*(1 + (roi / c)) ** (c*n)

amount = round(amount,2)

print(f"""After {n} years at {roi * 100}% with {c} 
        compounding per year, the investment will be 
        worth {amount}""")