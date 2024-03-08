#Tabulating Karvonen Heart Rate

from my_functions import conv_numbers
from my_functions import karvonen

#intensity is increasing by 5% 

while True:
    restP = conv_numbers(input("Enter resting Pulse rate: "))
    age = conv_numbers(input("Enter Age: "))
    if restP and age:
        break
    #break only if the above values are integers
print("\n")
print(f"Resting Pulse : {restP}", end='    ')
print(f"Age : {age}\n")
#print("\n")

print("Intensity   | Rate  ")
print('.'*13,end='')
print("|",end="")
print('.'*7,end='')
print("\n")
for intense in range(55, 95,5):
    #print(intense)
    print(f"{intense}%          |  {karvonen(age, intense / 100,restP)}bpm\n")
    #print("\n")