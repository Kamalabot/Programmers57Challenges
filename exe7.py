#Rectangular room area

numbers = [str(x) for x in range(1,10000000)]
t = 0

while True:
    print("Please provide the valid numbers")
    length = input("What is Length of the room?")
    breadth = input("What is the breadth of room?")
    t = t + 1
    print(t)
    if length in numbers and breadth in numbers:
        #Check the logic and break out of the loop
        break
length = int(length)
breadth = int(breadth)
print("You entered dimensions of {} feet by {} feet".format(length, breadth))

print("The area is\n")

#Calculations has to be seperate from the output
area = length * breadth 

area_m = length * breadth * 0.092 

#output is printed by refering to the answered variable
print(f"{area} square feet\n")

print(f"{area_m} square meters\n")