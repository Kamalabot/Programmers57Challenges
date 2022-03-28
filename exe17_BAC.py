#Blood Alcohol Calculator

"""
    Can add dictionary holding the each states' driving
    limit. 
    Create a tkinter GUI to update the value
"""

def conv_number(num):
    try:
        return int(num)
    except ValueError:
        print("Provide the numbers")

A = conv_number(input("Enter the Alcohol consumed : "))
W = conv_number(input("Your body weight : "))
H = conv_number(input("Hours since last drink : "))
G = input("Provide your gender M or F: ")

if G == "M":
    r = 0.73
else:
    r = 0.66

BAC = ( A * 5.14 )/( W * r ) - 0.015 * H

print(f"Your BAC is {BAC}")

if BAC > 0.08:
    print("It is not legal for you drive.")
else:
    print("It is legal for you drive.")