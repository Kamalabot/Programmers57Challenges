#Poping employee from the register

"""Program implements the removal of a name from 
the list. The program will be extended to read from 
file and write to file"""

#Creating the employee list

from matplotlib.pyplot import get
from numpy import empty_like


empl = ['John Smith', 
        'Jackie Jackson',
        'Chris Jones',
        'Amanda Cullen',
        'Jeremy Goodwin']

print(f"There are {len(empl)} employees")

for emp in empl:
    print(emp)

rem = input("Enter full employee name to remove: ")

get_i = empl.index(rem)

empl.pop(get_i)

print(f"There are {len(empl)} employees")

for emp in empl:
    print(emp)

print("Extending the program to read and write to files")

get_list = []
with open("empl_read.txt") as f:
    data = f.read()
    for line in data.split('\n'):
        get_list.append(line)

empl_list = get_list[1:]
print(f"The employees from the file are {empl_list}")

rem = input("Enter full employee name to remove: ")

get_i = empl_list.index(rem)

empl_list.pop(get_i)

print(f"There are {len(empl_list)} employees")

for emp in empl_list:
    print(emp)

#writing to the file
with open('Writing_empl.txt','w') as f:
    for emp in empl_list:
        f.write(emp+'\n')

print("New file with updated employees are written, please check")