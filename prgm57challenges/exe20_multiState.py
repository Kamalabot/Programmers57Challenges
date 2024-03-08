#Calculating tax for multiple state

from my_functions import conv_numbers

while True:
    order = conv_numbers(input('Enter your order amount :'))
    if order:
        break

state = input("Enter your state of residence :")
state = state.lower()

if state == 'wisconsin' or state == 'wi':
    county = input("""Enter your county of 
    residence (dunn / eau claire) : """)
    county = county.lower()
    if county == 'dunn':
        tax = order * 0.004
    else:
        tax = order * 0.005

    total = order + tax
    total = round(total, 1)

    print(f"Your tax is : {tax}")
    print(f"Your total is : {total}")

elif state == 'illinois' or state == 'il':
    tax = order * 0.08
    total = order + tax
    total = round(total,2)

    print(f"Your tax is : {tax}")
    print(f"Your total is : {total}")