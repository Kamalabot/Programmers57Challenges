#Converting numbers to name

"""There are 2 ways to execute this. 
1) Python has no switch case, so going to use
2) Using dictionary data structure

Both will be implemented in this code"""

from my_functions import conv_numbers

print("This program gives the month name for the given number")

while True:
    inp_month = conv_numbers(input("Provide the month number : "))
    if inp_month:
        break

#implementing with if-elif-else ladder

if inp_month == 1:
    print('The name of the month is January')

elif inp_month == 2:
    print('The name of the month is February')

elif inp_month == 3:
    print('The name of the month is March')

elif inp_month == 4:
    print('The name of the month is April')

elif inp_month == 5:
    print('The name of the month is May')

elif inp_month == 6:
    print('The name of the month is June')

elif inp_month == 7:
    print('The name of the month is July')

elif inp_month == 8:
    print('The name of the month is August')

elif inp_month == 9:
    print('The name of the month is September')

elif inp_month == 10:
    print('The name of the month is October')

elif inp_month == 11:
    print('The name of the month is November')

elif inp_month == 12:
    print('The name of the month is December')

else:
    print('Enter numbers between 1 and 12')

mapped = {1:'January', 2:'Feburuary',3: 'March', 
          4: 'April', 5:'May',6: 'June',
          7:'July',8:'August',9: 'Sepetember',
          10:'October',11:'November',12: 'December'}

def get_month(num:int)->str:
    """Takes the month number and returns 
    the month name"""
    try:
        return mapped[num]
    except KeyError:
        return None

assert get_month(1) == 'January'

print("We will get result as from the dictionary usage")

if get_month(inp_month):
    print(f"The name of the month is {get_month(inp_month)}.")

else:
    print(f"The month number has is between 1 and 12")