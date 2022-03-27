#Let's calculate the paint

from math import ceil


numbers = [str(x) for x in range(1,10000)]
t = 0

while True:
    print("Please provide the valid numbers")
    length = input("What is wall length?")
    width = input("What is wall breadth?")
    t = t + 1
    print(t)
    if length in numbers and width in numbers:
        #Check the logic and break out of the loop
        break

length = int(length)
width = int(width)

#using the ceil to round to the upper function

conv = 350

gallon = ceil((length * width) / conv) 

print(f""" You will need to purchase {gallon} gallons
        of paint to cover {length * width} square feet.""")

#Round room will need only radius, while the L shaped room 
#will require more information... How will I get it??