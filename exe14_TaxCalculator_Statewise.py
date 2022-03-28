#Computing Statewise tax calculator

def conv_number(num):
    try:
        return float(num)
    except ValueError:
        print("Enter only numbers")

assert conv_number('5') == 5

while True:
    amount = conv_number(input("What is the order amount : "))
    state = input("Which State ?: ").lower()
    if amount:
        break

print(f"{state} data recieved \n")

if state == 'wi' or state == 'wisconsin':
    subtotal = amount
    tax = 0.55 * subtotal
    total = round((subtotal + tax),2)

    print(f"What is the amount? {amount}")

    print(f"Which state? {state}")

    print(f"The total is {total}") 

    print("The 1st while breaks\n")

#logic matters the most along with the constraint. 

if state != 'wi' and state != 'wisconsin':

    print(f"What is the amount? {amount}")

    print(f"Which state? {state}")

    print(f"The total is {amount}")

    print("The is remaining \n")