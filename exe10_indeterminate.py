# Self checkout, indeterminate number of quantit
from my_functions import conv_numbers

qty = []
price = []
total = []
# loop until the have_next condition is 'No'
while True:
    print("Please provide the valid numbers")
    qty1 = conv_numbers(input("What is the quantity of the item? "))
    price1 = conv_numbers(input("What is the price of item? "))
    have_next = input("Have another item? Yes or No :")
    qty.append(qty1)  # append to qty list
    price.append(price1)  # append to price list

    if have_next == "No":
        # check if there are input values
        break
# enumerate on the range of quantities provided
for i in range(0, len(qty)):
    # calculate the total expenditure and append to total list
    total.append(int(qty[i]) * int(price[i]))

subtotal = sum(total)  # get sum of total
tax = 5.5 * subtotal / 100  # calculate the tax to be paid
grand_total = subtotal + tax  # add tax to the grand total

# Output the data calculated...
print(f"There are total {len(qty)} items")
print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {grand_total}")
