#Lets filter some values

"""Program takes the list of spaced numbers and gives 
back only even numbers"""

from typing import List

def filterEvenNumbers(num_list:List[float])->List[float]:
    return [x for x in num_list if x % 2 == 0]

def filterOddNumbers(num_list:List[float])->List[float]:
    return [x for x in num_list if x % 2 != 0]

read_file = input("read lines from file? y / n")

if read_file == 'y':
    file_name = input("please provide the file name in *.txt format : ")
    with open(file_name) as f:
        data = f.readlines()
        num_lines = len(data)
        print(num_lines)
        for x in range(num_lines):
            if x % 2 == 0:
                print(data[x])

numbers = input("Enter series of numbers with spaces in between :")

num_list = [int(x) for x in numbers.split(' ') if int(x)]

print(f"The even numbers are {filterEvenNumbers(num_list)}")
print(f"The odd numbers are {filterOddNumbers(num_list)}")


