#We will compare multiple numbers

"""Program takes 3 numbers and returns the biggest 
among them
The program will be extended to 10 and then unlimited 
numbers.
Algorithm is written manually.

"""
#importing the numbers checking function
from my_functions import conv_numbers
from Max_list_function import chek_biglist
from typing import List



while True:
    n1 = conv_numbers(input("Enter num 1 :"))
    n2 = conv_numbers(input("Enter num 2 :"))
    n3 = conv_numbers(input("Enter num 3 :"))
    if n1 and n2 and n3:
        break

def chek_biggest(x: float, y: float, z: float) -> float:
    """Program gets 3 input numbers and then returns
    the biggest number amongst the three."""

    if x > y:
        tmp = x
    else:
        tmp = y
    
    if z > tmp:
        return z
    else:
        return tmp

assert chek_biggest(5,8,7) == 8


print(f"The largest number is {chek_biggest(n1,n2,n3)}\n")

print("Lets extend the program to include 10 numbers\n")

print("Enter 10 numbers... at the prompt below\n")
num_list = [] #instantiate list

for i in range(10):
    while True:
        get_num = conv_numbers(input(f"Enter number {i+1} for cheking : "))
        if get_num:
            break
    num_list.append(get_num)

assert chek_biglist([5,8,9,2]) == 9

print(f"The biggest of the 10 numbers is {chek_biglist(num_list)}.")

print("Lets extend the program to include n numbers\n")

l_len = conv_numbers(input("Enter length of numbers list you want to check : "))

num_list = [] #instantiate list

for i in range(l_len):
    while True:
        get_num = conv_numbers(input(f"Enter number {i+1} for cheking : "))
        if get_num:
            break
    num_list.append(get_num)

assert chek_biglist([5,8,9,2]) == 9

print(f"The biggest of the {l_len} numbers is {chek_biglist(num_list)}.")