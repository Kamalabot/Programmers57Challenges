#Lets generate some passwords

"""Program generates passwords based on minimum length, 
and a number of special characters and numbers to use."""
import random
while True:
    min_length = int(input("Enter the minimum length of the password: "))
    spl_char = int(input("Enter the number of special characters to use: "))
    num_char = int(input("Enter the number of numbers to use: "))
    low_case = int(input("Enter the number of lower case characters to use: "))
    if min_length and spl_char and num_char and low_case:
        break
password = []

special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for spl in range(spl_char):
    password.append(random.choice(special))
#print(password)
for num in range(num_char):
    password.append(random.choice(numbers))
#print(password)
for alp in range(min_length - spl_char - num_char - low_case):
    password.append(random.choice(alphabets))
#print(password)
for low in range(low_case):
    password.append(random.choice(low_alpha))
#print(password)
password = "".join(password)

print(f"Your password is {password}")
