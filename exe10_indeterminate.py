#Self checkout, indeterminate number of quantit

numbers = [str(x) for x in range(1,100)]

qty = []
price = []
total = []
while True:
    print("Please provide the valid numbers")
    qty1 = input("What is the quantity of the item? ")
    price1 = input("What is the price of item? ")
    have_next = input("Have another item? Yes or No :")
    qty.append(qty1)
    price.append(price1)
    print(f"lis is {qty + price}")
    if all(item in numbers for item in qty + price) and have_next == "No" :
        #Check the logic and break out of the loop
        #print("yep all in numbers")
        break

for i in range(0, len(qty)):
    total.append(int(qty[i]) * int(price[i]))

subtotal = sum(total)
tax = 5.5 * subtotal / 100
grand_total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {grand_total}")

#How can we write a program to get the indeterminate number of items and quantities