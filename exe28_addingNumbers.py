#looping and adding numbers

from my_functions import conv_numbers

while True:
    cont = conv_numbers(input("Enter how many numbers you are going to Add: "))
    if cont:
        break
sum = 0
alpha = 0
for x in range(cont):
    get_num = conv_numbers(input("Enter a Number : "))
    if get_num:
        sum = sum + get_num
    else:
        alpha += 1

print(f"The sum of the nuumbers you entered is {sum} \n")
print(f"The number of non-numbers entered is {alpha}")