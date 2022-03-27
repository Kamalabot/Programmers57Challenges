#Let's do pizza party

numbers = [str(x) for x in range(1,100)]
t = 0

while True:
    print("Please provide the valid numbers")
    people = input("How many people?")
    pizza = input("How many pizza you have?")
    t = t + 1
    print(t)
    if pizza in numbers and people in numbers:
        #Check the logic and break out of the loop
        break

pizza = int(pizza)
people = int(people)
slice = 8
print(f"{people} people with {pizza} pizza")

print(f"Each person gets {round(pizza * slice / people,1)}")

print(f"{pizza * slice % people} slices leftover")

#Program can be refactored to calculate the number of 
#pizza required from the people and their needs...