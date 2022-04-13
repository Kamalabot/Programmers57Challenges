#This file contains only the helper functions

from random import randint

def conv_numbers(num:str) ->int:
    try:
        return int(num)
    except:
        print("enter only numbers in this option")

assert conv_numbers('2') == 2

def bmiCalc(height:int,weight:int)->float:
    bmi = (weight / (height * height)) * 703
    return round(bmi,1)

assert bmiCalc(height=72,weight=180) == 24.4

def karvonen(age: int, intens: float, restHR: int) -> int:
    temp = ((220 - age) - restHR) * intens + restHR
    return round(temp)

def give_rand(difficul: int)->int:
    if difficul == 1:
        return randint(1, 10)
    elif difficul == 2:
        return randint(1, 100)
    else:
        return randint(1, 1000)

def get_domain(email_address: str) -> str:
    """Split on @ and return the last piece"""
    return email_address.lower().split('@')[-1]

assert get_domain('kalj879p@gmail.com') == 'gmail.com'
assert get_domain('macdeh@theay.com') == 'theay.com'

from typing import List
import sys

def get_data()->List[List[int]]:
    no_of_boxes = int(sys.stdin.readline().strip('\n'))

    box_data = []

    for _ in range(no_of_boxes):
        box_temp = sys.stdin.readline().strip('\n').split(' ')
        
        num_figs = int(box_temp[0]) #Find how many action figures
    
        box_contains = [] #open a new container
    
        for x in box_temp[1:]: #iterate over the remaning box temp data

            box_contains.append(int(x)) #append the figures heights to box contains list
        
        box_data.append(box_contains) #append box contains list to box_data
    
    return box_data