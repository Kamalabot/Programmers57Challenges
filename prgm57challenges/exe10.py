# Self checkout
from my_functions import conv_numbers

qty = []
price = []
while True:
    print("Please provide the valid numbers")
    qty1 = conv_numbers(input("What is the quantity of 1st item?"))
    price1 = conv_numbers(input("What is the price of 1st item?"))
    qty2 = conv_numbers(input("What is the quantity of 2nd item?"))
    price2 = conv_numbers(input("What is the price of 2nd item?"))
    qty3 = conv_numbers(input("What is the quantity of 3rd item?"))
    price3 = conv_numbers(input("What is the price of 3rd item?"))
    if all([qty1, qty2, qty3, price1, price2, price3]):
        # Check if all vars recieved the break out of the loop
        break

subtotal = (qty1 * price1) + (qty2 * price2) + (qty3 * price3)
tax = 5.5 * subtotal / 100
total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {total}")