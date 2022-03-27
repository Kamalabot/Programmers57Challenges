#Retirement Calculator

numbers = [str(x) for x in range(1,100)]
t = 0

while True:
    print("Please provide the valid numbers")
    age = input("What is your current age?")
    retire = input("Which age you will retire?")
    t = t + 1
    print(t)
    if age in numbers and retire in numbers:
        #Check the logic and break out of the loop
        break
age = int(age)
retire = int(retire)
if retire - age < 0:
    print("You can retire any time you want.")

else: 
    print(f"You have {retire - age} years left until you retire.")
    print(f"It is 2022. You can retire in {2022 + retire - age}.")
