#Lets validate the inputs provided by the user

def name_check(name: str) -> bool:
    if name != " " or len(name) > 2:
        return True
    
from my_functions import conv_numbers

def zip_chec(zip: str) -> bool:
    if conv_numbers(zip):
        return True

import re

def id_chec(name: str) -> bool:
    match = re.search("[A-Z][A-Z]-\d\d\d\d", name)
    if match:
        return True

assert id_chec('EO-1567') is True
assert zip_chec('859858') is True
assert name_check('kam') is True

f_name = input("Enter your 1st Name: ")
l_name = input("Enter your last Name: ")
zip = input("Enter your Zip Code: ")
id = input("Enter your emp_id: ")

if not name_check(f_name):
    print("First name must be entered, and must be more than 2 characters")

elif not name_check(l_name):
    print("Last name must be entered, and must be more than 2 characters")

elif not zip_chec(zip):
    print("The zip code has to be numbers")

elif not id_chec(id):
    print("The id has to AA-5870 like format")

else:
    print("All well... ")