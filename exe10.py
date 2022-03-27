#Self checkout 

numbers = [str(x) for x in range(1,100)]
t = 0
qty = []
price = []
while True:
    print("Please provide the valid numbers")
    qty1 = input("What is the quantity of 1st item?")
    price1 = input("What is the price of 1st item?")
    qty2 = input("What is the quantity of 2nd item?")
    price2 = input("What is the price of 2nd item?")
    qty3 = input("What is the quantity of 3rd item?")
    price3 = input("What is the price of 3rd item?")
    t = t + 1
    print(t)
    if all(item in numbers for item in [qty1,qty2,qty3,price1,price2,price3]) :
        #Check the logic and break out of the loop
        #print("yep all in numbers")
        break

qty1 =  int(qty1)
price1 = int(price1)
qty2 = int(qty2)
price2 = int(price2)
qty3 = int(qty3)
price3 = int(price3)

subtotal = (qty1 * price1) + (qty2 * price2) + (qty3 * price3)
tax = 5.5 * subtotal / 100
total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {total}")

#How can we write a program to get the indeterminate number of items and quantities