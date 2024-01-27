#Computing Statewise tax calculator
from my_functions import conv_numbers

while True:
    amount = conv_numbers(input("What is the order amount : "))
    state = input("Which State ?: ").lower()
    if amount:
        break

print(f"{state} data recieved \n")

# check whether the given state is wisconsin
if state == 'wi' or state == 'wisconsin':
    subtotal = amount
    tax = 0.55 * subtotal
    total = round((subtotal + tax),2)

    print(f"What is the amount? {amount}")

    print(f"Which state? {state}")

    print(f"The total is {total}")

    print("The 1st while breaks\n")

# logic matters the most along with the constraint. 
# if the state is not wisconsin, then
if state != 'wi' and state != 'wisconsin':

    print(f"What is the amount? {amount}")

    print(f"Which state? {state}")

    print(f"The total is {amount}")

    print("The is remaining \n")