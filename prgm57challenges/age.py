#Retirement Calculator

numbers = [str(x) for x in range(1, 100)]
t = 0

while True:
    # The loop is checking number entered is a valid age
    # and retirement age
    print("Please provide the valid numbers")
    age = int(input("What is your current age?"))
    retire = int(input("Which age you will retire?"))
    t = t + 1
    print(t)
    if (age >= 1 and age < 100) or (retire >= 1 and retire < 100):
        # if it is valid age then move to next instruction
        break

if retire - age < 0:
    print("You can retire any time you want.")

else:
    print(f"You have {retire - age} years left until you retire.")
    print(f"It is 2022. You can retire in {2022 + retire - age}.")
